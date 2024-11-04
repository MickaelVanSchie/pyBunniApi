from pyBunniApi.objects.tax_rate import TaxRate
from pyBunniApi.objects.time import Duration, TimeObject
from pyBunniApi.objects.invoice import Invoice, InvoiceDesign
from pyBunniApi.objects.row import Row
from pyBunniApi.objects.project import Project
from pyBunniApi.objects.contact import Contact




def test_row_object():
    row = Row(
        unit_price=10.5,
        description='this is a test description',
        quantity=5,
        tax='NL_High21',
    )
    assert row


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