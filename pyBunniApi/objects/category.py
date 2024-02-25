import json
from typing import Optional

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Category:
    id: str
    name: str
    color: Optional[str]
    ledger_number: Optional[str]

    def __init__(
            self,
            id: str,
            name: str,
            color: str,
            ledger_number: str | None = None
    ):
        self.id = id
        self.name = name
        self.color = color
        self.ledger_number = ledger_number

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "ledgerNumber": self.ledger_number,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
