# -*- coding: utf-8 -*-
"""

    Обработка данных для пауков

"""
# встроенные модули
import re
from typing import Tuple


CHANNEL_PATTERN = re.compile(r'(\d+)([ABC])(x(.*)?)?')


def analyze_channels(string: str) -> Tuple[int, str, float]:
    """
    Разложить строку каналов на составляющие
    """
    number, phase, _, mul = CHANNEL_PATTERN.search(string).groups()
    return int(number), phase.upper(), 1.0 if mul is None else float(mul)
