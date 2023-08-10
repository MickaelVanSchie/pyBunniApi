import json

from ..objects.contact import Contact
from ..objects.row import Row


class Invoice:
    invoice_date: str
    invoice_number: str
    tax_mode: str
    design: str
    contact: Contact
    rows: list[Row]

    def __init__(self, invoice_date: str, tax_mode: str, design: str, contact: Contact, rows: list[Row], invoice_number:str):
        """
        Parameters:
        invoice_date(str): Invoice Date in YYYY-MM-DD format.
        invoice_number(str): Your invoice number, can be any format.
        tax_mode(str): Tax mode, can be either `incl` or `excl`
        design(str): should reference a invoice design id.
        rows(list[Row]): A list of rows.
        """
        self.invoice_date = invoice_date
        self.invoice_number = invoice_number
        self.tax_mode = tax_mode
        self.design = design
        self.contact = contact
        self.rows = rows

    def as_json(self) -> str:
        row_list = []

        for row in self.rows:
            row_list.append(
                {'unitPrice': row['unit_price'], 'description': row['description'], 'quantity': row['quantity'],
                 'tax': {'id': row['tax']}}
            )

        return json.dumps(
            {
                'invoiceDate': self.invoice_date,
                'invoiceNumber': self.invoice_number,
                'taxMode': self.tax_mode,
                'design': {"id": self.design},
                'contact': {
                    'companyName': self.contact['company_name'],
                    'attn': self.contact['attn'],
                    'street': self.contact['street'],
                    'streetNumber': self.contact['street_number'],
                    'postalCode': self.contact['postal_code'],
                    'city': self.contact['city'],
                    'phoneNumber': self.contact["phone_number"],
                },
                'rows': row_list
            }
        )
