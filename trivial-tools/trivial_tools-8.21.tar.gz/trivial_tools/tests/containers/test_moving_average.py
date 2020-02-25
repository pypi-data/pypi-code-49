# -*- coding: utf-8 -*-
"""

    Тесты скользящего среднего

"""
# сторонние модули
import pytest
from pytest import approx

# модули проекта
from trivial_tools.containers.class_moving_average import MovingAverage


@pytest.fixture()
def numbers():
    """
    Исходные данные для вычисления среднего
    """
    return [1, 3, 5, 6, 8, 41, 9, 6, 32, 58, 8, 78, 3, 2, 45, 6, 9, 87, 51, 23]


@pytest.fixture()
def reference():
    """
    Эталонные средние
    """
    return [1, 2, 3, 3.75, 5.5, 15, 16, 16, 22, 26.25, 26, 44,
            36.75, 22.75, 32, 14, 15.5, 36.75, 38.25, 42.5]


@pytest.fixture()
def summary():
    """
    Эталонные суммы
    """
    return [1, 4, 9, 15, 22, 60, 64, 64, 88, 105, 104, 176, 147, 91, 128, 56, 62, 147, 153, 170]


def test_creation():
    """
    Проверка создания
    """
    with pytest.raises(ValueError):
        MovingAverage()

    m = MovingAverage(window=2)
    assert approx(m.avg) == 0.0
    assert approx(m.sum) == 0.0

    m = MovingAverage([1, 2, 3])
    assert approx(m.avg) == 2.0
    assert approx(m.sum) == 6.0

    m = MovingAverage([1, 2, 3], window=2)
    assert approx(m.avg) == 2.5
    assert approx(m.sum) == 5.0


def test_pushing(reference, summary, numbers):
    """
    Проверка добавления элементов
    """
    m = MovingAverage(window=4)

    for ref, summ, number in zip(reference, summary, numbers):
        m.push(number)
        assert approx(m.avg) == ref
        assert approx(m.sum) == summ


def test_enlarge(numbers):
    """
    Проверка увеличения размеров
    """
    m = MovingAverage(window=4)
    for number in numbers:
        m.push(number)

    assert approx(m.avg) == 42.5
    assert approx(m.sum) == 170.0

    m.resize(10)

    assert approx(m.avg) == 42.5
    assert approx(m.sum) == 170.0

    reference_large = [34.2, 29, 25.571428, 23.125, 21.444444, 23.4, 23.4, 15.3, 13.4, 16.9,
                       17.6, 25.1, 24.9, 24.5, 28.2, 24.7, 24.7, 32.8, 34.7, 31.2]

    summary_large = [171, 174, 179, 185, 193, 234, 234, 153, 134, 169,
                     176, 251, 249, 245, 282, 247, 247, 328, 347, 312]

    for ref, summ, number in zip(reference_large, summary_large, numbers):
        m.push(number)
        assert approx(m.avg) == ref
        assert approx(m.sum) == summ


def test_shrink(numbers):
    """
    Проверка уменьшения размеров
    """
    m = MovingAverage(window=4)
    for number in numbers:
        m.push(number)

    assert approx(m.avg) == 42.5
    assert approx(m.sum) == 170.0

    m.resize(3)

    assert approx(m.avg) == 53.666666
    assert approx(m.sum) == 161.0

    reference_small = [25, 9, 3, 4.666666, 6.333333, 18.33333, 19.33333, 18.66666, 15.66666, 32,
                       32.66666, 48, 29.66666, 27.66666, 16.66666, 17.66666, 20, 34, 49, 53.66666]

    summary_small = [75, 27, 9, 14, 19, 55, 58, 56, 47, 96, 98,
                     144, 89, 83, 50, 53, 60, 102, 147, 161]

    for ref, summ, number in zip(reference_small, summary_small, numbers):
        m.push(number)
        assert approx(m.avg) == ref
        assert approx(m.sum) == summ


def test_getitem(numbers):
    """
    Проверка обращения к элементу
    """
    m = MovingAverage(window=4)
    for number in numbers:
        m.push(number)

    assert approx(m[0]) == 9.0
    assert approx(m[1]) == 87.0
    assert approx(m[2]) == 51.0
    assert approx(m[3]) == 23.0

    assert m[:] == [9.0, 87.0, 51.0, 23.0]

    assert approx(m.avg) == 42.5
    assert approx(m.sum) == 170.0


def test_setitem(numbers):
    """
    Проверка подмены элемента
    """
    m = MovingAverage(window=4)
    for number in numbers:
        m.push(number)

    m[0] = 99.0

    assert approx(m[0]) == 99.0
    assert approx(m[1]) == 87.0
    assert approx(m[2]) == 51.0
    assert approx(m[3]) == 23.0

    assert approx(m.avg) == 65.0
    assert approx(m.sum) == 260.0

    with pytest.raises(IndexError):
        m[:] = [7.0, 28.0, 31.0, -900.0]
