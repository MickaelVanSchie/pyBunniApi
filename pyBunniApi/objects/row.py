import json
from typing import TypedDict


class Row:
    """
    unit_price: str
    """
    unit_price: float
    description: str
    quantity: int
    tax: str

    def __init__(self, unit_price: float, description: str, quantity: float, tax: str) -> None:
        self.unit_price = unit_price
        self.description = description
        self.quantity = quantity
        self.tax = tax

    def as_dict(self) -> dict:
        return {
            "unitPrice": self.unit_price,
            "description": self.description,
            "quantity": self.quantity,
            "tax": {"id": self.tax},
        }
