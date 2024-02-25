import json
from dataclasses import dataclass
from typing import List
from typing import Optional

from dataclasses_json import dataclass_json


class Field:
    def __init__(self, label: str, value: str):
        self.label = label
        self.value = value

    label: str
    value: str


@dataclass_json
@dataclass
class Contact:
    id: Optional[str]

    attn: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None  # This is a string because this number can contain additions. eg 11c.
    postal_code: Optional[str] = None
    city: Optional[str] = None
    phone_number: Optional[str] = None
    vat_identification_number: Optional[str] = None
    chamber_of_commerce_number: Optional[str] = None
    email_addresses: Optional[list[str]] = None
    color: Optional[str] = None
    fields: Optional[List[Field]] = None
    company_name: Optional[str] = None
    def __init__(
            self,
            street: str | None = None,
            city: str | None = None,
            color: str | None = None,
            fields: dict | None = None,
            id: str | None = None,
            attn: str | None = None,
            company_name: str | None = None,
            phone_number: str | None = None,
            vat_identification_number: str | None = None,
            chamber_of_commerce_number: str | None = None,
            email_addresses: list[str] | None = None,
            street_number: str | None = None,
            postal_code: str | None = None,
    ):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.street_number = street_number
        self.id = id
        self.company_name = company_name
        self.attn = attn
        self.city = city
        self.phone_number = phone_number
        self.vat_identification_number = vat_identification_number
        self.chamber_of_commerce_number = chamber_of_commerce_number
        self.email_addresses = email_addresses
        self.color = color
        self.fields = [Field(**fi) for fi in fields] if fields else None

    def as_dict(self) -> dict:
        return {
                'id': self.id,
                'companyName': self.company_name,
                'attn': self.attn,
                'street': self.street,
                'streetNumber': self.street_number,
                'postalCode': self.postal_code,
                'city': self.city,
                'phoneNumber': self.phone_number,
                'vatIdentificationNumber': self.vat_identification_number,
                'chamberOfCommerceNumber': self.chamber_of_commerce_number,
                'emailAddresses': self.email_addresses,
                'color': self.color,
                'fields': self.fields,
            }

    def as_json(self) -> str:
        return json.dumps(self.as_dict())
