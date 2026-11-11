from pyBunniApi.objects.tax_rate import TaxRate
from pyBunniApi.resources.base import BaseListResource


class TaxRates(BaseListResource[TaxRate]):
    endpoint = 'tax-rates'
    model = TaxRate
