from dataclasses import dataclass
from typing import Optional, Mapping, Any

from ..objects.row import Row
from ..objects.document import Document
from ..tools.case_convert import to_snake_case


@dataclass
class Booking:
    id: str
    external_id: str
    invoice_number: str
    date: str
    description: str
    rows: list[Row]
    documents: list[Document]

    def __init__(
            self,
            id: Optional[str] = None,
            external_id: Optional[str] = None,
            invoice_number: Optional[str] = None,
            date: Optional[str] = None,
            description: Optional[str] = None,
            rows: Optional[list[Row]] = None,
            documents: Optional[list[Document]] = None,
            **kwargs: Mapping[Any, Any]
    ):
        # For init via pyBunniApi
        self.id = id
        self.external_id = external_id
        self.invoice_number = invoice_number
        self.date = date
        self.description = description
        self.rows = rows
        self.documents = documents

        #For init via Bunni
        for key, value in kwargs.items():
            setattr(self, to_snake_case(key), value)
