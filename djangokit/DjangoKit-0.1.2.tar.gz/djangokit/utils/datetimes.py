#
# Copyright (c) 2012, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the BSD 3-Clause License.
#
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime


def from_unixtime(timestamp=0, tzinfo=timezone.utc):
    if not isinstance(timestamp, int):
        timestamp = int(timestamp)
    dt = datetime.fromtimestamp(timestamp)
    return dt.replace(tzinfo=tzinfo)


def from_javascript(timestamp=0, tzinfo=timezone.utc):
    if not isinstance(timestamp, int):
        timestamp = int(timestamp)
    microsecond = (timestamp % 1000) * 1000
    timestamp = int(timestamp / 1000.0)
    dt = from_unixtime(timestamp, tzinfo=timezone.utc)
    if not microsecond:
        return dt
    return dt.replace(microsecond=microsecond)


def datetime_round(dt=None, minute=True, hour=False, day=False):
    """
    Округление времени до секунды, минуты, часа или дня.
    По умолчанию до минуты.
        до дня:     rounded(day=True)
        до часа:    rounded(hour=True)
        до минуты:  rounded()
        до секунды: rounded(minute=False)

    Если нужно округлить заданное время,то оно передаётся в
    параметре `dt`.

    На вход можно подавать как naive, так и aware, результатом будет
    аналогичное.
    Если генерируется новое время, то результатом будет naive при
    settings.USE_TZ = False, иначе - aware.
    """
    if not isinstance(dt, timezone.datetime):
        dt = timezone.now()

    dt = dt.replace(microsecond=0)

    if day:
        dt = dt.replace(hour=0, minute=0, second=0)
    elif hour:
        dt = dt.replace(minute=0, second=0)
    elif minute:
        dt = dt.replace(second=0)

    return dt


def datetime_local(value=None):
    """
    Переводит значение в текущую зону локального времени.
    На вход можно подавать как naive, так и aware, результатом будет
    аналогичное.
    Если генерируется новое время, то результатом будет naive при
    settings.USE_TZ = False, иначе - aware.
    """
    if not value:
        value = timezone.now()
    if value and timezone.is_naive(value):
        return value
    return timezone.localtime(value, value.tzinfo)


def datetime_server(value=None):
    """
    Переводит значение в зону серверного времени.
    На вход можно подавать как naive, так и aware, результатом будет
    аналогичное.
    Если генерируется новое время, то результатом будет naive при
    settings.USE_TZ = False, иначе - aware.
    """
    if not value:
        value = timezone.now()

    if timezone.is_naive(value):
        return value

    tz_curr = timezone.get_current_timezone()
    tz_serv = timezone.get_default_timezone()

    if tz_curr != tz_serv:
        timezone.activate(tz_serv)
        value = timezone.localtime(value, tz_serv)
        timezone.activate(tz_curr)
    else:
        value = timezone.localtime(value, tz_curr)

    return value


def datetime_naive(value=None):
    """
    Переводит значение в текущую зону локального времени.
    Возвращает простое время.
    """
    return datetime_local(value).replace(tzinfo=None)


def datetime_aware(value=None):
    """
    Переводит значение (даже простое) в текущую зону локального времени.
    Возвращает aware c текущей временной зоной.
    """
    tzinfo = timezone.get_current_timezone()
    if value and timezone.is_naive(value):
        return value.replace(tzinfo=tzinfo)
    return datetime_local(value).replace(tzinfo=tzinfo)


def datetime_server_naive(value=None):
    """
    Переводит значение в зону серверного времени settings.TIME_ZONE.
    Возвращает простое время.
    """
    return datetime_server(value).replace(tzinfo=None)


def datetime_server_aware(value=None):
    """
    Переводит значение (даже простое) в зону серверного времени.
    Возвращает aware c временной зоной сервера.
    """
    tzinfo = timezone.get_default_timezone()
    if value and timezone.is_naive(value):
        return value.replace(tzinfo=tzinfo)
    return datetime_server(value).replace(tzinfo=tzinfo)


def server_date():
    """
    Возвращает текущую дату сервера по settings.TIME_ZONE.
    """
    return datetime_server_naive().date()


def server_time():
    """
    Возвращает текущее время сервера по settings.TIME_ZONE.
    """
    return datetime_server_naive().time()


def parse_datetime_to_naive(value):
    """
    Парсер строкового значения (naive или aware) в локальное naive.
    """
    value = parse_datetime(value)
    if value:
        return datetime_naive(value)
    return None


def parse_datetime_to_aware(value):
    """
    Парсер строкового значения (naive или aware) в локальное aware.
    """
    value = parse_datetime(value)
    if value:
        return datetime_aware(value)
    return None


def parse_datetime_to_server_naive(value):
    """
    Парсер строкового значения (naive или aware) в серверное naive.
    """
    value = parse_datetime(value)
    if value:
        return datetime_server_naive(value)
    return None


def parse_datetime_to_server_aware(value):
    """
    Парсер строкового значения (naive или aware) в серверное aware.
    """
    value = parse_datetime(value)
    if value:
        return datetime_server_aware(value)
    return None
