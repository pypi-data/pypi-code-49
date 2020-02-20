# -*- coding: utf-8 -*-
"""

    Тесты шифрования интервалов времени

"""

from trivial_tools.datetime_tools.coding import (
    encode_digits, encode_letters, encode_period, decode_letters, decode_digits, decode_period
)


def test_encode_digits_unique():
    """
    Должен выдавать уникальный код времени для дня
    """
    codes = set()

    for sector in [1, 2, 3]:
        for day in range(1, 32):
            code = encode_digits(day, sector)
            codes.add(code)

    assert len(codes) == 31 * 3


def test_encode_letters_unique():
    """
    Должен выдавать три диапазона с общим числом уникальныз хначений не менее 24 * 24 = 576
    """
    sectors = set()
    codes = set()

    from collections import defaultdict
    di = defaultdict(int)
    for minute in range(1, 1441):
        sector, code = encode_letters(minute)
        sectors.add(sector)
        codes.add(code)
        di[code] += 1

    assert len(sectors) == 3
    assert {1, 2, 3} == sectors
    assert len(codes) == 1440 // 3


def test_encode_period_unique():
    """
    Должен выдавать уникальный код времени для месяца
    """
    codes = set()
    combinations = set()

    for day in range(1, 32):
        for minute in range(1, 1441):
            code = encode_period(day, minute)
            codes.add(code)
            combinations.add((day, minute))

    assert len(codes) == 31 * 1440
    assert len(combinations) == 31 * 1440


def test_decode_digits():
    """
    Должен получить обратно номер дня + сектор
    """
    assert decode_digits('01') == (1, 1)
    assert decode_digits('64') == (31, 2)
    assert decode_digits('87') == (21, 3)
    assert decode_digits('97') == (31, 3)
    assert decode_digits('40') == (7, 2)
    assert decode_digits('14') == (14, 1)


def test_decode_letters():
    """
    Должен получить обратно номер дня + сектор
    """
    assert decode_letters(1, 'AA') == 1
    assert decode_letters(3, 'ZZ') == 1440


def test_full():
    """
    Сквозная проверка работоспособности
    """
    for day in range(1, 32):
        for minute in range(1, 1441):
            code = encode_period(day, minute)
            out_day, out_minute = decode_period(code)
            assert day == out_day
            assert minute == out_minute
