from typing import Any, Generic, List, TYPE_CHECKING, Type, TypeVar

if TYPE_CHECKING:
    from pyBunniApi.client import Client

T = TypeVar("T")


class BaseListResource(Generic[T]):
    endpoint: str
    model: Type[T]

    def __init__(self, bunni_api: "Client"):
        self.bunni_api = bunni_api

    def list(self) -> list[dict[str, Any]] | List[T]:
        if self.bunni_api.TYPED:
            return self.typed_list()
        return self.untyped_list()

    def untyped_list(self) -> List[dict[str, Any]]:
        return self.bunni_api.create_http_request(f'{self.endpoint}/list')['items']

    def typed_list(self) -> List[T]:
        return [self.model(**item) for item in self.untyped_list()]
