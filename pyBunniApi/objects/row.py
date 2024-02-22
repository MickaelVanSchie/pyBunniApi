import json
from typing import TypedDict


class Row(TypedDict):
    """
    unit_price: str
    """
    unit_price: float
    description: str
    quantity: int
    tax: str

    def as_json(self) -> str:
        return json.dumps({
            "unitPrice": self.unit_price,
            "description": self.description,
            "quantity": self.quantity,
            "tax": self.tax,
        })
