from typing import TYPE_CHECKING, Any, List

from pyBunniApi.objects.transactions import Transaction

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Transactions:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> List[Transaction]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()


    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('transactions/list')['items']

    def typed_list(self) -> List[Transaction]:
        return [Transaction(**transaction) for transaction in self.bunni_api.create_http_request('transactions/list')['items']]
