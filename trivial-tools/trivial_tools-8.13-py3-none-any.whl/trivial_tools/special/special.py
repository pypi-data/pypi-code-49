# -*- coding: utf-8 -*-
"""

    Особые инструменты

"""
# встроенные модули
from itertools import zip_longest
from typing import NoReturn, Optional, Type, Sequence, Callable, List, Any

# модули проекта
from trivial_tools.formatters.base import decorate


def fail(message: str, reason: Type[Exception] = RuntimeError,
         raise_from: Optional[Exception] = None) -> NoReturn:
    """Выбросить исключение с заданным текстовым сообщением

    :param message: сообщение, которое необходимо передать
    :param reason: исключение, которые необходимо вызвать
    :param raise_from: возбудить исключение из переданного экземпляра
    :return: нет возврата
    """
    if isinstance(reason, (UnicodeDecodeError, UnicodeTranslateError, UnicodeEncodeError)):
        # Unicode ошибки нельзя выбросить просто с одним текстовым сообщением
        raise

    if isinstance(raise_from, Exception):
        # выбрасываем из экземпляра класса исключений
        name = raise_from.__class__.__name__
        instance = type(raise_from)(decorate(f'{name}: {message}'))
        raise instance from raise_from

    # выбрасываем из класса исключений
    name = reason.__name__

    # В настоящий момент (python 3.7) нет способа корректно указать исключения в аннотациях типов.
    # noinspection PyCallingNonCallable
    raise reason(decorate(f'{name}: {message}'))


def group_cast(elements: Sequence, *casters: Callable) -> List[Any]:
    """Выполнить групповое преобразование типа.

    Может сэкономить немного места на конверсиях.

    :param elements: последовательность элементов для преобразования.
    :param casters: последовательность типов или функций для преобразования
    :return: список преобразованных элементов
    """
    if not casters:
        return list(elements)

    elif casters[-1] != Ellipsis and len(casters) == len(elements):
        return [func(val) for func, val in zip(casters, elements)]

    elif casters[-1] == Ellipsis and len(casters) >= 2:
        return [func(val) for func, val in
                zip_longest(casters[:-1], elements, fillvalue=casters[-2])]

    fail(f'Количество преобразователей ({len(casters)}) не '
         f'совпадает с количеством аргументов ({len(elements)})!', reason=ValueError)
