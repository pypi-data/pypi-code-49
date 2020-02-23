# -*- coding: utf-8 -*-
"""

    Тесты кеширующей машины

"""
# встроенные модули
from datetime import datetime
from unittest.mock import patch

# сторонние модули
import pytest

# модули проекта
from trivial_tools.storage.caching_machine import CachingMachine


@pytest.fixture()
def machine_persistent():
    """
    Машина без срока хранения
    """
    return CachingMachine()


@pytest.fixture()
def machine_not_persistent():
    """
    Машина со сроком хранения 5 секунд
    """
    return CachingMachine(expiration=5)


@pytest.fixture()
def machine_tiny():
    """
    Машина со сроком хранения 5 секунд и всего на 4 элемента
    """
    return CachingMachine(expiration=5, max_items=4)


def test_fill(machine_tiny):
    """
    Проверка заполнения машины
    """
    with patch('trivial_tools.storage.caching_instance.datetime') as fake:
        fake.now.return_value = datetime(2019, 10, 31, 18, 6, 0)
        assert machine_tiny.total() == 0

        machine_tiny.set('key_1', 'value')
        assert machine_tiny.total() == 1

        machine_tiny.set('key_1', 'value')
        assert machine_tiny.total() == 1

        machine_tiny.set('key_2', 'value')
        assert machine_tiny.total() == 2

        machine_tiny.set('key_3', 'value')
        assert machine_tiny.total() == 3

        machine_tiny.set('key_4', 'value')
        assert machine_tiny.total() == 4

        machine_tiny.set('key_5', 'value')
        assert machine_tiny.total() == 4

        machine_tiny.clear()
        assert machine_tiny.total() == 0


def test_caching(machine_persistent):
    """
    Проверка работы декоратора
    """
    @machine_persistent.cache_call()
    def func(x, y):
        return x + y

    assert func(1, 2) == 3
    assert func(2, 3) == 5
    assert func(1, 2) == 3

    assert machine_persistent.keys() == [('func', (1, 2)), ('func', (2, 3))]


def test_caching_string(machine_persistent):
    """
    Проверка работы декоратора
    """

    @machine_persistent.cache_call_using_strings()
    def func(x, y):
        return x + y

    assert func(1, 2) == 3
    assert func(2, 3) == 5
    assert func(1, 2) == 3

    assert machine_persistent.keys() == ['func_1_2', 'func_2_3']
