from pyBunniApi.client import Client
from pyBunniApi.objects.tax_rate import TaxRate


def test_tax_rate_list_typed(tax_rate: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [tax_rate, tax_rate]}
    resp = testClient.tax_rates.list()
    assert len(resp) == 2
    assert isinstance(resp[0], TaxRate)
    assert resp[0].id_name == "NL_High_21"
    assert resp[0].percentage == 21.0


def test_tax_rate_list_untyped(tax_rate: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [tax_rate, tax_rate]}
    resp = untypedClient.tax_rates.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_initiate_tax_rate_model(tax_rate: dict):
    rate = TaxRate(**tax_rate)
    assert rate.id_name == "NL_High_21"
    assert rate.name == "Hoog"
    assert rate.percentage == 21.0
    assert rate.diverted is False
    assert rate.active is True
    assert rate.active_from == "2019-01-01"
    assert rate.active_to is None
