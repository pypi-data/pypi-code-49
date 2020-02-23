import collections
import copy
import functools
import json
import os

import xmltodict
import yaml
from pathlib import Path


class Dicto(object):
    def __init__(self, dict_=None, **kwargs):

        if dict_ is None:
            dict_ = {}

        if not isinstance(dict_, dict):
            raise ValueError("dict_ parameters is not a python dict")

        dict_.update(kwargs)

        to_dicto(dict_, dicto=self)

    def __setitem__(self, key, item):
        # self._dict[key] = item
        setattr(self, key, item)

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return repr(vars(self))

    def __len__(self):
        return len(vars(self))

    def __delitem__(self, key):
        delattr(self, key)

    def __contains__(self, item):
        return hasattr(self, item)

    def __iter__(self):
        return iter(vars(self))


def to_dicto(obj, dicto=None):

    if isinstance(obj, Dicto):
        return obj

    elif isinstance(obj, dict):

        if dicto is None:
            dicto = Dicto()

        for key, value in obj.items():

            value = to_dicto(value)

            setattr(dicto, key, value)

        return dicto

    elif isinstance(obj, str):
        return obj

    elif isinstance(obj, list):
        return [to_dicto(x) for x in obj]

    elif isinstance(obj, tuple):
        return tuple([to_dicto(x) for x in obj])

    elif hasattr(obj, "__iter__"):
        return (to_dicto(x) for x in obj)

    else:
        return obj


def to_dict(obj, dict_=None):

    if isinstance(obj, dict):
        return obj

    elif isinstance(obj, Dicto):

        if dict_ is None:
            dict_ = dict()

        for key, value in obj.__dict__.items():

            dict_[key] = to_dict(value)

        return dict_

    elif isinstance(obj, str):
        return obj

    elif isinstance(obj, list):
        return [to_dict(x) for x in obj]

    elif isinstance(obj, tuple):
        return tuple([to_dict(x) for x in obj])

    elif hasattr(obj, "__iter__"):
        return (to_dict(x) for x in obj)

    else:
        return obj


def merge(dicto, other):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``other`` is merged into
    ``dicto``.
    :param dicto: dict onto which the merge is executed
    :param other: dict that is going to merged into dicto
    :return: None
    """
    if not isinstance(dicto, Dicto):
        dicto = Dicto(dicto)

    if not isinstance(other, Dicto):
        other = Dicto(other)

    for k, v in other.__dict__.items():
        if k in dicto and isinstance(dicto[k], Dicto) and isinstance(other[k], Dicto):
            dicto[k] = merge(dicto[k], other[k])
        else:
            dicto[k] = other[k]

    return dicto


def load(filepath: Path, as_dicto: bool = True):
    if not isinstance(filepath, Path):
        filepath = Path(filepath)

    if filepath.suffix in (".yaml", ".yml"):

        with open(filepath, "r") as stream:
            dict_ = yaml.load(stream)

    elif filepath.suffix == ".json":

        with open(filepath, "r") as stream:
            dict_ = json.load(stream)

    elif filepath.suffix == ".xml":

        with open(filepath, "r") as stream:
            dict_ = xmltodict.parse(stream.read())

    else:
        raise Exception("File type not supported.")

    if as_dicto:
        return to_dicto(dict_)
    else:
        return dict_


def dump(dicto: Dicto, filepath: Path):

    if not isinstance(filepath, Path):
        filepath = Path(filepath)

    obj = to_dict(dicto)

    if filepath.suffix in (".yaml", ".yml"):
        with open(filepath, "w") as stream:
            yaml.safe_dump(obj, stream, default_flow_style=False)

    elif filepath.suffix == ".json":
        with open(filepath, "w") as stream:
            json.dump(obj, stream)
    else:
        raise Exception("File type not supported.")
