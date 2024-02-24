from pyBunniApi.objects.tax_rate import TaxRate
from pyBunniApi.objects.time import Duration, TimeObject
from pyBunniApi.objects.invoice import Invoice, InvoiceDesign
from pyBunniApi.objects.row import Row
from pyBunniApi.objects.project import Project
from pyBunniApi.objects.contact import Contact


def test_contact_object():
    company_name = 'Some Company Name'
    attn = 'Berry the Bunny'
    street = 'Carrot street'
    street_number = '21'
    postal_code = '1234AB'
    city = 'Carrot Town'
    phone_number = '123456'
    contact = Contact(
        companyName=company_name,
        toTheAttentionOf=attn,
        street=street,
        streetNumber=street_number,
        postalCode=postal_code,
        city=city,
        phoneNumber=phone_number,
        color="#FFFFFF",
        chamberOfCommerceNumber="",
        vatIdentificationNumber="",
        emailAddresses=["this@isfake.com"],
        fields={},
    )

    assert contact


def test_row_object():
    row = Row(
        unit_price=10.5,
        description='this is a test description',
        quantity=5,
        tax='NL_High21',
    )
    assert row


def test_invoice_object():
    contact = Contact(
        companyName='Some Company Name',
        toTheAttentionOf='Berry the Bunny',
        street='Carrot street',
        streetNumber='21',
        postalCode='1234AB',
        city='Carrot Town',
        phoneNumber='123456',
        color="#FFFFFF",
        chamberOfCommerceNumber="",
        vatIdentificationNumber="",
        emailAddresses=["this@isfake.com"],
        fields={},
    )
    row = Row(
        unit_price=10.5,
        description='this is a test description',
        quantity=5,
        tax='NL_High21',
    )
    design = InvoiceDesign(
        id='Design ID',
        name='Design Name',
        createdOn='2024-02-22'
    )

    invoice = Invoice(
        invoiceDate='2023-08-01',
        invoiceNumber='12345.67',
        rows=[row],
        duePeriodDays=14,
        id="SomeFakeId",
        isFinalized=False,
        pdfUrl="https:www.pdf.com/",
        contact=contact,
        design=design,
    )

    assert invoice


def test_project_object():
    project = Project(
        color='#123456',
        id='INTERNAL ID',
        name='Berry the Bunny'
    )
    assert project


def test_time_object():
    duration = Duration(
        {"h": 2, "m": 30}
    )
    project = Project(
        color='#123456',
        id='INTERNAL ID',
        name='Berry the Bunny'
    )
    time_object = TimeObject(
        date='2023-08-01',
        duration={"h": 2, "m": 30},
        description='some description string here',
        project=project,
        id="someFakeId"
    )

    assert time_object


def test_tax_object():
    tax_object = TaxRate(
        idName='NL_High_21',
        name='Hoog',
        percentage=21,
        diverted=False,
        active=True,
        activeFrom=2019,
        activeTo=None
    )
    assert tax_object