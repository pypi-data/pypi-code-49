# -*- coding: utf-8 -*-

"""
    Регистратор методов для JSON-RPC.

    Используется для централизованного управления всеми методами приложения.

"""
# встроенные модули
import json
from functools import partial
from inspect import signature
from types import FunctionType
from typing import Optional, List, Callable, Dict, Sequence, Union, Tuple, Coroutine

# сторонние модули
from trivial_tools.formatters.base import s_type
from trivial_tools.json_rpc.basic_tools import (
    Request, Error, form_error, Result, decide, authorize,
)


class JSONRPCMethodMaster:
    """
    Регистратор методов для JSON-RPC.

    Используется для централизованного управления всеми методами приложения.
    """

    def __init__(self, auth_func: Callable, ignores: Sequence[str] = ('secret_key',)):
        """
        Инициация.
        """
        self.auth_func = auth_func
        self._ignores = ['return'] + list(ignores)
        self._methods: Dict[str, Callable] = {}

    def __contains__(self, method_name: str):
        """
        Проверить, имеется ли этот метод в записях.
        """
        return method_name in self._methods

    def register_method(self, func: Union[FunctionType, Coroutine]) -> FunctionType:
        """
        Зарегистрировать метод.
        """
        self._methods[func.__name__] = func
        return func

    def unknown_method(self, method_name: str) -> bool:
        """
        Этот метод нам неизвестен?
        """
        return method_name not in self._methods

    def get_method(self, method_name: str) -> Optional[Callable]:
        """
        Получить метод.
        """
        return self._methods.get(method_name)

    def get_method_names(self) -> List[str]:
        """
        Получить имена доступных методов.
        """
        return sorted(self._methods.keys())

    @staticmethod
    def extract_attribute(request, how: str) -> Union[dict, Coroutine]:
        """
        Извлечь JSON из тела запроса
        """
        if how.endswith('()'):
            response = getattr(request, how.rstrip('()'))()
        else:
            response = getattr(request, how.rstrip('()'))
        return response

    async def async_json(self, request, how: str = 'json()') -> Tuple[Union[Request, Error], bool]:
        """
        Безопасное извлечение JSON из запроса. Асинхронная форма.
        """
        try:
            response = await self.extract_attribute(request, how)
            is_fail = False
        except json.JSONDecodeError as err:
            response = form_error(-32600, f'Неправильный формат запроса, {s_type(err)}{err}.')
            is_fail = True

        return response, is_fail

    def json(self, request, how: str = 'json') -> Tuple[Union[Request, Error], bool]:
        """
        Безопасное извлечение JSON из запроса. Синхронная форма.
        """
        try:
            response = self.extract_attribute(request, how)
            is_fail = False
        except json.JSONDecodeError as err:
            response = form_error(-32600, f'Неправильный формат запроса, {s_type(err)}{err}.')
            is_fail = True

        return response, is_fail

    @staticmethod
    def base_conveyor(requests: List[Request], errors: List[Error], func: Callable) -> None:
        """
        Базовая функция сортировки запросов.
        """
        filtered = []
        while requests:
            new_request = requests.pop()
            output = func(new_request)
            decide(output, filtered, errors)

        requests.extend(reversed(filtered))

    def check_request_conveyor(self, requests: List[Request], errors: List[Error]) -> None:
        """
        Проверить на предмет соответствия JSON RPC 2.0.
        """
        self.base_conveyor(requests, errors, func=self.check_dict)

    def check_signature_conveyor(self, requests: List[Request], errors: List[Error]) -> None:
        """
        Проверка полученных параметров на соответствие сигнатуре метода.
        """
        self.base_conveyor(requests, errors, func=self._check_signature)

    def check_auth_conveyor(self, requests: List[Request], errors: List[Error]) -> None:
        """
        Проверить авторизацию внешней функцией.
        """
        self.base_conveyor(requests, errors, func=partial(authorize, check_func=self.auth_func))

    def _check_signature(self, request: Request) -> Union[Request, Error]:
        """
        Проверка полученных параметров на соответствие сигнатуре метода.
        """
        method_name = request.get('method')
        params = request.get('params')
        msg_id = request.get('id')
        need_id = 'id' in request

        if isinstance(params, list):
            # мы не можем проверить аргументы, если они переданы по порядку
            return request

        params = params.keys()

        method: FunctionType = self._methods[method_name]
        sig = signature(method)

        if 'kwargs' in sig.parameters:
            # мы не можем проверить аргументы, если функция принимает их в запакованном виде
            return request

        valid_keys = {x for x in sig.parameters if x not in self._ignores}
        other_keys = {x for x in params if x not in self._ignores}

        message = 'Расхождение в аргументах метода: '

        if valid_keys != other_keys:
            insufficient = ', '.join(sorted(valid_keys - other_keys))
            excess = ', '.join(sorted(other_keys - valid_keys))

            if insufficient:
                message += 'не хватает аргументов ' + insufficient

                if excess:
                    message += ', '

            if excess:
                message += 'лишние аргументы ' + excess

            return form_error(-32602, message, need_id, msg_id)
        return request

    def check_dict(self, request: Request) -> Union[Request, Error]:
        """
        Проверить словарь запроса.
        """
        if not isinstance(request, dict):
            return form_error(-32600, f'Неправильный формат запроса, {s_type(request)}.')

        method = request.get('method')
        params = request.get('params')
        msg_id = request.get('id')
        need_id = 'id' in request

        if not request:
            response = form_error(-32600, 'Получен пустой запрос.')

        elif request.get('jsonrpc') != '2.0':
            response = form_error(-32600, 'Поддерживается только JSON-RPC 2.0.', need_id, msg_id)

        elif method is None:
            response = form_error(-32601, 'Не указан метод запроса.', need_id, msg_id)

        elif method not in self._methods:
            response = form_error(-32601, f'Неизвестный метод: "{method}".', need_id, msg_id)

        elif params is None:
            response = form_error(-32602, 'Не указаны аргументы вызова.', need_id, msg_id)

        elif not isinstance(params, (dict, list)):
            response = form_error(
                -32602, 'Неправильно оформлены аргументы вызова метода.', need_id, msg_id
            )

        elif isinstance(params, dict) and params.get('secret_key') is None:
            response = form_error(-32602, 'Не предоставлен ключ авторизации.', need_id, msg_id)

        else:
            response = request

        return response

    def execute(self, request: Request) -> Result:
        """
        Исполнить запрос.
        """
        method_name = request.get('method', 'unknown method')
        params = request.get('params', {})
        method = self.get_method(method_name)

        # @@@@@@@@@@@@@@@@@@@@@@@@
        if isinstance(params, dict):
            # секретный ключ не нужен внутри методов
            params.pop('secret_key', None)
            response = method(**params)
        else:
            response = method(*params)
        # @@@@@@@@@@@@@@@@@@@@@@@@

        return response

    async def async_execute(self, request: Request) -> Result:
        """
        Исполнить запрос.
        """
        method_name = request.get('method', 'unknown method')
        params = request.get('params', {})
        method = self.get_method(method_name)

        # @@@@@@@@@@@@@@@@@@@@@@@@
        if isinstance(params, dict):
            # секретный ключ не нужен внутри методов
            params.pop('secret_key', None)
            response = await method(**params)
        else:
            response = await method(*params)
        # @@@@@@@@@@@@@@@@@@@@@@@@

        return response
