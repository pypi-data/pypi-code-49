# -*- coding: utf-8 -*-
"""

    Тесты класса хранящего экземпляр себя

"""
# сторонние модули
import pytest

# модули проекта
from trivial_tools.classes.conservator import Conservator


@pytest.fixture
def class_():
    class Test(Conservator):
        def __init__(self, var):
            self.var = var
    return Test


def test_creation(class_):
    """
    Создание экземпляра
    """
    t = class_(1)
    assert t.var == 1


def test_double_creation(class_):
    """
    Создание экземпляра
    """
    t = class_(1)
    assert t.var == 1


def test_register(class_):
    """
    Добавить валидный экземпляр
    """
    assert not class_.has_instance()
    inst_1 = class_(1)
    assert not class_.has_instance()
    class_.register(inst_1)

    inst_2 = class_(2)
    inst_3 = class_(3)

    assert class_.get_instance() is inst_1

    class_.unregister()
    class_.register(inst_2)
    assert class_.get_instance() is inst_2

    class_.replace(inst_3)
    assert class_.get_instance() is inst_3


def test_register_force(class_):
    """
    Добавить валидный экземпляр
    """
    assert not class_.has_instance()

    with pytest.raises(ValueError):
        class_.register(1)

    class_.register_force(256)

    assert class_.get_instance() == 256
    assert class_.has_instance()

    with pytest.raises(ValueError):
        inst = class_(3)
        class_.register_force(inst)


def test_unregister(class_):
    """
    Удалить валидный экземпляр
    """
    assert not class_.has_instance()
    with pytest.raises(ValueError):
        class_.unregister()

    t = class_(1)
    class_.register(t)
    t.unregister()
    assert not class_.has_instance()


def test_replace(class_):
    """
    Заменить валидный экземпляр
    """
    assert not class_.has_instance()
    inst = class_(1)
    class_.register(inst)
    assert class_.has_instance()

    with pytest.raises(ValueError):
        class_.replace(25)

    with pytest.raises(ValueError):
        class_.register(25)

    assert class_.has_instance()
    assert class_.get_instance() is inst

    class_.unregister()
    assert not class_.has_instance()

    class_.register_force(25)

    assert class_.has_instance()
    assert class_.get_instance() == 25


def test_get_instance(class_):
    """
    Получить валидный экземпляр
    """
    assert not class_.has_instance()

    with pytest.raises(ValueError):
        class_.get_instance()
