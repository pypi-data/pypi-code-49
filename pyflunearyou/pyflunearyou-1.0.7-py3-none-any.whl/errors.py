"""Define package errors."""


class FluNearYouError(Exception):
    """Define a base error."""

    pass


class RequestError(FluNearYouError):
    """Define an error related to invalid requests."""

    pass
