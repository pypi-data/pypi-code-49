from spantools.errors_api import APIError


class CoughError(APIError):
    """Your got a hand cut off!"""

    api_code = 1100
    """api code"""

    http_code = 400
    """response code"""
