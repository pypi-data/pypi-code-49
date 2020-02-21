# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 21:04
# @File    : postion.py
# @User    : yangchuan
# @Desc    :
from quant_trade_framwork.common.logConfig import Logger
logger = Logger.module_logger("system")

class position:
    def __init__(self,asset:str,available:float,frozen:float,avg_cost:float):
        self.asset = asset
        self.available = available
        self.frozen = frozen
        self.avg_cost = avg_cost
        self.value_in_usdt = 0