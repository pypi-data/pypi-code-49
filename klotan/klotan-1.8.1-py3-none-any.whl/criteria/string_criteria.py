import re
from keyword import iskeyword

from klotan.criteria.core import fn_to_criteria

@fn_to_criteria
def regex(x):
    return lambda y: re.match(x, y) is not None

@fn_to_criteria
def is_capitalized():
    return lambda y: y.istitle()

@fn_to_criteria
def is_lower():
    return lambda y: y.islower()

@fn_to_criteria
def is_upper():
    return lambda y: y.isupper()

@fn_to_criteria
def is_alpha_only():
    return lambda y: y.isalpha()

@fn_to_criteria
def is_numeric_only():
    return lambda y: y.isdigit()

@fn_to_criteria
def is_alphanumeric_only():
    return lambda y: y.isalnum()

@fn_to_criteria
def is_valid_python_identifier():
    return lambda y: y.isidentifier()

@fn_to_criteria
def is_python_keyword():
    return lambda y: iskeyword(y)

@fn_to_criteria
def is_printable():
    return lambda y: y.isprintable()

@fn_to_criteria
def is_space():
    return lambda y: y.isspace()

@fn_to_criteria
def startswith(start):
    return lambda y: y.startswith(start)

@fn_to_criteria
def endswith(end):
    return lambda y: y.endswith(end)