# -*- coding: utf-8 -*-
"""

    Тесты вычислений

"""
# модули проекта
from trivial_tools.calculations.base_math import byte_count_to_si, byte_count_to_text


def test_byte_count_to_si_ru():
    """
    Проверить преобразование по основанию 1000, русский
    """
    assert byte_count_to_si(-2_000, lang='RU') == '-2.0 кБ'
    assert byte_count_to_si(-2_048, lang='RU') == '-2.0 кБ'
    assert byte_count_to_si(0, lang='RU') == '0 Б'
    assert byte_count_to_si(27, lang='RU') == '27 Б'
    assert byte_count_to_si(999, lang='RU') == '999 Б'
    assert byte_count_to_si(1_000, lang='RU') == '1.0 кБ'
    assert byte_count_to_si(1_023, lang='RU') == '1.0 кБ'
    assert byte_count_to_si(1_024, lang='RU') == '1.0 кБ'
    assert byte_count_to_si(1_728, lang='RU') == '1.7 кБ'
    assert byte_count_to_si(110_592, lang='RU') == '110.6 кБ'
    assert byte_count_to_si(7_077_888, lang='RU') == '7.1 МБ'
    assert byte_count_to_si(1_000_000, lang='RU') == '1.0 МБ'
    assert byte_count_to_si(452_984_832, lang='RU') == '453.0 МБ'
    assert byte_count_to_si(1_000_000_000, lang='RU') == '1.0 ГБ'
    assert byte_count_to_si(28_991_029_248, lang='RU') == '29.0 ГБ'
    assert byte_count_to_si(1_855_425_871_872, lang='RU') == '1.9 ТБ'
    assert byte_count_to_si(9_223_372_036_854_775_807, lang='RU') == '9.2 ЭБ'


def test_byte_count_to_si_en():
    """
    Проверить преобразование по основанию 1000, английский
    """
    assert byte_count_to_si(-2_000, lang='EN') == '-2.0 kB'
    assert byte_count_to_si(-2_048, lang='EN') == '-2.0 kB'
    assert byte_count_to_si(0, lang='EN') == '0 B'
    assert byte_count_to_si(27, lang='EN') == '27 B'
    assert byte_count_to_si(999, lang='EN') == '999 B'
    assert byte_count_to_si(1_000, lang='EN') == '1.0 kB'
    assert byte_count_to_si(1_023, lang='EN') == '1.0 kB'
    assert byte_count_to_si(1_024, lang='EN') == '1.0 kB'
    assert byte_count_to_si(1_728, lang='EN') == '1.7 kB'
    assert byte_count_to_si(110_592, lang='EN') == '110.6 kB'
    assert byte_count_to_si(7_077_888, lang='EN') == '7.1 MB'
    assert byte_count_to_si(1_000_000, lang='EN') == '1.0 MB'
    assert byte_count_to_si(452_984_832, lang='EN') == '453.0 MB'
    assert byte_count_to_si(1_000_000_000, lang='EN') == '1.0 GB'
    assert byte_count_to_si(28_991_029_248, lang='EN') == '29.0 GB'
    assert byte_count_to_si(1_855_425_871_872, lang='EN') == '1.9 TB'
    assert byte_count_to_si(9_223_372_036_854_775_807, lang='EN') == '9.2 EB'


def test_byte_count_to_text_ru():
    """
    Проверить преобразование по основанию 1024
    """
    assert byte_count_to_text(-2_000, lang='RU') == '-2.0 КиБ'
    assert byte_count_to_text(-2_048, lang='RU') == '-2.0 КиБ'
    assert byte_count_to_text(0, lang='RU') == '0 Б'
    assert byte_count_to_text(27, lang='RU') == '27 Б'
    assert byte_count_to_text(999, lang='RU') == '999 Б'
    assert byte_count_to_text(1_000, lang='RU') == '1000 Б'
    assert byte_count_to_text(1_023, lang='RU') == '1023 Б'
    assert byte_count_to_text(1_024, lang='RU') == '1.0 КиБ'
    assert byte_count_to_text(1_728, lang='RU') == '1.7 КиБ'
    assert byte_count_to_text(110_592, lang='RU') == '108.0 КиБ'
    assert byte_count_to_text(1_000_000, lang='RU') == '976.6 КиБ'
    assert byte_count_to_text(7_077_888, lang='RU') == '6.8 МиБ'
    assert byte_count_to_text(452_984_832, lang='RU') == '432.0 МиБ'
    assert byte_count_to_text(1_000_000_000, lang='RU') == '953.7 МиБ'
    assert byte_count_to_text(28_991_029_248, lang='RU') == '27.0 ГиБ'
    assert byte_count_to_text(1_855_425_871_872, lang='RU') == '1.7 ТиБ'
    assert byte_count_to_text(9_223_372_036_854_775_807, lang='RU') == '8.0 ЭиБ'


def test_byte_count_to_text_en():
    """
    Проверить преобразование по основанию 1024
    """
    assert byte_count_to_text(-2_000, lang='EN') == '-2.0 KiB'
    assert byte_count_to_text(-2_048, lang='EN') == '-2.0 KiB'
    assert byte_count_to_text(0, lang='EN') == '0 B'
    assert byte_count_to_text(27, lang='EN') == '27 B'
    assert byte_count_to_text(999, lang='EN') == '999 B'
    assert byte_count_to_text(1_000, lang='EN') == '1000 B'
    assert byte_count_to_text(1_023, lang='EN') == '1023 B'
    assert byte_count_to_text(1_024, lang='EN') == '1.0 KiB'
    assert byte_count_to_text(1_728, lang='EN') == '1.7 KiB'
    assert byte_count_to_text(110_592, lang='EN') == '108.0 KiB'
    assert byte_count_to_text(1_000_000, lang='EN') == '976.6 KiB'
    assert byte_count_to_text(7_077_888, lang='EN') == '6.8 MiB'
    assert byte_count_to_text(452_984_832, lang='EN') == '432.0 MiB'
    assert byte_count_to_text(1_000_000_000, lang='EN') == '953.7 MiB'
    assert byte_count_to_text(28_991_029_248, lang='EN') == '27.0 GiB'
    assert byte_count_to_text(1_855_425_871_872, lang='EN') == '1.7 TiB'
    assert byte_count_to_text(9_223_372_036_854_775_807, lang='EN') == '8.0 EiB'
