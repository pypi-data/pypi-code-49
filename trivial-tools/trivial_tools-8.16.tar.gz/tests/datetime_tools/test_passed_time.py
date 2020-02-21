# -*- coding: utf-8 -*-
"""

    Тесты описания прошедшего времени

"""
# встроенные модули
from datetime import timedelta

# модули проекта
from trivial_tools.datetime_tools.passed_time import form_minutes, form_weeks, form_days
from trivial_tools.datetime_tools.passed_time import form_seconds, form_hours, passed_time


def test_weeks():
    """
    Проверить отображение недель
    """
    assert form_weeks(timedelta(days=0)) == (None, 0)
    assert form_weeks(timedelta(days=2)) == (None, 2)
    assert form_weeks(timedelta(days=5)) == (None, 5)
    assert form_weeks(timedelta(days=7)) == ('1 неделя', 0)
    assert form_weeks(timedelta(days=10)) == ('1 неделя', 3)
    assert form_weeks(timedelta(days=14)) == ('2 недели', 0)
    assert form_weeks(timedelta(days=21)) == ('3 недели', 0)
    assert form_weeks(timedelta(days=28)) == ('4 недели', 0)
    assert form_weeks(timedelta(days=35)) == ('5 недель', 0)
    assert form_weeks(timedelta(days=42)) == ('6 недель', 0)


def test_days():
    """
    Проверить отображение дней
    """
    assert form_days(timedelta(days=0)) is None
    assert form_days(timedelta(days=1)) == '1 день'
    assert form_days(timedelta(days=2)) == '2 дня'
    assert form_days(timedelta(days=3)) == '3 дня'
    assert form_days(timedelta(days=4)) == '4 дня'
    assert form_days(timedelta(days=5)) == '5 дней'
    assert form_days(timedelta(days=6)) == '6 дней'


def test_hours():
    """
    Проверить отображение часов
    """
    assert form_hours(timedelta(seconds=0)) == (None, 0)
    assert form_hours(timedelta(seconds=15)) == (None, 15)
    assert form_hours(timedelta(minutes=1)) == (None, 60)
    assert form_hours(timedelta(minutes=30)) == (None, 1800)
    assert form_hours(timedelta(minutes=59)) == (None, 3540)
    assert form_hours(timedelta(hours=0)) == (None, 0)
    assert form_hours(timedelta(hours=1)) == ('1 час', 0)
    assert form_hours(timedelta(hours=3)) == ('3 часа', 0)
    assert form_hours(timedelta(hours=7)) == ('7 часов', 0)
    assert form_hours(timedelta(hours=10)) == ('10 часов', 0)
    assert form_hours(timedelta(hours=15)) == ('15 часов', 0)
    assert form_hours(timedelta(hours=23)) == ('23 часа', 0)


def test_minutes():
    """
    Проверить отображение минут
    """
    assert form_minutes(timedelta(seconds=0)) == (None, 0)
    assert form_minutes(timedelta(seconds=15)) == (None, 15)
    assert form_minutes(timedelta(minutes=1)) == ('1 минута', 0)
    assert form_minutes(timedelta(minutes=2)) == ('2 минуты', 0)
    assert form_minutes(timedelta(minutes=5)) == ('5 минут', 0)
    assert form_minutes(timedelta(minutes=7)) == ('7 минут', 0)
    assert form_minutes(timedelta(minutes=10)) == ('10 минут', 0)
    assert form_minutes(timedelta(minutes=11)) == ('11 минут', 0)
    assert form_minutes(timedelta(minutes=12)) == ('12 минут', 0)
    assert form_minutes(timedelta(minutes=13)) == ('13 минут', 0)
    assert form_minutes(timedelta(minutes=14)) == ('14 минут', 0)
    assert form_minutes(timedelta(minutes=15)) == ('15 минут', 0)
    assert form_minutes(timedelta(minutes=16)) == ('16 минут', 0)
    assert form_minutes(timedelta(minutes=17)) == ('17 минут', 0)
    assert form_minutes(timedelta(minutes=19)) == ('19 минут', 0)
    assert form_minutes(timedelta(minutes=21)) == ('21 минута', 0)
    assert form_minutes(timedelta(minutes=46)) == ('46 минут', 0)
    assert form_minutes(timedelta(minutes=53)) == ('53 минуты', 0)
    assert form_minutes(timedelta(minutes=59)) == ('59 минут', 0)


def test_seconds():
    """
    Проверить отображение секунд
    """
    assert form_seconds(timedelta(seconds=0)) is None
    assert form_seconds(timedelta(seconds=1)) == '1 секунда'
    assert form_seconds(timedelta(seconds=2)) == '2 секунды'
    assert form_seconds(timedelta(seconds=3)) == '3 секунды'
    assert form_seconds(timedelta(seconds=5)) == '5 секунд'
    assert form_seconds(timedelta(seconds=7)) == '7 секунд'
    assert form_seconds(timedelta(seconds=10)) == '10 секунд'
    assert form_seconds(timedelta(seconds=11)) == '11 секунд'
    assert form_seconds(timedelta(seconds=12)) == '12 секунд'
    assert form_seconds(timedelta(seconds=13)) == '13 секунд'
    assert form_seconds(timedelta(seconds=17)) == '17 секунд'
    assert form_seconds(timedelta(seconds=19)) == '19 секунд'
    assert form_seconds(timedelta(seconds=20)) == '20 секунд'
    assert form_seconds(timedelta(seconds=21)) == '21 секунда'
    assert form_seconds(timedelta(seconds=22)) == '22 секунды'
    assert form_seconds(timedelta(seconds=23)) == '23 секунды'
    assert form_seconds(timedelta(seconds=24)) == '24 секунды'
    assert form_seconds(timedelta(seconds=25)) == '25 секунд'
    assert form_seconds(timedelta(seconds=26)) == '26 секунд'
    assert form_seconds(timedelta(seconds=30)) == '30 секунд'
    assert form_seconds(timedelta(seconds=31)) == '31 секунда'
    assert form_seconds(timedelta(seconds=32)) == '32 секунды'
    assert form_seconds(timedelta(seconds=33)) == '33 секунды'
    assert form_seconds(timedelta(seconds=46)) == '46 секунд'
    assert form_seconds(timedelta(seconds=51)) == '51 секунда'
    assert form_seconds(timedelta(seconds=53)) == '53 секунды'
    assert form_seconds(timedelta(seconds=59)) == '59 секунд'


def test_combined():
    """
    Общая проверка работы всех блоков
    """
    delta = timedelta(seconds=0)
    assert passed_time(delta) == '0 секунд'

    delta = timedelta(weeks=4, days=6, hours=22, minutes=47, seconds=17)
    assert passed_time(delta) == '4 недели, 6 дней, 22 часа, 47 минут, 17 секунд'

    delta = timedelta(seconds=3601)
    assert passed_time(delta) == '1 час, 1 секунда'

    delta = timedelta(days=33)
    assert passed_time(delta) == '4 недели, 5 дней'

    delta = timedelta(seconds=53601)
    assert passed_time(delta) == '14 часов, 53 минуты, 21 секунда'

    delta = timedelta(hours=25, seconds=86)
    assert passed_time(delta) == '1 день, 1 час, 1 минута, 26 секунд'
