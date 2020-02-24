# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 21:04
# @File    : postion.py
# @User    : yangchuan
# @Desc    :
from quant_trade_framework.common.logConfig import Logger
from dataclasses import dataclass
logger = Logger.module_logger("system")


@dataclass
class Position:
    """
    position information:
    asset:str,security name
    available:float,security available count
    avg_cost:float,average cost for per available count,not used
    """
    def __init__(self,asset:str,available:int,avg_cost:float):
        self.asset = asset
        self.available = available
        self.avg_cost = avg_cost