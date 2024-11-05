from unittest import mock

import pytest

from pyBunniApi.client import Client
from pyBunniApi.objects.category import Category
from pyBunniApi.objects.contact import Contact
from pyBunniApi.objects.invoicedesign import InvoiceDesign


@pytest.fixture
def testClient() -> Client:
    cl = Client()
    cl.set_api_key = "FAKEAPIKEY"
    cl.set_business_id = "FAKEBUSINESSID"
    cl.create_http_request = mock.MagicMock()
    return cl


@pytest.fixture
def untypedClient(testClient: Client):
    testClient.use_typing(False)
    return testClient


@pytest.fixture
def bankAccount() -> dict:
    return {
        "id": "1",
        "name": "Test",
        "accountNumber": "1234",
        "type": {"name": "Test"},
    }


@pytest.fixture
def bankAccount_snake() -> dict:
    return {
        "id": "1",
        "name": "Test",
        "account_number": "1234",
        "type": {"name": "Test"},
    }


@pytest.fixture
def invoice(category: Category, invoiceDesign: InvoiceDesign, contact: Contact) -> dict:
    return {
        "invoiceDate": "17-07-2024",
        "invoiceNumber": "1234",
        "rows": [
            {
                "description": "Test",
                "quantity": 1,
                "unitPrice": 1.50,
                "category": category,
            }
        ],
        "isFinalized": True,
        "duePeriodDays": 30,
        "pdfUrl": "https://www.example.com",
        "id": "1",
        "taxMode": "EXCLUSIVE",
        "design": invoiceDesign,
        "externalId": "1234",
        "contact": contact,
    }


@pytest.fixture
def invoice_snake(
    category_snake: Category, invoiceDesign_snake: InvoiceDesign, contact_snake: Contact
) -> dict:
    return {
        "invoice_date": "17-07-2024",
        "invoice_number": "2345",
        "rows": [
            {
                "description": "Test",
                "quantity": 1,
                "unit_price": 1.50,
                "category": category_snake,
                "tax": "NL_High_21",
            }
        ],
        "is_finalized": True,
        "due_period_days": 30,
        "pdf_url": "https://www.example.com",
        "id": "1",
        "tax_mode": "EXCLUSIVE",
        "design": invoiceDesign_snake,
        "external_id": "1234",
        "contact": contact_snake,
    }


@pytest.fixture
def category() -> dict:
    return {"id": "1", "name": "Test", "color": "#FFFFFF", "ledgerNumber": "1234"}


@pytest.fixture
def category_snake() -> dict:
    return {"id": "1", "name": "Test", "color": "#FFFFFF", "ledger_number": "1234"}


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
        "emailAddresses": ["private@email.com", "work@email.com"],
        "color": "#FFFFFF",
        "fields": [{"label": "Test Label", "value": "Test Value"}],
        "id": "1",
    }


@pytest.fixture
def contact_snake() -> dict:
    return {
        "attn": "Test Person",
        "street": "Test Street",
        "street_number": "1",
        "postal_code": "1234AA",
        "city": "Test City",
        "company_name": "Test Company",
        "phone_number": "0612345678",
        "vat_identification_number": "NL123456789B01",
        "chamber_of_commerce_number": "12345678",
        "email_addresses": ["private@email.com", "work@email.com"],
        "color": "#FFFFFF",
        "fields": [{"label": "Test Label", "value": "Test Value"}],
        "id": "1",
    }


@pytest.fixture
def row(category: Category) -> dict:
    return {
        "description": "Test",
        "quantity": 1,
        "price": 1.0,
        "taxRate": 21,
        "category": category,
    }


@pytest.fixture
def invoiceDesign() -> dict:
    return {
        "id": "1",
        "createdOn": "17-07-2024",
        "name": "Some Design",
    }


@pytest.fixture
def invoiceDesign_snake() -> dict:
    return {
        "id": "1",
        "created_on": "17-07-2024",
        "name": "Some Design",
    }


@pytest.fixture
def project() -> dict:
    return {
        "id": "1",
        "color": "#FFFFFF",
        "name": "Test project"
    }
