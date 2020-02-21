# -*- coding: utf-8 -*-
"""

    Тесты обработчика методов JSON RPC

"""
# встроенные модули
import json
from unittest.mock import MagicMock

# сторонние модули
import pytest

# модули проекта
from json_rpc.basic_tools import form_request
from trivial_tools.json_rpc.method_master import JSONRPCMethodMaster


def func_1(a, b):
    return a + b


def func_2(c, d):
    return c * d


@pytest.fixture
def master():
    """
    Экземпляр мастера методов
    """
    m = JSONRPCMethodMaster()
    m.register_method(func_1)
    m.register_method(func_2)
    return m


def test_contains(master):
    """
    Должен проверять наличие методов
    """
    assert 'func_1' in master
    assert 'func_2' in master
    assert 'func_3' not in master


def test_unknown_method(master):
    """
    Должен отмечать неизвестные методы
    """
    assert master.unknown_method('func_3')
    assert not master.unknown_method('func_1')


def test_get_method(master):
    """
    Должен выдать тело метода
    """
    assert master.get_method('func_1') is func_1
    assert master.get_method('func_2') is func_2
    assert master.get_method('func_3') is None


def test_get_method_names(master):
    """
    Должен выдать имена методов
    """
    assert master.get_method_names() == ['func_1', 'func_2']


def test_extract_json(master):
    """
    Должет вытащить JSON
    """
    fake = MagicMock()
    fake.get_json.return_value = 1
    result = master.extract_json(fake)
    assert result == 1

    class Fake:
        pass

    fake = Fake()
    fake.json = lambda: 2
    result = master.extract_json(fake)
    assert result == 2

    fake = MagicMock()
    fake.get_json.side_effect = json.JSONDecodeError('', '', 0)
    result = master.extract_json(fake)
    assert result == {'error': {'code': -32600,
                                'message': 'Неправильный формат запроса, JSONDecodeError: line 1 '
                                           'column 1 (char 0)'},
                      'id': None,
                      'jsonrpc': '2.0'}


def test_check_signature(master):
    """
    Должен проверить сигнатуры списка запросов или одного запроса
    """
    request = form_request(method='func_1')
    result = master.check_signature(request)
    assert result == [{
        'error': {
            'code': -32602,
            'message': 'Расхождение в аргументах метода: не хватает аргументов a, b'},
        'id': None,
        'jsonrpc': '2.0'}]

    request = form_request(method='func_1', a=1, z=2)
    result = master.check_signature(request)
    assert result == [
        {'error': {
            'code': -32602,
            'message':
                'Расхождение в аргументах метода: не хватает аргументов b, лишние аргументы z'},
            'id': None,
            'jsonrpc': '2.0'}]

    request = [
        form_request(method='func_1', a=1, b=2),
        form_request(method='func_1', c=1, d=2),
        form_request(method='func_2', c=1, d=2),
    ]
    result = master.check_signature(request)
    assert result == [
        {'id': None, 'jsonrpc': '2.0', 'method': 'func_1', 'params': {'a': 1, 'b': 2}},
        {'error': {'code': -32602,
                   'message': 'Расхождение в аргументах метода: не хватает аргументов '
                              'a, b, лишние аргументы c, d'},
         'id': None,
         'jsonrpc': '2.0'},
        {'id': None, 'jsonrpc': '2.0', 'method': 'func_2', 'params': {'c': 1, 'd': 2}}]

    result = master.check_signature(None)
    assert result == [
        {'error': {'code': -32600, 'message': 'Неправильный формат запроса, NoneType'},
         'id': None,
         'jsonrpc': '2.0'}]


def test_check_dict(master):
    """
    Должен проверить что запрос это правильный словарь
    """
    request = form_request(method='func_1', a=1, b=2)
    result = master.check_dict(request)
    assert result == {'error': {'code': -32602, 'message': 'Не предоставлен ключ авторизации.'},
                      'id': None,
                      'jsonrpc': '2.0'}

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

    request = {'jsonrpc': '2.0', 'method': 'func_1', 'params': []}
    result = master.check_dict(request)
    assert result == {'error': {'code': -32602,
                                'message': 'Позиционные аргументы не поддерживаеются.'},
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
    request = form_request(method='func_1', a=1, b=2, secret_key='xxx')
    result = master.check_request(request)
    assert result == [request]

    result = master.check_request(None)
    assert result == [
        {'error': {'code': -32600, 'message': 'Неправильный формат запроса, NoneType'},
         'id': None,
         'jsonrpc': '2.0'}]

    req_1 = form_request(method='func_1', a=1, b=2, secret_key='xxx')
    req_2 = form_request(method='func_1', a=1, z=2, secret_key='xxx')
    req_3 = form_request(method='func_2', c=1, d=2, secret_key='xxx')
    request = [req_1, req_2, req_3]
    result = master.check_request(request)
    assert result == request


def test_authorize(master):
    """
    Должен проверить авторизацию
    """
    request = form_request(method='func_1', a=1, b=2)
    assert master.authorize(request, lambda x: False) == {
        'error': {'code': -32602, 'message': 'Отказано в доступе.'},
        'id': None,
        'jsonrpc': '2.0'}
    assert master.authorize(request, lambda x: True) == request


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
