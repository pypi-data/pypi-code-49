# -*- coding: utf-8 -*-
"""

    Функция красивой печати

"""
# встроенные модули
from typing import Any, List
from collections.abc import Collection, Mapping, Sized


def render(something: Any, threshold: int, storage: list, tab: str = '') -> None:
    """
    Собрать текстовое представление для варианта с коротким списком аргументов
    """
    sub_storage = []
    i = 1
    if isinstance(something, Mapping):
        sub_storage += [tab + '{']
        sub_storage.extend(render_dict(something, threshold, tab))
        sub_storage += [tab + '}']

    elif isinstance(something, Collection):
        if isinstance(something, list):
            left, right = '[]'
        elif isinstance(something, (set, frozenset)):
            left, right = '{}'
        elif isinstance(something, tuple):
            left, right = '()'
        else:
            left, right = '<>'

        sub_storage += [tab + left]
        sub_storage.extend(render_list(something, threshold, tab))
        sub_storage += [tab + right]

    else:
        sub_storage.append(f'{tab}{i}| {something}')

    storage.extend(sub_storage)


def render_dict(something: Mapping, threshold: int, tab: str) -> List[str]:
    """
    Разложить словарь
    """
    i = 1
    sub_storage = []

    order = '{:0' + str(len(str(len(something)))) + 'd}'

    for key, value in something.items():
        if isinstance(value, Sized) and len(value) > threshold:
            add = []
            render(value, threshold, add, tab + '\t')
            sub_storage.extend(add)
        else:
            sub_storage.append(f'{tab}{order.format(i)}| {key}={value!r}')
        i += 1

    return sub_storage


def render_list(something: Collection, threshold: int, tab: str) -> List[str]:
    """
    Разложить список или что то подобное
    """
    i = 1
    sub_storage = []

    order = '{:0' + str(len(str(len(something)))) + 'd}'

    for element in something:
        if isinstance(element, Sized) and len(element) > threshold:
            add = []
            render(element, threshold, add, tab + '\t')
            sub_storage.extend(add)
        else:
            sub_storage.append(f'{tab}{order.format(i)}| {element!r}')
        i += 1

    return sub_storage


def unfolds(something: Any, threshold: int = 2) -> str:
    """
    Красивая печать с разложением на компоненты
    """
    storage = []
    render(something, threshold, storage)
    return '\n'.join(storage)
