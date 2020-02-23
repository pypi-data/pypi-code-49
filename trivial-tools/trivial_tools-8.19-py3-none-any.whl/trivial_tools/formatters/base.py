# -*- coding: utf-8 -*-
"""

    Инструменты форматирования текста

"""
# встроенные модули
from typing import Any, Sequence, Union


def decorate(message: str, symbol: str = '+', line_width: int = 79) -> str:
    """Вывести текст в обрамлении символов

    :param message: оригинальное сообщение
    :param symbol: каким символом написать строки
    :param line_width: какую ширину заполнить символами
    :return: оформленное текстовое сообщение в виде нескольких строк
    """
    separator = '\n' + symbol * line_width + '\n'
    result = separator + message.strip() + separator
    return result


def s_type(something: Any) -> str:
    """
    Вывести укороченное название типа

    >>> s_type(9)
    'int'

    >>> s_type(None)
    'NoneType'

    >>> class MyTestClass: pass
    >>> s_type(MyTestClass())
    'MyTestClass'

    >>> s_type(Union[int, type(None)])
    'typing.Union[int, NoneType]'
    """
    if isinstance(something, type):
        return something.__name__

    result = type(something).__name__
    if result == '_GenericAlias':
        return str(something).lstrip('typing.')

    return result


def shorten(something: Any) -> str:
    """
    Выдать укороченную форму записи
    """
    if isinstance(something, str):
        if len(something) <= 20:
            result = repr(something)
        else:
            result = repr(something[:10] + ' ... ' + something[-10:])

    elif isinstance(something, Sequence):
        if len(something) <= 10:
            result = repr(something)
        else:
            result = (', '.join(repr(x) for x in something[0:4])
                      + ' ... '
                      + ', '.join(repr(x) for x in something[-4:]))

            if isinstance(something, list):
                result = f'[{result}]'

            elif isinstance(something, tuple):
                result = f'({result})'
    else:
        result = repr(something)

    return result


def detail(something: Any) -> str:
    """
    Вывести параметри неизвестного объекта

    >>> detail(9)
    '9, int'
    """
    return f'{shorten(something)}, {s_type(something)}'


def dict_as_args(input_dict: dict) -> str:
    """
    Разложить словарь на последовательность аргументов будто это ключевые слова

    >>> dict_as_args(dict(a=1, b=2, c="test"))
    "a=1, b=2, c='test'"
    """
    return ', '.join(f'{key}={value!r}' for key, value in input_dict.items())
