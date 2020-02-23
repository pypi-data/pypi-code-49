# -*- coding: utf-8 -*-
"""

    Набор инструментов для упрощённого кодирования времени

"""
# сторонние модули
from typing import Tuple

# модули проекта общие
from trivial_tools.special.special import fail


LETTERS = 'A B C D E F G H J K L M N P Q R S T U V W X Y Z'.split()


def encode_period(day_num: int, minute_num: int) -> str:
    """
    Зашифровать период

    Пример шифра: AA25

    Сначала идут две буквы, потом две цифры. Буква I не используется
    Нумерация дней и минут начинается с 1

    >>> encode_period(day_num=1, minute_num=1)
    'AA01'

    >>> encode_period(day_num=7, minute_num=800)
    'PH40'

    >>> encode_period(day_num=14, minute_num=37)
    'BN14'

    >>> encode_period(day_num=21, minute_num=1270)
    'NX87'

    >>> encode_period(day_num=31, minute_num=1440)
    'ZZ97'
    """
    if not (1 <= day_num <= 31) or not (1 <= minute_num <= 1440):
        fail(f'Неправильно указано время: день {day_num} [1, 31], минута {minute_num} [1, 1440]')

    sector, letters = encode_letters(minute_num)
    digits = encode_digits(day_num, sector)

    return letters + digits


def encode_letters(minute_num: int) -> Tuple[int, str]:
    """
    Получить буквенное начало

    >>> encode_letters(1)
    (1, 'AA')
    >>> encode_letters(1440)
    (3, 'ZZ')
    """
    base = minute_num - 1
    sector = base // 480 + 1

    value = minute_num % 480
    higher = (value - 1) // len(LETTERS)

    if higher > len(LETTERS) - 1:
        higher //= len(LETTERS)

    lower = base % len(LETTERS)
    code = LETTERS[higher] + LETTERS[lower]

    return sector, code


def encode_digits(day_num: int, sector: int) -> str:
    """
    Получить числовую концовку

    >>> encode_digits(1, 1)
    '01'

    >>> encode_digits(31, 2)
    '64'
    """
    return '{:02d}'.format(int(day_num + (sector - 1) * 33))


def decode_period(code: str) -> Tuple[int, int]:
    """
    Преобразовать период из кода в кортеж [день, минута]

    >>> decode_period('AA11')
    (11, 1)
    """
    if len(code) != 4:
        fail(f'Неправильно указан код периода: {code}')

    letters = code[0:2]
    digits = code[2:]
    day_num, sector = decode_digits(digits)
    minute = decode_letters(sector, letters)
    return day_num, minute


def decode_letters(sector: int, code: str) -> int:
    """
    Раскодировать буквенную часть кода

    >>> decode_letters(1, 'AA')
    1
    """
    min_value = (sector - 1) * 480 + 1
    max_value = sector * 480

    for i in range(min_value, max_value + 1):
        check_sector, check_code = encode_letters(i)
        if check_code == code:
            return i

    fail(f'Не удалось расшифровать код времени: {code}')


def decode_digits(code: str) -> Tuple[int, int]:
    """
    Раскодировать цифровую часть кода

    >>> decode_digits('64')
    (31, 2)
    """
    value = int(code)
    day_num = value % 33
    sector = value // 33 + 1
    return day_num, sector
