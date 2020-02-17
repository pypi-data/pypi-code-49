# -*- coding: utf-8 -*-
"""

    Тесты кеширующего инстанса

"""
# встроенные модули
from datetime import datetime
from unittest.mock import patch

# модули проекта
from trivial_tools.storage.caching_instance import CachingInstance


def test_expiration_persistent():
    """
    Экземпляр без уставки на протухание
    """
    inst = CachingInstance(123)
    assert inst.value == 123
    assert inst.not_expired
    assert inst.not_expired()
    assert not inst.expired()


def test_expiration():
    """
    Проверка протухания экземпляра
    """
    with patch('trivial_tools.storage.caching_instance.datetime') as fake:
        fake.now.return_value = datetime(2019, 10, 31, 18, 6, 0)
        inst = CachingInstance(123, 5)
        assert inst.value == 123
        assert inst.expires == datetime(2019, 10, 31, 18, 6, 5)
        assert inst.not_expired()
        assert not inst.expired()

    with patch('trivial_tools.storage.caching_instance.datetime') as fake:
        fake.now.return_value = datetime(2019, 10, 31, 18, 6, 4)
        assert inst.value == 123
        assert inst.expires == datetime(2019, 10, 31, 18, 6, 5)
        assert inst.not_expired()
        assert not inst.expired()

    with patch('trivial_tools.storage.caching_instance.datetime') as fake:
        fake.now.return_value = datetime(2019, 10, 31, 18, 6, 5)
        assert inst.value == 123
        assert inst.expires == datetime(2019, 10, 31, 18, 6, 5)
        assert inst.expired()
        assert not inst.not_expired()


def test_repr():
    """
    Проверка преобразования в текст
    """
    inst = CachingInstance(123)
    assert str(inst) == 'CachingInstance(value=123, expires=None)'

    with patch('trivial_tools.storage.caching_instance.datetime') as fake:
        fake.now.return_value = datetime(2019, 10, 31, 18, 6, 5)
        inst = CachingInstance(345, 56)
        assert str(inst) == ('CachingInstance(value=345, '
                             'expires=datetime.datetime(2019, 10, 31, 18, 7, 1))')
