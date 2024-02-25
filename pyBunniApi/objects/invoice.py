import json
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json, LetterCase
from .invoicedesign import InvoiceDesign
from ..objects.contact import Contact
from ..objects.row import Row


@dataclass_json(letter_case=LetterCase.CAMEL)
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
            rows: list[Row] | list[dict],
            contact: Contact | dict,
            invoice_date: str,
            invoice_number: str,
            design: InvoiceDesign | dict[str, str] | None,
            external_id: str | None = None,
            tax_mode: str | None = None,
            id: str | None = None,
            due_period_days: int | None = None,
            is_finalized: bool | None = None,
            pdf_url: str | None = None
    ):

        self.id = id
        self.invoice_date = invoice_date
        self.invoice_number = invoice_number
        self.external_id = external_id
        self.is_finalized = is_finalized
        self.due_period_days = due_period_days
        self.pdf_url = pdf_url
        self.tax_mode = tax_mode
        if any(isinstance(row, dict) for row in rows):
            self.rows = [Row(**row) for row in rows]
        else:
            self.rows = rows
        if design:
            if isinstance(design, InvoiceDesign):
                self.design = design
            else:
                self.design = InvoiceDesign.from_dict(design)
        else:
            self.design = None

        if isinstance(contact, Contact):
            self.contact = contact
        else:
            self.contact = Contact(**contact)

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
