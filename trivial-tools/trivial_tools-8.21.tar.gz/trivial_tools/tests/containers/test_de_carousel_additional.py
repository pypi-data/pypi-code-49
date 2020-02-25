# -*- coding: utf-8 -*-
"""

    Дополнительные тесты двусторонней карусели

"""
# сторонние модули
import pytest

# модули проекта
from trivial_tools.containers.class_de_carousel import DeCarousel


def test_full_cycle():
    """
    Проверка работы
    """
    d = DeCarousel(window=4, sentinel=None)

    for i in range(100):
        d.append(i)

    assert d.get_contents() == [96, 97, 98, 99]
    assert d.left == 96
    assert d.right == 99
    assert len(d) == 4

    for i in range(3):
        d.popleft()

    assert d.get_contents() == [99]
    assert d._data == [None, None, None, 99]
    assert d._index == 0
    assert d.left == 99
    assert d.right == 99
    assert len(d) == 1

    d.append(1)
    assert d.get_contents() == [99, 1]
    assert d._data == [1, None, None, 99]
    assert d.left == 99
    assert d.right == 1
    assert len(d) == 2

    for i in range(1, 200):
        d.append(i)

    assert d.get_contents() == [196, 197, 198, 199]
    assert d._data == [196, 197, 198, 199]
    assert d.left == 196
    assert d.right == 199
    assert len(d) == 4
