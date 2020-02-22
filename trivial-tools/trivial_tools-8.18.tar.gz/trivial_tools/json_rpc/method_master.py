# -*- coding: utf-8 -*-

"""
    Регистратор методов для JSON-RPC.

    Используется для централизованного управления всеми методами приложения.

"""
# встроенные модули
import json
from inspect import signature
from types import FunctionType
from typing import Optional, List, Callable, Dict, Sequence, Union, Tuple, Coroutine

# сторонние модули
from trivial_tools.formatters.base import s_type
from trivial_tools.json_rpc.basic_tools import (
    Request, Error, form_error, GroupRequest, Result, decide, authorize,
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
    def extract_json(request) -> Tuple[Union[Request, Coroutine, None], Optional[Error]]:
        """
        Безопасное извлечение JSON из запроса.
        """
        try:
            try:
                # Starlette, Requests
                response = request.json()
            except AttributeError:
                # Flask
                response = request.get_json()

            error_response = None
        except json.JSONDecodeError as err:
            response = None
            error_response = form_error(-32600, f'Неправильный формат запроса, {s_type(err)}{err}')

        return response, error_response

    def check_signature_conveyor(self, input_list: GroupRequest, requests: List[Request],
                                 errors: List[Error]) -> None:
        """
        Проверка полученных параметров на соответствие сигнатуре метода.
        """
        while input_list:
            new_request = input_list.pop()
            output = self._check_signature(new_request)
            decide(output, requests, errors)

    def check_request_conveyor(self, input_list: GroupRequest, requests: List[Request],
                               errors: List[Error]) -> None:
        """
        Проверить на предмет соответствия JSON RPC 2.0.
        """
        while input_list:
            new_request = input_list.pop()
            output = self.check_dict(new_request)
            decide(output, requests, errors)

    def check_auth_conveyor(self, input_list: GroupRequest, requests: List[Request],
                            errors: List[Error]) -> None:
        """
        Проверить авторизацию внешней функцией.
        """
        while input_list:
            new_request = input_list.pop()
            output = authorize(new_request, self.auth_func)
            decide(output, requests, errors)

    def _check_signature(self, request: Request) -> Union[Request, Error]:
        """
        Проверка полученных параметров на соответствие сигнатуре метода.
        """
        method_name = request.get('method')
        parameters = request.get('params').keys()
        msg_id = request.get('id')
        need_id = 'id' in request

        method: FunctionType = self._methods[method_name]

        sig = signature(method)

        valid_keys = {x for x in sig.parameters if x not in self._ignores}
        other_keys = {x for x in parameters if x not in self._ignores}

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

        elif isinstance(params, list):
            response = form_error(
                -32602, 'Позиционные аргументы не поддерживаются.', need_id, msg_id
            )

        elif not isinstance(params, dict):
            response = form_error(
                -32602, 'Неправильно оформлены аргументы вызова метода.', need_id, msg_id
            )

        elif params.get('secret_key') is None:
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

        # секретный ключ не нужен внутри методов
        params.pop('secret_key', None)

        # @@@@@@@@@@@@@@@@@@@@@@@@
        response = method(**params)
        # @@@@@@@@@@@@@@@@@@@@@@@@

        return response
