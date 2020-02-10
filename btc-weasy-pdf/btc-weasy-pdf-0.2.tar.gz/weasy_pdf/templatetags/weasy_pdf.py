from typing import Any, Iterator

from django import template

from weasy_pdf.utils import safety_parse_dict

register = template.Library()


@register.filter
def times(number: int) -> Iterator:
    return range(number)


@register.filter
def parse_dict(base_dict: dict, key_expression: str) -> Any:
    """
    Filter for extracting values from a dictionary.
    """

    return safety_parse_dict(base_dict, str(key_expression))
