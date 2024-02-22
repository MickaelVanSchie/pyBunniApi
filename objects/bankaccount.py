class Type:
    def __init__(self, name: str):
        self.name = name

    name: str


class BankAccount:
    id: str
    name: str
    account_number: str
    type: Type

    def __init__(self, id: str, name: str, accountNumber: str, type: dict[str, str]):
        self.id = id
        self.name = name
        self.account_number = accountNumber
        self.type = Type(**type)
