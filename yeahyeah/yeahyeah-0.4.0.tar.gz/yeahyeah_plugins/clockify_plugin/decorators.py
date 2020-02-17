from functools import wraps

from click.exceptions import ClickException
from clockifyclient.exceptions import ClockifyClientException


def handle_clockify_exceptions(func):
    """Convert any clockify api exceptions to click exceptions"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ClockifyClientException as e:
            raise ClickException(f"Error in Clockify API: {e}")

    return wrapper
