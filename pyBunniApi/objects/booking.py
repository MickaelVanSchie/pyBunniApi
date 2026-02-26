import json
from dataclasses import dataclass
from typing import Optional

from pyBunniApi.objects.category import Category
from pyBunniApi.tools.case_convert import to_snake_case


@dataclass
class Booking:
    id: str
    external_id: str
    date: str
    rows: list[Category]
    invoice_number: str = None
    description: str = None
    documents: list[str] = None
    def __init__(
            self,
            external_id: Optional[str] = None,
            date: Optional[str] = None,
            rows: Optional[list[Category]] = None,
            invoice_number: Optional[str] = None,
            description: Optional[str] = None,
            documents: Optional[list[str]] = None,
            **kwargs: Optional[dict]
    ):
        # For init via pyBunniApi
        if external_id:
            self.external_id = external_id
        if date:
            self.date = date
        if rows:
            self.rows = rows
        if invoice_number:
            self.invoice_number = invoice_number
        if description:
            self.description = description
        if documents:
            self.documents = documents
        # For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "externalId": self.external_id,
            "date": self.date,
            "invoiceNumber": self.invoice_number,
            "description": self.description,
            "documents": self.documents,
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
