from typing import TypedDict


class Project(TypedDict):
    id: str | None
    external_id: str | None
    color: str
    name: str