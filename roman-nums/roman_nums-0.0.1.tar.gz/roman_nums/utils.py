
import re
from .errors import RTextError, RomanValidationError

CASE_UPPER = 1
CASE_LOWER = -1
CASE_IGNORE = 0


def rn_validator(rn: str, case: int = CASE_UPPER):
    """
    Check the roman number for validity.
    :param rn: roman number
    :param case: upper (1), lower (-1) or ignore (0) case. Default upper (1).
    :return: True if roman number is valid or False if not.
    :rtype: bool
    """
    if not isinstance(rn, str):
        raise RomanValidationError(f"Invalid data type {type(rn)}, must be str")
    elif case not in (CASE_UPPER, CASE_LOWER, CASE_IGNORE):
        raise RomanValidationError("Not found type of case. Possible values: -1, 0 or 1")

    regex = r"\b(N)\b|\b(?=[MDCLXVI])(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})\b"
    regex_l = r"\b(n)\b|\b(?=[mdclxvi])(m*)(c[md]|d?c{0,3})(x[cl]|l?x{0,3})(i[xv]|v?i{0,3})\b"

    if case == CASE_UPPER:
        return True if re.fullmatch(regex, rn) is not None else False
    if case == CASE_LOWER:
        return True if re.fullmatch(regex_l, rn) is not None else False
    if case == CASE_IGNORE:
        return True if re.fullmatch(regex, rn, re.IGNORECASE) is not None else False


class RText:
    """Class for the work with text: found/replace roman numbers and integers."""
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise RTextError("неверный формат входных данных")
        self.text = text

        self.__regex_int = r"(?<![.,])\b\d+\b(?![.,]\d+)"
        self.__regex_roman = r"\bN\b|\b(?=[MDCLXVI])(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})\b"
        self.__regex_roman_l = r"\bn\b|\b(?=[mdclxvi])(m*)(c[md]|d?c{0,3})(x[cl]|l?x{0,3})(i[xv]|v?i{0,3})\b"

    def rnb(self, case: int = CASE_UPPER):
        """
        Find all roman numbers in input text.
        :param case: upper (1), lower (-1) or ignore(0). Default and recommended upper (1).
        :return: list of all found roman numbers
        :rtype: list
        """
        if case not in (CASE_UPPER, CASE_LOWER, CASE_IGNORE):
            raise RTextError("Not found type of case. Possible values: -1, 0 or 1")

        if case == CASE_UPPER:
            return [r.group() for r in re.finditer(self.__regex_roman, self.text) if len(r.group()) > 0]
        elif case == CASE_LOWER:
            return [r.group() for r in re.finditer(self.__regex_roman_l, self.text) if len(r.group()) > 0]
        elif case == CASE_IGNORE:
            return [r.group() for r in re.finditer(self.__regex_roman, self.text, re.IGNORECASE) if len(r.group()) > 0]

    def nb(self):
        """
        Find all positive integers in input text.
        :return: list of all found integers.
        :rtype: list
        """
        return [int(x) for x in re.findall(self.__regex_int, self.text)]

    def from_roman(self, case: int = CASE_UPPER):
        """
        Replace all found roman numbers to integers.
        :param case: upper (1), lower (-1) or ignore (0). Default and recommended upper (1).
        :return: input text with replacements roman to integers.
        :rtype: str
        """
        if case not in (CASE_UPPER, CASE_LOWER, CASE_IGNORE):
            raise RTextError("Not found type of case. Possible values: -1, 0 or 1")

        if case == CASE_UPPER:
            return re.sub(self.__regex_roman, lambda rn: self._repr_from_roman(rn), self.text)
        elif case == CASE_LOWER:
            return re.sub(self.__regex_roman_l, lambda rn: self._repr_from_roman(rn), self.text)
        elif case == CASE_IGNORE:
            return re.sub(self.__regex_roman, lambda rn: self._repr_from_roman(rn), self.text, flags=re.IGNORECASE)

    @staticmethod
    def _repr_from_roman(rn):
        if len(rn.group()) == 0:
            return ""
        if str(rn.group()).upper() == "N":
            return "0"
        list_3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        list_2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        list_1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        gr = rn.groups()

        result = sum([
            list_1.index(gr[3].upper()), list_2.index(gr[2].upper()) * 10,
            list_3.index(gr[1].upper()) * 100, len(gr[0]) * 1000
        ])
        return str(result)

    def to_roman(self, case: int = CASE_UPPER):
        """
        Replace all found integers to roman numbers.
        :param case: upper (1) or lower (-1). Default upper (1).
        :return: input text with replacements integers to roman numbers.
        :rtype: str
        """
        if case not in (CASE_UPPER, CASE_LOWER):
            raise RTextError("Not found type of case. Possible values: -1 or 1")

        return re.sub(self.__regex_int, lambda n: self._repr_to_roman(int(n.group()), case), self.text)

    @staticmethod
    def _repr_to_roman(n, case):
        if n == 0:
            return "N" if case == CASE_UPPER else "n"
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

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"{self.text[:50]}..." if len(self.text) > 53 else self.text

