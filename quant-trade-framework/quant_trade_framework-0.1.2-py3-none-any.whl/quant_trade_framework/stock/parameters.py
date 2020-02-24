# -*-coding:utf-8 -*-

# @Time    : 2020/2/16 21:10
# @File    : parameters.py
# @User    : yangchuan
# @Desc    : 
from dataclasses import dataclass
from quant_trade_framework.common.constant import Constant

@dataclass
class OrderCost:
    """
    cost for per order
    open_tax：买入时印花税 (只股票类标的收取，基金与期货不收)
    close_tax：卖出时印花税 (只股票类标的收取，基金与期货不收)
    open_commission：买入时佣金，申购场外基金的手续费
    close_commission： 卖出时佣金，赎回场外基金的手续费
    close_today_commission： 平今仓佣金
    min_commission： 最低佣金，不包含印花税
    """
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
    """
    slippage parameters
    type:滑点类型
    固定值： 这个价差可以是一个固定的值(比如0.02元, 交易时加减0.01元), 设定方式为：FixedSlippage(0.02)
    百分比： 这个价差可以是是当时价格的一个百分比(比如0.2%, 交易时加减当时价格的0.1%), 设定方式为：PriceRelatedSlippage(0.002)
    跳数（期货专用，双边）: 这个价差可以是合约的价格变动单位（跳数），比如2跳，设定方式为： StepRelatedSlippage(2)；滑点为小数时，向下取整，例如设置为3跳，单边1.5，向下取整为1跳。
    value：float
    """
    type:str = Constant.FIXED_SLIPPAGE
    value:float = 0

    def __init__(self,type:str,value:float):
        self.type = type
        self.value = value


