import json
from dataclasses import dataclass
from typing import Optional

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
            **kwargs: Optional[dict]
    ) -> None:
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
