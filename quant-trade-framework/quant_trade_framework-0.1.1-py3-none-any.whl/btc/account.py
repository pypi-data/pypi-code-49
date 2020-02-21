# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 20:11
# @File    : account.py
# @User    : yangchuan
# @Desc    :
from .position import position

from quant_trade_framwork.common.logConfig import Logger
logger = Logger.module_logger("system")


class account:
    def __init__(self, name: str, exchange: str, account_type: str, position_base: list()):
        self.name = name
        self.exchange = exchange
        self.account_type = account_type
        self.position = {}
        self.security_type = 'btc'
        for item in position_base:
            self.position[item["asset"]] = position(item["asset"],item["qty"],0,1)
        logger.info("account created")

    def set_security_type(self,security):
        self.security_type = security

    def buy(self, symbol: str, price: float, qty):
        """
        buy trade
        :param symbol:str,交易对 BTC/USDT.binance，BTC为base_currency，USDT为quote_currency
        :param price: float
        :param qty: float
        :return: none
        """
        symbol_temp = symbol.split('.')[0]
        base_currency = symbol_temp('/')[0]
        quote_currency = symbol_temp('/')[1]
        if quote_currency not in self.position:
            logger.error("没有指定资产，买入失败")
        else:
            cost = price * qty
            if cost > self.position[quote_currency].available:
                logger.error("指定资产不足，买入失败")
            else:
                self.position[quote_currency].available = self.position[quote_currency].available - cost
                if base_currency in self.position:
                    self.position[base_currency].available = self.position[base_currency].available + qty
                else:
                    self.position[base_currency] = position(base_currency, qty, 0, price)



    def sell(self, symbol: str, price: float, qty):
        """
        sell trade
        :param symbol: str,交易对 BTC/USDT.binance，BTC为base_currency，USDT为quote_currency
        :param price: float
        :param qty: float
        :return:
        """
        symbol_temp = symbol.split('.')[0]
        base_currency = symbol_temp('/')[0]
        quote_currency = symbol_temp('/')[1]
        if base_currency not in self.position:
            logger.error("没有指定资产，卖出失败")
        else:
            if self.position[base_currency].available < qty:
                logger.error("指定资产不足，卖出失败")
            else:
                self.position[base_currency].available = self.position[base_currency].available - qty
                cost = price * qty

                if quote_currency in self.position:
                    self.position[quote_currency].available = self.position[quote_currency].available + cost
                else:
                    self.position[quote_currency] = position(quote_currency, cost, 0, price)



    def buy_pct(self, symbol: str, price: float, qty):
        pass

    def sell_pct(self, symbol: str, price: float, qty):
        pass

    def get_position(self, asset: str):
        """
        获取指定币仓位
        :param asset: 资产名
        :return:
        """
        result = {}
        if asset and len(asset) > 0:
            result['asset'] = self.position[asset].asset
            result['available'] = self.position[asset].available
            result['frozen'] = self.position[asset].frozen
            result['avg_cost'] = self.position[asset].avg_cost
        return result

    def get_posistions(self):
        """
        获取所有币仓位
        :return:
        """
        result = {}
        for item in self.position:
            temp = {}
            temp['asset'] = self.position[item.asset].asset
            temp['available'] = self.position[item.asset].available
            temp['frozen'] = self.position[item.asset].frozen
            temp['avg_cost'] = self.position[item.asset].avg_cost
            result[item.asset] = temp
        return result
