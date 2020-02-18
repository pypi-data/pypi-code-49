#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Additional Python typing module utilities
"""

from typeguard import origin_type_checkers  # type: ignore


def is_type_hint(type_):
    """
    Check if class is a generic type, for example `Union` or `List[int]`

    :param type_: type to check
    """
    if not hasattr(type_, '__module__'):
        return False

    # check if the class inherits from any `typing` class
    if type_.__module__ != 'typing':
        if not any(t.__module__ == 'typing' for t in type_.mro()):
            return False

    origin = getattr(type_, '__origin__', type_)  # Note: List.__origin__ == list

    return origin in origin_type_checkers


def is_generic(type_):
    """
    Check if class is a user-defined generic type, for example `Union[int, float]` but
    not `List`.

    :param type_: type to check
    """
    return is_type_hint(type_) and bool(getattr(type_, '__args__', ()))


def check_generic_type(value, type_, name="instance"):
    """
    Check if `value` is of a generic type `type_`. Raises `TypeError` if it's not.

    :param name: name to report in case of an error
    :param value: value to check
    :param type_: generic type to check against
    """
    if not hasattr(type_, '__origin__') or type_.__origin__ not in origin_type_checkers:
        raise ValueError('Type {} is not a generic type.'.format(type_))
    origin_type_checkers[type_.__origin__](name, value, type_, None)
