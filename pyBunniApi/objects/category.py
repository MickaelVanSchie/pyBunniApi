import json
from dataclasses import dataclass
from typing import Optional

from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class Category:
    id: str
    name: str
    color: Optional[str] = None
    ledger_number: Optional[str] = None

    def __init__(
            self,
            id: Optional[str] = None,
            name: Optional[str] = None,
            color: Optional[str] = None,
            ledger_number: Optional[str] = None,
            **kwargs: Optional[dict]
    ):
        # For init via pyBunniApi
        if id:
            self.id = id
        if name:
            self.name = name
        if color:
            self.color = color
        if color:
            self.ledger_number = ledger_number

        # For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "ledgerNumber": self.ledger_number,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
