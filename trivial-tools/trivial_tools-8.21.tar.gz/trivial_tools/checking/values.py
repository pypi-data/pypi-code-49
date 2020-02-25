# -*- coding: utf-8 -*-
"""

    Инструменты для проверки значений

"""
# встроенные модули
from typing import Collection, Optional, List, TypeVar, Any

T = TypeVar('T')
OptCol = Optional[Collection[T]]


def filter_by_inclusion(collection: Collection[T], only: OptCol = None,
                        without: OptCol = None, sort: bool = True) -> List[T]:
    """
    Отфильтровать по вхождению в диапазон
    """
    result = list(collection)

    if only:
        only = set(only)
        result = [x for x in result if x in only]

    if without:
        without = set(without)
        result = [x for x in result if x not in without]

    if sort:
        return sorted(result)
    return result


def filter_by_value(collection: Collection[T], start: Optional[Any] = None,
                    stop: Optional[Any] = None, sort: bool = True) -> List[T]:
    """
    Отфильтровать по величине
    """
    result = list(collection)

    if start:
        result = [x for x in result if x >= start]

    if stop:
        result = [x for x in result if x <= stop]

    if sort:
        return sorted(result)
    return result
