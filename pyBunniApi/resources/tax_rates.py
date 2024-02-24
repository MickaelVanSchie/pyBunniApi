from typing import TYPE_CHECKING, Any, List

from pyBunniApi.objects.tax_rate import TaxRate

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class TaxRates:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> List[dict[str, Any]] | List[TaxRate]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('tax-rates/list')['items']

    def typed_list(self) -> List[TaxRate]:
        return [TaxRate(**tax_rate) for tax_rate in self.bunni_api.create_http_request('tax-rates/list')['items']]
