# -*- coding: utf-8 -*-
"""

    Тесты обработчика методов JSON RPC

"""
# встроенные модули
import json
import asyncio
from unittest.mock import MagicMock

# сторонние модули
import pytest

# модули проекта
from trivial_tools.json_rpc.method_master import JSONRPCMethodMaster
from trivial_tools.json_rpc.basic_tools import form_request, authorize


def func_1(a, b):
    return a + b


def func_2(c, d):
    return c * d


async def func_3(e, f):
    return e ** f


@pytest.fixture
def master():
    """
    Экземпляр мастера методов
    """
    m = JSONRPCMethodMaster(lambda x: True)
    m.register_method(func_1)
    m.register_method(func_2)
    m.register_method(func_3)
    return m


def test_contains(master):
    """
    Должен проверять наличие методов
    """
    assert 'func_1' in master
    assert 'func_2' in master
    assert 'func_3' in master
    assert 'func_4' not in master


def test_unknown_method(master):
    """
    Должен отмечать неизвестные методы
    """
    assert master.unknown_method('func_4')
    assert not master.unknown_method('func_1')


def test_get_method(master):
    """
    Должен выдать тело метода
    """
    assert master.get_method('func_1') is func_1
    assert master.get_method('func_2') is func_2
    assert master.get_method('func_4') is None


def test_get_method_names(master):
    """
    Должен выдать имена методов
    """
    assert master.get_method_names() == ['func_1', 'func_2', 'func_3']


def test_json(master):
    """
    Должет вытащить JSON
    """

    class Fake:
        pass

    fake = Fake()

    fake.json = lambda: 1
    result = master.json(fake, how='json()')
    assert result == (1, False)

    fake.json = 2
    result = master.json(fake, how='json')
    assert result == (2, False)

    fake = MagicMock()
    fake.json.side_effect = json.JSONDecodeError('', '', 0)
    result = master.json(fake, how='json()')
    assert result == ({'error': {'code': -32600,
                                 'message': 'Неправильный формат запроса, JSONDecodeError: line 1 '
                                            'column 1 (char 0)'},
                       'id': None,
                       'jsonrpc': '2.0'}, True)


def test_async_json(master):
    """
    Должет вытащить JSON
    """
    class Fake:
        @staticmethod
        async def json():
            return 1

        @property
        async def get_json(self):
            return 2

    fake = Fake()
    result = asyncio.run(master.async_json(fake, how='json()'))
    assert result == (1, False)

    result = asyncio.run(master.async_json(fake, how='get_json'))
    assert result == (2, False)

    fake = MagicMock()
    fake.json.side_effect = json.JSONDecodeError('', '', 0)
    result = asyncio.run(master.async_json(fake, how='json()'))
    assert result == ({'error': {'code': -32600,
                                 'message': 'Неправильный формат запроса, JSONDecodeError: line 1 '
                                            'column 1 (char 0)'},
                       'id': None,
                       'jsonrpc': '2.0'}, True)


def test_check_signature(master):
    """
    Должен проверить сигнатуры списка запросов или одного запроса
    """
    requests = [form_request(method='func_1', msg_id=1)]
    errors = []
    master.check_signature_conveyor(requests, errors)
    assert errors == [{
        'error': {
            'code': -32602,
            'message': 'Расхождение в аргументах метода: не хватает аргументов a, b'},
        'id': 1,
        'jsonrpc': '2.0'}]

    requests = [form_request(method='func_1', a=1, z=2, msg_id=1)]
    errors = []
    master.check_signature_conveyor(requests, errors)
    assert errors == [
        {'error': {
            'code': -32602,
            'message':
                'Расхождение в аргументах метода: не хватает аргументов b, лишние аргументы z'},
            'id': 1,
            'jsonrpc': '2.0'}]

    requests = [
        form_request(method='func_1', a=1, b=2, msg_id=1),
        form_request(method='func_1', c=1, d=2, id=2),
        form_request(method='func_2', c=1, d=2, id=3),
    ]
    errors = []
    master.check_signature_conveyor(requests, errors)
    assert requests == [{'id': 1, 'jsonrpc': '2.0', 'method': 'func_1', 'params': {'a': 1, 'b': 2}},
                        {'id': 3, 'jsonrpc': '2.0', 'method': 'func_2', 'params': {'c': 1, 'd': 2}}]
    assert errors == [
        {'error': {'code': -32602,
                   'message': 'Расхождение в аргументах метода: не хватает аргументов '
                              'a, b, лишние аргументы c, d'},
         'id': 2,
         'jsonrpc': '2.0'},
    ]


