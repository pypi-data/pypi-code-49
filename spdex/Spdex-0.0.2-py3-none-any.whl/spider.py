#coding=utf-8

import os
from datetime import datetime
from pymongo import MongoClient

import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
pd.set_option('display.max_colwidth', 150)

rootPath=r'./'


class IOSdown():
    #初始化
    def __init__(self,stamp=None):
        self.stamp = (datetime.now()).strftime('%Y%m%d') if stamp is None else stamp
        self.client = MongoClient("localhost", 27017)
        self.db=self.client['spdex']
        self._matches = self.db['matches']
        self._record = self.db['records']
    #析构函数
    def __del__(self):
        self.client.close()

    # 列出所有联赛
    def leagues(self):
        result=[]
        try:
            leagues=self._record.find_one({'date': self.stamp})['events']
            for league in leagues:
                try:
                    if league['next'] != []:
                        line = [league['SortName'], league['Id'], league['Classification'], league['SportTypeId'],
                                league['FullName'], league['Eng'], league['Chs']]
                        result.append(line)
                except:
                    continue
            df = pd.DataFrame(data=result, columns=['SortName','Id',  'Classification', 'SportTypeId', 'FullName', 'Eng', 'Chs'])
            return df
        except Exception as e:
            print(e)
            return None

    # 列出所有比赛场次
    def events(self, kv):
        result=[]
        try:
            leagues=self._record.find_one({'date': self.stamp})['events']
            for league in leagues:
                # 多关键字匹配
                if kv not in [league['SortName'],league['Id'],league['FullName']]:
                    continue
                try:
                    if league['next'] != []:
                        for event in league['next']:
                            keys = event.keys()
                            line = [event[key] for key in keys]
                            result.append(line)
                except:
                    continue
            df = pd.DataFrame(data=result, columns=keys)
            # df=df['...']      #列排序
            return df
        except Exception as e:
            print(e)
            return None

    # 列出赛事详细信息
    def markets(self, eventid, kv):
        result=[]
        try:
            match=self._matches.find_one({'EventId': eventid})
            #分时数据?
            if kv=='csData':
                csData=match['Data']
                for row in csData.values():
                    keys = row.keys()
                    line = [row[key] for key in keys]
                    result.append(line)
            else:
                srData = match['Times'][-1]
                if kv in srData.keys():
                    # 字典数组形式
                    if isinstance(srData[kv],list):
                        for row in srData[kv]:
                            keys = row.keys()
                            line = [row[key] for key in keys]
                            result.append(line)
                    else:
                        # 字典形式
                        row=srData[kv]
                        keys=row.keys()
                        line=[row[key] for key in keys]
                        result.append(line)
                else:
                    print('请输入以下正确的关键字进行查询：')
                    print(srData.keys())
                    return None

            df = pd.DataFrame(data=result, columns=keys)
            return df
        except Exception as e:
            print(e)
            return None




# 主程序入口
if __name__ == '__main__':
    # Ctrl+ / 切换注释
    # db = Mongo("2019-04-03")   #下载历史数据（但必须已写入数据库）
    db = IOSdown()
    db.leagues()

    print('TS:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



