import json

from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


class Type:
    def __init__(self, name: str):
        self.name = name

    name: str

    def as_dict(self) -> dict:
        return {"name": self.name}

@dataclass_json
@dataclass
class BankAccount:
    id: str
    name: str
    account_number: Optional[str]
    type: Type

    def __init__(
            self,
            id: str,
            name: str,
            type: dict[str, str] | Type,
            account_number: Optional[str] | None = None,
    ):
        self.id = id
        self.name = name
        self.account_number = account_number
        if isinstance(type, Type):
            self.type = type
        else:
            self.type = Type(**type)

    def as_dict(self) -> dict:
        # Returns a snakeCase dict
        return {
            "id": self.id,
            "name": self.name,
            "accountNumber": self.account_number,
            "type": self.type.as_dict()
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
