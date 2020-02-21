# -*- coding: utf-8 -*-
"""

    Работа с распечаткой из pandas

"""
# сторонние модули
import pandas as pd


def pandas_output(*args, min_rows: int = 100, max_rows: int = 100, max_columns: int = 100,
                  expand_frame_repr: bool = False):
    """
    Распечатать с настройками контекста
    """
    with pd.option_context(
            'display.min_rows', min_rows,
            'display.max_rows', max_rows,
            'display.max_columns', max_columns,
            'display.expand_frame_repr', expand_frame_repr
    ):
        print(*args)
