import random
import uuid
import exrex
import json

class Message:
    def __init__(self, msg):
        self.msg = msg

def rand_str(min_length=5, max_length=20):
    """Return a random non-empty string."""
    if min_length <= 0:
        raise ValueError("min_length must be greater than 0.")
    if min_length > max_length:
        raise ValueError("min_length must by greater than or equal to max_length.")
    length = random.randint(min_length-1, max_length-1)
    cfg = "[a-z A-Z 0-9][a-z A-Z 0-9 ]{{{}}}".format(length)
    return exrex.getone(cfg)

def rand_int(min_value=1, max_value=1000):
    """Return a randon int."""
    if min_value > max_value:
        raise ValueError("max_length must be greater than or equal to min_length.")
    return random.randint(min_value, max_value)

def rand_uuid(as_string=True):
    """Return a random uuid."""
    return str(uuid.uuid4()) if as_string else uuid.uuid4()


def value_from_dict(dict_, key):
    """Return the value for the key.

    Parameters
    ----------
    dict_: dict
        Dict containing the key
    key: str
        Key to lookup in the dict
    """
    return dict_[key]

def dict_has_value(dict_, key):
    """Return True if the key is contained in the dict.

    Parameters
    ----------
    dict_: dict
        Dict to check in
    key: str
        Key to check
    """
    return key in dict_

def attr_from_obj(obj, name):
    """Return the value of the attribute name.

    Parameters
    ----------
    obj: object
        Object with attribute name
    name: str
        Attribute name to return
    """
    return getattr(obj, name)

def obj_has_attr(obj, name):
    """Return True if the object has the attribute.

    Parameters
    ----------
    obj: object
        Object to check
    name: str
        Attribute name to check
    """
    return hasattr(obj, name)
