# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 17:11
# @File    : general_test.py
# @User    : yangchuan
# @Desc    : 
# from quant_trade_framework.gateway.binance import base
from datetime import datetime
from quant_trade_framework.common.constant import Constant
from quant_trade_framework.gateway.jointquant.jqdata import JqDataCore
import talib
import numpy as np

if __name__ == '__main__':
    # result = JqDataCore.get_bar("000001.XSHE",1,
    #                             datetime.strptime("2020-02-21 14:00:00",
    #                                               "%Y-%m-%d %H:%M:%S"),Constant.KLINE_INTERVAL_1DAY)
    # print(result)
    # print(binanceData.get_all_realtime_price())
    # print(base.get_symbol_klines("BNBBTC",
    #                                    Constant.KLINE_INTERVAL_1DAY,
    #                                    limit=1,
    #                                    startTime=datetime.strptime("2019-01-01 00:00:00","%Y-%m-%d %H:%M:%S"),
    #                                    endTime=datetime.strptime("2019-02-01 00:00:00","%Y-%m-%d %H:%M:%S")))
    # temp = context()
    # temp.get_price("M9999.XDCE")
    # result = temp.history("M9999.XDCE",["open","close"],10,"dataframe")
    # print(temp.current_datetime())
    # func_b(func_name = func_a,func_a_p1 = "123",func_b_p1='Hello Python')
    # binanceData.get_symbol_historical_klines("BNBBTC",
    #                                     binanceData.KLINE_INTERVAL_1MINUTE,
    #                                     startTime=datetime.strptime("2020-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    #                                     endTime=datetime.strptime("2020-02-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
    # print(binanceData.get_latest_klines("BNBBTC"))
    a=np.array([16.95, 17.6,  17.35 ,17.44 ,17.,   17.04 ,16.97, 16.93, 16.67, 17. ,  16.96, 17.04,
     16.93 ,16.96 ,16.47, 17. ,  17.25 ,17.44 ,17.26 ,17.07])
    b=np.array([16.2 , 16.92, 16.82, 16.63, 16.55, 16.43, 16.43, 16.03, 16.23 ,16.44, 16.58, 16.48,
     16.56, 16.42 ,16.24, 16.28, 16.77, 16.79, 16.88, 16.75])
    c=np.array([16.81, 17.22, 17.18 ,16.79, 16.7,  16.51, 16.89, 16.42, 16.45 ,16.87, 16.88 ,16.66,
     16.91, 16.43, 16.26, 16.86, 16.92, 17.15, 16.96 ,16.89])
    result = talib.ATR(high=a,low=b,close=c,timeperiod=10)
    print(result)