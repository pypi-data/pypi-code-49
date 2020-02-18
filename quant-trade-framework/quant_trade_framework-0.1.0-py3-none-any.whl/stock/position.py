# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 21:04
# @File    : postion.py
# @User    : yangchuan
# @Desc    :
from quant_trade_framwork.common.logConfig import Logger
from dataclasses import dataclass
logger = Logger.module_logger("system")

@dataclass
class position:
    def __init__(self,asset:str,count:int,avg_cost:float):
        self.asset = asset
        self.count = count
        self.avg_cost = avg_cost