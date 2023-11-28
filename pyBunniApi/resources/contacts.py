from typing import Any, TYPE_CHECKING, List

from pyBunniApi.objects.contact import Contact

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Contacts:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | List[Contact]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('contacts/list')['items']

    def typed_list(self) -> List[Contact]:
        return [Contact(**contact) for contact in self.bunni_api.create_http_request('contacts/list')['items']]
