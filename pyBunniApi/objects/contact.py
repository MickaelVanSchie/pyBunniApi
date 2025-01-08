import json
from dataclasses import dataclass
from typing import List
from typing import Optional

from pyBunniApi.pb_tools.case_convert import to_snake_case


class Field:
    def __init__(self, label: str, value: str):
        self.label = label
        self.value = value

    label: str
    value: str


@dataclass
class Contact:
    attn: Optional[str]
    street: Optional[str]
    street_number: Optional[str]  # This is a string because this number can contain additions. eg 11c.
    postal_code: Optional[str]
    city: Optional[str]
    company_name: Optional[str] = None
    phone_number: Optional[str] = None
    vat_identification_number: Optional[str] = None
    chamber_of_commerce_number: Optional[str] = None
    email_addresses: Optional[list[str]] = None
    color: Optional[str] = None
    fields: Optional[List[Field]] = None
    id: Optional[str] = None

    def __init__(
            self,
            attn: Optional[str] = None,
            street: Optional[str] = None,
            street_number: Optional[str] = None,
            postal_code: Optional[str] = None,
            city: Optional[str] = None,
            company_name: Optional[str] = None,
            phone_number: Optional[str] = None,
            vat_identification_number: Optional[str] = None,
            chamber_of_commerce_number: Optional[str] = None,
            email_addresses: Optional[list[str]] = None,
            color: Optional[str] = None,
            fields: Optional[List[Field]] = None,
            id: Optional[str] = None,
            **kwargs: Optional[dict]
    ):
        # For init via pyBunniApi
        self.attn = attn
        self.street = street
        self.street_number = street_number
        self.postal_code = postal_code
        self.city = city
        self.company_name = company_name
        self.phone_number = phone_number
        self.vat_identification_number = vat_identification_number
        self.chamber_of_commerce_number = chamber_of_commerce_number
        if email_addresses:
            self.email_addresses = email_addresses
        self.color = color
        self.fields = fields
        self.id = id

        for key, value in kwargs.items():
            if key in ['toTheAttentionOf', 'attn']:
                key = 'attn'
            setattr(self, to_snake_case(key), value)


    def as_dict(self, type: str = "invoice") -> dict[str, str | None | list[str] | list[Field]]:
        # Bunni doesn't accept the complete dictionary on invoices/create-or-update.
        # In order to prevent a empty object being stored on Bunni's sid we just send the required data.
        _dict: dict[str, str | None | list[str] | list[Field]] = {
            'companyName': self.company_name,
            'attn': self.attn,
            'street': self.street,
            'streetNumber': self.street_number,
            'postalCode': self.postal_code,
            'city': self.city,
        }
        if type == "complete":
            _dict["id"] = self.id
            _dict["phoneNumber"] = self.phone_number
            _dict["vatIdentificationNumber"] = self.vat_identification_number
            _dict["chamberOfCommerceNumber"] = self.chamber_of_commerce_number
            if self.email_addresses:
                _dict["emailAddresses"]= self.email_addresses
            _dict["color"] = self.color
            _dict["fields"] = self.fields
        return _dict


    def as_json(self) -> str:
        return json.dumps(self.as_dict())
