from pyBunniApi.client import Client
from pyBunniApi.objects.invoicedesign import InvoiceDesign

def test_invoice_design_list_typed(invoiceDesign: InvoiceDesign, testClient: Client):
    testClient.create_http_request.return_value = {
        "items": [invoiceDesign, invoiceDesign]
    }
    resp = testClient.invoice_designs.list()
    assert len(resp) == 2
    assert isinstance(resp[0], InvoiceDesign)


def test_invoice_design_list_untyped(invoiceDesign: InvoiceDesign, untypedClient: Client):
    untypedClient.create_http_request.return_value = {
        "items": [invoiceDesign, invoiceDesign]
    }
    resp = untypedClient.invoice_designs.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_initiate_model_camel_case(invoiceDesign: InvoiceDesign):
    invoice_design = InvoiceDesign(**invoiceDesign)

    assert invoice_design.id == "1"
    assert invoice_design.created_on == "17-07-2024"

def test_initiate_model_snake_case(invoiceDesign_snake: InvoiceDesign):
    invoice_design = InvoiceDesign(**invoiceDesign_snake)

    assert invoice_design.id == "1"
    assert invoice_design.created_on == "17-07-2024"