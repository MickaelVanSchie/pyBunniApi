from typing import TypedDict


class Row(TypedDict):
    """
    unit_price: str
    """
    unit_price: float
    description: str
    quantity: int
    tax: str
