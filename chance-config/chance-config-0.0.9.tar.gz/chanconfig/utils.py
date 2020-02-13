#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: chanconfig/utils.py
# Author: Cai Mingshi <i@unoiou.com>
# Date: 20.08.2018
from __future__ import absolute_import
import os
from collections import Mapping


def deep_update(orig_dict, update_dict):
    """Deeply update nested dict.

    Args:
        orig_dict: a `dict`
        update_dict: a `dict`

    Return:
        a `dict`
    """
    for key, val in update_dict.items():
        temp = val
        if isinstance(val, Mapping):
            temp = deep_update(orig_dict.get(key, {}), val)
        orig_dict[key] = temp
    return orig_dict


def update_dict_by_path(dict_obj, path, value):
    """Update dict with value py path.

    Args:
        dict_obj: a `dict`
        path: a `list`
        value: an `object`

    Return:
        a `dict`
    """
    obj = dict_obj
    for index, val in enumerate(path):
        if index + 1 == len(path):
            obj[val] = value
        obj.setdefault(val, {})
        obj = obj[val]
    return dict_obj


def deep_find(dict_obj, path):
    """Deeply find element in dict by path.

    Args:
        dict_obj: a `dict`
        path: a `list`

    Return:
        an 'object'

    Raises:
        `KeyError`
    """
    obj = dict_obj
    for key in path:
        obj = obj[key]
    return obj


def generate_update_value(val, existing_value):
    """Generate update value with priority.

    Args:
        val: (obj) setting value of specified key
        existing_value: (obj) existing setting value of specified key

    Return:
        (obj)

    Raises:
        `AssertionError`
        `ValueError`
    """
    assert isinstance(val, tuple)

    update_value = None
    env, process, default = val

    update_value = (env and os.getenv(env)) or existing_value or default

    if process is not None:
        update_value = process(update_value)
    return update_value
