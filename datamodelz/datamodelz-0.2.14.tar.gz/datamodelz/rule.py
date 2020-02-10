import re
import logging
from typing import Any

from .consts import frequencies

"""
Rules are the base class for the very basic checks. They ensure that a type exists before more comlicated checks are run.

The important thing when writing an error for a rule is the error is the *opposite* of what the rule does.
"""


class Rule:
    def __init__(self, name: str, funct, error=""):
        self.name = name  # the message printed out when the rule fails
        self.funct = funct
        self.error = error

    def run(self, x) -> bool:
        logging.debug("running rule {} on {}".format(self.name, x))
        return self.funct(x)


no_error = Rule("there is an error when querying for the company",
                lambda x: x and (type(x) != dict or "error" not in x))

type_str = Rule("Type is string", lambda x: x is not None and type(x) == str)
type_int = Rule("Type is integer", lambda x: x is not None and type(x) == int)
type_bool = Rule("Type is boolean", lambda x: x is not None and type(x) == bool)  # check not None first
type_dct = Rule("Type is dictionary", lambda x: x is not None and type(x) == dict)
type_lst = Rule("Type is list", lambda x: x is not None and type(x) == list)
type_float = Rule("Type is float", lambda x: x is not None and type(x) in [int, float])

type_url = Rule("Is valid url (must have https://www.)",
                lambda x: x is not None and len(re.findall(r"^https://www\.(.+)\.(.+)", str(x))) > 0)

type_https = Rule("Is valid domain (must have https://)",
                  lambda x: x is not None and len(re.findall(r"^https://(.+)\.(.+)", str(x))) > 0)

type_domain = Rule("Is valid domain",
                   lambda x: x is not None and len(re.findall(r"(.+)\.(.+)", str(x))) > 0)

type_date = Rule("Is valid date", lambda x: x is not None and x)  # TODO: update this!

type_ticker = Rule("Is valid ticker, must have at least 1 letter and if a dot then at least 1 letter after ",
                   lambda x: x is not None and re.findall(r"^(\w+)((\.)\w+)?", str(x)))

non_empty_field = Rule("Is not None and not empty", lambda x: x is not None and x)

not_none = Rule("Is not None", lambda x: x is not None)

frequency_name = Rule("Is a valid frequency name",
                      lambda x: x is not None and x in frequencies)


def has_field(field_name):  # uses string name (field in x)
    return Rule("Has field `{}`".format(field_name),
                lambda x: x is not None and field_name in x,
                "does not have field `{}`".format(field_name))


def has_non_empty_field(field):  # uses field - not the name
    return Rule("Has field `{}`".format(field.name),
                lambda x: field is not None and field and (type(field) == list or
                                                           (field.value is not None and field.value)))


def in_field(field_names):  # uses actual field
    return Rule("Is within the fields `{}`".format(field_names),
                lambda x: x is not None and x in field_names)


def len_eq(number):
    return Rule("Has length `{}`".format(number),
                lambda x: x is not None and len(x) == number)


def len_gt(number):
    return Rule("Has length greater than `{}`".format(number),
                lambda x: x is not None and len(x) > number)


def len_lt(number):
    return Rule("Has length less than `{}`".format(number),
                lambda x: x is not None and len(x) < number)


def gte(number):
    return Rule("Is greater than or equal to `{}`".format(number),
                lambda x: x is not None and x >= number)


def lte(number):
    return Rule("Is less than of equal to `{}`".format(number), lambda x: x is not None and x <= number)


def matches_url(field_name):
    return Rule("Has a url for `{}`".format(field_name),
                lambda x: x is not None and matches_url_funct(field_name, x))


def matches_url_funct(field, url):
    return len(re.findall(r"https://(www\.)?{name}\.com.*".format(name=field.name), str(url))) > 0
