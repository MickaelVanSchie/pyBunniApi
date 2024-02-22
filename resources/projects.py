from typing import TYPE_CHECKING, Any, List

from pyBunniApi.objects.project import Project

if TYPE_CHECKING:
    from pyBunniApi.client import Client


class Projects:
    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | List[Project]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request('projects/list')['items']

    def typed_list(self) -> List[Project]:
        return [Project(**project) for project in self.bunni_api.create_http_request('projects/list')['items']]
