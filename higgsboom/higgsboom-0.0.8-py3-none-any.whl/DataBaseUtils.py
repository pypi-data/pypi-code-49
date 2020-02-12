# -*- coding: utf-8 -*-
import re, datetime, sqlalchemy
import pandas as pd

def ProductIdFromInstrumentId(instrumentId):
    return instrumentId[:re.search("\d", instrumentId).start()]

def IsValidDate(strdate):
    try:
        if "-" in strdate:
            datetime.datetime.strptime(strdate, "%Y-%m-%d")
        else:
            datetime.datetime.strptime(strdate, "%Y%m%d")
        return True
    except:
        return False

def EngineConfigToCreateStr(engineConfig):
    return "%s+%s://%s:%s@%s:%d/%s" % (engineConfig["dbEngine"], engineConfig["dbDriver"],
                                       engineConfig["user"], engineConfig["passwd"], engineConfig["host"], 
                                       engineConfig["port"], engineConfig["dbName"])

class DataBaseUtils(object):
    def __init__(self):
        self.dataEngines = {
                "astock-daily":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"ASTOCK-DAILY"
                        }, 
                "astock-minute":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"ASTOCK-MINUTE"
                        }, 
                "cffex-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"CFFEX"
                        },
                "cffex-l2-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"CFFEX-L2"
                        },
                "shfe-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"SHFE"
                        },
                "shfe-l2-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"SHFE-L2"
                        },
                "dce-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"DCE"
                        },
                "dce-l2-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"DCE-L2"
                        },
                "czce-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"CZCE"
                        },
                "ine-tick":{
                        "dbEngine":"mysql",
                        "dbDriver":"mysqlconnector",
                        "host":"192.168.0.202",
                        "user":"root",
                        "port":3306,
                        "passwd":"higgs123",
                        "dbName":"INE"
                        },
                    }
        self.conns = dict()
        self.meta = dict()
    
    def InitDataEngine(self, engine):
        if not engine in self.dataEngines.keys():
            print("Data Engine Init Failure: error, no matching data engine for name '%s'!" % engine)
            return
        self.conns[engine] = sqlalchemy.create_engine(EngineConfigToCreateStr(self.dataEngines[engine]), echo=False)
        self.meta[engine] = sqlalchemy.MetaData(self.conns[engine])
    
    def GetDailyDataFrameByInstrumentId(self, engine, instrumentId):
        if not engine.endswith("daily"):
            print("Data Engine Type Unmatched: '%s' is not a daily data engine!" % engine)
            return
        if not engine in self.conns.keys():
            self.InitDataEngine(engine)
        table = sqlalchemy.Table(instrumentId, self.meta[engine], autoload=True)
        selectSql = sqlalchemy.select([table])
        return pd.read_sql(selectSql, self.conns[engine])
    
    def GetMinuteDataFrameByInstrumentId(self, engine, instrumentId):
        if not engine.endswith("minute"):
            print("Data Engine Type Unmatched: '%s' is not a minute data engine!" % engine)
            return
        if not engine in self.conns.keys():
            self.InitDataEngine(engine)
        table = sqlalchemy.Table(instrumentId, self.meta[engine], autoload=True)
        selectSql = sqlalchemy.select([table])
        return pd.read_sql(selectSql, self.conns[engine])

    def GetSqlResultForDataEngine(self, engine, sql):
        if not engine in self.conns.keys():
            self.InitDataEngine(engine)
        result = self.conns[engine].execute(sql)
        return result.fetchall()
            
