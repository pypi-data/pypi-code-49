# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 17:11
# @File    : general_test.py
# @User    : yangchuan
# @Desc    : 
from quant_trade_framwork.gateway import binanceData
from datetime import datetime
from quant_trade_framwork.common import Constant

if __name__ == '__main__':
    # print(binanceData.get_all_realtime_price())
    print(binanceData.get_symbol_klines("BNBBTC",
                                       Constant.KLINE_INTERVAL_1DAY,
                                       limit=1,
                                       startTime=datetime.strptime("2019-01-01 00:00:00","%Y-%m-%d %H:%M:%S"),
                                       endTime=datetime.strptime("2019-02-01 00:00:00","%Y-%m-%d %H:%M:%S")))
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