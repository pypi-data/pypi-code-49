# -*-coding:utf-8 -*-

# @Time    : 2020/2/10 10:51
# @File    : base.py
# @User    : yangchuan
# @Desc    : 
from binance.client import Client
from datetime import datetime
import time
from dataclasses import asdict
from quant_trade_framwork.model.KlineData import KlineData
from quant_trade_framwork.common import Constant
from quant_trade_framwork.core import setting
from quant_trade_framwork.data.database import initialize
from pandas import DataFrame

client = Client("EzmGEpb5xJAbp5ZzmMNbmvdfXmmUKguynR2bPUQF06tA7o8kYDv6m4usUGQRSNV6",
                "av3JBNxYbBxF6YkZwREzTeHt65SLCM7gAnde3ZHiyFA7RG25Ww9kHhgGexzXBMSl")
class binanceData:
    def __init__(self):
        pass

    @staticmethod
    def get_all_realtime_price():
        return client.get_all_tickers()

    @staticmethod
    def get_symbol_klines(symbol:str,inteval:str,limit:int,startTime:datetime,endTime:datetime):
        _starttime = int(time.mktime(startTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)

        _endtime = int(time.mktime(endTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)
        query_results = client.get_klines(symbol=symbol, interval=inteval, limit=limit, startTime=_starttime, endTime=_endtime)
        result = list()

        for item in query_results:
            kline_item = KlineData(
                symbol=symbol,
                exchange='binance',
                datetime=datetime.utcfromtimestamp(float(item[0]/1000)),
                interval=inteval,
                open_price=item[1],
                high_price=item[2],
                low_price=item[3],
                close_price=item[4],
                volume=item[5]
            )
            result.append(kline_item)
        return result

    @staticmethod
    def get_symbol_historical_klines(symbol: str, inteval: str, startTime: datetime, endTime: datetime):
        _starttime = int(time.mktime(startTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)

        _endtime = int(time.mktime(endTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)
        query_results = client.get_historical_klines(symbol=symbol, interval=inteval,start_str =_starttime,
                                          end_str=_endtime)
        result = list()

        for item in query_results:
            kline_item = KlineData(
                symbol=symbol,
                exchange='binance',
                datetime=datetime.utcfromtimestamp(float(item[0] / 1000)),
                interval=inteval,
                open_price=item[1],
                high_price=item[2],
                low_price=item[3],
                close_price=item[4],
                volume=item[5]
            )
            result.append(kline_item)
        return result

    @staticmethod
    def get_symbol_kline(symbol: str, inteval: str, startTime:datetime,endTime:datetime):
        _starttime = int(time.mktime(startTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)
        _endtime = int(time.mktime(endTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)
        query_results = client.get_klines(symbol=symbol, interval=inteval, limit=1,startTime=_starttime,
                                          endTime=_endtime)
        result = KlineData(
            symbol=symbol,
            exchange='binance',
            datetime=datetime.utcfromtimestamp(float(query_results[0][0] / 1000)),
            interval=inteval,
            open_price=float(query_results[0][1]),
            high_price=float(query_results[0][2]),
            low_price=float(query_results[0][3]),
            close_price=float(query_results[0][4]),
            volume=float(query_results[0][5])
        )
        return asdict(result)

    @staticmethod
    def get_latest_klines(symbol: str):
        query_results = client.get_klines(symbol=symbol, interval=Constant.KLINE_INTERVAL_1MINUTE, limit=1)
        result = KlineData(
            symbol=symbol,
            exchange='binance',
            datetime=datetime.utcfromtimestamp(float(query_results[0][0] / 1000)),
            interval=Constant.KLINE_INTERVAL_1MINUTE,
            open_price=query_results[0][1],
            high_price=query_results[0][2],
            low_price=query_results[0][3],
            close_price=query_results[0][4],
            volume=query_results[0][5]
        )
        return asdict(result)

    @staticmethod
    def get_symbol_historical_klines_and_storage(symbol: str, inteval: str, startTime: datetime, endTime: datetime):
        _starttime = int(time.mktime(startTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)

        _endtime = int(time.mktime(endTime.timetuple()) * 1000 + 8 * 60 * 60 * 1000)
        query_results = client.get_historical_klines(symbol=symbol, interval=inteval, start_str=_starttime,
                                                     end_str=_endtime)
        result_pd = DataFrame(columns=['date', 'open', 'max', 'min', 'close', 'volume'])

        for item in query_results:
            result_pd = result_pd.append(
                DataFrame(
                    {
                        'date': [datetime.utcfromtimestamp(float(item[0] / 1000))],
                        'open': [item[1]],
                        'max': [item[2]],
                        'min': [item[3]],
                        'close': [item[4]],
                        'volume': [item[5]]
                    }
                ),ignore_index = True
            )
        if result_pd.size > 0:
            binanceData.save_to_mongodb(result_pd,symbol,inteval)


    @staticmethod
    def save_to_mongodb(data,symbol,interval):
        database_manager = initialize.init(setting.SETTINGS)
        # insert into database
        database_manager.save_bar_data(symbol, data, interval)

if __name__ == '__main__':
    binanceData.get_symbol_historical_klines_and_storage("BTCUSDT",
                                                         Constant.KLINE_INTERVAL_1HOUR,
                                                         startTime=datetime.strptime("2019-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
                                                         endTime=datetime.strptime("2020-02-14 00:00:00", "%Y-%m-%d %H:%M:%S"))