# -*- coding: utf-8 -*-

"""

    Форматирование прошедшего времени в виде удобной строки

"""
# встроенные модули
from datetime import timedelta
from typing import Tuple, Optional

# модули проекта
from trivial_tools.datetime_tools.basic import cast_seconds_to_timedelta


__all__ = [
    'passed_time',
    'passed_time_short'
]


def passed_time(delta: timedelta) -> str:
    """
    Трансформировать timedelta в описание времени в форме '6 дней, 4 часа, 35 минут'
    """
    weeks, days, hours, minutes, seconds = calculate_time(delta)

    result = join(weeks, days, hours, minutes, seconds)

    if not result:
        return '0 секунд'
    return result


def passed_time_short(delta: timedelta) -> str:
    """
    Трансформировать timedelta в описание времени в форме '6д 4ч 35м'
    """
    weeks, days, hours, minutes, seconds = calculate_time(delta)

    result = join_short(weeks, days, hours, minutes, seconds)

    if not result:
        return '0с'
    return result


def calculate_time(delta: timedelta) -> Tuple[str, str, str, str, str]:
    """
    Рассчитать временные показатели
    """
    delta = cast_seconds_to_timedelta(delta)

    weeks, rest_days = form_weeks(delta)
    delta = timedelta(days=rest_days, seconds=delta.seconds)

    days = form_days(delta)
    delta = timedelta(days=0, seconds=delta.seconds)

    hours, rest_seconds = form_hours(delta)
    delta = timedelta(days=0, hours=0, seconds=rest_seconds)

    minutes, rest_seconds = form_minutes(delta)
    delta = timedelta(days=0, hours=0, minutes=0, seconds=rest_seconds)

    seconds = form_seconds(delta)

    return weeks, days, hours, minutes, seconds


def join(weeks: str, days: str, hours: str, minutes: str, seconds: str) -> str:
    """
    Сшить все компоненты вместе
    """
    result = ', '.join([x for x in [weeks, days, hours, minutes, seconds] if x is not None])
    return result


def join_short(weeks: str, days: str, hours: str, minutes: str, seconds: str) -> str:
    """
    Сшить все компоненты вместе (укороченно)
    """
    result = ''.join([x for x in [
        weeks.split()[0] + 'н ' if weeks else '',
        days.split()[0] + 'д ' if days else '',
        hours.split()[0] + 'ч ' if hours else '',
        minutes.split()[0] + 'м ' if minutes else '',
        seconds.split()[0] + 'с' if seconds else ''
    ] if x is not None])
    return result.strip()


def form_weeks(delta: timedelta) -> Tuple[Optional[str], int]:
    """
    Сформировать описание недель
    """
    days = delta.days

    if days < 7:
        return None, days

    weeks = days // 7
    rest = days - weeks * 7

    if weeks in (1, 21, 31, 41, 51, 61, 71, 81, 91):
        result = f'{weeks} неделя', rest

    elif weeks in (2, 3, 4):
        result = f'{weeks} недели', rest

    else:
        result = f'{weeks} недель', rest

    return result


def form_days(delta: timedelta) -> Optional[str]:
    """
    Сформировать описание дней
    """
    if not delta.days:
        return None

    days = delta.days

    if days in (1, 21, 31, 41, 51, 61, 71, 81, 91):
        result = f'{days} день'

    elif days in (2, 3, 4):
        result = f'{days} дня'

    else:
        result = f'{days} дней'

    return result


def form_hours(delta: timedelta) -> Tuple[Optional[str], int]:
    """
    Сформировать описание часов
    """
    hours = delta.seconds // 3600

    if not hours:
        return None, delta.seconds

    rest = delta.seconds % (hours * 3600)

    d1 = abs(hours) % 100
    d2 = d1 % 10

    if d2 in (1,):
        result = f'{hours} час', rest

    elif d2 in (2, 3, 4) and d1 != 14:
        result = f'{hours} часа', rest

    else:
        result = f'{hours} часов', rest

    return result


def form_minutes(delta: timedelta) -> Tuple[Optional[str], int]:
    """
    Сформировать описание минут
    """
    minutes = delta.seconds // 60

    if not minutes:
        return None, delta.seconds

    rest = delta.seconds % (minutes * 60)

    d1 = abs(minutes) % 100
    d2 = d1 % 10

    if d2 in (1,) and minutes not in (11, 12, 13):
        result = f'{minutes} минута', rest

    elif d2 in (2, 3, 4) and minutes not in (11, 12, 13, 14):
        result = f'{minutes} минуты', rest

    else:
        result = f'{minutes} минут', rest

    return result


def form_seconds(delta: timedelta) -> Optional[str]:
    """
    Сформировать описание секунд
    """
    seconds = delta.seconds

    if not seconds:
        return None

    d1 = abs(seconds) % 100
    d2 = d1 % 10

    if d2 in (1,) and seconds not in (11, 12, 13):
        result = f'{seconds} секунда'

    elif d2 in (2, 3, 4) and seconds not in (11, 12, 13):
        result = f'{seconds} секунды'

    else:
        result = f'{seconds} секунд'

    return result
