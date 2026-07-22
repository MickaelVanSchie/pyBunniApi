import json
from unittest import mock

import pytest

from pyBunniApi.client import Client
from pyBunniApi.error import BunniApiException, BunniApiSetupException


@pytest.fixture
def testClient() -> Client:
    cl = Client()
    return cl


@pytest.fixture
def configuredClient(testClient: Client) -> Client:
    testClient.set_api_key("FAKEAPIKEY")
    testClient.set_business_id("FAKEBUSINESSID")
    return testClient


def _mock_response(payload: dict):
    response = mock.MagicMock()
    response.content = json.dumps(payload).encode()
    return response


def test_client_without_api_key(testClient: Client):
    # This test should fail if there is no api key or business ID setup.
    with pytest.raises(BunniApiSetupException) as excinfo:
        testClient.bank_accounts.list()
    assert (
        str(excinfo.value) == "You have not set a API_KEY. Please use set_api_key() to set the API key."
    )


def test_client_without_business_id(testClient: Client):
    # This test should fail if there is no business ID setup.
    testClient.set_api_key("FAKEAPIKEY")

    with pytest.raises(BunniApiSetupException) as excinfo:
        testClient.bank_accounts.list()
    assert (
        str(excinfo.value)
        == "You have not set the BUSINESS_ID. Please use set_business_id() to set the BUSINESS_ID"
    )


def test_use_typing_toggle(testClient: Client):
    assert testClient.TYPED is True
    testClient.use_typing(False)
    assert testClient.TYPED is False


def test_api_version_override(testClient: Client):
    testClient.api_version("0.2")
    assert testClient.API_VERSION == "0.2"


def test_build_api_url(configuredClient: Client):
    configuredClient.build_api_url()
    assert configuredClient.API_URL == "https://api.bunni.nl/0.1/FAKEBUSINESSID"


def test_create_http_request_success(configuredClient: Client, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        configuredClient._client,
        "request",
        mock.MagicMock(return_value=_mock_response({"status": "success", "data": {"foo": "bar"}})),
    )
    result = configuredClient.create_http_request("some/endpoint")
    assert result == {"foo": "bar"}
    configuredClient._client.request.assert_called_once_with(
        method="GET",
        url="https://api.bunni.nl/0.1/FAKEBUSINESSID/some/endpoint",
        data=None,
        headers=configuredClient.HEADER,
    )


def test_create_http_request_builds_bearer_header(configuredClient: Client, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        configuredClient._client,
        "request",
        mock.MagicMock(return_value=_mock_response({"status": "success", "data": {}})),
    )
    configuredClient.create_http_request("some/endpoint")
    assert configuredClient.HEADER["Authorization"] == "Bearer FAKEAPIKEY"


def test_create_http_request_failure_raises_bunni_exception(
    configuredClient: Client, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(
        configuredClient._client,
        "request",
        mock.MagicMock(
            return_value=_mock_response(
                {
                    "status": "failed",
                    "error": {"errors": [{"domain": "invoice", "message": "Something went wrong"}]},
                }
            )
        ),
    )
    with pytest.raises(BunniApiException) as excinfo:
        configuredClient.create_http_request("some/endpoint")
    assert "domain: invoice, message: Something went wrong" in str(excinfo.value)
