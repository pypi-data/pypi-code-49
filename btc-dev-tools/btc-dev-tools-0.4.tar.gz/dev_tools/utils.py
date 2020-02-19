import logging
import re
import sys
from typing import Any

from django.conf import settings
from django.utils import timezone
from django.utils.formats import date_format

logger = logging.getLogger(__name__)


# region class handlers

def get_class_from_path(path: str, split_symbol: str = '.') -> Any:
    class_object = None
    if path and split_symbol in path:
        class_path = path.rsplit(split_symbol, 1)
        module = sys.modules.get(class_path[0])
        class_object = getattr(module, class_path[1], None)
    return class_object


def get_class_from_settings(settings_var_name: str, error_message: str, default: Any) -> Any:
    class_path_from_settings = getattr(settings, settings_var_name, None)
    class_from_settings = get_class_from_path(class_path_from_settings)
    if class_path_from_settings and not class_from_settings:
        logger.error(error_message)
    return class_from_settings or default


# endregion


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

def camel_to_snake(camel_case_str: str) -> str:
    return re.sub('(?!^)([A-Z]+)', r'_\1', camel_case_str).lower()


def safety_get_attribute(base_object: Any,
                         attr_expression: str,
                         default: Any = None,
                         get_last_object: bool = False,
                         enable_log: bool = False) -> Any:
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
            if enable_log:
                logger.debug(f"Can't resolve expression part: '{expression_part} "
                             f"for object '{step_object}': type: {type(step_object)}")
            value = default
            break

    if unpacked_attr_expression and get_last_object:
        return step_object, expression_part
    else:
        value = value if value is not None else default

    return value


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

# endregion
