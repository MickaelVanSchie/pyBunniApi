from typing import TYPE_CHECKING, Any, List

from pyBunniApi.objects.invoicedesign import InvoiceDesign

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class InvoiceDesigns:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> dict[str, Any] | List[InvoiceDesign]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self):
        return self.bunni_api.create_http_request('invoice-designs/list')['items']

    def typed_list(self) -> List[InvoiceDesign]:
        return [InvoiceDesign(**invoice_design) for invoice_design in self.bunni_api.create_http_request('invoice-designs/list')['items']]