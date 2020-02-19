import re

from klotan.criteria.core import fn_to_criteria

UUID_REGEX = r"(?i)^[0-9A-F]{8}-[0-9A-F]{4}-[%version%][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$"


@fn_to_criteria
def is_uuid1():
    return (
        lambda y: isinstance(y, (str, bytes))
        and re.match(UUID_REGEX.replace("%version%", "1"), y) is not None
    )


@fn_to_criteria
def is_uuid2():
    return (
        lambda y: isinstance(y, (str, bytes))
        and re.match(UUID_REGEX.replace("%version%", "2"), y) is not None
    )


@fn_to_criteria
def is_uuid3():
    return (
        lambda y: isinstance(y, (str, bytes))
        and re.match(UUID_REGEX.replace("%version%", "3"), y) is not None
    )


@fn_to_criteria
def is_uuid4():
    return (
        lambda y: isinstance(y, (str, bytes))
        and re.match(UUID_REGEX.replace("%version%", "4"), y) is not None
    )


@fn_to_criteria
def is_uuid5():
    return (
        lambda y: isinstance(y, (str, bytes))
        and re.match(UUID_REGEX.replace("%version%", "5"), y) is not None
    )
