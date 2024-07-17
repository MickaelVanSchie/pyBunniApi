import pytest

from pyBunniApi.client import Client
from pyBunniApi.error import BunniApiSetupException


@pytest.fixture
def testClient() -> Client:
    cl = Client()
    return cl


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
