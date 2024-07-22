from pyBunniApi.client import Client
from pyBunniApi.objects.invoicedesign import InvoiceDesign

def test_invoice_design_list_typed(invoiceDesign: InvoiceDesign, testClient: Client):
    testClient.create_http_request.return_value = {
        "items": [invoiceDesign, invoiceDesign]
    }
    resp = testClient.invoice_designs.list()
    assert len(resp) == 2
    assert isinstance(resp[0], InvoiceDesign)


def test_invoice_design_list_untyped(invoiceDesign: InvoiceDesign, testClient: Client):
    testClient.create_http_request.return_value = {
        "items": [invoiceDesign, invoiceDesign]
    }
    testClient.TYPED = False
    resp = testClient.invoice_designs.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)
