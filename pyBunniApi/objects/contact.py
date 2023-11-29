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
            companyName: str,
            toTheAttentionOf: str,
            street: str,
            streetNumber: str,
            postalCode: str,
            city: str,
            phoneNumber: str,
            vatIdentificationNumber: str,
            chamberOfCommerceNumber: str,
            emailAddresses: list[str],
            color,
            fields,
            id: str | None = None,
    ):
        self.id = id
        self.company_name = companyName
        self.attn = toTheAttentionOf or companyName
        self.street = street
        self.street_number = streetNumber
        self.postal_code = postalCode
        self.city = city
        self.phone_number = phoneNumber
        self.vat_identification_number = vatIdentificationNumber
        self.chamber_of_commerce_number = chamberOfCommerceNumber
        self.email_addresses = emailAddresses
        self.color = color
        self.fields = [Field(**fi) for fi in fields]

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
