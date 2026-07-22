import json

from pyBunniApi.client import Client
from pyBunniApi.objects.bankaccount import BankAccount


def test_bank_account_list_typed(bankAccount: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [bankAccount, bankAccount]}
    resp = testClient.bank_accounts.list()

    assert len(resp) == 2
    assert isinstance(resp[0], BankAccount)


def test_bank_account_list_untyped(bankAccount: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [bankAccount, bankAccount]}
    resp = untypedClient.bank_accounts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_initialize_bank_object_camel_case(bankAccount: dict):
    bank_account = BankAccount(**bankAccount)
    assert bank_account.id == "1"
    assert bank_account.name == "Test"
    assert bank_account.account_number == "1234"
    assert bank_account.type.name == "Test"

def test_initialize_bank_object_snake_case(bankAccount_snake: dict):
    bank_account = BankAccount(**bankAccount_snake)
    assert bank_account.id == "1"
    assert bank_account.name == "Test"
    assert bank_account.account_number == "1234"
    assert bank_account.type.name == "Test"


def test_bank_account_as_dict(bankAccount: dict):
    bank_account = BankAccount(**bankAccount)
    assert bank_account.as_dict() == {
        "id": "1",
        "name": "Test",
        "accountNumber": "1234",
        "type": {"name": "Test"},
    }


def test_bank_account_as_json(bankAccount: dict):
    bank_account = BankAccount(**bankAccount)
    assert json.loads(bank_account.as_json()) == bank_account.as_dict()


def test_bank_account_from_bunni(bankAccount: dict):
    bank_account = BankAccount()
    bank_account.from_bunni(bankAccount)
    assert bank_account.id == "1"
    assert bank_account.name == "Test"
    assert bank_account.accountNumber == "1234"
    assert bank_account.type == {"name": "Test"}