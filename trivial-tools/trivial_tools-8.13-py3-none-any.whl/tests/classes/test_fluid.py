# -*- coding: utf-8 -*-
"""

    Тесты класса с динамическими параметрами

"""
# сторонние модули
import pytest

from trivial_tools.classes.fluid import Fluid


def test_creation():
    """
    Создание экземпляра
    """
    f = Fluid(a=1, b=2)
    assert f.a == 1
    assert f.b == 2
    assert vars(f) == {'a': 1, 'b': 2}


def test_creation_wrong():
    """
    Создание экземпляра
    """
    with pytest.raises(ValueError):
        Fluid(1, 2)


def test_creation_dict():
    """
    Создание экземпляра
    """
    source = dict(a=1, b=2, c='3')
    f1 = Fluid(**source)
    f2 = Fluid.from_dict(source)
    assert f1 == f2
    assert f1.to_dict() == source
    assert f2.to_dict() == source


def test_alter():
    """
    Изменение
    """
    source = dict(a=1, b=2, c='3')
    f1 = Fluid(**source)
    assert f1.to_dict() == {'a': 1, 'b': 2, 'c': '3'}
    f2 = f1.alter(c='test', d=285)
    assert f2.to_dict() == {'a': 1, 'b': 2, 'c': 'test', 'd': 285}
    assert f1.to_dict() == {'a': 1, 'b': 2, 'c': '3'}


def test_eq():
    """
    Проверка равенства
    """
    f1 = Fluid(a=1, b=2)
    f2 = Fluid(a=1, b=2)
    assert f1 == f2
    assert f1 != 1
    assert f2 != dict(a=1, b=2)


def test_str():
    """
    Текстовое представление
    """
    f = Fluid(par_1=285, par_2='test', par_3=None)
    assert str(f) == 'Fluid(par_1=285, par_2=test, par_3=None)'

    f = Fluid(par_1=[1, 2, 3], par_2='test', par_3=None, par_4=dict(a=1), par_5=[1, 2, 3, 4, 5, 6])
    assert str(f) == """
Fluid(
    01. par_1 = [1, 2, 3]
    02. par_2 = test
    03. par_3 = None
    04. par_4 = {'a': 1}
    05. par_5 = [
                 1,
                 2,
                 3,
                 4,
                 5,
                 6
                ]
)
    """.strip()


def test_repr():
    """
    Текстовое представление
    """
    f = Fluid(par_1=285, par_2='test', par_3=None)
    assert repr(f) == "Fluid(par_1=285, par_2='test', par_3=None)"
