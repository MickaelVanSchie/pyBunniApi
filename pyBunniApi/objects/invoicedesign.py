class InvoiceDesign:
    def __init__(self, id: str, name: str | None = None, createdOn: str | None = None):
        self.id = id
        self.name = name
        self.created_on = createdOn

    id: str
    name: str
    created_on: str  # Todo: Make this a proper date

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "createdOn": self.created_on,
        }