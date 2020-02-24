# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 14:20
# @File    : Context.py
# @User    : yangchuan
# @Desc    : get the quant trade data
from pymongo import MongoClient,DESCENDING
from quant_trade_framwork.common.constant import Constant
from .account import account
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from quant_trade_framwork.common.logConfig import Logger
from pytz import timezone
# from generalquant.gateway.binance.base import binanceData

logger = Logger.module_logger("system")

cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')

class context:
    accounts = {}
    run_freq = Constant.KLINE_INTERVAL_1MINUTE
    is_digtal_currency = True
    exchange = "btc"
    benchmark_symbol = 'china_next10'
    security_type = "stock"

    def __init__(self):
        pass
        # self.accounts = {}
        # self.run_freq = Constant.KLINE_INTERVAL_1DAY
        # self.is_digtal_currency = True

    @staticmethod
    def set_account(account:account):
        context.accounts[account.name] = account

    @staticmethod
    def set_current_datetime(dt):
        context.current_dt = dt

    @staticmethod
    def set_run_freq(type):
        context.run_freq = type

    @staticmethod
    def get_account(name:str):
        return context.accounts[name]

    @staticmethod
    def get_price(symbol:str):
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        # if not context.is_digtal_currency:
        #     mc = MongoClient(
        #         host="182.151.7.177",
        #         port=27017,
        #         username="admin",
        #         password="admin"
        #     )
        #     db = mc[context.exchange]
        #     collection = db[symbol]
        #     cursor = collection.find_one(filter={"date": {"$lte": context.current_datetime()}},
        #                                  sort=[('date',-1)])
        #
        #     return cursor['close']
        # else:
        #     result = binanceData.get_symbol_kline(symbol,context.run_freq,context.previous_datetime(),context.current_datetime())
        #     return result['close_price']
        col = symbol + "-"  + context.run_freq
        result = 0
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[context.exchange]
            collection = db[col]
            cursor = collection.find({"date": {"$lte": context.current_datetime()}}).sort([('date', -1)]).limit(1)
            if cursor and cursor.count() > 0:
                result = cursor[0]['close']
        except BaseException as e:
            print(str(e))
        return float(result)

    @staticmethod
    def get_benchmark_price():
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        # return JqDataCore.get_benchmark_price(context.current_datetime(),Constant.KLINE_INTERVAL_1DAY,"close")
        col = context.benchmark_symbol + "-" + context.run_freq
        result = 0
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[context.exchange]
            collection = db[col]
            cursor = collection.find({"date": {"$lte": context.current_datetime()}}).sort([('date', -1)]).limit(1)
            if cursor and cursor.count() > 0:
                result = cursor[0]['close']
        except BaseException as e:
            print(str(e))
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
        result = None
        if context.current_dt and type(context.current_dt) == datetime:
            temp = context.current_dt
            if context.run_freq == Constant.KLINE_INTERVAL_1DAY:
                result = datetime(temp.year, temp.month, temp.day, 0, 0, 0)
            elif context.run_freq == Constant.KLINE_INTERVAL_1HOUR:
                result = datetime(temp.year, temp.month, temp.day, temp.hour, 0, 0)
            else:
                result = datetime(temp.year, temp.month, temp.day, temp.hour, temp.minute, 0)
        return result


    @staticmethod
    def previous_datetime():
        """
        get the last trade datetime
        :return: datetime
        """
        result = None
        if context.current_dt and type(context.current_dt) == datetime:
            now = context.current_dt
            if context.run_freq == Constant.KLINE_INTERVAL_1DAY:
                diff = timedelta(days=1)
                temp = now - diff
                result = datetime(temp.year, temp.month, temp.day, 0, 0, 0)
            elif context.run_freq == Constant.KLINE_INTERVAL_1HOUR:
                diff = timedelta(hours=1)
                temp = now - diff
                result = datetime(temp.year, temp.month, temp.day, temp.hour, 0, 0)
            else:
                diff = timedelta(minutes=1)
                temp = now - diff
                result = datetime(temp.year, temp.month, temp.day, temp.hour, temp.minute, 0)
        return result


