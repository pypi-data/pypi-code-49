"""This module contains common validations."""

from typing import Any


def validate_in_range(number: int, minimum: int, maximum: int, field: str) -> None:
    """Check if a given number is between a minimum and maximum."""
    validate_is_integer(number=number, field=field)
    validate_is_integer(number=minimum, field="Minimum Value")
    validate_is_integer(number=maximum, field="Maximum Value")
    if minimum > maximum:
        error_msg = build_error_msg("Minimum > Maximum", Field=field, Minimum=minimum, Maximum=maximum)
        raise ValueError(error_msg)
    if number < minimum or number > maximum:
        error_msg = build_error_msg("Number out of range", number, Field=field, Minimum=minimum, Maximum=maximum)
        raise ValueError(error_msg)


def validate_at_least_minimum(number: int, minimum: int, field: str) -> None:
    """Check if a given number is greater than or equal to a given minimum."""
    validate_is_integer(number=number, field=field)
    validate_is_integer(number=minimum, field="Minimum Value")
    if number < minimum:
        error_msg = build_error_msg("Number < Minimum", number, Field=field, Minimum=minimum)
        raise ValueError(error_msg)


def validate_is_integer(number: int, field: str) -> None:
    """Check if a given number is an integer."""
    if not isinstance(number, int):
        error_msg = build_error_msg("Number is not an integer", str(number), Field=field)
        raise ValueError(error_msg)


def validate_is_string(text: str, field: str) -> None:
    """Check if a given text is a string."""
    if not isinstance(text, str):
        error_msg = build_error_msg("Text is not a string", str(text), Field=field)
        raise ValueError(error_msg)


def validate_is_not_empty_string(text: str, field: str) -> None:
    """Check if a given text is not empty."""
    validate_is_string(text=text, field=field)
    if len(text) < 1:
        error_msg = build_error_msg("Text is empty", Field=field)
        raise ValueError(error_msg)


def validate_in_choices(value: Any, field: str, *args: Any, ) -> None:
    """Check if a given string is in a list of possible choices."""
    if len(args) < 1:
        error_msg = build_error_msg("No choices provided to choose from", Field=field)
        raise ValueError(error_msg)
    if value not in args:
        error_msg = build_error_msg("Value not found in choices", str(value),
                                    Field=field, Choices=str(args))
        raise ValueError(error_msg)


def build_error_msg(error_msg: str, error_value: Any = None, **kwargs: Any) -> str:
    """Build an error message in the format:
    msg: error_value, field_key1:field_value1, field_key2:field_value2 ..."""
    msg = str(error_msg)
    msg += (": " + str(error_value)) if error_value is not None else ""
    for key, value in kwargs.items():
        msg += ", " + key + ": " + str(value)
    return msg
