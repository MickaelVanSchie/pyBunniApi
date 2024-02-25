from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TaxRate:
    id_name: str
    name: str
    percentage: float
    diverted: bool
    active: bool
    active_from: int | None
    active_to: int | None

    def __init__(
            self,
            idName: str,
            name: str,
            percentage: float,
            diverted: bool,
            active: bool,
            active_from: int | None = None,
            active_to: int | None = None
    ):
        self.id_name = idName
        self.name = name
        self.percentage = percentage
        self.diverted = diverted
        self.active = active
        self.active_from = active_from
        self.active_to = active_to
