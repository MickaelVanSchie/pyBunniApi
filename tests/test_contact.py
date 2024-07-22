from pyBunniApi.client import Client
from pyBunniApi.objects.contact import Contact


def test_contact_list_typed(contact: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [contact, contact]}
    resp = testClient.contacts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Contact)


def test_contact_list_untyped(contact: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [contact, contact]}
    testClient.TYPED = False
    resp = testClient.contacts.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)