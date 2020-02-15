import boto3
import time

from pspring import Configuration

import logging

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class DynamoDBTable():
    def __init__(self,*args,**kargs):
        self.tableName = kargs.get("tableName")
        self.primaryKey = kargs.get("primaryKey")
        self.sortKey = kargs.get("sortKey")
        self.region = kargs.get("region") or config.getProperty("region")
        self.ttlcolumnname = kargs.get("ttlColumnName") or config.getProperty("ttlColumnName")
        self.ttl = int(kargs.get("ttl") or config.getProperty("ttl"))
        dynamodb = boto3.resource("dynamodb",region_name=self.region)
        self.table = dynamodb.Table(self.tableName)

    def __call__(self,classObj):
        def put(selfObj,data):
            if(self.ttlcolumnname != None and data.get(self.ttlcolumnname) == None):
                data[self.ttlcolumnname] = int(time.time())+self.ttl
            self.table.put_item(Item=data)

        def get(selfObj,primaryKey,**kargs):
            key = {}
            key[self.primaryKey] = primaryKey
            sortKey = kargs.get(self.sortKey,None)
            columns = kargs.get("columns",None)
            column = kargs.get("column",None)
            if self.sortKey != None and sortKey != None:
                key.update({
                    self.sortKey : sortKey
                })
            response = self.table.get_item(Key=key)
            responseData = {}
            item = response.get("Item")
            if item != None:
                if columns != None:
                    for column in columns:
                        responseData.update({
                            column : item.get(column)
                        })
                    return responseData
                if column != None:
                    return item.get(column)
            return item
        classObj.put = put
        classObj.get = get
        return classObj
