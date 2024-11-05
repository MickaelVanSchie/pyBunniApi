from pyBunniApi.client import Client
from pyBunniApi.objects.invoice import Invoice
from pyBunniApi.objects.invoicedesign import InvoiceDesign
from pyBunniApi.objects.row import Row


def test_invoice_list_typed(invoice: Invoice, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoice, invoice]}
    resp = testClient.invoices.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Invoice)


def test_invoice_list_untyped(invoice: Invoice, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [invoice, invoice]}
    resp = untypedClient.invoices.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_invoice_list_finalized_typed(invoice: Invoice, testClient: Client):
    invoice_2 = invoice.copy()
    invoice_2.update({"isFinalized": False})
    testClient.create_http_request.return_value = {"items": [invoice, invoice_2]}
    resp = testClient.invoices.list(finalized=True)
    assert len(resp) == 1
    assert isinstance(resp[0], Invoice)
    assert resp[0].is_finalized


def test_invoice_list_quotation_typed(invoice: Invoice, testClient: Client):
    invoice_2 = invoice.copy()
    invoice_2.update({"isFinalized": False})
    testClient.create_http_request.return_value = {"items": [invoice, invoice_2]}
    resp = testClient.invoices.list(finalized=False)
    assert len(resp) == 1
    assert isinstance(resp[0], Invoice)
    assert not resp[0].is_finalized


def test_invoice_finalized_list_typed(invoice: Invoice, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoice, invoice]}
    resp = testClient.invoices.finalized_list()
    assert len(resp) == 2
    assert isinstance(resp[0], Invoice)


def test_quotation_list_typed(invoice: Invoice, testClient: Client):
    invoice_2 = invoice.copy()
    invoice_2.update({"isFinalized": False})
    testClient.create_http_request.return_value = {"items": [invoice, invoice_2]}
    resp = testClient.invoices.quotation_list()
    assert len(resp) == 1
    assert isinstance(resp[0], Invoice)
    assert not resp[0].is_finalized


def test_get_next_invoice_number(invoice: dict, testClient: Client):
    invoice_2 = invoice
    invoice_3 = invoice

    invoice_2["invoiceNumber"] = '1235'
    invoice_3["invoiceNumber"] = '1236'
    invoice_list = [invoice, invoice_2, invoice_3]

    testClient.create_http_request.return_value = {"items": invoice_list}
    resp = testClient.invoices.next_invoice_number()
    assert resp == 1237


# Test Initialization methods of Invoice.
def test_initialize_invoice_camel_case(invoice: Invoice):
    # Test initialization of the Invoice object as they are received from Bunni.
    # Unfortunately there are some discrepancies between the required fields per Bunni endpoint.
    invoice = Invoice(**invoice)

    assert invoice.invoice_number == '1234'
    assert len(invoice.rows) == 1
    assert isinstance(invoice.rows[0], Row)
    assert invoice.rows[0].description == 'Test'
    assert invoice.rows[0].unit_price == 1.50
    assert invoice.due_period_days == 30
    assert isinstance(invoice.design, InvoiceDesign)


def test_initialize_invoice_snake_case(invoice_snake: Invoice):
    invoice = Invoice(**invoice_snake)

    assert invoice.invoice_number == '2345'
    assert len(invoice.rows) == 1
    assert isinstance(invoice.rows[0], Row)
    assert invoice.rows[0].description == 'Test'
    assert invoice.rows[0].unit_price == 1.50
    assert invoice.rows[0].tax_rate == "NL_High_21"
    assert invoice.rows[0].as_dict().get("tax_rate") == {"id": "NL_High_21"}
    assert isinstance(invoice.design, InvoiceDesign)
    assert invoice.is_finalized
