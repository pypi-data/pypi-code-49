# -*- coding: utf-8 -*-
"""

    Регистратор методов для JSON-RPC.
    Используется для централизованного управления всеми методами приложения.

"""
# встроенные модули
import json
from inspect import signature
from types import FunctionType
from typing import Optional, List, Callable, Dict, Sequence, Union, TypedDict, Literal

# сторонние модули
from trivial_tools.json_rpc.basic_tools import error
from trivial_tools.formatters.base import s_type


class Request(TypedDict):
    """
    JSON-RPC запрос
    """
    jsonrpc: Literal['2.0']
    method: str
    params: Dict[str, Union[int, str, float, bool, None, list, dict]]
    id: Optional[Union[str, int, None]]


GroupRequest = List[Request]


class Result(TypedDict):
    """
    JSON-RPC ответ
    """
    jsonrpc: Literal['2.0']
    result: Dict[str, Union[int, str, float, bool, None, list, dict]]
    id: Union[int, str, None]


class ErrorMessage(TypedDict):
    """
    JSON-RPC описание ошибки
    """
    code: int
    message: str


class Error(TypedDict):
    """
    JSON-RPC ошибка
    """
    jsonrpc: Literal['2.0']
    error: ErrorMessage
    id: Union[int, str, None]


Response = Union[Result, Error]


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
        Получить метод
        """
        return self._methods.get(method_name)

    def get_method_names(self) -> List[str]:
        """
        Получить имена доступных методов
        """
        return sorted(self._methods.keys())

    def extract_json(self, request) -> Union[Request, Error]:
        """
        Безопасное извлечение JSON из запроса
        """
        try:
            if hasattr(request, 'get_json'):
                # Flask
                response = request.get_json()
            else:
                # Starlette
                response = request.json()

        except json.JSONDecodeError as err:
            response = self.form_err(
                -32600,
                f'Неправильный формат запроса, {s_type(err)}{err}', True, None
            )

        return response

    def check_signature(self, request: Union[Request, GroupRequest]) -> List[Union[Request, Error]]:
        """
        Проверка полученных параметров на соответствие сигнатуре метода
        """
        result = []
        if isinstance(request, dict):
            # одиночный запрос
            output = self._check_signature(request)
            result.append(output)

        elif isinstance(request, list):
            # групповой запрос
            for sub_request in request:
                output = self._check_signature(sub_request)
                result.append(output)

        else:
            output = self.form_err(-32600, f'Неправильный формат запроса, {s_type(request)}',
                                   True, None)
            result.append(output)

        return result

    def _check_signature(self, request: Request) -> Union[Request, Error]:
        """
        Проверка полученных параметров на соответствие сигнатуре метода
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

            return self.form_err(-32602, message, need_id, msg_id)
        return request

    def check_request(self, request: Union[Request, GroupRequest]) -> List[Union[Request, Error]]:
        """
        Проверить на предмет соответствия JSON RPC 2.0
        """
        result = []

        if isinstance(request, dict):
            output = self.check_dict(request)
            result.append(output)

        elif isinstance(request, list):
            for sub_body in request:
                output = self.check_dict(sub_body)
                result.append(output)
        else:
            output = self.form_err(-32600, f'Неправильный формат запроса, {s_type(request)}',
                                   True, None)
            result.append(output)

        return result

    @staticmethod
    def form_err(code: int, message: str, need_id: bool,
                 msg_id: Optional[Union[int, str]] = None) -> Error:
        """
        Сформировать ошибку
        """
        return error({"code": code, "message": message}, need_id=need_id, msg_id=msg_id)

    def check_dict(self, request: Request) -> Union[Request, Error]:
        """
        Проверить словарь запроса
        """
        version = request.get('jsonrpc')
        method = request.get('method')
        params = request.get('params')
        msg_id = request.get('id')
        need_id = 'id' in request

        if not request:
            response = self.form_err(-32600, 'Получен пустой запрос.', True, None)

        elif version != '2.0':
            response = self.form_err(-32600, 'Поддерживается только JSON-RPC 2.0.', need_id, msg_id)

        elif method is None:
            response = self.form_err(-32601, 'Не указан метод запроса.', need_id, msg_id)

        elif method not in self._methods:
            response = self.form_err(-32601, f'Неизвестный метод: "{method}".', need_id, msg_id)

        elif params is None:
            response = self.form_err(-32602, f'Не указаны аргументы вызова.', need_id, msg_id)

        elif isinstance(params, list):
            response = self.form_err(-32602, f'Позиционные аргументы не поддерживаеются.',
                                     need_id, msg_id)

        elif not isinstance(params, dict):
            response = self.form_err(-32602, f'Неправильно оформлены аргументы вызова метода.',
                                     need_id, msg_id)

        elif params.get('secret_key') is None:
            response = self.form_err(-32602, f'Не предоставлен ключ авторизации.', need_id, msg_id)

        else:
            response = request

        return response

    def authorize(self, request: Request, check_func: Callable) -> Union[Request, Error]:
        """
        Проверить авторизацию внешней функцией
        """
        valid = check_func(request)

        if not valid:
            msg_id = request.get('id')
            need_id = 'id' in request
            response = self.form_err(-32602, f'Отказано в доступе.', need_id, msg_id)
        else:
            response = request

        return response

    def execute(self, request: Request) -> Result:
        """
        Исполнить запрос
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
