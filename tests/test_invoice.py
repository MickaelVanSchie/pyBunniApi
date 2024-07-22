from pyBunniApi.client import Client
from pyBunniApi.objects.invoice import Invoice


def test_invoice_list_typed(invoice: Invoice, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoice, invoice]}
    resp = testClient.invoices.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Invoice)


def test_invoice_list_untyped(invoice: Invoice, testClient: Client):
    testClient.create_http_request.return_value = {"items": [invoice, invoice]}
    testClient.TYPED = False
    resp = testClient.invoices.list()
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
