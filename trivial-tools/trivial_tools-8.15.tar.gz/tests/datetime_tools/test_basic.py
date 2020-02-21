# -*- coding: utf-8 -*-
"""

    Тесты простых операций преобразования времени

"""
# встроенные модули
from datetime import datetime

# сторонние модули
import pytest

# модули проекта
from trivial_tools.datetime_tools.basic import get_seconds_diff, get_seconds_diff_int


@pytest.fixture()
def time_1():
    return datetime(2019, 1, 1, 1, 1, 1, 530)


@pytest.fixture()
def time_2():
    return datetime(2019, 1, 1, 1, 1, 21, 740)


def test_get_seconds_diff(time_1, time_2):
    """
    Должен выдавать разницу в секундах
    """
    assert pytest.approx(get_seconds_diff(time_1, time_2)) == 20.00021


def test_get_seconds_diff_int(time_1, time_2):
    """
    Должен выдавать разницу в секундах
    """
    assert get_seconds_diff_int(time_1, time_2) == 20
