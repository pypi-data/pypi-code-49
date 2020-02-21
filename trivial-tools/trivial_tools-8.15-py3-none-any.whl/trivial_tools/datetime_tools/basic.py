# -*- coding: utf-8 -*-
"""

    Инструменты вычисления времени и дат

"""
# встроенные модули
import calendar
from typing import Union
from datetime import timedelta, datetime


def cast_seconds_to_timedelta(value: Union[timedelta, int, float]) -> timedelta:
    """Преобразовать число секунд в экземпляр timedelta (при возможности).

    :param value: число секунд или экземпляр timedelta
    :return: экземпляр timedelta

    >>> cast_seconds_to_timedelta(1)
    datetime.timedelta(seconds=1)
    """
    if isinstance(value, timedelta):
        return value
    return timedelta(seconds=float(value))


def days_in_month(year: int, month: int) -> int:
    """
    Получить число дней в месяце

    >>> days_in_month(2016, 1)
    31

    >>> days_in_month(2019, 4)
    30
    """
    _, length = calendar.monthrange(year, month)
    return length


def hours_in_month(year: int, month: int) -> int:
    """
    Получить число часов в месяце

    >>> hours_in_month(2016, 1)
    744

    >>> hours_in_month(2019, 4)
    720
    """
    result = days_in_month(year, month) * 24
    return result


def get_seconds_diff(old: datetime, new: datetime) -> float:
    """
    Получить число секунд между метками
    """
    return (new - old).total_seconds()


def get_seconds_diff_int(old: datetime, new: datetime) -> int:
    """
    Получить число секунд между метками
    """
    return int(get_seconds_diff(old, new))
