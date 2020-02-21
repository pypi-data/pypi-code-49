"""Composible functions for Cerberus validation"""
import re
from typing import List

import pytz
from cerberus import Validator


class CustomValidator(Validator):
    def _validate_equals_key(self, other_key, field, value):
        """ Test the value is equal to the value of another key.

       The rule's arguments are validated against this schema:
       {'type': 'string'}
       """
        if other_key not in self.document:
            return
        if self.document[other_key] is None:
            return
        if value != self.document[other_key]:
            self._error(
                field,
                f"{field} {value} does not match {other_key}: {self.document[other_key]}",
            )


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


def validate_list(target: List[dict], validator: Validator, schema: dict) -> dict:
    v = validator(
        {
            "a_list": {
                "type": "list",
                "required": True,
                "schema": {"type": "dict", "schema": schema},
            }
        }
    )
    v.validate({"a_list": target})
    return v.errors
