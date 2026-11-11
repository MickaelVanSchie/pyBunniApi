from pyBunniApi.client import Client
from pyBunniApi.objects.time import Duration, TimeObject


def test_time_list_typed(time_entry: dict, testClient: Client):
    testClient.create_http_request.return_value = {"items": [time_entry, time_entry]}
    resp = testClient.time.list()
    assert len(resp) == 2
    assert isinstance(resp[0], TimeObject)
    assert resp[0].id == "ti_1"
    assert resp[0].duration.h == 5
    assert resp[0].duration.m == 3
    assert resp[0].external_id == "1234"


def test_time_list_untyped(time_entry: dict, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [time_entry, time_entry]}
    resp = untypedClient.time.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)


def test_time_create_or_update(time_entry: dict, testClient: Client):
    time_object = TimeObject(**time_entry)
    testClient.time.create_or_update(time_object)
    testClient.create_http_request.assert_called_once_with(
        "time/create-or-update", data=time_object.as_json(), method="POST"
    )


def test_duration_as_dict():
    duration = Duration(h=5, m=3)
    assert duration.as_dict() == {"h": 5, "m": 3}


def test_time_object_as_dict(time_entry: dict):
    time_object = TimeObject(**time_entry)
    assert time_object.as_dict() == {
        "id": "ti_1",
        "date": "2023-08-10",
        "duration": {"h": 5, "m": 3},
        "description": "Time description",
        "project": {
            "id": "1",
            "color": "#FFFFFF",
            "name": "Test project",
            "externalId": None,
        },
        "externalId": "1234",
    }
