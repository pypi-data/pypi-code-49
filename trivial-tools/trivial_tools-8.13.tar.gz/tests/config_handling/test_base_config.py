# -*- coding: utf-8 -*-
"""

    Тесты конфига

"""
# модули проекта
from trivial_tools.config_handling.base_config import BaseConfig


def test_creation():
    """
    Создание экземпляра
    """
    c = BaseConfig(a=1, b=2)
    assert c.a == 1
    assert c.b == 2


def test_context():
    """
    Создание экземпляра
    """
    c = BaseConfig(a=1, b=2)
    BaseConfig.register(c)

    instance = BaseConfig.get_instance()

    assert instance is c
    assert instance.a == c.a
    assert instance.b == c.b

    with BaseConfig.temporary_config(a='test', b='value'):
        instance = BaseConfig.get_instance()
        assert instance.a == 'test'
        assert instance.b == 'value'

    instance = BaseConfig.get_instance()
    assert instance is c
    assert instance.a == c.a
    assert instance.b == c.b
