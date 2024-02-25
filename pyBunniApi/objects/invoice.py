import json
from dataclasses import dataclass
from typing import Optional, Mapping, Any

from .invoicedesign import InvoiceDesign
from ..objects.contact import Contact
from ..objects.row import Row
from ..tools.case_convert import to_snake_case


@dataclass
class Invoice:
    invoice_date: str
    invoice_number: str
    rows: list[Row]
    is_finalized: Optional[bool]
    due_period_days: Optional[int]
    pdf_url: Optional[str]
    id: Optional[str] = None
    tax_mode: Optional[str] = None
    design: Optional[InvoiceDesign] = None
    external_id: Optional[str] = None
    contact: Optional[Contact] = None

    def __init__(
            self,
            invoice_date: Optional[str] = None,
            invoice_number: Optional[str] = None,
            rows: Optional[list[Row]] = None,
            is_finalized: Optional[bool] = None,
            due_period_days: Optional[int] = None,
            pdf_url: Optional[str] = None,
            id: Optional[str] = None,
            tax_mode: Optional[str] = None,
            design: Optional[InvoiceDesign] = None,
            external_id: Optional[str] = None,
            contact: Optional[Contact] = None,
            **kwargs: Mapping[Any, Any]
    ):
        # For init via pyBunniApi
        if invoice_date:
            self.invoice_date = invoice_date
        if invoice_number:
            self.invoice_number = invoice_number
        if rows:
            self.rows = rows
        self.is_finalized = is_finalized
        self.due_period_days = due_period_days
        self.pdf_url = pdf_url
        self.id = id
        self.tax_mode = tax_mode
        self.design = design
        self.external_id = external_id
        self.contact = contact

        # For init via Bunni
        for key, value in kwargs.items():
            snake_case_key = to_snake_case(key)
            if snake_case_key == "rows":
                _rows = []
                assert isinstance(value, list)
                for row in value:
                    if isinstance(row, Row):
                        _rows.append(row)
                    else:
                        _rows.append(Row(**row))
            if snake_case_key == "contact":
                contact = Contact(**value) if isinstance(value, Mapping) else value
                self.contact = contact
            if snake_case_key == "design":
                inv_design = InvoiceDesign(**value)
                self.design = inv_design
            setattr(self, to_snake_case(key), value)

    def as_dict(self) -> dict:
        return {
            "externalId": self.external_id,
            "invoiceDate": self.invoice_date,
            "invoiceNumber": self.invoice_number,
            "taxMode": self.tax_mode,
            "design": self.design.as_dict() if self.design else None,
            "contact": self.contact.as_dict() if self.contact else None,
            "rows": [r.as_dict() for r in self.rows],
        }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
