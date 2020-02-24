# encoding: UTF-8
from datetime import datetime, timedelta
import jqdatasdk as jq
from pandas import DataFrame
import pandas as pd
from quant_trade_framwork.core import setting
from quant_trade_framwork.data.database import initialize

class JqDataCore:
    gateway = 'JQData'
    exchange = 'JQData'
    jquser = "17745021310"
    jqpassword = "021310"
    barFields = ['date', 'open', 'high', 'low', 'close', 'volume']
    priceFields = ['open', 'high', 'low', 'close', 'volume']
    symbol = ''
    jq.auth(jquser, jqpassword)

    @staticmethod
    def get_benchmark_price(end_datetime:datetime,frequency:str,price_type:str):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        result = 0
        df = jq.get_price("000016.XSHG",
                         count=1,
                         end_date=end_datetime,
                         frequency=frequency,
                         fq=None)
        pd.to_datetime(df.iloc[:,0],unit='s')
        for ix, row in df.iterrows():
            print(ix)
            print(type(ix))
            result = row[price_type]
        print(df)
        return result

    @staticmethod
    def get_bars(symbol:str,count: int,end_datetime: datetime, unit: str,fields:[]):
        """
        获取上证50基准价格
        :param end_datetime: datetime
        :param frequency:'Xd','Xm', 'daily'(等同于'1d'),
        'minute'(等同于'1m'), X是一个正整数
        :param price_type: str,price type,'open', 'close',
         'high', 'low', 'volume', 'money'
        :return: float
        """
        result = 0
        df = jq.get_bars(security=symbol,
                         count=count,
                         unit=unit,
                         fields=fields,
                        end_dt=end_datetime)
        return df

    @staticmethod
    def save_to_mongodb(data, symbol, inteval):
        database_manager = initialize.init(setting.SETTINGS)
        # insert into database
        database_manager.save_bar_data(symbol, data, str(inteval).lower())

    @staticmethod
    def bar_data_get_and_storage(symbol:str,start_datetime: datetime,end_datetime: datetime, frequency: str):
        result = 0
        df = jq.get_bars(symbol,
                          start_date=start_datetime,
                          end_date=end_datetime,
                          frequency=frequency,
                          fq=None)
        result_pd = DataFrame(columns=['date', 'open', 'max', 'min', 'close', 'volume'])

        for ix, row in df.iterrows():
            result_pd = result_pd.append(
                DataFrame(
                    {
                        'date': [pd.to_datetime(ix, unit='s')],
                        'open': [row['open']],
                        'max': [row['high']],
                        'min': [row['low']],
                        'close': [row['close']],
                        'volume': [row['volume']]
                    }
                ), ignore_index=True
            )

        if result_pd.size > 0:
            JqDataCore.save_to_mongodb(result_pd, symbol, frequency)

    @staticmethod
    def logout(self):
        if jq.is_auth():
            jq.logout()
        return

if __name__ == '__main__':
    now = datetime.now()
    temp = now + timedelta(days=-400)
    # print(JqDataCore.get_benchmark_price(temp,Constant.KLINE_INTERVAL_1DAY,"close"))
    JqDataCore.bar_data_get_and_storage('000300.XSHG',temp,now,'1d')
    # temp.getTradeDays("2020-01-01","2020-06-01")
#     print(temp.get_api_counts())
#     temp.sdkTest()
#     symbols = temp.get_future_contracts("M")
#     # print(symbols)
#     symbols = ["M2005.XDCE"]
#     temp.setSymbol(symbols)
#     temp.getSymbolBarByTimeSpan(
#         '2019-05-31 11:30:00',
#         '2019-11-19 15:30:00',
#         '1m', True)
#     # temp.setSymbol('JD2001.XDCE')
#     # temp.getSymbolBar(
#     #     10,
#     #     '2019-11-18 09:30:00',
#     #     '1m', True)