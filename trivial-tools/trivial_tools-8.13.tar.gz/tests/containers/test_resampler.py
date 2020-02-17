# -*- coding: utf-8 -*-
"""

    Тесты ресемплировщика

"""
# встроенные модули
from datetime import datetime

# сторонние модули
import pytest

# модули проекта
from trivial_tools.containers.class_resampler import Resampler


@pytest.fixture()
def var_a():
    return datetime(2019, 12, 1, 12, 0, 0), 'A'


@pytest.fixture()
def var_b():
    return datetime(2019, 12, 1, 12, 0, 5), 'B'


@pytest.fixture()
def var_c():
    return datetime(2019, 12, 1, 12, 0, 10), 'C'


@pytest.fixture()
def var_d():
    return datetime(2019, 12, 1, 12, 0, 15), 'D'


@pytest.fixture()
def var_e():
    return datetime(2019, 12, 1, 12, 0, 20), 'E'


@pytest.fixture()
def var_items(var_a, var_b, var_c, var_d, var_e):
    return [var_a, var_b, var_c, var_d, var_e]


def test_creation():
    """
    Проверка создания
    """
    r = Resampler()
    assert r.max_gap == 30
    assert r.datetime_index == 0


def test_str(var_a):
    """
    Проверка текстового представления
    """
    r = Resampler()
    assert str(r) == 'Resampler[None]'

    r = Resampler(40, 0)
    list(r.iter_push(var_a))
    assert str(r) == 'Resampler[2019-12-01 12:00:00]'


def test_repr():
    """
    Проверка текстового представления
    """
    r = Resampler()
    assert repr(r) == 'Resampler(max_gap=30, datetime_index=0, placeholder=None)'

    r = Resampler(40, 4)
    assert repr(r) == 'Resampler(max_gap=40, datetime_index=4, placeholder=None)'

    r = Resampler(40, 4, 'Fail!')
    assert repr(r) == "Resampler(max_gap=40, datetime_index=4, placeholder='Fail!')"


def test_iter_push(var_items):
    """
    Должен выдавать генератор с набором заполнителей
    """
    r = Resampler()

    ref = 0
    for payload in var_items:
        for each in r.iter_push(payload):
            assert each[0].second == ref
            ref += 1


def test_same_time(var_a, var_b, var_c, var_d, var_e):
    """
    Проверка получения нескольких значений с одной меткой времени
    """
    r = Resampler()
    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 0), 'A')))
    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 0), 'B')))
    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 0), 'C')))
    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 0), 'D')))
    assert r.previous == [datetime(2019, 12, 1, 12, 0, 0), 'D']


def test_wrong_time():
    """
    Проверка получения значения с неправильным временем
    """
    r = Resampler()

    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 9), 'A')))
    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 0), 'B')))
    list(r.iter_push((datetime(2019, 12, 1, 12, 0, 15), 'C')))

    gen = r.iter_push((datetime(2019, 12, 1, 12, 0, 17), 'D'))

    assert next(gen) == [datetime(2019, 12, 1, 12, 0, 16), 'C']
    assert next(gen) == [datetime(2019, 12, 1, 12, 0, 17), 'D']


def test_empty_payload():
    """
    Проверить отсутствие срабатывания при подаче пустого значения
    """
    r = Resampler()
    list(r.iter_push(()))
    assert r.previous is None


def test_long_gap():
    """
    Проверить заполнение при слишком больших паузах
    """
    r = Resampler(max_gap=4, placeholder='null')

    package = [
        (datetime(2019, 12, 1, 12, 0, 0), 'A'),
        (datetime(2019, 12, 1, 12, 0, 4), 'B'),
        (datetime(2019, 12, 1, 12, 0, 8), 'C'),
        (datetime(2019, 12, 1, 12, 0, 15), 'D'),
        (datetime(2019, 12, 1, 12, 0, 19), 'E')
    ]

    ref = iter([
        'A', 'A', 'A', 'A', 'B',
        'B', 'B', 'B', 'C',
        'null', 'null', 'null', 'null', 'null', 'null', 'D',
        'D', 'D', 'D', 'E'
    ])

    for payload in package:
        for each in r.iter_push(payload):
            assert next(ref) == each[-1]


def test_push(var_a, var_b):
    """
    Проверка алгоритма добавления без итераций
    """
    r = Resampler(max_gap=5, placeholder='null')
    assert r.push(var_a) == []

    item_1 = r.push(var_b)
    assert item_1 == [
        [datetime(2019, 12, 1, 12, 0, 0), 'A'],
        [datetime(2019, 12, 1, 12, 0, 1), 'A'],
        [datetime(2019, 12, 1, 12, 0, 2), 'A'],
        [datetime(2019, 12, 1, 12, 0, 3), 'A'],
        [datetime(2019, 12, 1, 12, 0, 4), 'A'],
        [datetime(2019, 12, 1, 12, 0, 5), 'B']
    ]

    r.clear()

    assert r.push(var_a) == []
    for each_x, each_y in zip(item_1, r.iter_push(var_b)):
        assert each_x == each_y


def test_clear(var_a, var_b):
    """
    Проверка на стирание памяти
    """
    ref = [
        [datetime(2019, 12, 1, 12, 0, 0), 'A'],
        [datetime(2019, 12, 1, 12, 0, 1), 'A'],
        [datetime(2019, 12, 1, 12, 0, 2), 'A'],
        [datetime(2019, 12, 1, 12, 0, 3), 'A'],
        [datetime(2019, 12, 1, 12, 0, 4), 'A'],
        [datetime(2019, 12, 1, 12, 0, 5), 'B']
    ]
    r = Resampler(max_gap=5, placeholder='null')

    assert r.push(var_a) == []
    assert r.push(var_b) == ref

    r.clear()

    assert r.push(var_a) == []
    assert r.push(var_b) == ref

    r.clear()

    assert r.push(var_a) == []
    assert r.push(var_b) == ref
