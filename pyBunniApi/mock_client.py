from typing import Any

from pyBunniApi.error import BunniApiSetupException

from .client import Client


class MockClient(Client):
    def create_http_request(self, endpoint: str, data: dict[str, Any] | str | None = None, method: str = "GET") -> Any:
        if not self.API_KEY:
            raise BunniApiSetupException("You have not set a API_KEY. Please use set_api_key() to set the API key.")
        if not self.BUSINESS_ID:
            raise BunniApiSetupException(
                "You have not set the BUSINESS_ID. Please use set_business_id() to set the BUSINESS_ID")
        if endpoint == "bank-accounts/list":
            return [
                {
                    "id": "fake_bank_id",
                    "name": "fakeBankSupplier",
                    "accountNumber": "NL12ABCA1234567890",
                    "type": {
                        "name": "internalFakeName"
                    }
                },
            ]
        elif endpoint == "categories/list":
            ...
        elif endpoint == "contacts/list":
            ...
        elif endpoint == "invoices/list":
            ...
        elif endpoint == "invoices/create-pdf":
            ...
        elif endpoint == "invoice-designs/list":
            ...
        elif endpoint == "projects/list":
            ...
        elif endpoint == "time/list":
            ...
        elif endpoint == "time/create-or-update":
            ...
