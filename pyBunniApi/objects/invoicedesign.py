import json
from typing import Optional

import dataclasses_json
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class InvoiceDesign:
    id: str
    created_on: Optional[str] = None  # Todo: Make this a proper date
    name: Optional[str] = None

    def __init__(
            self,
            id: str,
            name: str | None = None,
            created_on: str | None = None,
    ):
        # Required properties
        self.id = id

        # Optional properties
        if name:
            self.name = name
        if created_on:
            self.created_on = created_on

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name if self.name else "",
            "createdOn": self.created_on,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
