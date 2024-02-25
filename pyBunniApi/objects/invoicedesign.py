import json
from dataclasses import dataclass
from typing import Optional

from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class InvoiceDesign:
    id: str
    created_on: Optional[str] = None  # Todo: Make this a proper date
    name: Optional[str] = None

    def __init__(
            self,
            id: Optional[str] = None,
            created_on: Optional[str] = None,
            name: Optional[str] = None,
            **kwargs: Optional[dict]
    ):
        # For init via pyBunniApi
        if id:
            self.id = id
        if created_on:
            self.created_on = created_on
        if name:
            self.name = name

        # For init via Bun=ni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)

    def as_dict(self, type: str = "invoice") -> dict:
        _dict = {
            "id": self.id,
        }

        if type == "complete":
            if self.name:
                _dict["name"] = self.name
            if self.created_on:
                _dict["createdOn"] = self.created_on
        return _dict

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
