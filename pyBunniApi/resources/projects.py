from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Projects:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | dict[str, Any]:
        return self.bunni_api.create_http_request('projects/list')
