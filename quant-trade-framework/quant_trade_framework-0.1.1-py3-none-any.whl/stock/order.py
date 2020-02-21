#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 15:53
# @Author  : chuan.yang
# @File    : order.py
# @Desc    : order detail
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    """
    order_date: datetime 委托日期
    order_time: datetime 委托时间
    deal_date: datetime 成交日期
    deal_time: datetime 成交时间
    security: str   标的
    order_type: str 交易类型：买 卖
    order_price_type: str 下单类型：市价但 限价单
    order_counts: int 下单数量
    order_price: float 委托价格
    deal_price: float 成交价格
    deal_total_value: float 成交额
    deal_status: int 成交状态
    deal_count: int 成交数量
    commission: float 手续费
    last_update_datetime: datetime 上一次更新时间
    """
    order_date: datetime
    order_time: datetime
    deal_date: datetime
    deal_time: datetime
    security: str
    order_type: str
    order_price_type: str
    order_counts: float
    order_price: float
    deal_price: float
    deal_total_value: float
    deal_status: int
    deal_count: float
    commission: float
    last_update_datetime: datetime

    def to_dict(self):
        return vars(self)


