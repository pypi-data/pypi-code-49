# -*- coding: utf-8 -*-
"""

    Инструменты для работы с API

"""
# встроенные модули
from typing import Optional, Any

# сторонние модули
import requests
from loguru import logger

# модули проекта
from trivial_tools.special.special import fail
from trivial_tools.formatters.base import dict_as_args
from trivial_tools.runners.base import repeat_on_exceptions
from trivial_tools.json_rpc.basic_tools import form_request


@repeat_on_exceptions(repeats=5, case=Exception, delay=1)
def call_api(url: str, *, method: str, error_msg: str, debug: bool, **kwargs) -> Optional[Any]:
    """
    Выполнить POST запрос
    """
    payload = form_request(
        method=method,
        msg_id=kwargs.get('msg_id'),
        **kwargs
    )

    if debug:
        # запомнить, что мы запросили, скрыть секреты
        safe_kwargs = {
            key: value if key != 'secret_key' else '***' for key, value in kwargs.items()
        }
        logger.debug(f'---> {method}({dict_as_args(safe_kwargs)})')

    r = requests.post(url, json=payload)

    if r.status_code == 200:
        body = r.json()

        if 'result' in body:
            result = body['result']

            if debug:
                # запомнить, что мы получили
                logger.debug(f'<--- {method}: <' + str(result)[0:100] + '>')

            return result

        else:
            post_mortem = body['error']
    else:
        post_mortem = r.content.decode('utf-8')

    logger.critical(post_mortem)
    fail(error_msg, reason=ConnectionError)
    return None
