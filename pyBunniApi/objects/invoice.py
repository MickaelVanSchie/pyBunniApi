import json
from dataclasses import dataclass
from typing import Optional, Mapping, Any

from .invoicedesign import InvoiceDesign
from ..objects.contact import Contact
from ..objects.row import Row
from ..pb_tools.case_convert import to_snake_case


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
        self.invoice_date = invoice_date or kwargs.get("invoiceDate")
        self.invoice_number = invoice_number or kwargs.get("invoiceNumber")
        self.rows = [Row(**row) if isinstance(row, dict) else row for row in rows]
        self.is_finalized = is_finalized or kwargs.get("isFinalized")
        self.due_period_days = due_period_days or kwargs.get("duePeriodDays")
        self.pdf_url = pdf_url or kwargs.get("pdfUrl")
        self.id = id
        self.tax_mode = tax_mode or kwargs.get("taxMode")
        self.design = design 
        self.external_id = external_id or kwargs.get("externalId")
        self.contact = Contact(**contact) if isinstance(contact, dict) else contact
        self.design = InvoiceDesign(**design) if isinstance(design, dict) else design


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
