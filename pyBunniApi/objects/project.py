import json

from dataclasses import dataclass


@dataclass
class Project:
    def __init__(self, id: str, color: str, name: str):
        self.id = id
        self.color = color
        self.name = name

    id: str | None
    color: str
    name: str

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "color": self.color,
            "name": self.name,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
