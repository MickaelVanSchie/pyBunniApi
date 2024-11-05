from typing import Any, TYPE_CHECKING, List

from ..objects.invoice import Invoice

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Invoices:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def create_pdf(self, invoice: Invoice) -> None:
        return self.bunni_api.create_http_request(
            "invoices/create-pdf", data=invoice.as_json(), method="POST"
        )["pdf"]["url"]

    def create_or_update(self, invoice: Invoice) -> None:
        return self.bunni_api.create_http_request(
            "invoices/create-or-update", data=invoice.as_json(), method="POST"
        )

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request("invoices/list")["items"]

    def typed_list(self) -> List[Invoice]:
        return [Invoice(**invoice) for invoice in self.untyped_list()]

    def next_invoice_number(self) -> int:
        """
        This function unfortunately only works if your invoice numbers are integers. I still need to figure out a neat
        way to get this working with more complex invoice number formats.
        """
        ...
        invoices = self.typed_list()
        invoices.sort(key=lambda invoice: invoice.invoice_number, reverse=True)
        return int(invoices[0].invoice_number) + 1

    def list(self, finalized: bool | None = None) -> List[dict[str, Any]] | List[Invoice]:
        if finalized is not None:
            if finalized:
                return self.finalized_list()
            return self.quotation_list()
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def finalized_list(self) -> List[dict[str, Any]] | List[Invoice]:
        if self.bunni_api.TYPED:
            return [invoice for invoice in self.typed_list() if invoice.is_finalized]
        else:
            return [invoice for invoice in self.untyped_list() if invoice["is_finalized"] == "true"]

    def quotation_list(self) -> List[dict[str, Any]] | List[Invoice]:
        if self.bunni_api.TYPED:
            return [invoice for invoice in self.typed_list() if not invoice.is_finalized]
        else:
            return [invoice for invoice in self.untyped_list() if invoice["is_finalized"] == "false"]
