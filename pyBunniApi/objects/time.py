import json
from dataclasses import dataclass

from ..objects.project import Project


@dataclass
class Duration:
    def __init__(self, duration: dict):
        self.h = duration.get("h", 0)
        self.m = duration.get("m", 0)

    h: int
    m: int

    def as_dict(self):
        return {"h": self.h, "m": self.m}

    def as_json(self):
        return json.dumps(self.as_dict())


@dataclass
class TimeObject:
    id: str
    date: str
    duration: Duration
    description: str
    project: Project

    def __init__(
            self,
            id: str,
            date: str,
            duration: dict,
            description: str,
            project: Project
    ):
        self.id = id
        self.date = date
        self.duration = Duration(duration)
        self.description = description
        self.project = project

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            "date": self.date,
            "duration": self.duration.as_dict(),
            "description": self.description,
            "project": self.project.as_dict()
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
