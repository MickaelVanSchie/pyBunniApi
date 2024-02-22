class BunniApiException(BaseException):
    """Raised when a BunniApi response returns a response with the status 'failed'"""
    errors_string = ''

    def __init__(self, errors):
        for error in errors['errors']:
            self.errors_string += f"domain: {error['domain']}, message: {error['message']} "
        super().__init__(self.errors_string)


class BunniApiSetupException(BaseException):
    """This exception is raised when the BunniApi isn't configured correctly."""
    pass
