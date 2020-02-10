from typing import Any

from django.utils import timezone
from django.utils.formats import date_format


# region date formatting

def format_date(date: Any, output_format: str = 'd.m.Y', default: Any = '') -> Any:
    """
    Function that returns formatted datetime object.
    """

    if date is not None:
        if isinstance(date, timezone.datetime) and timezone.is_aware(date):
            date = timezone.localtime(date)
        return date_format(date, output_format)
    return default

# endregion


# region parse features

def safety_parse_dict(base_dict: dict, key_expression: str, default: str = '') -> Any:
    """
    Method to get value from dictionary based on expression
    Example:
        expression = 'key_1__key_2__key_3'
    """

    value = default
    unpacked_key_expression = key_expression.split('__')
    for index, expression_part in enumerate(unpacked_key_expression):
        if index == 0:
            step_object = base_dict
        else:
            step_object = value
        if not isinstance(step_object, dict):
            value = default
            break
        else:
            value = step_object.get(expression_part)

    return value if value is not None else default


def safety_get_attribute(base_object: Any,
                         attr_expression: str,
                         default: Any = None,
                         get_last_object: bool = False,
                         raise_exc: bool = False) -> Any:
    """
    Method to get attribute value based on expression.
    Example:
        expression = 'some_object.get_data()__fk_field_1__target_field'
    """

    value = default
    unpacked_attr_expression = attr_expression.split('__')
    step_object = None
    expression_part = None

    for index, expression_part in enumerate(unpacked_attr_expression):
        if index == 0:
            step_object = base_object
        else:
            step_object = value
        if hasattr(step_object, expression_part):
            value = getattr(step_object, expression_part)
            if hasattr(value, '__call__'):
                value = value()
        else:
            if raise_exc:
                raise RuntimeError(f"Can't resolve expression part: '{expression_part}' "
                                   f"for object '{step_object}': type: {type(step_object)}")
            value = default
            break

    if unpacked_attr_expression and get_last_object:
        return step_object, expression_part
    else:
        value = value if value is not None else default

    return value

# endregion
