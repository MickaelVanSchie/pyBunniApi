from dataclasses import dataclass
from typing import Optional

from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class TaxRate:
    id_name: str
    percentage: float
    diverted: bool
    active: bool
    name: Optional[str]
    active_from: Optional[str]
    active_to: Optional[str]

    def __init__(
            self,
            id_name: Optional[str] = None,
            name: Optional[str] = None,
            percentage: Optional[float] = None,
            diverted: Optional[bool] = None,
            active: Optional[bool] = None,
            active_from: Optional[str] = None,
            active_to: Optional[str] = None,
            **kwargs: Optional[dict]
    ):
        # For init via pyBunniApi
        if id_name:
            self.id_name = id_name
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if diverted is not None:
            self.diverted = diverted
        if active is not None:
            self.active = active
        if active_from:
            self.active_from = active_from
        if active_to:
            self.active_to = active_to

        # For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)
