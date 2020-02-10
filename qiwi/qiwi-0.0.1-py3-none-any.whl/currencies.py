# -*- coding: utf-8 -*-
from typing import Union, Optional, Any


class CurrencyError(TypeError, ValueError):
    pass


class CompareCurrencyError(CurrencyError):
    def __init__(self, message: Optional[str] = None):
        super().__init__(
            message or f'Currency classes can be compared only with int, float, base Currency class and with '
                       f'a currency with the same code')


class CurrencyMathError(CurrencyError):
    def __init__(self, message):
        super().__init__(message)


class AmountTypeError(CurrencyError):
    pass


class AmountValueError(CurrencyError):
    pass


class _Currency:
    __slots__ = ('_amount', '_http')

    code: Optional[int] = None

    def __init__(self, amount: Union[int, float] = 0):
        self._amount = amount

    def __new__(cls, amount: Union[int, float] = 0):
        if not isinstance(amount, (int, float)):
            raise AmountTypeError(f'Invalid amount argument type: {amount.__class__.__name__}, '
                                  f'there are only int and float available')

        if amount < 0:
            raise AmountValueError('Currency amount cannot be less than 0')

        return super().__new__(cls)

    def __setattr__(self, name, value):
        if name == 'code':
            raise CurrencyError('Currency code cannot be changed')

        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'code':
            raise CurrencyError('Currency code cannot be deleted')

        super().__delattr__(name)

    @property
    def amount(self) -> Union[int, float]:
        return self._amount

    @amount.setter
    def amount(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise AmountTypeError(f'Invalid value argument type: {value.__class__.__name__}, '
                                  f'there are only int and float available')

        self._amount = value

    def __repr__(self):
        return "<{0.__class__.__name__} code={0.code} amount={0._amount}>".format(self)

    def __hash__(self):
        return self.code

    # to number conversion

    def __int__(self):
        return int(self._amount)

    def __float__(self):
        return float(self._amount)

    # math operations

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                currency = super(self.__class__, self).__new__(self.__class__, self._amount + other._amount)
                currency.__init__(self._amount + other._amount)

                return currency

        # TODO
        raise CurrencyMathError('# TODO')

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                currency = super(self.__class__, self).__new__(self.__class__, self._amount - other._amount)
                currency.__init__(self._amount + other._amount)

                return currency

        # TODO
        raise CurrencyMathError('# TODO')

    # <, >, <=, >=, ==, !=

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self._amount < other

        if isinstance(other, self.__class__):
            if self.code == other.code:
                return self._amount < other._amount

        raise CompareCurrencyError

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self._amount > other

        if isinstance(other, self.__class__):
            if self.code == other.code:
                return self._amount > other._amount

        raise CompareCurrencyError

    def __le__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self._amount == other

        if isinstance(other, self.__class__):
            if self.code == other.code:
                return self._amount == other._amount

        raise CompareCurrencyError

    def __ne__(self, other):
        return not self.__eq__(other)


class KZT(_Currency):
    code = 398


class RUB(_Currency):
    code = 643


class CHF(_Currency):
    code = 756


class USD(_Currency):
    code = 840


class TJS(_Currency):
    code = 972


class EUR(_Currency):
    code = 978


class UAH(_Currency):
    code = 980


def try_currency(code: int, amount: Union[int, float] = 0) -> Union[_Currency, int]:
    for cls in _Currency.__subclasses__():
        if code == getattr(cls, 'code'):
            return cls(amount)

    return amount


print(EUR)