#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: providerBase.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################
import abc
import os

class ProviderBase:
    def __init__(self,host,port,user,password,db,sql,pageSize=1000,canSaveId=False,idFile='',idName=''):        
        self.host=host
        self.port=port
        self.user=user
        self.password = password
        self.db=db
        self.sql=sql
        self.pageSize=pageSize
        self.canSaveId=canSaveId
        self.idFile=idFile
        self.idName=idName
        self.getLastId()


    def saveId(self):
        '''
        按照配置文件保存最后执行的id值
        '''
        with open(self.idFile, 'w') as f:
            print(self.lastId, file=f)

    def getLastId(self):
        '''
        按照配置文件获取最后的id值
        '''
        if self.canSaveId:
            if os.path.exists(self.idFile):
                with open(self.idFile) as f:
                    self.lastId = int(f.read())
            else:
                self.lastId=0
        else:
            self.lastId = 0      


       
    def getData(self):
        self.run_sql = self.sql.format(last_run_id=self.lastId)
            
        