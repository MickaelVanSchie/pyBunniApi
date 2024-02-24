from typing import Any

from pyBunniApi.error import BunniApiSetupException

from .client import Client


class MockClient(Client):
    def create_http_request(self, endpoint: str, data: dict[str, Any] | str | None = None, method: str = "GET") -> Any:
        # Todo: Figure out a proper way to test this. As of now I'm rewriting the code that actually does stuff.
        # Because of that, this simply doesn't actually test the code.
        if not self.API_KEY:
            raise BunniApiSetupException("You have not set a API_KEY. Please use set_api_key() to set the API key.")
        if not self.BUSINESS_ID:
            raise BunniApiSetupException(
                "You have not set the BUSINESS_ID. Please use set_business_id() to set the BUSINESS_ID")
        if endpoint == "bank-accounts/list":
            return {
                "items": [
                    {
                        "id": "fake_bank_id",
                        "name": "fakeBankSupplier",
                        "accountNumber": "NL12ABCA1234567890",
                        "type": {
                            "name": "internalFakeName"
                        }
                    },
                ]}
        elif endpoint == "categories/list":
            return {
                "items":
                    [{
                        "id": "fake_category_id",
                        "name": "CategoryName",
                        "ledgerNumber": "1100",
                        "color": "#FFFFFF"
                    },
                    ]}

        elif endpoint == "contacts/list":
            return {
                "items": [{
                    "id": "contactId",
                    "companyName": "Fake Company Name",
                    "toTheAttentionOf": "Fake Company Employee",
                    "street": "FakeStreet",
                    "streetNumber": "11",
                    "postalCode": "1234AB",
                    "city": "FakeCity",
                    "phoneNumber": "",
                    "vatIdentificationNumber": "null",
                    "chamberOfCommerceNumber": "null",
                    "color": "#f9e7cc",
                    "fields": [],
                    "emailAddresses": [
                        "fake@gmail.com"
                    ]
                }]
            }
        elif endpoint == "invoices/list":
            return {
                "items": [
                    {
                        "id": "in_xxxxx",
                        "invoiceDate": "2023-11-24",
                        "invoiceNumber": "in10101",
                        "isFinalized": True,
                        "duePeriodDays": 14,
                        "pdfUrl": "https://pdfUrl.com",
                        "rows": [
                            {
                                "description": "This is a avery nice description",
                                "quantity": 1.00,
                                "unitPrice": 20
                            },
                        ]
                    },
                ]
            }
        elif endpoint == "invoice-designs/list":
            return {
                "items": [
                    {
                        "id": "design_id",
                        "name": "Design Name",
                        "createdOn": "2023-09-04T10:10:01Z"
                    }
                ]
            }
        elif endpoint == "projects/list":
            return {
                "items": [
                    {
                        "id": "project_id",
                        "color": "#FFFFFF",
                        "name": "Project Name"
                    }
                ]
            }
        elif endpoint == "time/list":
            return {
                "items": [
                    {
                        "id": "time_id",
                        "date": "2024-11-29",
                        "duration": {"h": 2, "m": 30},
                        "project": {
                            "id": "project_id",
                            "color": "#FFFFFF",
                            "name": "project name",
                        },
                        "description": "Some description"
                    }
                ]
            }
        elif endpoint == "time/create-or-update":
            ...

        elif endpoint == "invoices/create-pdf":
            ...
