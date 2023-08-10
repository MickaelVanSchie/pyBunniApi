from ..pyBunniApi.objects.time import Duration, TimeObject
from ..pyBunniApi.objects.invoice import Invoice
from ..pyBunniApi.objects.row import Row
from ..pyBunniApi.objects.project import Project
from ..pyBunniApi.objects.contact import Contact


def test_contact_object():
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
        company_name='Some Company Name',
        attn='Berry the Bunny',
        street='Carrot street',
        street_number='21',
        postal_code='1234AB',
        city='Carrot Town',
        phone_number='123456',
    )
    row = Row(
        unit_price=10.5,
        description='this is a test description',
        quantity=5,
        tax='NL_High21',

    )
    invoice = Invoice(
        invoice_date='2023-08-01',
        invoice_number='12345.67',
        tax_mode='NL_High_21',
        design='de_XXXX',
        contact=contact,
        rows=[row],
    )

    assert invoice


def test_project_object():
    project = Project(
        color='#123456',
        external_id='EXTERNAL ID',
        id='INTERNAL ID',
        name='Berry the Bunny'
    )
    assert project


def test_time_object():
    duration = Duration(
        h=2,
        m=30,
    )
    project = Project(
        color='#123456',
        external_id='EXTERNAL ID',
        id='INTERNAL ID',
        name='Berry the Bunny'
    )
    time_object = TimeObject(
        date='2023-08-01',
        duration=duration,
        description='some description string here',
        external_id='external id',
        project=project,
    )

    assert time_object
