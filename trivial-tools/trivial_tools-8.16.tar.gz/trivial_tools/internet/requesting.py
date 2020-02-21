# -*- coding: utf-8 -*-
"""

    Инструменты запросов

"""
# встроенные модули
from typing import Dict, Any, Optional

# сторонние модули
import requests
from loguru import logger

# модули проекта
from trivial_tools.runners.base import repeat_on_exceptions


def make_post(url: str, json: dict) -> Optional[Dict[str, Any]]:
    """
    Выполнить POST запрос и получить данные
    """
    response = requests.post(url, json=json)

    if response.status_code == 200:
        result = response.json()
    else:
        logger.critical(f'Код возврата: {response.status_code}')
        logger.critical(response.content.decode('utf-8'))
        result = None

    return result


@repeat_on_exceptions(repeats=0, case=requests.ConnectionError, delay=1.0)
def make_safe_post(url: str, json: dict) -> Optional[Dict[str, Any]]:
    """
    Безопасный вариант POST запроса
    """
    return make_post(url, json)
