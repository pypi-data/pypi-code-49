# -*- coding: utf-8 -*-

"""

    Простые инструменты для работы с JSON-RPC

"""
# встроенные модули
from typing import Dict, Any, Union, Optional, TypedDict, Literal, List, Callable

LIKE_JSON = Dict[str, Union[int, str, float, bool, None, list, dict]]
MSG_ID = Optional[Union[str, int, None]]


class Request(TypedDict):
    """
    JSON-RPC запрос.
    """
    jsonrpc: Literal["2.0"]
    method: str
    params: LIKE_JSON
    id: MSG_ID


class Result(TypedDict):
    """
    JSON-RPC ответ.
    """
    jsonrpc: Literal["2.0"]
    result: LIKE_JSON
    id: MSG_ID


class ErrorMessage(TypedDict):
    """
    JSON-RPC описание ошибки.
    """
    code: int
    message: str


class Error(TypedDict):
    """
    JSON-RPC ошибка.
    """
    jsonrpc: Literal["2.0"]
    error: ErrorMessage
    id: MSG_ID


Response = Union[Result, Error]


def form_request(*, method: str, msg_id: MSG_ID = None, **kwargs) -> Request:
    """
    Собрать запрос к API.
    """
    if msg_id and 'id' not in kwargs:
        return {'jsonrpc': '2.0', 'method': method, 'params': {**kwargs}, 'id': msg_id}

    elif 'id' in kwargs:
        msg_id = kwargs.pop('id')
        return {'jsonrpc': '2.0', 'method': method, 'params': {**kwargs}, 'id': msg_id}

    elif msg_id is None and 'id' not in kwargs:
        return {'jsonrpc': '2.0', 'method': method, 'params': {**kwargs}}

    return {'jsonrpc': '2.0', 'method': method, 'params': {**kwargs}, 'id': msg_id}


def result(output: Any, need_id: bool = True, msg_id: MSG_ID = None) -> Result:
    """
    Успешный результат.
    """
    if need_id:
        return {"jsonrpc": "2.0", "result": output, "id": msg_id}
    return {"jsonrpc": "2.0", "result": output}


def error(output: Any, need_id: bool = True, msg_id: MSG_ID = None) -> Error:
    """
    Неудачный результат.
    """
    if need_id:
        return {"jsonrpc": "2.0", "error": output, "id": msg_id}
    return {"jsonrpc": "2.0", "error": output}


def form_error(code: int, message: str, need_id: bool = True, msg_id: MSG_ID = None) -> Error:
    """
    Сформировать ошибку.
    """
    return error({"code": code, "message": message}, need_id=need_id, msg_id=msg_id)


def authorize(request: Request, check_func: Callable) -> Union[Request, Error]:
    """
    Проверить авторизацию внешней функцией.
    """
    valid = check_func(request)

    if valid:
        return request

    msg_id = request.get('id')
    need_id = 'id' in request
    return form_error(-32602, 'Отказано в доступе.', need_id, msg_id)


def decide(request: Union[Request, Error], requests: List[Request], errors: List[Error]) -> None:
    """
    Отсортировать на ошибочные и нормальные пакеты.
    """
    if 'error' in request:
        errors.append(request)
    else:
        requests.append(request)
