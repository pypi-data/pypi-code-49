# -*- coding: utf-8 -*-
"""

    Регистратор методов для JSON-RPC.
    Используется для централизованного управления всеми методами приложения.

"""
# встроенные модули
import json
from inspect import signature
from types import FunctionType
from typing import Optional, List, Callable, Dict, Sequence, Tuple, Any, Union

# сторонние модули
from trivial_tools.formatters.base import s_type

JSON_RPC = Dict[str, Any]


OK: int = 200
BAD_REQUEST: int = 400
NOT_AUTHORIZED: int = 401
METHOD_NOT_ALLOWED: int = 405
NOT_ACCEPTABLE: int = 406
INTERNAL_ERROR: int = 500


class JSONRPCMethodMaster:
    """
    Регистратор методов для JSON-RPC.
    Используется для централизованного управления всеми методами приложения.
    """
    def __init__(self, ignores: Sequence[str] = ('secret_key',)):
        """
        Инициация
        """
        self._ignores = ['return'] + list(ignores)
        self._methods: Dict[str, Callable] = {}

    def __contains__(self, item):
        """
        Проверить, имеется ли этот метод в записях.
        """
        return item in self._methods

    def register_method(self, func: FunctionType) -> FunctionType:
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

    def check_signature(self, body: Union[JSON_RPC, List[JSON_RPC]]):
        """
        Проверка полученных параметров на соответствие сигнатуре метода
        """
        response = []
        return_code = NOT_ACCEPTABLE

        if isinstance(body, dict):
            error_message = self._check_signature(body)
            if error_message:
                return {'code': -32602, 'message': error_message}, return_code
            else:
                return body, OK

        else:
            for sub_body in body:
                error_message = self._check_signature(sub_body)
                if error_message:
                    response.append(({'code': -32602, 'message': error_message}, return_code))
                else:
                    response.append(({'code': -32602, 'message': error_message}, OK))

        return response, return_code

    def _check_signature(self, body: JSON_RPC) -> str:
        """
        Проверка полученных параметров на соответствие сигнатуре метода
        """
        method_name = body.get('method')
        parameters = body.get('params').keys()

        method: FunctionType = self._methods[method_name]

        sig = signature(method)

        valid_keys = {x for x in sig.parameters if x not in self._ignores}
        other_keys = {x for x in parameters if x not in self._ignores}

        response = 'Расхождение в аргументах метода: '

        if valid_keys != other_keys:
            insufficient = ', '.join(valid_keys - other_keys)
            excess = ', '.join(other_keys - valid_keys)

            if insufficient:
                response += 'не хватает аргументов ' + insufficient

                if excess:
                    response += ', '

            if excess:
                response += 'лишние аргументы ' + excess

            return response
        return ''

    def get_method(self, method_name: str) -> Optional[Callable]:
        """
        Получить метод
        """
        return self._methods.get(method_name)

    def get_method_names(self) -> List[str]:
        """
        Получить имена доступных методов
        """
        return sorted(self._methods.keys())

    @staticmethod
    def extract_json(request) -> Tuple[Union[JSON_RPC, List[JSON_RPC]], int]:
        """
        Безопасное извлечение JSON из запроса
        """
        try:
            request_body = request.json()
            return_code = OK

        except json.JSONDecodeError as err:
            request_body = {'code': -32700, 'message': f'Неправильный формат запроса, {err}'}
            return_code = BAD_REQUEST

        return request_body, return_code

    def check_request(self, body: Union[JSON_RPC, List[JSON_RPC]])\
            -> Tuple[Union[JSON_RPC, List[JSON_RPC]], int]:
        """
        Проверить на предмет соответствия JSON RPC 2.0
        """
        return_code = BAD_REQUEST

        if isinstance(body, dict):
            response, return_code = self.check_dict(body)

        elif isinstance(body, list):
            response = []
            for sub_body in body:
                checked_body, return_code = self.check_dict(sub_body)

                if return_code != OK:
                    break

                response.append(checked_body)
        else:
            response = {'code': -32700, 'message': f'Неправильный формат запроса, {s_type(body)}'}

        return response, return_code

    def check_dict(self, body: JSON_RPC) -> Tuple[JSON_RPC, int]:
        """
        Проверить словарь запроса
        """
        return_code = BAD_REQUEST

        version = body.get('jsonrpc')
        method = body.get('method')
        params = body.get('params')

        if version != '2.0':
            return {'code': -32600,
                    'message': 'Поддерживается только JSON-RPC 2.0.'}, return_code

        if method is None:
            return {'code': -32601,
                    'message': 'Не указан метод запроса.'}, return_code

        elif method not in self._methods:
            return {'code': -32601,
                    'message': f'Неизвестный метод: {method}.'}, METHOD_NOT_ALLOWED

        if params is None:
            return {'code': -32602,
                    'message': 'Не указаны аргументы вызова.'}, return_code

        elif params.get('secret_key') is None:
            return {'code': -32602,
                    'message': 'Не предоставлен ключ авторизации.'}, NOT_AUTHORIZED

        elif isinstance(params, list):
            return {'code': -32602,
                    'message': 'Передача аргументов по позиции не поддерживается.'}, NOT_ACCEPTABLE

        elif not isinstance(params, dict):
            return {'code': -32602,
                    'message': f'Неправильно оформлены аргументы: {params}'}, NOT_ACCEPTABLE

        return body, OK

    @staticmethod
    def authorize(body: JSON_RPC, check_func: Callable) -> Tuple[JSON_RPC, int]:
        """
        Проверить авторизацию внешней функцией
        """
        checked_body, return_code = check_func(body)
        if return_code != OK:
            return {'code': -32602,
                    'message': f'Отказано в доступе.'}, NOT_AUTHORIZED
        return checked_body, OK

    def execute(self, body: JSON_RPC) -> Any:
        """
        Исполнить запрос
        """
        method_name = body.get('method')
        params = body.get('params', {})
        method = self.get_method(method_name)

        # секуретный ключ не нужен внутри методов
        params.pop('secret_key', None)

        response = method(**params)
        return response
