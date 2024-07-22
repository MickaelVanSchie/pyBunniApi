from pyBunniApi.client import Client
from pyBunniApi.objects.bankaccount import BankAccount


def test_bank_account_list_typed(bankAccount: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [bankAccount, bankAccount]}
    resp = testClient.bank_accounts.list()

    assert len(resp) == 2
    assert isinstance(resp[0], BankAccount)


def test_bank_account_list_untyped(bankAccount: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [bankAccount, bankAccount]}
    testClient.TYPED = False
    resp = testClient.bank_accounts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)
