import json

from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from pyBunniApi.objects.category import Category


@dataclass_json
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
            description: str = "",
            unit_price: float | None = None,
            quantity: float = 1,
            tax: str | None = None,
            booking_category: Category | dict | None = None,
    ) -> None:
        self.unit_price = unit_price
        self.description = description
        self.quantity = quantity
        self.tax = tax

        if booking_category and not isinstance(booking_category, Category):
            self.booking_category = Category(**booking_category)

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
