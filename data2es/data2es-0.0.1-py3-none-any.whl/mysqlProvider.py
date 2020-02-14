#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: mysqlProvider.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################
import pymysql
from datetime import datetime


from providerBase import ProviderBase


class MysqlProvider(ProviderBase):

    def __init__(self,host,port,user,password,db,sql,pageSize=1000,canSaveId=False,idFile='',idName=''):
        super().__init__(host,port,user,password,db,sql,pageSize,canSaveId,idFile,idName)
        self.con = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db)
        self.cursor = self.con.cursor()

    def getData(self):
        super().getData()        
        self.cursor.execute(self.run_sql)
        result = self.cursor.fetchall()  # 获取查询结果
        col_result = self.cursor.description  # 获取查询结果的字段描述
        columns = []
        for i in range(len(col_result)):
            columns.append(col_result[i][0])  # 获取字段名，以列表形式保存
        package = []
        last = None
        for r in result:
            row = {}
            row["@timestamp"] = datetime.now().strftime( "%Y-%m-%dT%H:%M:%S.000+0800" )
            for index,c in enumerate(columns):
                row[c] = r[index]
            package.append(row)
        if self.canSaveId and len(package)>0:  
            self.lastId = package[len(package)-1][self.idName]    
        return package,self.run_sql

    

