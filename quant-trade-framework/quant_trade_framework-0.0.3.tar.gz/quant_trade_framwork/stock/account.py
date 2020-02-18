# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 20:11
# @File    : account.py
# @User    : yangchuan
# @Desc    :
from quant_trade_framwork.stock.position import position
from quant_trade_framwork.common.constant import Constant

from quant_trade_framwork.common.logConfig import Logger
logger = Logger.module_logger("system")


class account:
    def __init__(self, name: str, balance: float, account_type: str):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.position = {}
        self.context = None
        logger.info("account created")

    def set_context(self,context):
        self.context = context


    def buy(self, symbol: str, price: float, qty: int):
        """
        buy method
        :param symbol:str,交易对 BTC/USDT.binance，BTC为base_currency，USDT为quote_currency
        :param price: float
        :param qty: float
        :return: none
        """
        cost = price * qty
        if cost > self.balance:
            logger.error("指定资产不足，买入失败")
        else:
            self.balance = self.balance - cost
            if symbol in self.position:
                self.position[symbol].count = self.position[symbol].count + qty
            else:
                self.position[symbol] = position(symbol, qty, price)

            logger.info("account buy symbol:" + str(symbol) + " counts:" + str(qty))


    def sell(self, symbol: str, price: float, qty):
        """
        sell trade
        :param symbol: str,交易对 BTC/USDT.binance，BTC为base_currency，USDT为quote_currency
        :param price: float
        :param qty: float
        :return:
        """
        if symbol not in self.position:
            logger.error("不存在指定资产")
            return

        if self.position[symbol].count < qty:
            logger.error("指定资产不足，卖出失败")
        else:
            self.position[symbol].count = self.position[symbol].count - qty
            cost = price * qty
            self.balance = self.balance + cost
            logger.info("account sell symbol:" + str(symbol) + " counts:" + str(qty))

    def get_position(self, asset: str):
        """
        获取指定币仓位
        :param asset: 资产名
        :return: position object
        """
        result = {}
        if asset and len(asset) > 0:
            result['asset'] = self.position[asset].asset
            result['available'] = self.position[asset].available
            result['avg_cost'] = self.position[asset].avg_cost
        return result

    def get_posistions(self):
        """
        获取所有币仓位
        :return: position object
        """
        result = {}
        for item in self.position:
            temp = {}
            temp['asset'] = self.position[item.asset].asset
            temp['available'] = self.position[item.asset].available
            temp['avg_cost'] = self.position[item.asset].avg_cost
            result[item.asset] = temp
        return result

    def order(self,security:str, amount:float, style=None):
        """
        按照指定数量进行交易
        :param security:
        :param amount:
        :param style:
        :return:
        """
        if amount == 0:
            logger.error("交易数量不能为0")
            return
        price = self.context.get_price(security)
        if amount > 0:
            #buy
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price + self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 + self.context.slippage["all"].value)
                    logger.info("price slippage process")

            #caculate order cost
            order_cost_fee = self.order_cost(Constant.ORDER_OPEN,security,price,amount)

            cost = price * amount + order_cost_fee
            if cost > self.balance:
                logger.error("指定资产不足，买入失败")
            else:
                self.balance = self.balance - cost
                if security in self.position:
                    self.position[security].count = self.position[security].count + amount
                else:
                    self.position[security] = position(security, amount, price)

                logger.info("account buy symbol:" + str(security) + " counts:" + str(amount))
        else:
            #sell
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price - self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 - self.context.slippage["all"].value)
                    logger.info("price slippage process")

            if security not in self.position:
                logger.error("无指定资产，无法卖出")
            else:
                if amount > self.position[security].count:
                    logger.error("指定资产不足，买入失败")
                else:
                    # caculate order cost
                    order_cost_fee = self.order_cost(Constant.ORDER_CLOSE, security, price, amount)

                    cost = price * amount - order_cost_fee
                    self.balance = self.balance + cost
                    self.position[security].count = self.position[security].count - amount
            logger.info("account sell symbol:" + str(security) + " counts:" + str(amount))

    def order_target(self,security:str, amount:float, style=None):
        if amount < 0:
            logger.error("暂不支持空入")

        price = self.context.get_price(security)
        current_security_position = 0

        if security in self.position:
            current_security_position = self.position[security].count

        if amount > current_security_position:
            #buy

            #slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price + self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 + self.context.slippage["all"].value)
                    logger.info("price slippage process")

            buy_amount = amount - current_security_position
            # caculate order cost
            order_cost_fee = self.order_cost(Constant.ORDER_OPEN, security, price, amount)
            cost = price * buy_amount + order_cost_fee

            if cost > self.balance:
                logger.error("指定资产不足，买入失败")
                return
            self.balance = self.balance - cost
            if security in self.position:
                self.position[security].count = amount
            else:
                self.position[security] = position(security, amount, price)
            logger.info("account buy symbol:" + str(security) + " counts:" + str(amount))
        else:
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price - self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 - self.context.slippage["all"].value)
                    logger.info("price slippage process")

            if amount == 0 and current_security_position <= 0:
                logger.error("amount == 0 and current_security_position <= 0")
                return
            #sell
            sell_amount = current_security_position - amount
            # caculate order cost
            order_cost_fee = self.order_cost(Constant.ORDER_CLOSE, security, price, amount)

            cost = price * sell_amount - order_cost_fee
            self.balance = self.balance + cost
            if security in self.position:
                self.position[security].count = amount
            else:
                self.position[security] = position(security, amount, price)
            logger.info("account sell symbol:" + str(security) + " counts:" + str(amount))

    def order_value(self,security:str, value:float, style=None):
        if value == 0:
            logger.error("交易价值不能为0")
            return
        price = self.context.get_price(security)

        if value > 0:
            # buy
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price + self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 + self.context.slippage["all"].value)
                    logger.info("price slippage process")

            amount = value / price
            # caculate order cost
            order_cost_fee = self.order_cost(Constant.ORDER_OPEN, security, price, amount)
            if value > self.balance:
                logger.error("指定资产不足，买入失败")
            else:
                self.balance = self.balance - value
                amount = (value-order_cost_fee) / price
                if security in self.position:
                    self.position[security].count = self.position[security].count + amount
                else:
                    self.position[security] = position(security, amount, price)

                logger.info("account buy symbol:" + str(security) + " counts:" + str(amount))
        else:
            # sell
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price - self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 - self.context.slippage["all"].value)
                    logger.info("price slippage process")
            amount = value / price

            if security not in self.position:
                logger.error("无指定资产，无法卖出")
            else:
                if amount > self.position[security].count:
                    logger.error("指定资产不足，买入失败")
                else:
                    # caculate order cost
                    order_cost_fee = self.order_cost(Constant.ORDER_CLOSE, security, price, amount)
                    value = value - order_cost_fee
                    self.balance = self.balance + value
                    self.position[security].count = self.position[security].count - amount
            logger.info("account sell symbol:" + str(security) + " counts:" + str(amount))


    def order_cost(self,type:str,symbol:str,price:float,qty:int):
        """

        :param type:
        :param symbol:
        :param price:
        :param qty:
        :return:
        """
        cost_fee = 0
        if "all" in self.context.order_cost:
            if type == Constant.ORDER_OPEN:
                cost_fee = self.context.order_cost["all"].open_tax * price * qty
            elif type == Constant.ORDER_CLOSE:
                cost_fee = self.context.order_cost["all"].close_tax * price * qty
        if cost_fee > 0:
            logger.info(type + " order cost fee:" + str(cost_fee))
        return cost_fee
