# -*- coding: utf-8 -*-
"""

    Тесты специфических операций

"""
# сторонние модули
import pytest

# модули проекта
from trivial_tools.special.special import group_cast


def test_group_cast():
    """
    Должен преобразовывать типы
    """
    raw = ['1', '2', '3']
    assert group_cast(raw) == raw
    assert group_cast(raw, int, float, str) == [1, 2.0, '3']


def test_group_cast_ellipsis():
    """
    Должен преобразовывать типы для больших коллекий
    """
    raw = ['1', '2', '3']
    assert group_cast(raw) == raw
    assert group_cast(raw, int, ...) == [1, 2, 3]
    assert group_cast(raw, str, int, ...) == ['1', 2, 3]


def test_group_cast_fail():
    """
    Должен преобразовывать типы
    """
    with pytest.raises(ValueError):
        group_cast([1, 2], float, float, float)

    with pytest.raises(ValueError):
        group_cast([1, 2], float)
