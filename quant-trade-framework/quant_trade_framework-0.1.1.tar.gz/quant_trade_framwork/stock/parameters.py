# -*-coding:utf-8 -*-

# @Time    : 2020/2/16 21:10
# @File    : parameters.py
# @User    : yangchuan
# @Desc    : 
from dataclasses import dataclass
from quant_trade_framwork.common.constant import Constant

@dataclass
class OrderCost:
    open_tax:float = 0
    close_tax:float = 0
    open_commission:float = 0
    close_commission:float = 0
    close_today_commission:float = 0
    min_commission:float = 0

    def __init__(self,open_tax,close_tax,open_commission,
                 close_commission,close_today_commission,min_commission):
        self.open_tax = open_tax
        self.close_tax = close_tax
        self.open_commission = open_commission
        self.close_commission = close_commission
        self.close_today_commission = close_today_commission
        self.min_commission = min_commission

@dataclass
class SlipPage:
    type:str = Constant.FIXED_SLIPPAGE
    value:float = 0

    def __init__(self,type:str,value:float):
        self.type = type
        self.value = value


