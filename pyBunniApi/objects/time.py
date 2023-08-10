import json
from typing import TypedDict

from ..objects.project import Project


class Duration(TypedDict):
    h: int
    m: int


class TimeObject:
    date: str
    duration: Duration
    description: str
    external_id: str | None
    project: Project

    def __init__(
            self,
            date: str,
            duration: Duration,
            description: str,
            external_id: str | None,
            project: Project
    ):
        self.id = id
        self.date = date
        self.duration = duration
        self.description = description
        self.external_id = external_id
        self.project = project

    def as_json(self):
        return json.dumps(
            {
                'Id': self.id,
                "date": self.date,
                "duration": {"h": self.duration["h"], "m": self.duration["m"]},
                "description": self.description,
                "externalId": self.external_id,
                "project": {
                    "externalId": self.project["external_id"],
                    "color": self.project["color"],
                    "name": self.project["name"],
                }
            }
        )
