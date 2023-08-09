from typing import Any, TYPE_CHECKING

from ..objects.invoice import Invoice

if TYPE_CHECKING:
    from pyBunniApi import PyBunniApi


class Invoices:
    def __init__(self, bunni_api: "PyBunniApi"):
        self.bunni_api = bunni_api

    def create(self, invoice: Invoice):
        return self.bunni_api.create_http_request('invoices/create-pdf', data=invoice.as_json(), method="POST")['pdf']['url']

    def list(self) -> list[dict[str, Any]] | dict[str, Any]:
        return self.bunni_api.create_http_request('invoices/list')['items']
