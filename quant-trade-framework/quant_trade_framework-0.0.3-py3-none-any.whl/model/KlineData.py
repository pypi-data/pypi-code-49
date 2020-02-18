# -*-coding:utf-8 -*-

# @Time    : 2020/2/10 11:50
# @File    : KlineData.py
# @User    : yangchuan
# @Desc    : 
from dataclasses import dataclass
from datetime import datetime

@dataclass
class KlineData():
    """
    Candlestick bar data of a certain trading period.
    """

    symbol: str
    exchange: str
    datetime: datetime

    interval: str
    volume: float = 0
    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    close_price: float = 0
    refresh_time: datetime = datetime.now()

    def __post_init__(self):
        """"""
        # self.vt_symbol = f"{self.symbol}.{self.exchange.value}"
        self.vt_symbol = self.symbol