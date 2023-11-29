import json

from ..objects.project import Project


class Duration:
    def __init__(self, duration: dict):
        self.h = duration.get("h", 0)
        self.m = duration.get("m", 0)
    h: int
    m: int


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

    def as_json(self):
        return json.dumps(
            {
                'Id': self.id,
                "date": self.date,
                "duration": {"h": self.duration["h"], "m": self.duration["m"]},
                "description": self.description,
                "project": {
                    "externalId": self.project["external_id"],
                    "color": self.project["color"],
                    "name": self.project["name"],
                }
            }
        )
