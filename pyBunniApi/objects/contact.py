from typing import List


class Field:
    def __init__(self, label: str, value: str):
        self.label = label
        self.value = value

    label: str
    value: str


class Contact:
    def __init__(
            self,
            street: str,
            streetNumber: str,
            postalCode: str,
            city: str,
            color: str | None = None,
            fields: dict | None = None,
            id: str | None = None,
            attn: str | None = None,
            companyName: str | None = None,
            toTheAttentionOf: str | None = None,
            phoneNumber: str | None = None,
            vatIdentificationNumber: str | None = None,
            chamberOfCommerceNumber: str | None = None,
            emailAddresses: list[str] | None = None,
    ):
        self.id = id
        self.company_name = companyName
        self.attn = toTheAttentionOf or companyName or attn
        self.street = street
        self.street_number = streetNumber
        self.postal_code = postalCode
        self.city = city
        self.phone_number = phoneNumber
        self.vat_identification_number = vatIdentificationNumber
        self.chamber_of_commerce_number = chamberOfCommerceNumber
        self.email_addresses = emailAddresses
        self.color = color
        self.fields = [Field(**fi) for fi in fields] if fields else None

    id: str
    company_name: str
    attn: str
    street: str
    street_number: str  # This is a string because this number can contain additions. eg 11c.
    postal_code: str
    city: str
    phone_number: str
    vat_identification_number: str
    chamber_of_commerce_number: str
    email_addresses = List[str]
    color: str
    fields: List[Field]

    def pdf_contact(self) -> dict:
        return {
            "companyName": self.company_name,
            "attn": self.attn,
            "street": self.street,
            "streetNumber": self.street_number,
            "postalCode": self.postal_code,
            "city": self.city,
            "phoneNumber": self.phone_number,
        }

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