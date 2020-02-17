# -*- coding: utf-8 -*-
"""

    Инструменты для работы с именами в АПК "ПАУК"

"""
# встроенные модули
import re
from contextlib import suppress as _suppress

# шаблон имени паука
from datetime import date
from typing import Optional

# шаблон для проверки spider_id
SPIDER_ID_PATTERN = re.compile(r'^\d{2}-\d{5}$')

# шаблон для извлечения даты из имени CSV файла
CSV_DATE_PATTERN = re.compile(r'\d{2}-\d{5}_(\d{4})-(\d{2})-(\d{2}).csv$')

# шаблон для извлечения spider_id из имени CSV файла
CSV_ID_PATTERN = re.compile(r'(\d{2}-\d{5})_\d{4}-\d{2}-\d{2}.csv$')


def spider_id_to_int(spider_id: str, pattern=re.compile(r'(\d{2})-(\d{5})')) -> int:
    """
    Конвертировать spider_id в числовое представление

    >>> spider_id_to_int('02-00241')
    200241

    >>> spider_id_to_int('99-99999')
    9999999
    """
    group, number = pattern.match(spider_id).groups()
    result = int(group) * 100_000 + int(number)
    return result


def spider_id_to_str(spider_iid: int) -> str:
    """
    Конвертировать spider_id из числового представления в строковое

    >>> spider_id_to_str(200241)
    '02-00241'

    >>> spider_id_to_str(9999999)
    '99-99999'
    """
    group, number = divmod(spider_iid, 100_000)
    result = f'{group:02d}-{number:05d}'
    return result


def spider_sorter(key: str) -> int:
    """
    Ключевая функция для сортировки пауков. Сортирует по номеру паука без учёта серии

    >>> spider_sorter('02-00241')
    241
    """
    result = -1
    if isinstance(key, str) and len(key) == 8:
        with _suppress(ValueError):
            result = int(key[3:])
    return result


def is_spider_id(string: str, pattern=SPIDER_ID_PATTERN) -> bool:
    """
    Проверить, является ли строка валидным id паука

    >>> is_spider_id('02-00125')
    True
    >>> is_spider_id('asd kjk')
    False
    """
    result = pattern.match(string) is not None
    return result


def date_from_spider_csv(filename: str, pattern=CSV_DATE_PATTERN) -> Optional[date]:
    """
    Извлечь дату из имени CSV файла паука

    >>> date_from_spider_csv('02-00183_2019-07-24.csv')
    datetime.date(2019, 7, 24)
    """
    data = pattern.search(filename)
    if data:
        year, month, day = data.groups()
        spider_date = date(int(year), int(month), int(day))
        return spider_date
    return None


def spider_id_from_spider_csv(filename: str, pattern=CSV_ID_PATTERN) -> Optional[str]:
    """
    Извлечь id паука из имени файла

    >>> spider_id_from_spider_csv('02-00183_2019-07-24.csv')
    '02-00183'

    >>> spider_id_from_spider_csv('02-00183_201s9-07-24.csv')

    """
    spider_id = pattern.search(filename)
    if spider_id:
        spider_id = spider_id.group(1)
        return spider_id
    return None


def has_csv_date(string: str, pattern=CSV_DATE_PATTERN) -> bool:
    """
    Проверить, похоже ли это на CSV файл паука с датой
    """
    result = pattern.match(string)
    return bool(result)
