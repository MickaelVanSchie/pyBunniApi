from pyBunniApi.client import Client

from pyBunniApi.objects.booking import Booking


def test_booking_list(testClient: Client, booking: dict):
    testClient.create_http_request.return_value = {"items": [booking, booking]}
    resp = testClient.bookings.list()

    assert isinstance(resp[0], Booking)
    assert len(resp) == 2


def test_booking_list_untyped(untypedClient: Client, booking: dict):
    untypedClient.create_http_request.return_value = {"items": [booking, booking]}
    resp = untypedClient.bookings.untyped_list()

    assert isinstance(resp[0], dict)
    assert len(resp) == 2