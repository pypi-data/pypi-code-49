# coding=utf-8
from __future__ import absolute_import, print_function

import os

environ = os.environ


def lazyget(
    key, default=None, required=False, type=str
):  # pylint: disable=used-before-assignment
    return property(
        lambda self: get(key, default=default, required=required, type=type)
    )


def get(key, default=None, required=False, type=str):
    if key not in environ:
        if required:
            raise Exception(f"No such env: {key}")
        return default
    value = environ[key]
    try:
        return type(value)
    except Exception:
        raise Exception(f"EnvTypeErr: ({key}) {value} except {getTypeName(type)}")


def getTypeName(type):
    name = getattr(type, "name", None) or getattr(type, "__name__", None)
    if not name:
        raise Exception(f"Unknown env type: {type}")
    return name


def update(*args, **kwargs):
    return environ.update(*args, **kwargs)


def str(value):
    return str(value)


def int(value):
    return int(value)


def float(value):
    return float(value)


def bool(value):
    return value in ("true", "True")
