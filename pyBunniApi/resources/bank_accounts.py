from typing import TYPE_CHECKING, Any, List

from pyBunniApi.objects.bankaccount import BankAccount

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class BankAccounts:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | List[BankAccount]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[Any, Any]]:
        return self.bunni_api.create_http_request('bank-accounts/list')['items']

    def typed_list(self) -> List[BankAccount]:
        return [BankAccount(**ba) for ba in self.bunni_api.create_http_request('bank-accounts/list')['items']]
