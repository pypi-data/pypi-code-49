# -*- coding: utf-8 -*-
"""

    Кеширующий класс

"""
# встроенные модули
from types import FunctionType
from typing import Any, Dict, Optional

# модули проекта
from trivial_tools.storage.caching_instance import CachingInstance


class CachingMachine:
    """
    Специальный класс для выполнения функции локального кеша.
    Redis для бедных. Подразумевается, что эта штука может его
    временно заменить при сильной необходимости
    """
    def __init__(self, expiration: Optional[int] = None, max_items: int = 1000):
        self.expiration = expiration
        self.max_items = max_items
        self._cache: Dict[str, CachingInstance] = {}

    def __getitem__(self, item):
        """
        Прямой доступ к содержимому словаря
        """
        return self._cache[item]

    def __contains__(self, item):
        """
        Проверка наличия внутри кеша
        """
        return item in self._cache

    def extract(self, key: Any) -> Optional[Any]:
        """
        Общая функция извлечения значения. В отличии от редиса,
        мы можем хранить какие попало значения, поэтому в итоге всё сводится к
        одной этой функции
        """
        if key in self._cache:
            instance = self._cache[key]
            if instance.not_expired():
                return self._cache[key].value
            else:
                self.delete(key)
        return None

    def assign(self, key: Any, value: Any, expires: Optional[int] = None) -> bool:
        """
        Общая функция установки значения. В отличии от редиса,
        мы можем хранить какие попало значения, поэтому в итоге всё сводится к
        одной этой функции. Типы должны быть проверены перед вызовом
        """
        if self.is_full():
            self.cleanup()
            if self.is_full():
                return False

        if expires is None:
            expires = self.expiration

        self._cache[key] = CachingInstance(
            value=value,
            expires=expires
        )
        return True

    def get(self, key: str) -> Optional[str]:
        """
        Получить строковое значение по ключу
        """
        return self.extract(key)

    def set(self, key: str, value: str, expires: Optional[int] = None) -> bool:
        """
        Установить строковое значение по ключу
        """
        if not isinstance(value, str):
            print('Метод set принимает только строковые значения!')
            return False

        return self.assign(key, value, expires)

    def exists(self, key: str) -> bool:
        """
        Проверить, есть ли у нас значение для этого ключа
        """
        return key in self._cache

    def delete(self, key: str) -> bool:
        """
        Удалить значение из кеша
        """
        if self.exists(key):
            del self._cache[key]
            return True
        return False

    def total(self) -> int:
        """
        Узнать сколько элементов мы храним
        """
        return len(self._cache)

    def clear(self):
        """
        Очистить память
        """
        self._cache.clear()

    def cleanup(self) -> int:
        """
        Удалить устаревшие элементы
        """
        removed = 0
        keys = list(self._cache.keys())
        for key in keys:
            if self.exists(key) and self[key].expired():
                self.delete(key)
                removed += 1
        return removed

    def is_full(self):
        """
        Проверить заполнен ли кеш
        """
        return self.total() == self.max_items

    def keys(self) -> list:
        """
        Получить все ключи машины
        """
        return list(self._cache.keys())

    def cache_call(self, expires: Optional[int] = None):
        """
        Кешировать результат выполнения функции
        """
        def decorator(func: FunctionType):
            def wrapper(*args):
                key = (func.__name__, args)
                if key in self:
                    result = self.extract(key)
                else:
                    result = func(*args)
                    self.assign(key, result, expires)
                return result
            return wrapper
        return decorator

    def cache_call_using_strings(self, expires: Optional[int] = None):
        """
        Кешировать результат выполнения функции, но ключи хранить в виде строк
        """
        def decorator(func: FunctionType):
            def wrapper(*args):
                key = f'{func.__name__}_' + '_'.join(str(x) for x in args)
                if key not in self:
                    result = func(*args)
                    self.assign(key, result, expires)
                value = self.extract(key)
                return value
            return wrapper
        return decorator
