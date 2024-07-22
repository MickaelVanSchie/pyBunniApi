from pyBunniApi.client import Client
from pyBunniApi.objects.category import Category


def test_categories_list_typed(category: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [category, category]}
    resp = testClient.categories.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Category)


def test_categories_list_untyped(category: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [category, category]}
    resp = untypedClient.categories.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_initiate_category_model_snake_case(category: dict):
    category = Category(**category)
    assert category.id == "1"
    assert category.name == "Test"
    assert category.ledger_number == "1234"

def test_initialize_category_model_camel_case(category_snake: dict):
    category = Category(**category_snake)
    assert category.id == "1"
    assert category.name == "Test"
    assert category.ledger_number == "1234"