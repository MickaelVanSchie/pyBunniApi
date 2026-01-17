from typing import Any, TYPE_CHECKING, List

from pyBunniApi.objects.booking import Booking

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Bookings:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | List[Booking]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('bookings/list')['items']

    def typed_list(self) -> List[Booking]:
        return [Booking(**booking) for booking in self.bunni_api.create_http_request('bookings/list')['items']]


    def create_or_update(self, booking: Booking) -> None:
        raise NotImplementedError