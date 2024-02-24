from typing import Any, TYPE_CHECKING, List

from ..objects.invoice import Invoice, InvoicePDF

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Invoices:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def create_pdf(self, invoice: InvoicePDF) -> None:
        return self.bunni_api.create_http_request('invoices/create-pdf', data=invoice.as_json(), method="POST")['pdf'][
            'url']

    def create_or_update(self, invoice: Invoice) -> None:
        return self.bunni_api.create_http_request('invoices/create-or-update', data=invoice.as_json(), method="POST")

    def list(self) -> List[dict[str, Any]] | List[Invoice]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('invoices/list')['items']

    def typed_list(self) -> List[Invoice]:
        return [Invoice(**invoice) for invoice in self.bunni_api.create_http_request('invoices/list')['items']]
