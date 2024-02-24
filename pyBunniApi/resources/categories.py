from typing import Any, TYPE_CHECKING, List

from pyBunniApi.objects.category import Category

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Categories:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | List[Category]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('categories/list')['items']

    def typed_list(self) -> List[Category]:
        return [Category(**category) for category in self.bunni_api.create_http_request('categories/list')['items']]
