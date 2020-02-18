from datetime import datetime
from pymongo import MongoClient
from quant_trade_framwork.core.constant import Exchange, Interval
from .database import Driver
from quant_trade_framwork.common import Logger
import pandas as pd

logger = Logger.module_logger("system")
def init(_: Driver, settings: dict):
    database = settings["database.database"]
    host = settings["database.host"]
    port = settings["database.port"]
    username = settings["database.user"]
    password = settings["database.password"]
    type = settings["type"]
    if not username:  # if username == '' or None, skip username
        username = None
        password = None
    return MongoManagerNew(host, port, database, username,
                           password,type)


class MongoManagerNew:
    def __init__(self,para_host,para_port,para_database,
                 para_username,para_password,type):
        if type == "btc":
            self.bar_database = "btc"
            self.tick_database = "bars"
        else:
            self.bar_database = "quant"
            self.tick_database = "ticks"
        self.mongo_client = MongoClient(
            host=para_host,
            port=para_port,
            username=para_username,
            password=para_password
        )
        return

    def load_bar_data(
        self,
        symbol: str,
        exchange: Exchange,
        interval: Interval,
        start: datetime,
        end: datetime,
    ):
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            start_datetime_obj = datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
            end_datetime_obj = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            data = mongo_db_col_obj.find({"date": {"$gte": start_datetime_obj,"$lte":end_datetime_obj}})
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
            logger.info("load_bar_data success")
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def load_tick_data(
        self, symbol: str, exchange: Exchange, start: datetime, end: datetime
    ):
        try:
            mongo_db_obj = self.mongo_client[self.tick_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            start_datetime_obj = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
            end_datetime_obj = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            data = mongo_db_col_obj.find({"date": {"$gte": start_datetime_obj, "$lte": end_datetime_obj}})
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
            logger.info("load_tick_data success")
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def save_bar_data(self,symbol,df,interval):
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[(symbol + "-" + interval)]
            data = df.to_dict(orient='records')

            for item in data:
                if "d" in interval:
                    item['date'] = datetime.strptime(item['date'].strftime('%Y-%m-%d'),'%Y-%m-%d')
                mongo_db_col_obj.update_one({"date":item['date']}, {"$set":item}, upsert=True)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))

    def save_tick_data(self, symbol,df,interval):
        try:
            mongo_db_obj = self.mongo_client[self.tick_database]
            mongo_db_col_obj = mongo_db_obj[(symbol + "-" + interval)]
            data = df.to_dict(orient='records')
            for item in data:
                mongo_db_col_obj.update_one({"date": item['date']}, {"$set": item}, upsert=True)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))

    def get_newest_bar_data(
        self, symbol: str, exchange: "Exchange", interval: "Interval"
    ):
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            data = mongo_db_col_obj.find().sort([('date', -1)]).limit(1)
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def get_newest_tick_data(
        self, symbol: str, exchange: "Exchange"
    ):
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            data = mongo_db_col_obj.find().sort([('date', -1)]).limit(1)
            dataframe_obj = pd.DataFrame(data)
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))
        return dataframe_obj

    def clean(self, symbol: str):
        try:
            mongo_db_obj = self.mongo_client[self.bar_database]
            mongo_db_col_obj = mongo_db_obj[symbol]
            data = mongo_db_col_obj.remove({})
            self.mongo_client.close()
        except BaseException as e:
            logger.error(str(e))


