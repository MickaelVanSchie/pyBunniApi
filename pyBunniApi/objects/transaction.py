from dataclasses import dataclass
from typing import Optional

from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class Transaction:
    id: str
    bank_account_id: str
    date: str
    account_number: str
    amount: float
    description: str

    def __init__(
            self,
            id: Optional[str] = None,
            bank_account_id: Optional[str] = None,
            date: Optional[str] = None,
            account_number: Optional[str] = None,
            amount: Optional[float] = None,
            description: Optional[str] = None,
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

        if id:
            self.id = id
        if bank_account_id:
            self.bank_account_id = bank_account_id
        if date:
            self.date = date
        if account_number:
            self.account_number = account_number
        if amount:
            self.amount = amount
        if description:
            self.description = description

        # For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)
