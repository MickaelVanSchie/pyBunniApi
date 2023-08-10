from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Contacts:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]]:
        return self.bunni_api.create_http_request('contacts/list')['items']
