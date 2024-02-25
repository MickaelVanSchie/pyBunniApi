import json
from dataclasses import dataclass
from typing import Optional, Mapping, Any

from pyBunniApi.objects.category import Category
from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class Row:
    """
    unit_price: str
    """
    description: str
    quantity: float
    tax: Optional[str] = None
    unit_price: Optional[float] = None
    booking_category: Optional[Category] = None

    def __init__(
            self,
            description: Optional[str] = None,
            quantity: Optional[float] = None,
            tax: Optional[str] = None,
            unit_price: Optional[float] = None,
            booking_category: Optional[Category] = None,
            **kwargs: Mapping[Any, Any]
    ) -> None:
        # For init via pyBunniApi
        if description:
            self.description = description
        if quantity:
            self.quantity = quantity
        if tax:
            self.tax = tax
        if unit_price:
            self.unit_price = unit_price
        if booking_category:
            self.booking_category = booking_category
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)

    def as_dict(self) -> dict:
        return {
            "unitPrice": self.unit_price,
            "description": self.description,
            "quantity": self.quantity,
            "tax": {"id": self.tax},  # Todo Make tax a proper model.,
            "bookingCategory": self.booking_category.as_dict() if self.booking_category else None
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
