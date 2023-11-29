import pytest

from pyBunniApi.error import BunniApiSetupException
from pyBunniApi.mock_client import MockClient


def test_client_without_api_key():
    # This test should fail if there is no api key or business ID setup.
    client = MockClient()
    with pytest.raises(BunniApiSetupException) as excinfo:
        lst = client.bank_accounts.list()
    assert str(excinfo.value) == "You have not set a API_KEY. Please use set_api_key() to set the API key."


def test_client_without_business_id():
    # This test should fail if there is no business ID setup.
    client = MockClient()
    client.set_api_key("FAKEAPIKEY")

    with pytest.raises(BunniApiSetupException) as excinfo:
        test = client.bank_accounts.list()
    assert str(excinfo.value) == "You have not set the BUSINESS_ID. Please use set_business_id() to set the BUSINESS_ID"
