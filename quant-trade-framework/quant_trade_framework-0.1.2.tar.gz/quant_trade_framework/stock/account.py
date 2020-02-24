# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 20:11
# @File    : account.py
# @User    : yangchuan
# @Desc    :
from quant_trade_framework.stock.position import Position
from quant_trade_framework.common.constant import Constant,TradeConfig
from quant_trade_framework.stock.order import Order
from datetime import datetime

from quant_trade_framework.common.logConfig import Logger
logger = Logger.module_logger("system")


class Account:
    """
    user account information:
    name: str, account name
    balance: float, account current balance
    account_type: str, account type
    position: position dict,user account positions
    context: strategy runtime context
    orders: orders during strategy running
    """
    def __init__(self, name: str, balance: float, account_type: str):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.position = {}
        self.context = None
        self.orders = []
        logger.info("account created")

    def set_context(self,context):
        """
        set the context environment before start strategy
        :param context: Context object
        :return: none
        """
        self.context = context


    def buy(self, symbol: str, price: float, qty: int):
        """
        buy method
        :param symbol:str
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
                self.position[symbol].available = self.position[symbol].available + qty
            else:
                self.position[symbol] = Position(symbol, qty, price)

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

        if self.position[symbol].available < qty:
            logger.error("指定资产不足，卖出失败")
        else:
            self.position[symbol].available = self.position[symbol].available - qty
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
        if asset and len(asset) > 0 and asset in self.position:
            result['asset'] = self.position[asset].asset
            result['available'] = self.position[asset].available
            result['avg_cost'] = self.position[asset].avg_cost
        else:
            result['asset'] = asset
            result['available'] = 0
            result['avg_cost'] = 0
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
        order the amount of security
        :param security:str,security name
        :param amount:float, order amount
        :param style:
        :return: none
        """
        if amount == 0:
            logger.error("交易数量不能为0")
            return
        price = self.context.get_price(symbol=security,inteval=self.context.run_freq).close_price
        new_order = None
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
                    self.position[security].available = self.position[security].available + amount
                else:
                    self.position[security] = Position(security, amount, price)

                new_order = Order(
                    order_date=self.context.current_datetime(),
                    order_time=self.context.current_datetime(),
                    deal_date=self.context.next_price_datetime(),
                    deal_time=self.context.next_price_datetime(),
                    security=security,
                    order_type=TradeConfig.TYPE_BUY,
                    order_price_type=TradeConfig.PRICE_MARKET,
                    order_counts=amount,
                    order_price=price,
                    deal_price=price,
                    deal_total_value=price * amount,
                    deal_status=TradeConfig.DEAL_STATUS_FULL,
                    deal_count=amount,
                    commission=order_cost_fee,
                    last_update_datetime=datetime.now()
                )
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
                    self.position[security].available = self.position[security].available - amount

            new_order = Order(
                order_date=self.context.current_datetime(),
                order_time=self.context.current_datetime(),
                deal_date=self.context.next_price_datetime(),
                deal_time=self.context.next_price_datetime(),
                security=security,
                order_type=TradeConfig.TYPE_SELL,
                order_price_type=TradeConfig.PRICE_MARKET,
                order_counts=amount,
                order_price=price,
                deal_price=price,
                deal_total_value=price * amount - order_cost_fee,
                deal_status=TradeConfig.DEAL_STATUS_FULL,
                deal_count=amount,
                commission=order_cost_fee,
                last_update_datetime=datetime.now()
            )
            logger.info("account sell symbol:" + str(security) + " counts:" + str(amount))

        if new_order:
            self.orders.append(new_order)

    def order_target(self,security:str, amount:float, style=None):
        """
        oder to the target position amount for the specific security
        :param security:str,security name
        :param amount: float, target position amount
        :param style:
        :return:none
        """

        price = self.context.get_price(symbol=security,inteval=self.context.run_freq).close_price
        current_security_position = 0
        new_order = None
        if security in self.position:
            current_security_position = self.position[security].available

        op_type = ""
        op_amount = 0

        if amount >0:
            if amount > current_security_position:
                #buy
                op_type = "buy"
                op_amount = amount - current_security_position
            else:
                #sell
                op_type = "sell"
                op_amount = current_security_position - amount
        elif amount < 0:
            if amount > current_security_position:
                # sell
                op_type = "sell"
                op_amount = amount - current_security_position
            else:
                # buy
                op_type = "buy"
                op_amount = current_security_position - amount
        else:
            #平仓
            if current_security_position < 0:
                #buy
                op_type = "buy"
                op_amount = current_security_position * -1
            else:
                op_type = "sell"
                op_amount = current_security_position

        if op_type == "buy" and op_amount > 0:
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price + self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 + self.context.slippage["all"].value)
                    logger.info("price slippage process")

            buy_amount = op_amount
            # caculate order cost
            order_cost_fee = self.order_cost(Constant.ORDER_OPEN, security, price, buy_amount)
            cost = price * buy_amount + order_cost_fee

            if cost > self.balance:
                logger.error("指定资产不足，买入失败")
                return

            self.balance = self.balance - cost
            if security in self.position:
                self.position[security].available = amount
            else:
                self.position[security] = Position(security, amount, price)

            new_order = Order(
                order_date=self.context.current_datetime(),
                order_time=self.context.current_datetime(),
                deal_date=self.context.next_price_datetime(),
                deal_time=self.context.next_price_datetime(),
                security=security,
                order_type=TradeConfig.TYPE_BUY,
                order_price_type=TradeConfig.PRICE_MARKET,
                order_counts=buy_amount,
                order_price=price,
                deal_price=price,
                deal_total_value=price * buy_amount,
                deal_status=TradeConfig.DEAL_STATUS_FULL,
                deal_count=buy_amount,
                commission=order_cost_fee,
                last_update_datetime=datetime.now()
            )
            logger.info("account buy symbol:" + str(security) + " counts:" + str(amount))
        elif op_type == "sell" and op_amount > 0:
            # slippage price process
            if "all" in self.context.slippage:
                if self.context.slippage["all"].type == Constant.FIXED_SLIPPAGE:
                    price = price + self.context.slippage["all"].value
                elif self.context.slippage["all"].type == Constant.PRICE_RELATED_SLIPPAGE:
                    price = price * (1 + self.context.slippage["all"].value)
                    logger.info("price slippage process")

            sell_amount = op_amount
            # caculate order cost
            order_cost_fee = self.order_cost(Constant.ORDER_CLOSE, security, price, op_amount)

            cost = price * sell_amount - order_cost_fee
            self.balance = self.balance + cost
            if security in self.position:
                self.position[security].available = amount
            else:
                self.position[security] = Position(security, amount, price)

            new_order = Order(
                order_date=self.context.current_datetime(),
                order_time=self.context.current_datetime(),
                deal_date=self.context.next_price_datetime(),
                deal_time=self.context.next_price_datetime(),
                security=security,
                order_type=TradeConfig.TYPE_BUY,
                order_price_type=TradeConfig.PRICE_MARKET,
                order_counts=sell_amount,
                order_price=price,
                deal_price=price,
                deal_total_value=price * sell_amount - order_cost_fee,
                deal_status=TradeConfig.DEAL_STATUS_FULL,
                deal_count=sell_amount,
                commission=order_cost_fee,
                last_update_datetime=datetime.now()
            )
            logger.info("account sell symbol:" + str(security) + " counts:" + str(amount))

        if new_order:
            self.orders.append(new_order)

    def order_value(self,security:str, value:float, style=None):
        """
        oder security the amount of value
        :param security:str,security name
        :param value: float, order value
        :param style:
        :return: none
        """
        if value == 0:
            logger.error("交易价值不能为0")
            return
        price = self.context.get_price(symbol=security,inteval=self.context.run_freq).close_price

        new_order = None
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
                    self.position[security].available = self.position[security].available + amount
                else:
                    self.position[security] = Position(security, amount, price)

                new_order = Order(
                    order_date=self.context.current_datetime(),
                    order_time=self.context.current_datetime(),
                    deal_date=self.context.next_price_datetime(),
                    deal_time=self.context.next_price_datetime(),
                    security=security,
                    order_type=TradeConfig.TYPE_BUY,
                    order_price_type=TradeConfig.PRICE_MARKET,
                    order_counts=amount,
                    order_price=price,
                    deal_price=price,
                    deal_total_value=value - order_cost_fee,
                    deal_status=TradeConfig.DEAL_STATUS_FULL,
                    deal_count=amount,
                    commission=order_cost_fee,
                    last_update_datetime=datetime.now()
                )
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
                if amount > self.position[security].available:
                    logger.error("指定资产不足，买入失败")
                else:
                    # caculate order cost
                    order_cost_fee = self.order_cost(Constant.ORDER_CLOSE, security, price, amount)
                    value = value - order_cost_fee
                    self.balance = self.balance + value
                    self.position[security].available = self.position[security].available - amount

                new_order = Order(
                    order_date=self.context.current_datetime(),
                    order_time=self.context.current_datetime(),
                    deal_date=self.context.next_price_datetime(),
                    deal_time=self.context.next_price_datetime(),
                    security=security,
                    order_type=TradeConfig.TYPE_BUY,
                    order_price_type=TradeConfig.PRICE_MARKET,
                    order_counts=amount,
                    order_price=price,
                    deal_price=price,
                    deal_total_value=value - order_cost_fee,
                    deal_status=TradeConfig.DEAL_STATUS_FULL,
                    deal_count=amount,
                    commission=order_cost_fee,
                    last_update_datetime=datetime.now()
                )
                logger.info("account sell symbol:" + str(security) + " counts:" + str(amount))

        if new_order:
            self.orders.append(new_order)

    def order_cost(self,type:str,symbol:str,price:float,qty:int):
        """
        cost of per order
        :param type:str,order type
        :param symbol:str, symbol name
        :param price: unit price for security
        :param qty: order qty
        :return: float
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
