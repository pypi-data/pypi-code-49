# -*- coding: utf-8 -*-
"""

    Простые инструменты для работы с JSON-RPC

"""
# встроенные модули
from typing import Dict, Any, Union, Optional


def form_request(*, method: str, msg_id: Optional[Union[int, str]] = None,
                 **kwargs) -> Dict[str, Any]:
    """
    Собрать запрос к API
    """
    return {"jsonrpc": "2.0", "method": method, "params": {**kwargs}, "id": msg_id}


def result(output: Any, need_id: bool = True,
           msg_id: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """
    Успешный результат
    """
    if need_id:
        return {"jsonrpc": "2.0", "result": output, "id": msg_id}
    return {"jsonrpc": "2.0", "result": output}


def error(output: Any, need_id: bool = True,
          msg_id: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    """
    Неудачный результат
    """
    if need_id:
        return {"jsonrpc": "2.0", "error": output, "id": msg_id}
    return {"jsonrpc": "2.0", "error": output}
