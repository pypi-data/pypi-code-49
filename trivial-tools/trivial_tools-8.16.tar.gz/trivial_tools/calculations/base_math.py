# -*- coding: utf-8 -*-
"""

    Инструменты простых вычислений

"""
# встроенные модули
import math
from typing import Union

SUFFIXES = {
    'RU': {'B': 'Б', 'kB': 'кБ', 'MB': 'МБ', 'GB': 'ГБ', 'TB': 'ТБ', 'PB': 'ПБ', 'EB': 'ЭБ',
           'KiB': 'КиБ', 'MiB': 'МиБ', 'GiB': 'ГиБ', 'TiB': 'ТиБ', 'PiB': 'ПиБ', 'EiB': 'ЭиБ'},
    'EN': {'B': 'B', 'kB': 'kB', 'MB': 'MB', 'GB': 'GB', 'TB': 'TB', 'PB': 'PB', 'EB': 'EB',
           'KiB': 'KiB', 'MiB': 'MiB', 'GiB': 'GiB', 'TiB': 'TiB', 'PiB': 'PiB', 'EiB': 'EiB'},
}


def math_round(number: float, decimals: int = 0) -> float:
    """Округлить математическиим (не банковским) способом.

    Работает обычным математическим образом, в отличие от встроенной функции round(),
    которая использует банковское округление.

    :param number: число, которое требуется округлить
    :param decimals: сколько разрядов после запятой оставить
    :return: округлённое число с плавающей запятой

    >>> math_round(2.735, 2)
    2.74
    >>> round(2.735, 2)
    2.73
    """
    if math.isnan(number):
        return math.nan

    exp = number * 10 ** decimals
    if abs(exp) - abs(math.floor(exp)) < 0.5:
        return math.floor(exp) / 10 ** decimals
    return math.ceil(exp) / 10 ** decimals


def sep_digits(number: Union[int, float, str], precision: int = 2) -> str:
    """
    Вывести число с разделением на разряды

    >>> sep_digits('12345678')
    '12345678'

    >>> sep_digits(12345678)
    '12 345 678'

    >>> sep_digits(1234.5678)
    '1 234.57'

    >>> sep_digits(1234.5678, precision=4)
    '1 234.5678'
    """
    if isinstance(number, int):
        result = '{:,}'.format(number).replace(',', ' ')

    elif isinstance(number, float):
        result = '{:,}'.format(math_round(number, precision)).replace(',', ' ')
        if '.' in result:
            tail = result.rsplit('.')[-1]
            result += '0' * (precision - len(tail))

    else:
        result = str(number)

    return result


def byte_count_to_si(total_bytes: int, lang: str = 'RU') -> str:
    """
    Перевести число байт в укороченную форму согласно системы СИ, по основанию 1000

    :param total_bytes: целое число байт
    :param lang: язык, на котором должен быть написан суффикс
    :return: текстовое представление величины

    >>> byte_count_to_si(1023)
    '1.0 kB'
    """
    prefix = ''
    if total_bytes < 0:
        prefix = '-'
        total_bytes = abs(total_bytes)

    if total_bytes < 1000:
        return f'{prefix}{int(total_bytes)} ' + SUFFIXES[lang]['B']

    if total_bytes < 999_950:
        return f'{prefix}{total_bytes / 1000:0.1f} ' + SUFFIXES[lang]['kB']

    total_bytes /= 1000

    if total_bytes < 999_950:
        return f'{prefix}{total_bytes / 1000 :0.1f} ' + SUFFIXES[lang]['MB']

    total_bytes /= 1000

    if total_bytes < 999_950:
        return f'{prefix}{total_bytes / 1000 :0.1f} ' + SUFFIXES[lang]['GB']

    total_bytes /= 1000

    if total_bytes < 999_950:
        return f'{prefix}{total_bytes / 1000 :0.1f} ' + SUFFIXES[lang]['TB']

    return f'{prefix}{total_bytes / 1_000_000_000 :0.1f} ' + SUFFIXES[lang]['EB']


def byte_count_to_text(total_bytes: int, lang: str = 'RU') -> str:
    """
    Перевести число байт в укороченную форму по основанию 1024

    :param total_bytes: целое число байт
    :param lang: язык, на котором должен быть написан суффикс
    :return: текстовое представление величины

    >>> byte_count_to_text(1023)
    '1023 B'
    """
    prefix = ''
    if total_bytes < 0:
        prefix = '-'
        total_bytes = abs(total_bytes)

    if total_bytes < 1024:
        return f'{prefix}{int(total_bytes)} ' + SUFFIXES[lang]['B']

    total_bytes /= 1024

    if total_bytes < 1024:
        return f'{prefix}{total_bytes:0.1f} ' + SUFFIXES[lang]['KiB']

    total_bytes /= 1024

    if total_bytes < 1024:
        return f'{prefix}{total_bytes:0.1f} ' + SUFFIXES[lang]['MiB']

    total_bytes /= 1024

    if total_bytes < 1024:
        return f'{prefix}{total_bytes:0.1f} ' + SUFFIXES[lang]['GiB']

    total_bytes /= 1024

    if total_bytes < 1024:
        return f'{prefix}{total_bytes:0.1f} ' + SUFFIXES[lang]['TiB']

    return f'{total_bytes / 1024 / 1024 :0.1f} ' + SUFFIXES[lang]['EiB']
