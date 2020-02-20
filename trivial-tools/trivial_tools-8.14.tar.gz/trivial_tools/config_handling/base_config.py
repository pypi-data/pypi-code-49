# -*- coding: utf-8 -*-
"""

    Базовый класс для управления конфигурациями

"""
# встроенные модули
from contextlib import contextmanager

# модули проекта
from trivial_tools.classes.fluid import Fluid
from trivial_tools.config_handling import AbstractConfig
from trivial_tools.classes.conservator import Conservator


class BaseConfig(Fluid, Conservator, AbstractConfig):
    """
    Базовый класс конфигураций
    """
    @classmethod
    def from_json_if_need(cls, config_name: str, filename: str = 'config.json'):
        """
        Создать экземпляр только если он ещё не существует
        """
        if cls.has_instance():
            return cls.get_instance()
        return cls.from_json(config_name, filename)

    @classmethod
    @contextmanager
    def temporary_config(cls, **kwargs):
        """
        Контекстный менеджер для тестового экземпляра
        """
        if cls.has_instance():
            original = cls.get_instance()
            cls.unregister()
        else:
            original = None

        tmp_instance = cls(**kwargs)
        cls.register(tmp_instance)

        yield

        if original is None:
            cls.unregister()
        else:
            cls.replace(original)
