# -*- coding: utf-8 -*-
"""

    Тесты скольщяей суммы

"""
# сторонние модули
import pytest
from pytest import approx

# модули проекта
from trivial_tools.containers.class_moving_sum import MovingSum


@pytest.fixture()
def numbers_1():
    """
    Исходные данные для вычисления среднего
    """
    return [8, 41, 9, 6, 32, 58, 8, 78, 3, 2, 45, 6, 9, 87, 51, 23]


@pytest.fixture()
def reference_1():
    """
    Эталонные суммы
    """
    return [8, 49, 58, 64, 88, 105, 104, 176, 147, 91, 128, 56, 62, 147, 153, 170]


@pytest.fixture()
def numbers_2():
    """
    Исходные данные для вычисления среднего
    """
    return [-40.4, 85.6, 37.65, 1548.456, 0, 11.25, -74, 0.0000001, 34, 45, 67]


@pytest.fixture()
def reference_2():
    """
    Эталонные суммы
    """
    return [-40.4, 45.199999, 82.85, 1631.3059999, 1671.706, 1597.356,
            1485.706, -62.7499999, -28.7499999, 5.0000001]


def test_creation():
    """
    Проверка создания
    """
    with pytest.raises(ValueError):
        MovingSum()

    s = MovingSum(window=2)
    assert approx(s.sum) == 0.0

    s = MovingSum([1, 2, 3])
    assert approx(s.sum) == 6.0

    s = MovingSum([1, 2, 3], window=2)
    assert approx(s.sum) == 5.0


def test_pushing(reference_1, numbers_1, reference_2, numbers_2):
    """
    Проверка добавления элементов
    """
    s = MovingSum(window=4)

    for ref, number in zip(reference_1, numbers_1):
        s.push(number)
        assert approx(s.sum) == ref

    s.restore()

    for ref, number in zip(reference_2, numbers_2):
        s.push(number)
        assert approx(s.sum) == ref


def test_enlarge(numbers_1, numbers_2):
    """
    Проверка увеличения размеров
    """
    s = MovingSum(window=4)
    for number in numbers_1:
        s.push(number)

    assert approx(s.sum) == 170

    s.resize(10)
    assert approx(s.sum) == 170

    reference_large = [178, 219, 228, 234, 266, 324, 323, 314,
                       266, 245, 282, 247, 247, 328, 347, 312]

    for ref, number in zip(reference_large, numbers_1):
        s.push(number)
        assert approx(s.sum) == ref

    s.resize(15)
    assert approx(s.sum) == 312

    reference_large = [271.6, 357.2, 394.85, 1943.306, 1943.306, 1946.556, 1794.556,
                       1791.5560001, 1823.5560001, 1823.5560001, 1884.5560001]

    for ref, number in zip(reference_large, numbers_2):
        s.push(number)
        assert approx(s.sum) == ref


def test_shrink(numbers_1):
    """
    Проверка уменьшения размеров
    """
    s = MovingSum(window=4)
    for number in numbers_1:
        s.push(number)

    assert approx(s.sum) == 170.0

    s.resize(3)

    assert approx(s.sum) == 161.0

    reference_small = [82, 72, 58, 56, 47, 96, 98, 144, 89, 83, 50, 53, 60, 102, 147, 161]

    for ref, number in zip(reference_small, numbers_1):
        s.push(number)
        assert approx(s.sum) == ref


def test_getitem(numbers_1, numbers_2):
    """
    Проверка обращения к элементу
    """
    s = MovingSum(window=4)
    for number in numbers_1:
        s.push(number)

    assert approx(s[0]) == 9.0
    assert approx(s[1]) == 87.0
    assert approx(s[2]) == 51.0
    assert approx(s[3]) == 23.0

    assert s[:] == [9.0, 87.0, 51.0, 23.0]

    assert approx(s.sum) == 170.0

    s.restore()
    for number in numbers_2:
        s.push(number)

    assert approx(s[0]) == 0.0000001
    assert approx(s[1]) == 34
    assert approx(s[2]) == 45
    assert approx(s[3]) == 67

    assert s[:] == [0.0000001, 34, 45, 67]

    assert approx(s.sum) == 146.0000001


def test_setitem(numbers_1, numbers_2):
    """
    Проверка подмены элемента
    """
    s = MovingSum(window=4)
    for number in numbers_1:
        s.push(number)

    s[0] = 99.0

    assert approx(s[0]) == 99.0
    assert approx(s[1]) == 87.0
    assert approx(s[2]) == 51.0
    assert approx(s[3]) == 23.0

    assert approx(s.sum) == 260.0

    with pytest.raises(IndexError):
        s[:] = [7.0, 28.0, 31.0, -900.0]
