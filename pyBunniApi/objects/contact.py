from typing import TypedDict


class Contact(TypedDict):
    company_name: str
    attn: str
    street: str
    street_number: str  # This is a string because this number can contain additions. eg 11c.
    postal_code: str
    city: str
    phone_number: str
