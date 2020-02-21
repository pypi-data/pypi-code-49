# -*- coding: utf-8 -*-
"""

    Базовый класс для управления конфигурациями

"""
# встроенные модули
import os
import json
from abc import abstractmethod, ABC

# модули проекта
from trivial_tools.special.special import fail


class AbstractConfig(ABC):
    """
    Абстрактный класс для хранения параметров
    """
    default_config_name: str = 'base'

    @abstractmethod
    def __init__(self, **kwargs):
        """
        Инициация
        """

    @staticmethod
    def get_config_path(filename: str) -> str:
        """
        Получить путь к файлу конфигурации
        """
        folder = os.path.abspath(os.getcwd())
        if folder.endswith('tests'):
            # при тестировании конфиг обычно находится на каталог выше
            parts = os.path.split(folder)
            return os.path.join(*parts[:-1], filename)
        return os.path.join(folder, filename)

    @classmethod
    def extract_json(cls, config_name: str, path: str) -> dict:
        """
        Вытащить данные из JSON файла
        """
        if not os.path.exists(path):
            fail(f'Не найден файл конфигурации: "{path}"', reason=FileNotFoundError)

        with open(path, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        if config_name not in data:
            fail(f'В конфиге не представлен раздел "{config_name}"', reason=KeyError)

        config = {**data.get(cls.default_config_name, {}), **data[config_name]}

        if config:
            return config

        fail(f'Не удалось загрузить конфигурацию "{config_name}" из файла: "{path}"',
             reason=KeyError)

    @classmethod
    def from_json(cls, config_name: str, filename: str = 'config.json'):
        """
        Собрать экземпляр из JSON файла
        """
        path = cls.get_config_path(filename)
        data = cls.extract_json(config_name, path)
        return cls(created_from=path, **data)
