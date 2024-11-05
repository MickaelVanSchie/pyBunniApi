from pyBunniApi.client import Client
from pyBunniApi.objects.contact import Contact


def test_contact_list_typed(contact: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [contact, contact]}
    resp = testClient.contacts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Contact)


def test_contact_list_untyped(contact: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [contact, contact]}
    resp = untypedClient.contacts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_contact_get_typed(contact: dict, testClient: Client):
    testClient.create_http_request.return_value = contact
    resp = testClient.contacts.get(contact["id"])
    print(resp, contact)
    assert isinstance(resp, Contact)
    assert resp == Contact(**contact)


def test_contact_get_untyped(contact: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = contact
    resp = untypedClient.contacts.get(contact["id"])
    assert isinstance(resp, dict)
    assert resp == contact


def test_initiate_contact_model_snake_case(contact: dict):
    contact = Contact(**contact)
    assert contact.id == "1"
    assert contact.attn == "Test Person"
    assert isinstance(contact.email_addresses, list)
    assert contact.vat_identification_number == "NL123456789B01"
    assert contact.chamber_of_commerce_number == "12345678"


def test_initiate_contact_model_camel_case(contact_snake: dict):
    contact = Contact(**contact_snake)
    assert contact.id == "1"
    assert contact.attn == "Test Person"
    assert isinstance(contact.email_addresses, list)
    assert contact.vat_identification_number == "NL123456789B01"
    assert contact.chamber_of_commerce_number == "12345678"
