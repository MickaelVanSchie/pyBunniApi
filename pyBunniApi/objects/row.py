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
        self.description = description
        self.quantity = quantity
        self.tax_rate = tax
        self.unit_price = unit_price or kwargs.get("unitPrice")
        self.booking_category = booking_category or None

    def as_dict(self) -> dict:
        return {
            "unitPrice": self.unit_price,
            "description": self.description,
            "quantity": self.quantity,
            "tax_rate": {"id": self.tax_rate} if self.tax_rate else None,
            "bookingCategory": self.booking_category.as_dict() if self.booking_category else None
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
