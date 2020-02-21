# -*-coding:utf-8 -*-

# @Time    : 2020/2/14 9:48
# @File    : benchmark_index.py
# @User    : yangchuan
# @Desc    :
from datetime import datetime,timedelta
import time
from quant_trade_framwork.core import setting
from quant_trade_framwork.data.database import initialize
from pandas import DataFrame
import requests

class ChinaNextBenchmarkIndex:
    url_base = "https://api.chainext.io/v1/"
    url_klines = "kchart"

    @staticmethod
    def get_history_klines(index_id:str,grouping:str,start_datetime:datetime,
                           end_datetime:datetime):
        _starttime = int(time.mktime(start_datetime.timetuple()))

        _endtime = int(time.mktime(end_datetime.timetuple()))
        payload = {'id': index_id,
                   'grouping': grouping,
                   'tstart':_starttime,
                   'tend':_endtime}
        try:
            r = requests.get(ChinaNextBenchmarkIndex.url_base +
                             ChinaNextBenchmarkIndex.url_klines, params=payload)
            if r.status_code == 200:
                result_json = r.json()
                result_pd = DataFrame(columns=['date', 'open', 'max', 'min','close','volume'])
                for item in result_json["data"]["lines"]:
                    item[0] = datetime.utcfromtimestamp(float(item[0]))
                    result_pd = result_pd.append(
                        DataFrame({
                            'date':[item[0]],
                            'open':[item[1]],
                            'max':[item[2]],
                            'min':[item[3]],
                            'close':[item[4]],
                            'volume':[item[5]]
                        }),ignore_index = True
                    )
                if result_pd.size > 0:
                    ChinaNextBenchmarkIndex.save_to_mongodb(result_pd,"china_next10",grouping)
        except BaseException as e:
            print(str(e))

    @staticmethod
    def save_to_mongodb(data,symbol,inteval):
        database_manager = initialize.init(setting.SETTINGS)
        # insert into database
        database_manager.save_bar_data(symbol,data,str(inteval).lower())

if __name__ == '__main__':
    end = datetime(2020,2,14,0,0,0)
    start = end + timedelta(days=-800)
    result = ChinaNextBenchmarkIndex.get_history_klines("4","1D",start,end)