from pyBunniApi.client import Client

from pyBunniApi.objects.booking import Booking


def test_booking_list(testClient: Client, booking: dict):
    testClient.create_http_request.return_value = {"items": [booking, booking]}
    resp = testClient.bookings.list()

    assert resp == [booking, booking]
    assert type(resp[0]) == Booking


def test_booking_list_untyped(untypedClient: Client, booking: dict):
    untypedClient.create_http_request.return_value = {"items": [booking, booking]}
    resp = untypedClient.bookings.untyped_list()

    assert resp == [booking, booking]
    assert type(resp[0]) == dict