from typing import TypedDict


class Contact(TypedDict):
    company_name: str
    attn: str
    street: str
    street_number: int
    postal_code: str
    city: str
    phone_number: str
