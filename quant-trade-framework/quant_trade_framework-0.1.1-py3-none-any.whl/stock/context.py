# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 14:20
# @File    : Context.py
# @User    : yangchuan
# @Desc    : get the quant trade data
from pymongo import MongoClient,DESCENDING
from quant_trade_framwork.common.constant import Constant
from quant_trade_framwork.stock import account
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from quant_trade_framwork.common.logConfig import Logger
from pytz import timezone
from quant_trade_framwork.stock.parameters import OrderCost,SlipPage
from quant_trade_framwork.common.redisConfig import RuntimeConfig

logger = Logger.module_logger("system")

cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')


class Context:
    """
    策略运行上下文环境
    next_price_day_diff：int，下次交易的时间间隔
    next_price_time：datetime,下次交易的时间点
    """
    accounts = {}
    run_freq = Constant.KLINE_INTERVAL_1MINUTE
    is_digtal_currency = True
    exchange = "quant"
    benchmark_symbol = '000300.XSHG'
    order_cost = {}
    slippage = {}
    user_name = ""
    user_pwd = ""
    next_price_day_diff = 1
    next_price_time = datetime(2019,1,1,9,15,00)
    runtime_config_obj = RuntimeConfig()

    @staticmethod
    def set_auth(user_name:str, user_pwd:str):
        Context.user_name = user_name
        Context.user_pwd = user_pwd

    @staticmethod
    def set_account(account: account):
        """
        set the account object to the context environments
        :param account:
        :return: None
        """
        Context.accounts[account.name] = account

    @staticmethod
    def set_order_cost(cost:OrderCost,type:str):
        """
        set the order cost parameters
        :param cost: Order Cost Object
        :param type: stock、fund or index,none for set all
        :return:
        """
        if type:
            Context.order_cost["all"] = cost
        else:
            Context.order_cost[type] = cost

    @staticmethod
    def set_benckmark(security):
        Context.benchmark_symbol = security

    @staticmethod
    def set_slippage(slippage:SlipPage,type:str):
        if type:
            Context.slippage["all"] = slippage
        else:
            Context.slippage[type] = slippage

    @staticmethod
    def set_current_datetime(dt):
        Context.current_dt = dt

    @staticmethod
    def set_run_freq(type):
        Context.run_freq = type

    @staticmethod
    def get_account(name:str):
        return Context.accounts[name]

    @staticmethod
    def get_price(symbol:str):
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        col = symbol + "-"  + Context.run_freq
        result = 0
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[Context.exchange]
            collection = db[col]
            cursor = collection.find({"date": {"$lte": Context.next_price_datetime(),"$gt":Context.current_datetime()}}).sort([('date', -1)]).limit(1)
            if cursor and cursor.count() > 0:
                result = cursor[0]['close']
        except BaseException as e:
            logger.error(str(e))
        return float(result)

    @staticmethod
    def get_benchmark_price():
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        col = Context.benchmark_symbol + "-" + Context.run_freq
        result = 0
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[Context.exchange]
            collection = db[col]
            cursor = collection.find({"date": {"$lte": Context.next_price_datetime(),
                                               "$gt":Context.current_datetime()}}).sort([('date', -1)]).limit(1)
            if cursor and cursor.count() > 0:
                result = cursor[0]['close']
        except BaseException as e:
            logger.error(str(e))
        return float(result)

    @staticmethod
    def history(symbol:str,attributes:object,bars:int,rtype:str):
        """
        get the symbol history price
        :param symbol: symbol name
        :param attributes: returned fields,including open,high,low,close,volume
        :param bars: latest price records
        :param rtype: returned data type:list,ndarray,dataframe
        :return:returned data with type:list,ndarray,dataframe
        """
        mc = MongoClient(
            host="182.151.7.177",
            port=27017,
            username="admin",
            password="admin"
        )
        columns = {}
        for column in attributes:
            columns[column] = 1

        db = mc[Constant.DB_NAME]
        collection = db[symbol]

        # cursor = collection.find(columns,sort=[('date', -1)]).limit(bars)
        cursor = collection.find(projection=attributes,sort=[('date', DESCENDING)]).limit(bars)
        result = list(cursor)
        if rtype == "ndarray":
            result = np.array(result)
        elif rtype == "dataframe":
            result = pd.DataFrame(result)
        return result

    @staticmethod
    def current_datetime():
        """
        get current trade datetime
        :return: datetime
        """
        return Context.current_dt

    @staticmethod
    def next_price_datetime():
        """
        get the next price datetime from the current datetime
        :return:
        """
        if Context.next_price_day_diff > 0 and Context.next_price_time and \
                type(Context.next_price_time) == datetime:
            next = Context.current_dt + timedelta(days=Context.next_price_day_diff)
            while True:
                next = datetime(next.year,next.month,next.day,
                                Context.next_price_time.hour,Context.next_price_time.minute,0)
                datetime_now_date_str = next.strftime('%Y-%m-%d')
                if Context.runtime_config_obj.check_day_is_valid_trade_day(datetime_now_date_str):
                    break
                next = next + + timedelta(days=Context.next_price_day_diff)
        else:
            next = Context.current_dt + timedelta(minutes=1)
        return next

    @staticmethod
    def previous_datetime():
        """
        get the last trade datetime
        :return: datetime
        """
        result = None
        if Context.current_dt and type(Context.current_dt) == datetime:
            now = Context.current_dt
            if Context.run_freq == Constant.KLINE_INTERVAL_1DAY:
                diff = timedelta(days=1)
                temp = now - diff
                result = datetime(temp.year, temp.month, temp.day, 0, 0, 0)
            elif Context.run_freq == Constant.KLINE_INTERVAL_1HOUR:
                diff = timedelta(hours=1)
                temp = now - diff
                result = datetime(temp.year, temp.month, temp.day, temp.hour, 0, 0)
            else:
                diff = timedelta(minutes=1)
                temp = now - diff
                result = datetime(temp.year, temp.month, temp.day, temp.hour, temp.minute, 0)
        return result


