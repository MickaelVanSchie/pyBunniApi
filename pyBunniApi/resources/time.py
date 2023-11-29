from typing import TYPE_CHECKING, Any, List

from ..objects.time import TimeObject

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Time:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> List[dict[str, Any]] | List[TimeObject]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('time/list')['items']

    def typed_list(self) -> List[TimeObject]:
        return [TimeObject(**time_object) for time_object in self.bunni_api.create_http_request('time/list')['items']]

    def create_or_update(self, time: TimeObject) -> None:
        self.bunni_api.create_http_request('time/create-or-update', data=time.as_json(), method="POST")
