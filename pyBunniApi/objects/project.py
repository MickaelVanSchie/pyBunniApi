import json
from dataclasses import dataclass
from typing import Any, Mapping, Optional

from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class Project:
    id: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None
    external_id: Optional[str] = None

    def __init__(
            self,
            id: Optional[str] = None,
            color: Optional[str] = None,
            name: Optional[str] = None,
            external_id: Optional[str] = None,
            **kwargs: Mapping[Any, Any]
    ):
        # For init via pyBunniApi
        self.id = id
        self.color = color
        self.name = name
        self.external_id = external_id

        # For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "color": self.color,
            "name": self.name,
            "externalId": self.external_id,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
