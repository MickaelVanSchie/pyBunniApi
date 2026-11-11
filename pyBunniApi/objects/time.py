import json
from dataclasses import dataclass
from typing import Any, Mapping, Optional

from ..objects.project import Project
from ..tools.case_convert import to_snake_case


@dataclass
class Duration:
    h: int = 0
    m: int = 0

    def __init__(
            self,
            duration: Optional[dict] = None,
            h: Optional[int] = None,
            m: Optional[int] = None,
    ):
        if duration is not None:
            self.h = duration.get("h", 0)
            self.m = duration.get("m", 0)
        else:
            self.h = h or 0
            self.m = m or 0

    def as_dict(self):
        return {"h": self.h, "m": self.m}

    def as_json(self):
        return json.dumps(self.as_dict())


@dataclass
class TimeObject:
    id: Optional[str] = None
    date: Optional[str] = None
    duration: Optional[Duration] = None
    description: Optional[str] = None
    project: Optional[Project] = None
    external_id: Optional[str] = None

    def __init__(
            self,
            id: Optional[str] = None,
            date: Optional[str] = None,
            duration: Optional[dict] = None,
            description: Optional[str] = None,
            project: Optional[Project] = None,
            external_id: Optional[str] = None,
            **kwargs: Mapping[Any, Any]
    ):
        # For init via pyBunniApi
        self.id = id
        self.date = date
        self.duration = duration if isinstance(duration, Duration) else Duration(duration) if duration else None
        self.description = description
        self.project = project if isinstance(project, Project) else Project(**project) if isinstance(project, dict) else None
        self.external_id = external_id

        # For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            "date": self.date,
            "duration": self.duration.as_dict(),
            "description": self.description,
            "project": self.project.as_dict(),
            "externalId": self.external_id,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
