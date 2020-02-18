"""Composible functions for Cerberus validation"""

import pytz
import re


def valid_timezone(field, value, error):
    if value not in pytz.common_timezones:
        error(field, f"{value} is not a valid timezone")


def valid_email(field, value, error):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if pattern.match(value) is None:
        error(field, f"{value} did not match valid email pattern")


def valid_phone_number(field, value, error):
    pattern = re.compile(r"^\+?(1-|1)?\(?\d{3}\)?-?\d{3}-?\d{4}$")
    if pattern.match(value) is None:
        error(field, f"{value} did not match phone number pattern.")


def valid_url(field, value, error):
    if value is None:
        return

    pattern = re.compile(
        r"^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    )
    if pattern.match(value) is None:
        error(field, f"{value} did not match URL pattern")
