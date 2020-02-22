# -*- coding: utf-8 -*-
"""

    Инструменты проверок типов

"""
# встроенные модули
from typing import Any


def is_int(something: Any) -> bool:
    """Проверить, можно ли этот объект преобразовать в int.

    :param something: неизвестный объект, который надо преобразовать
    :return: True если можно преобразовать, False если нельзя

    >>> is_int('25')
    True

    >>> is_int(25.4)
    True

    >>> is_int('0.25')
    False
    """
    try:
        int(something)
        return True
    except (ValueError, TypeError):
        # Для вариантов типа str(0.25) базовая проверка возвращает False!
        return False


def is_float(something: Any) -> bool:
    """Проверить, можно ли этот объект преобразовать в float.

    :param something: неизвестный объект, который надо преобразовать
    :return: True если можно преобразовать, False если нельзя

    >>> is_float('0.25')
    True

    >>> is_float(25)
    True

    >>> is_float('test')
    False
    """
    try:
        float(something)
        return True
    except (ValueError, TypeError):
        return False
