# -*- coding: utf-8 -*-
"""

    Регистратор методов для JSON-RPC.
    Используется для централизованного управления всеми методами приложения.

"""
# встроенные модули
import json
from enum import Enum
from inspect import signature
from types import FunctionType
from typing import Optional, List, Callable, Dict, Sequence, Tuple, Any, Union

# сторонние модули
from trivial_tools.formatters.base import s_type

# словарь запроса
SingleRequest = Dict[str, Any]
GroupRequest = List[Dict[str, Any]]

# словарь ответа
SingleResponse = Tuple[SingleRequest, int]


class HTTP(Enum):
    """
    Коды ответов
    """
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

    def check_signature(self, body: Union[SingleRequest, GroupRequest]) -> List[SingleResponse]:
        """
        Проверка полученных параметров на соответствие сигнатуре метода
        """
        if isinstance(body, dict):
            # одиночный запрос
            error_msg = self._check_signature(body)
            if error_msg:
                return [({'code': -32602, 'message': error_msg}, HTTP.NOT_ACCEPTABLE)]
            return [(body, HTTP.OK)]

        if isinstance(body, list):
            # групповой запрос
            response = []
            for sub_body in body:
                error_msg = self._check_signature(sub_body)
                if error_msg:
                    response.append(({'code': -32602, 'message': error_msg}, HTTP.BAD_REQUEST))
                else:
                    response.append((sub_body, HTTP.OK))

            return response

        # bad request
        bad_response = {'code': -32700, 'message': f'Неправильный формат запроса.'}
        return_code = HTTP.BAD_REQUEST
        return [(bad_response, return_code)]

    def _check_signature(self, body: SingleRequest) -> str:
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
    def extract_json(request) -> Tuple[Union[SingleRequest, List[SingleRequest]], int]:
        """
        Безопасное извлечение JSON из запроса
        """
        try:
            request_body = request.json()
            return_code = HTTP.OK

        except json.JSONDecodeError as err:
            request_body = {'code': -32700, 'message': f'Неправильный формат запроса, {err}'}
            return_code = HTTP.BAD_REQUEST

        return request_body, return_code

    def check_request(self, body: Union[SingleRequest, GroupRequest]) -> List[SingleResponse]:
        """
        Проверить на предмет соответствия JSON RPC 2.0
        """
        result = []

        if isinstance(body, dict):
            response, status_code = self.check_dict(body)
            result.append((response, status_code))

        elif isinstance(body, list):
            for sub_body in body:
                response, status_code = self.check_dict(sub_body)
                result.append((response, status_code))
        else:
            response = {'code': -32700, 'message': f'Неправильный формат запроса, {s_type(body)}'}
            result.append((response, HTTP.BAD_REQUEST))

        return result

    def check_dict(self, body: SingleRequest) -> SingleResponse:
        """
        Проверить словарь запроса
        """
        version = body.get('jsonrpc')
        method = body.get('method')
        params = body.get('params')

        response = body
        status_code = HTTP.OK

        if version != '2.0':
            response = {'code': -32600, 'message': 'Поддерживается только JSON-RPC 2.0.'}
            status_code = HTTP.BAD_REQUEST

        elif method is None:
            response = {'code': -32601, 'message': 'Не указан метод запроса.'}
            status_code = HTTP.BAD_REQUEST

        elif method not in self._methods:
            response = {'code': -32601, 'message': f'Неизвестный метод: {method}.'}
            status_code = HTTP.METHOD_NOT_ALLOWED

        elif params is None:
            response = {'code': -32602, 'message': 'Не указаны аргументы вызова.'}
            status_code = HTTP.BAD_REQUEST

        elif params.get('secret_key') is None:
            response = {'code': -32602, 'message': 'Не предоставлен ключ авторизации.'}
            status_code = HTTP.NOT_AUTHORIZED

        elif isinstance(params, list):
            response = {'code': -32602, 'message': 'Позиционные аргументы не поддерживаеются.'}
            status_code = HTTP.NOT_ACCEPTABLE

        elif not isinstance(params, dict):
            response = {'code': -32602, 'message': f'Неправильно оформлены аргументы: {params!r}'}
            status_code = HTTP.NOT_ACCEPTABLE

        return response, status_code

    @staticmethod
    def authorize(body: SingleRequest, check_func: Callable) -> SingleResponse:
        """
        Проверить авторизацию внешней функцией
        """
        response, status_code = check_func(body)

        if status_code != HTTP.OK:
            response = {'code': -32602, 'message': f'Отказано в доступе.'}
            status_code = HTTP.NOT_AUTHORIZED

        return response, status_code

    def execute(self, body: SingleRequest) -> Any:
        """
        Исполнить запрос
        """
        method_name = body.get('method')
        params = body.get('params', {})
        method = self.get_method(method_name)

        # секретный ключ не нужен внутри методов
        params.pop('secret_key', None)

        # @@@@@@@@@@@@@@@@@@@@@@@@
        response = method(**params)
        # @@@@@@@@@@@@@@@@@@@@@@@@

        return response
