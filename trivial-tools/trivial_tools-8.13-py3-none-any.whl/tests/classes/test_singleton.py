# -*- coding: utf-8 -*-
"""

    Тесты одиночки

"""
# сторонние модули
import pytest

# модули проекта
from trivial_tools.classes.singleton_base import MetaSingleton


@pytest.fixture
def class_():
    class Test(metaclass=MetaSingleton):
        def __init__(self, x):
            self.x = x
    return Test


def test_creation(class_):
    """
    Создание экземпляра
    """
    t = class_(1)
    assert t
    assert t.x == 1


def test_creation2(class_):
    """
    Создание экземпляра второй раз, проверка работы фикстуры
    """
    t = class_(2)
    assert t
    assert t.x == 2


def test_creation3(class_):
    """
    Создание экземпляра, проверка собственно метакласса
    """
    t1 = class_(3)
    assert t1
    assert t1.x == 3

    t2 = class_(4)
    assert t2
    assert t2.x == 3


def test_get_instance(class_):
    """
    Создание экземпляра, проверка собственно метакласса
    """
    t1 = class_(4)
    assert t1
    assert t1.x == 4

    t2 = class_.get_instance(t1)
    assert t1 is t2

    t3 = class_.get_instance(class_)
    assert t1 is t3


def test_get_instance_fail(class_):
    """
    Создание экземпляра, проверка собственно метакласса
    """
    with pytest.raises(KeyError):
        MetaSingleton.get_instance(1)
