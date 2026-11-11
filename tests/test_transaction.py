from pyBunniApi.client import Client
from pyBunniApi.objects.transaction import Transaction


def test_transaction_list_typed(transaction: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [transaction, transaction]}
    resp = testClient.transactions.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Transaction)
    assert resp[0].bank_account_id == "ba_1"
    assert resp[0].amount == 100.0


def test_transaction_list_untyped(transaction: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [transaction, transaction]}
    resp = untypedClient.transactions.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_initiate_transaction_model(transaction: dict):
    txn = Transaction(**transaction)
    assert txn.id == "tr_1"
    assert txn.bank_account_id == "ba_1"
    assert txn.date == "2023-08-10"
    assert txn.account_number == "NL00BANK0123456789"
    assert txn.amount == 100.0
    assert txn.description == "Transaction description"
