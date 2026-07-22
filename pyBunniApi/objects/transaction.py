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
            **kwargs: Mapping[Any, Any]
    ):
        # For init via pyBunniApi
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