def test_check_dict(master):
    """
    Должен проверить что запрос это правильный словарь
    """
    requests = [form_request(method='func_1', a=1, b=2)]
    errors = []
    master.check_request_conveyor(requests, errors)
    assert errors == [{'error': {'code': -32602, 'message': 'Не предоставлен ключ авторизации.'},
                       'jsonrpc': '2.0'}]

    request = {}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32600, 'message': 'Получен пустой запрос.'},
                      'id': None,
                      'jsonrpc': '2.0'}

    request = {'jsonrpc': '1.2'}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32600, 'message': 'Поддерживается только JSON-RPC 2.0.'},
                      'jsonrpc': '2.0'}

    request = {'jsonrpc': '2.0'}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32601, 'message': 'Не указан метод запроса.'},
                      'jsonrpc': '2.0'}

    request = {'jsonrpc': '2.0', 'method': 'zo'}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32601, 'message': 'Неизвестный метод: "zo".'},
                      'jsonrpc': '2.0'}

    request = {'jsonrpc': '2.0', 'method': 'func_1'}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32602, 'message': 'Не указаны аргументы вызова.'},
                      'jsonrpc': '2.0'}

    request = {'jsonrpc': '2.0', 'method': 'func_1', 'params': {}}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32602, 'message': 'Не предоставлен ключ авторизации.'},
                      'jsonrpc': '2.0'}

    request = {'jsonrpc': '2.0', 'method': 'func_1', 'params': False}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32602,
                                'message': 'Неправильно оформлены аргументы вызова метода.'},
                      'jsonrpc': '2.0'}

    request = form_request(method='func_1', a=1, b=2, secret_key='xxx')
    result = master.check_dict(request)
    assert result == request


def test_check_request(master):
    """
    Должен проверить запрос
    """
    requests = [form_request(method='func_1', a=1, b=2, secret_key='xxx')]
    requests_before = requests.copy()
    errors = []
    master.check_request_conveyor(requests, errors)
    assert requests == requests_before

    requests = [None]
    errors = []
    master.check_request_conveyor(requests, errors)
    assert errors == [
        {'error': {'code': -32600, 'message': 'Неправильный формат запроса, NoneType.'},
         'id': None,
         'jsonrpc': '2.0'}]

    errors = []
    req_1 = form_request(method='func_1', a=1, b=2, secret_key='xxx')
    req_2 = form_request(method='func_1', a=1, z=2, secret_key='xxx')
    req_3 = form_request(method='func_2', c=1, d=2, secret_key='xxx')
    requests = [req_1, req_2, req_3]
    requests_before = requests.copy()
    master.check_request_conveyor(requests, errors)
    assert requests == requests_before


def test_authorize(master):
    """
    Должен проверить авторизацию
    """
    request = form_request(method='func_1', a=1, b=2, id=825)
    assert authorize(request, lambda x: False) == {
        'error': {'code': -32602, 'message': 'Отказано в доступе.'},
        'id': 825,
        'jsonrpc': '2.0'}
    assert authorize(request, lambda x: True) == request


def test_authorize_conveyor(master):
    """
    Должен проверить авторизацию
    """
    errors = []
    req_1 = form_request(method='func_1', a=1, b=2, secret_key='xxx')
    req_2 = form_request(method='func_1', a=1, z=2, secret_key='xxx')
    req_3 = form_request(method='func_2', c=1, d=2, secret_key='xxx')
    requests = [req_1, req_2, req_3]
    requests_before = requests.copy()
    master.check_auth_conveyor(requests, errors)
    assert requests == requests_before


def test_execute(master):
    """
    Должен исполнить запрос
    """
    request = form_request(method='func_1', a=1, b=2)
    result = master.execute(request)
    assert result == 3

    request = form_request(method='func_2', c=1, d=2)
    result = master.execute(request)
    assert result == 2


def test_async_execute(master):
    """
    Должен исполнить запрос
    """
    request = form_request(method='func_3', e=4, f=5)
    result = asyncio.run(master.async_execute(request))
    assert result == 1024

    request = form_request(method='func_3', e=5, f=6)
    result = asyncio.run(master.async_execute(request))
    assert result == 15625
