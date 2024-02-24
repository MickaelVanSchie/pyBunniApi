class TaxRate:
    id_name: str
    name: str
    percentage: float
    diverted: bool
    active: bool
    activeFrom: int | None
    activeTo: int | None
    def __init__(
            self,
            idName: str,
            name: str,
            percentage: float,
            diverted: bool,
            active: bool,
            activeFrom: int | None = None,
            activeTo: int | None = None
    ):
        self.id_name = idName
        self.name=name
        self.percentage = percentage
        self.diverted = diverted
        self.active=active
        self.activeFrom = activeFrom
        self.activeTo = activeTo
