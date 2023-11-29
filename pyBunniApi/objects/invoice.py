import json
from typing import Any

from ..objects.contact import Contact
from ..objects.row import Row


class InvoicePDF:
    id: str
    invoice_date: str
    invoice_number: str
    tax_mode: str
    design: dict[str, str]
    contact: Contact | dict[str, Any]
    rows: list[Row]

    def __init__(
            self,
            invoice_date: str,
            invoice_number: str,
            tax_mode: str,
            design: str,
            rows: list[Row],
            contact: dict | Contact,
            id: str
    ):
        self.id = id
        self.invoice_date = invoice_date
        self.invoice_number = invoice_number
        self.tax_mode = tax_mode
        self.design = {"id": design}
        self.rows = [Row(**row) for row in rows]
        if type(contact) == Contact:
            self.contact = contact
        else:
            self.contact = Contact(**contact)

    def as_json(self) -> str:
        row_list = []

        for row in self.rows:
            row_list.append(
                {'unitPrice': row['unit_price'], 'description': row['description'], 'quantity': row['quantity'],
                 'tax': {'id': row['tax']}}
            )

        return json.dumps(
            {
                'id': self.id,
                'invoiceDate': self.invoice_date,
                'invoiceNumber': self.invoice_number,
                'rows': row_list,
                'taxMode': self.tax_mode,
                'design': self.design,
                'contact': self.contact.pdf_contact()
            }
        )


class Invoice:
    id: str
    invoice_date: str
    invoice_number: str
    is_finalized: bool
    due_period_days: int
    rows: list[Row]
    pdf_url: str

    def __init__(
            self,
            id: str,
            invoiceDate: str,
            rows: list[Row],
            invoiceNumber: str,
            isFinalized: bool,
            duePeriodDays: int,
            pdfUrl: str
    ):
        """
        Parameters:
        id(str): Invoice Id like Bunni refers to it.
        invoiceDate(str): Invoice Date in YYYY-MM-DD format.
        rows(list[Row]): A list of rows.
        invoiceNumber(str): Your invoice number, can be any format.
        duePeriodDays(int): A integer which represents the due date in days.
        pdfUrl(str): location of the PDF stored on Bunni's servers.
        """
        self.id = id
        self.invoice_date = invoiceDate
        self.invoice_number = invoiceNumber
        self.rows = rows
        self.is_finalized = isFinalized
        self.due_period_days = duePeriodDays
        self.pdf_url = pdfUrl
