import json
from dataclasses import dataclass
from typing import Optional, Any, Mapping

from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class Type:
    name: str

    def __init__(self, name: str):
        self.name = name

    def as_dict(self) -> dict:
        return {"name": self.name}


@dataclass
class BankAccount:
    id: str
    type: Type
    name: str
    account_number: Optional[str]

    def __init__(
            self,
            id: Optional[str] = None,
            type: Optional[Type] = None,
            name: Optional[str] = None,
            account_number: Optional[str] = None,
            **kwargs: Mapping[Any, Any]
    ):

        # For init via pyBunniApi
        self.id = id
        self.type = Type(**type) if isinstance(type, dict) else type
        self.name = name
        self.account_number = account_number or kwargs.get("accountNumber")

        # For init via Bunni
        for key, value in kwargs.items():
            if key == "type":
                if not isinstance(value, Type):
                    self.type = Type(**value)
            setattr(self, to_snake_case(key), value)

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

    def from_bunni(self, bunni_dict):
        for key, value in bunni_dict.items():
            setattr(self, key, value)
