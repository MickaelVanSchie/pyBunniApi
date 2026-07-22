from ..objects.time import TimeObject
from .base import BaseListResource


class Time(BaseListResource[TimeObject]):
    endpoint = 'time'
    model = TimeObject

    def create_or_update(self, time: TimeObject) -> None:
        self.bunni_api.create_http_request('time/create-or-update', data=time.as_json(), method="POST")
