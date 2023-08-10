from ..pyBunniApi.objects.contact import Contact


def test_initiate_contact():
    company_name = 'Some Company Name'
    attn = 'Berry the Bunny'
    street = 'Carrot street'
    street_number = '21'
    postal_code = '1234AB'
    city = 'Carrot Town'
    phone_number = '123456'
    contact = Contact(
        company_name=company_name,
        attn=attn,
        street=street,
        street_number=street_number,
        postal_code=postal_code,
        city=city,
        phone_number=phone_number,
    )

    assert contact
