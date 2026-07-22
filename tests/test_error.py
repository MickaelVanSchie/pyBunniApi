from pyBunniApi.error import BunniApiException, BunniApiSetupException


def test_bunni_api_exception_formats_single_error():
    exc = BunniApiException({"errors": [{"domain": "invoice", "message": "Something went wrong"}]})
    assert str(exc) == "domain: invoice, message: Something went wrong "


def test_bunni_api_exception_formats_multiple_errors():
    exc = BunniApiException(
        {
            "errors": [
                {"domain": "invoice", "message": "First error"},
                {"domain": "contact", "message": "Second error"},
            ]
        }
    )
    assert str(exc) == "domain: invoice, message: First error domain: contact, message: Second error "


def test_bunni_api_setup_exception_message():
    exc = BunniApiSetupException("custom message")
    assert str(exc) == "custom message"
