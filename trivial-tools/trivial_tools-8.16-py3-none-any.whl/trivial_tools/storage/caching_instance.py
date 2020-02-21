# -*- coding: utf-8 -*-
"""

    Экземпляр поля для кеширующего класса

"""
# встроенные модули
from typing import Any, Optional
from datetime import datetime, timedelta


class CachingInstance:
    """
    Экземпляры этого класса хранятся в кеширующей машине
    """
    __slots__ = ('value', 'expires')

    def __init__(self, value: Any, expires: Optional[int] = None):
        self.value = value

        if expires is None:
            self.expires = None
        else:
            self.expires = datetime.now() + timedelta(seconds=expires)

    def expired(self) -> bool:
        """
        Проверить, протухло ли значение
        """
        return not self.not_expired()

    def not_expired(self) -> bool:
        """
        Проверить, не протухло ли значение
        """
        if self.expires is None:
            return True
        return bool(self.expires > datetime.now())

    def __repr__(self):
        """
        Текстовое представление
        """
        return f'{type(self).__name__}(value={self.value!r}, expires={self.expires!r})'
