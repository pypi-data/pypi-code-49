# -*- coding: utf-8 -*-
"""

    Инструменты обработки текстового представления дат

"""
# встроенные модули
import time
from datetime import date, datetime
from typing import Sequence, List, Union

__all__ = [
    'parse_date',
    'parse_dates',
    'parse_time',
    'parse_time_s',
    'parse_time_ms',
    'cur_time',
    'cur_time_s',
    'cur_time_ms',
    'timestamp_to_str',
    'date_to_text',
    'datetime_to_text',
    'datetime_to_text_s',
    'datetime_to_text_ms'
]


def parse_date(string: str, format_string: str = '%Y-%m-%d') -> date:
    """
    Обработка даты (при возможности)

    >>> parse_date('2019-12-01')
    datetime.date(2019, 12, 1)
    """
    return datetime.strptime(string, format_string).date()


def parse_dates(container: Sequence, format_string: str = '%Y-%m-%d') -> List[date]:
    """
    Распарсить множество дат

    >>> parse_dates(['2019-12-01', '2019-12-02'])
    [datetime.date(2019, 12, 1), datetime.date(2019, 12, 2)]
    """
    result = [parse_date(each, format_string) for each in container]
    result.sort()
    return result


def parse_time(text: str, format_string: str) -> datetime:
    """
    Преобразовать текст в объект времени
    """
    return datetime.strptime(text, format_string)


def parse_time_s(text: str, format_string: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Преобразовать текст в объект времени с точностью до секунд

    >>> parse_time_s('2019-12-01 14:32:27')
    datetime.datetime(2019, 12, 1, 14, 32, 27)
    """
    return datetime.strptime(text, format_string)


def parse_time_ms(text: str, format_string: str = "%Y-%m-%d %H:%M:%S.%f") -> datetime:
    """
    Преобразовать текст в объект времени с точностью до микросекунд

    >>> parse_time_ms('2019-12-01 14:32:27.235486')
    datetime.datetime(2019, 12, 1, 14, 32, 27, 235486)
    """
    return parse_time(text, format_string)


def cur_time(format_string: str) -> str:
    """
    Получить строку с текущим временем
    """
    return datetime.now().strftime(format_string)


def cur_time_s(format_string: str = '%H:%M:%S') -> str:
    """
    Получить строку с текущим временем с точностью до секунд
    """
    return cur_time(format_string)


def cur_time_ms(format_string: str = '%H:%M:%S.%f') -> str:
    """
    Получить строку с текущим временем с точностью до микросекунд
    """
    return cur_time(format_string)


def timestamp_to_str(timestamp: float, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Преобразовать timestamp в текстовую форму
    """
    return time.strftime(format_string, datetime.fromtimestamp(timestamp).timetuple())


def date_to_text(moment: date, format_string: str = "%Y-%m-%d") -> str:
    """
    Преобразовать время в виде date в текстовую форму
    """
    return datetime_to_text(moment, format_string)


def datetime_to_text(moment: Union[date, datetime], format_string: str) -> str:
    """
    Преобразовать время в виде datetime в текстовую форму
    """
    return moment.strftime(format_string)


def datetime_to_text_s(moment: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Преобразовать время в виде datetime в текстовую форму
    """
    return datetime_to_text(moment, format_string)


def datetime_to_text_ms(moment: datetime, format_string: str = "%Y-%m-%d %H:%M:%S.%f") -> str:
    """
    Преобразовать время в виде datetime в текстовую форму
    """
    return datetime_to_text(moment, format_string)
