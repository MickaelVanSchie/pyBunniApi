from typing import TYPE_CHECKING, Any

from ..objects.time import TimeObject

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Time:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | dict[str, Any]:
        return self.bunni_api.create_http_request('time/list')

    def create_or_update(self, time: TimeObject) -> None:
        self.bunni_api.create_http_request('time/create-or-update', data=time.as_json(), method="POST")
