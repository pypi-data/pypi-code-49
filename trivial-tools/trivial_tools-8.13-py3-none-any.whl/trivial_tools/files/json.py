# -*- coding: utf-8 -*-
"""

    Инструменты обработки JSON файлов

"""
# встроенные модули
import os
import sys
import json
from typing import Dict, Any, Optional

# сторонние модули
from loguru import logger


def json_config_load(filename: str, config_name: Optional[str],
                     default_config: str) -> Dict[str, Any]:
    """
    Открыть указанный файл и прочитать его содержимое
    """
    path = os.path.join(os.getcwd(), filename)

    if not os.path.exists(path):
        logger.critical(f'Не найден файл конфигурации: "{path}"')
        raise FileNotFoundError

    with open(path, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    if default_config not in data:
        logger.critical(f'В конфиге не представлен обязательный раздел "{default_config}"')
        raise KeyError

    if config_name in data:
        resulting_config = {**data.get('base', {}), **data[config_name]}
    else:
        resulting_config = {**data.get('base', {}), **data[default_config]}

    if resulting_config:
        return resulting_config

    logger.critical(f'Не удалось загрузить конфигурацию "{config_name}" из файла: "{path}"')
    sys.exit(1)
