
import re
from .errors import (RomanNumsError, RomanValidationError)

__version__ = "0.0.1"
__author__ = "Kovalenko Nikolay"
__email__ = "kovalenko.n.r-g@yandex.ru"

CASE_UPPER = 1
CASE_LOWER = -1


def from_roman(rn: str, ignore_case: bool = False):
    """
    Make an integer from roman number.
    :param rn: input roman number.
    :param ignore_case: if True, you can input roman number in lower or upper case.
    :return: positive integer from roman number.
    :rtype: int
    """
    pattern = r"^N|(?=[MDCLXVI])(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
    if not isinstance(rn, str):
        raise RomanNumsError(f"Invalid data type {type(rn)}, must be str")
    match = re.fullmatch(pattern, rn, re.IGNORECASE if ignore_case is True else False)
    if match is None:
        raise RomanNumsError("Number not found")
    if match.group().upper() == "N":
        return 0

    list_3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    list_2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    list_1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    gr = match.groups()

    result = sum([
        list_1.index(gr[3].upper()), list_2.index(gr[2].upper()) * 10,
        list_3.index(gr[1].upper()) * 100, len(gr[0].upper()) * 1000
    ])
    return result


def to_roman(n: int, case: int = CASE_UPPER):
    """
    Make roman number from positive integer.
    :param n: positive integer
    :param case: upper (1) or lower (-1). Default upper (1)
    :return: roman number
    :rtype: str
    """
    if not isinstance(n, int):
        raise RomanNumsError(f"Invalid data type {type(n)}, must be int")
    elif case not in (CASE_UPPER, CASE_LOWER):
        raise RomanNumsError("Not found type of case. Possible values: -1, 1")
    elif n == 0:
        return "N" if case == CASE_UPPER else "n"
    elif n < 0:
        raise RomanNumsError("Only positive integer")

    list_3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    list_2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    list_1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    result = "{}{}{}{}".format(
        (n // 1000) * "M",
        list_3[n // 100 % 10],
        list_2[n // 10 % 10],
        list_1[n % 10]
    )
    return result if case == CASE_UPPER else result.lower()
