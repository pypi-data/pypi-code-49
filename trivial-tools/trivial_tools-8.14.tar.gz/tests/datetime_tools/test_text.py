# -*- coding: utf-8 -*-
"""

    Тесты преобразования дат в текст и обратно

"""
# встроенные модули
from unittest.mock import patch
from datetime import datetime, date

# сторонние модули
import pytest

# модули проекта
from trivial_tools.datetime_tools.text import *


@pytest.fixture()
def timestamp():
    return 1576052808.2121792


@pytest.fixture()
def str_date1():
    return '2019-12-01'


@pytest.fixture()
def str_date2():
    return '2019-12-02'


@pytest.fixture()
def str_time_s():
    return '13:27:34'


@pytest.fixture()
def str_time_ms():
    return '13:27:34.123456'


@pytest.fixture()
def date1():
    return date(2019, 12, 1)


@pytest.fixture()
def date2():
    return date(2019, 12, 2)


@pytest.fixture()
def datetime0():
    return datetime(2019, 12, 1, 13, 27, 34)


@pytest.fixture()
def datetime1():
    return datetime(2019, 12, 1, 13, 27, 34, 123456)


@pytest.fixture()
def datetime1_str_s():
    return '2019-12-01 13:27:34'


@pytest.fixture()
def datetime1_str_ms():
    return '2019-12-01 13:27:34.123456'


def test_parse_date(date1, str_date1):
    """
    Обработка даты
    """
    assert parse_date(str_date1) == date1


def test_parse_dates(date1, date2, str_date1, str_date2):
    """
    Распарсить множество дат
    """
    assert parse_dates([str_date1, str_date2]) == [date1, date2]


def test_parse_time(datetime1, datetime1_str_s, datetime1_str_ms):
    """
    Преобразовать текст в объект времени
    """
    fmt = "%Y-%m-%d %H:%M:%S"
    assert parse_time(datetime1_str_s, fmt) == datetime.strptime(datetime1_str_s, fmt)

    fmt = "%Y-%m-%d %H:%M:%S.%f"
    assert parse_time(datetime1_str_ms, fmt) == datetime.strptime(datetime1_str_ms, fmt)


def test_parse_time_s(datetime0, datetime1_str_s):
    """
    Преобразовать текст в объект времени с точностью до секунд
    """
    assert parse_time_s(datetime1_str_s) == datetime0


def test_parse_time_ms(datetime1, datetime1_str_ms):
    """
    Преобразовать текст в объект времени с точностью до микросекунд
    """
    assert parse_time_ms(datetime1_str_ms) == datetime1


@patch('trivial_tools.datetime_tools.text.datetime')
def test_cur_time(mocked_time, datetime1, str_time_s):
    """
    Получить строку с текущим временем
    """
    mocked_time.now.return_value = datetime1
    assert cur_time("%H:%M:%S") == str_time_s


@patch('trivial_tools.datetime_tools.text.datetime')
def test_cur_time_s(mocked_time, datetime1, str_time_s):
    """
    Получить строку с текущим временем с точностью до секунд
    """
    mocked_time.now.return_value = datetime1
    assert cur_time_s() == str_time_s


@patch('trivial_tools.datetime_tools.text.datetime')
def test_cur_time_ms(mocked_time, datetime1, str_time_ms):
    """
    Получить строку с текущим временем с точностью до микросекунд
    """
    mocked_time.now.return_value = datetime1
    assert cur_time_ms() == str_time_ms


def test_timestamp_to_str(timestamp):
    """
    Преобразовать timestamp в текстовую форму.
    """
    assert timestamp_to_str(timestamp) == '2019-12-11 11:26:48'


def test_date_to_text(date1, str_date1):
    """
    Преобразовать время в виде date в текстовую форму
    """
    assert date_to_text(date1) == str_date1


def test_datetime_to_text(datetime1, str_date1, datetime1_str_s):
    """
    Преобразовать время в виде datetime в текстовую форму
    """
    assert datetime_to_text(datetime1, "%Y-%m-%d") == str_date1
    assert datetime_to_text(datetime1, "%Y-%m-%d %H:%M:%S") == datetime1_str_s


def test_datetime_to_text_s(datetime1, datetime1_str_s):
    """
    Преобразовать время в виде datetime в текстовую форму
    """
    assert datetime_to_text_s(datetime1) == datetime1_str_s


def test_datetime_to_text_ms(datetime1, datetime1_str_ms):
    """
    Преобразовать время в виде datetime в текстовую форму
    """
    assert datetime_to_text_ms(datetime1) == datetime1_str_ms
