import re
from collections.abc import Iterable

import humanfriendly
from dateutil.parser import parse as dateparse

from .utils import args_convert

# basics


def _default(val, default="", func_name="bool"):
    func = filters[func_name]
    return val if func(val) else default


# string operations


def _reverse(val):
    if isinstance(val, Iterable):
        return val[::-1]
    return val


def _strip(val: str, chars=None):
    if isinstance(val, str):
        return val.strip(chars)
    return val


def _trim(val: str):
    if isinstance(val, str):
        return val.strip()
    return val


def _replace(val, old, new, count=-1):
    count = int(count)
    return val.replace(old, new, count)


def _re(val, regex, group=0):
    group = int(group)
    match = re.search(regex, val or "")
    if match:
        return match.group(group)
    return val


# iterable operations


def _get(vals, index=0):
    index = int(index)
    return vals[index] if len(vals) > index else None


def _slice(vals, start, stop=None, step=None):
    start, stop, step = args_convert(
        start, stop, step, converter=int, validator=lambda v: v is not None
    )

    return vals[slice(start, stop, step)]


def _map(vals, func_name, *args):
    func = filters[func_name]
    return [func(val, *args) for val in vals]


def _filter(vals, func_name, *args):
    func = filters[func_name]
    return [val for val in vals if func(val, *args)]


# type convert


def _int(val):
    if val:
        match = re.search(r"\d+", val)
        if match:
            return int(match.group())
    return val


def _float(val):
    if val:
        match = re.search(r"[+-]?([0-9]*[.])?[0-9]+", val)
        if match:
            return float(match.group())
    return val


def _bool(val):
    return bool(val)


# parsers for human


def _date(val):
    return dateparse(val)


def _size(val):
    return humanfriendly.parse_size(val or "", binary=True)


filters = {
    "default": _default,
    #
    "reverse": _reverse,
    "strip": _strip,
    "trim": _trim,
    "replace": _replace,
    "re": _re,
    #
    "get": _get,
    "slice": _slice,
    "map": _map,
    "filter": _filter,
    #
    "int": _int,
    "float": _float,
    "bool": _bool,
    #
    "date": _date,
    "size": _size,
}
