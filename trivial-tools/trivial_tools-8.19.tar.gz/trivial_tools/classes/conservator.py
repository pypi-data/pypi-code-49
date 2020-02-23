# -*- coding: utf-8 -*-
"""

    Класс, хранящий экземпляр себя. Синглтон, для тех, кто пишет тесты

"""
# встроенные модули
from typing import TypeVar, Generic, Optional

# модули проекта
from trivial_tools.special.special import fail
from trivial_tools.formatters.base import s_type

T = TypeVar('T')


class Conservator(Generic[T]):
    """
    Класс, хранящий экземпляр себя
    """
    __instance: Optional[T] = None

    @classmethod
    def register(cls, instance: T) -> None:
        """
        Добавить валидный экземпляр
        """
        if not isinstance(instance, cls):
            fail(f'Класс {s_type(cls)} не добавляет посторонние типы!\n'
                 'При необходимости используйте метод register_force',
                 reason=ValueError)

        cls.register_force(instance)

    @classmethod
    def register_force(cls, instance: T) -> None:
        """
        Добавить валидный экземпляр
        """
        if cls.__instance:
            fail(f'Класс {s_type(cls)} уже имеет хранимый экземпляр!', reason=ValueError)

        cls.__instance = instance

    @classmethod
    def unregister(cls) -> None:
        """
        Удалить валидный экземпляр
        """
        if not cls.has_instance():
            fail(f'Класс {s_type(cls)} ещё не имеет хранимого экземпляра!', reason=ValueError)

        cls.__instance = None

    @classmethod
    def replace(cls, instance: T) -> None:
        """
        Заменить валидный экземпляр
        """
        previous = cls.__instance
        cls.unregister()
        try:
            cls.register(instance)
        except ValueError:
            cls.__instance = previous
            raise

    @classmethod
    def get_instance(cls) -> T:
        """
        Получить валидный экземпляр
        """
        if not cls.__instance:
            fail(f'Класс {s_type(cls)} ещё не имеет хранимого экземпляра!', reason=ValueError)

        return cls.__instance

    @classmethod
    def has_instance(cls) -> bool:
        """
        Проверить наличие экземпляра
        """
        return cls.__instance is not None
