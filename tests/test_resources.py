from unittest import mock

import pytest

from pyBunniApi.client import Client
from pyBunniApi.objects.bankaccount import BankAccount
from pyBunniApi.objects.category import Category
from pyBunniApi.objects.contact import Contact
from pyBunniApi.objects.invoice import Invoice
from pyBunniApi.objects.invoicedesign import InvoiceDesign


@pytest.fixture
def testClient() -> Client:
    cl = Client()
    cl.set_api_key("SOME FAKE API KEY")
    cl.set_business_id("SOME FAKE BUSINESS ID")
    cl.create_http_request = mock.MagicMock()
    return cl

@pytest.fixture
def bankAccount() -> dict:
    return {
        "id": "1",
        "name": "Test",
        "accountNumber": "1234",
        "type": {"name": "Test"}
    }

@pytest.fixture
def category() -> dict:
    return {
        "id": "1",
        "name": "Test",
        "color": "#FFFFFF",
        "ledgerNumber": "1234"
    }

@pytest.fixture
def contact() -> dict:
    return {
        "attn": "Test Person",
        "street": "Test Street",
        "streetNumber": "1",
        "postalCode": "1234AA",
        "city": "Test City",
        "companyName": "Test Company",
        "phoneNumber": "0612345678",
        "vatIdentificationNumber": "NL123456789B01",
        "chamberOfCommerceNumber": "12345678",
        "emailAddresses":["private@email.com", "work@email.com"],
        "color": "#FFFFFF",
        "fields": [{"label": "Test Label", "value": "Test Value"}],
        "id": "1"             
    }

@pytest.fixture
def invoiceDesign() -> dict:
    return {
        "id": "1",
        "createdOn": "17-07-2024",
        "name": "Some Design",
    }

@pytest.fixture
def invoice() -> dict:
    return {
        "id": "1",
        "name": "Some Design",
        "contact": contact,

    }

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

def test_categories_list_typed(category: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [category, category]}
    resp = testClient.categories.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Category)

def test_categories_list_untyped(category: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [category, category]}
    testClient.TYPED = False
    resp = testClient.categories.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)

def test_contact_list_typed(contact: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [contact, contact]}
    resp = testClient.contacts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Contact)

def test_contact_list_untyped(contact: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [contact, contact]}
    testClient.TYPED = False
    resp = testClient.contacts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)

def test_invoice_design_list_typed(invoiceDesign: InvoiceDesign, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoiceDesign, invoiceDesign]}
    resp = testClient.invoice_designs.list()
    assert len(resp) == 2
    assert isinstance(resp[0], InvoiceDesign)

def test_invoice_design_list_untyped(invoiceDesign: InvoiceDesign, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoiceDesign, invoiceDesign]}
    testClient.TYPED = False
    resp = testClient.invoice_designs.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)

def test_invoice_list_typed(invoice: InvoiceDesign, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoice, invoice]}
    resp = testClient.invoices.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Invoice)