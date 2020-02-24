# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 14:20
# @File    : self.py
# @User    : yangchuan
# @Desc    : get the quant trade data
from pymongo import MongoClient,DESCENDING
from quant_trade_framework.common.constant import Constant
from quant_trade_framework.stock import account
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from quant_trade_framework.common.logConfig import Logger
from pytz import timezone
from quant_trade_framework.stock.parameters import OrderCost,SlipPage
from quant_trade_framework.common.redisConfig import RuntimeConfig
from quant_trade_framework.core.object import BarData
from quant_trade_framework.common.array_manager import ArrayManager

logger = Logger.module_logger("system")

cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')


class Context:
    """
    策略运行上下文环境
    accounts: Account dictm user accounts, one or more account information
    run_freq:str, strategy run inteval
    is_digtal_currency:bool,digital currency flag
    benchmark_symbol:str,benchmark symbol name
    order_cost:dict,order cost parameters
    slippage:dict,slippage parameters
    user_name:str,user name
    user_pwd:str, user password
    next_price_day_diff：int，下次交易的时间间隔
    next_price_time：datetime,下次交易的时间点
    runtime_config_obj:RuntimeConfig object, online redis check methods
    current_dt: contenxt current datetime
    bars: cached bars
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
    current_dt = None
    bars = ArrayManager()
    
    def __init__(self):
        pass

    def set_bar_cache_size(self,size:int):
        """
        set the cached bar counts
        :param size: int, cached counts
        :return: none
        """
        self.bars = ArrayManager(size=size)


    def set_auth(self,user_name:str, user_pwd:str):
        """
        set system auth information
        :param user_name: str, user name
        :param user_pwd: str, user password
        :return:
        """
        self.user_name = user_name
        self.user_pwd = user_pwd

    def set_account(self,account: account):
        """
        set the account object to the self environments
        :param account:
        :return: None
        """
        self.accounts[account.name] = account

    def set_order_cost(self,cost:OrderCost,type:str):
        """
        set the order cost parameters
        :param cost: Order Cost Object
        :param type: stock、fund or index,none for set all
        :return:
        """
        if type:
            self.order_cost["all"] = cost
        else:
            self.order_cost[type] = cost

    def set_benckmark(self,security):
        """
        set the benchmark security name
        :param security: str,name
        :return: none
        """
        self.benchmark_symbol = security

    def set_slippage(self,slippage:SlipPage,type:str):
        """
        set the slippage parameters
        :param slippage: dcit,slippage parameters
        :param type: string,slippage parameters, default is 'all'
        :return: none
        """
        if type:
            self.slippage["all"] = slippage
        else:
            self.slippage[type] = slippage

    def set_current_datetime(self,dt):
        """
        set current datetime
        :param dt: datetime
        :return: none
        """
        self.current_dt = dt

    def set_run_freq(self,type):
        """
        set strategy run frequncy
        :param type: str,Constant.XXXX
        :return: none
        """
        self.run_freq = type
        
    def get_account(self,name:str):
        """
        get the account of name
        :param name: str,account name
        :return: Account object
        """
        return self.accounts[name]

    def get_price(self,symbol:str,inteval:str = "1d"):
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        col = symbol + "-"  + inteval
        result = BarData()
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[self.exchange]
            collection = db[col]
            cursor = collection.find({"date": {"$lte": self.current_datetime(),"$gt":self.previous_datetime()}}).sort([('date', -1)]).limit(1)
            if cursor and cursor.count() > 0:
                result.close_price = cursor[0]['close']
                result.high_price = cursor[0]['max']
                result.low_price = cursor[0]['min']
                result.open_price = cursor[0]['open']
                result.volume = cursor[0]['volume']
                result.datetime = self.current_datetime()
                result.interval = inteval
        except BaseException as e:
            logger.error(str(e))
        return result

    def get_benchmark_price(self):
        """
        get latest symbol price
        :param symbol:
        :return: float
        """
        col = self.benchmark_symbol + "-" + self.run_freq
        result = BarData()
        try:
            mc = MongoClient(
                host="182.151.7.177",
                port=27017,
                username="admin",
                password="admin"
            )
            db = mc[self.exchange]
            collection = db[col]
            cursor = collection.find({"date": {"$lte": self.current_datetime(),
                                               "$gt":self.previous_datetime()}}).sort([('date', -1)]).limit(1)
            if cursor and cursor.count() > 0:
                result.close_price = cursor[0]['close']
                result.high_price = cursor[0]['max']
                result.low_price = cursor[0]['min']
                result.open_price = cursor[0]['open']
                result.volume = cursor[0]['volume']
                result.datetime = self.next_price_datetime()
                result.interval = self.run_freq
        except BaseException as e:
            logger.error(str(e))
        return result

    def history(self,symbol:str,attributes:object,bars:int,rtype:str):
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

    def current_datetime(self):
        """
        get current trade datetime
        :return: datetime
        """
        return self.current_dt

    def next_price_datetime(self):
        """
        get the next price datetime from the current datetime
        :return:
        """
        if self.next_price_day_diff > 0 and self.next_price_time and \
                type(self.next_price_time) == datetime:
            next = self.current_dt + timedelta(days=self.next_price_day_diff)
            while True:
                next = datetime(next.year,next.month,next.day,
                                self.next_price_time.hour,self.next_price_time.minute,0)
                datetime_now_date_str = next.strftime('%Y-%m-%d')
                if self.runtime_config_obj.check_day_is_valid_trade_day(datetime_now_date_str):
                    break
                next = next + timedelta(days=self.next_price_day_diff)
        else:
            next = self.current_dt + timedelta(minutes=1)
        return next

    def previous_datetime(self):
        """
        get the last trade datetime
        :return: datetime
        """
        if self.next_price_day_diff > 0 and self.next_price_time and \
                type(self.next_price_time) == datetime:
            next = self.current_dt - timedelta(days=self.next_price_day_diff)
            while True:
                next = datetime(next.year, next.month, next.day,
                                self.next_price_time.hour, self.next_price_time.minute, 0)
                datetime_now_date_str = next.strftime('%Y-%m-%d')
                if self.runtime_config_obj.check_day_is_valid_trade_day(datetime_now_date_str):
                    break
                next = next - timedelta(days=self.next_price_day_diff)
        else:
            next = self.current_dt + timedelta(minutes=1)
        return next
