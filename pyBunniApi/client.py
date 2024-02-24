import json
from typing import Any

import requests

from .error import BunniApiSetupException, BunniApiException
from .resources import BankAccounts
from .resources import Contacts
from .resources import Categories
from .resources import InvoiceDesigns
from .resources import Invoices
from .resources import Projects
from .resources import Time
from .resources import TaxRates


class Client:
    API_KEY: str = ""
    API_VERSION: str = "0.1"
    BUSINESS_ID: str = ""
    API_URL: str = f"https://api.bunni.nl/{API_VERSION}/{BUSINESS_ID}"
    HEADER: dict[str, Any] = {}
    TYPED: bool = True
    _client = requests.session()
    from .objects.invoicedesign import InvoiceDesign  # noqa: E402
    from .objects.bankaccount import BankAccount  # noqa: E402
    from .objects.contact import Contact  # noqa: E402
    from .objects.category import Category # noqa: E402
    from .objects.invoice import Invoice  # noqa: E402
    from .objects.project import Project  # noqa: E402
    from .objects.row import Row  # noqa: E402
    from .objects.time import Duration, TimeObject  # noqa: E402
    from .objects.tax_rate import TaxRate # noqa: E402

    # Create endpoints
    def __init__(self):
        self.bank_accounts = BankAccounts(self)
        self.contacts = Contacts(self)
        self.categories = Categories(self)
        self.invoice_designs = InvoiceDesigns(self)
        self.invoices = Invoices(self)
        self.projects = Projects(self)
        self.time = Time(self)
        self.tax_rates = TaxRates(self)

    def use_typing(self, typed: bool) -> None:
        self.TYPED = typed

    def set_api_key(self, api_key: str) -> None:
        self.API_KEY = api_key

    def api_version(self, api_version: str) -> None:
        self.API_VERSION = api_version

    def set_business_id(self, business_id: str) -> None:
        self.BUSINESS_ID = business_id

    def create_header(self) -> None:
        self.HEADER = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}",
        }

    def build_api_url(self):
        self.API_URL = f"https://api.bunni.nl/{self.API_VERSION}/{self.BUSINESS_ID}"

    def create_http_request(self, endpoint: str, data: dict[str, Any] | str | None = None, method: str = "GET") -> Any:
        if not self.API_KEY:
            raise BunniApiSetupException("You have not set a API_KEY. Please use set_api_key() to set the API key.")
        if not self.BUSINESS_ID:
            raise BunniApiSetupException(
                "You have not set the BUSINESS_ID. Please use set_business_id() to set the BUSINESS_ID")
        self.build_api_url()
        self.create_header()
        content = b''
        decoded_content = {}

        try:
            content = self._client.request(
                method=method,
                url=f"{self.API_URL}/{endpoint}",
                data=data,
                headers=self.HEADER
            ).content
        except requests.HTTPError:
            print('A HTTP error occurred')
        try:
            decoded_content = json.loads(content.decode())
        except json.JSONDecodeError:
            print('JSON could not be decoded.')

        if decoded_content['status'] != 'success':
            raise BunniApiException(decoded_content['error'])
        else:
            return decoded_content['data']
