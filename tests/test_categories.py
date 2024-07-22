from pyBunniApi.client import Client
from pyBunniApi.objects.category import Category


def test_categories_list_typed(category: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [category, category]}
    resp = testClient.categories.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Category)


def test_categories_list_untyped(category: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [category, category]}
    testClient.TYPED = False
    resp = testClient.categories.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)

    