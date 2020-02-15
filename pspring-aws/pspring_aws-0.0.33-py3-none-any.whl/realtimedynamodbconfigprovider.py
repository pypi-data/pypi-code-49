from pspring import ConfigurationProvider, Configuration
from .realtimes3 import RealTimeS3
import logging
import json
from .dynamodb import DynamoDBTable
from .realtimedynamodb import RealTimeDynamoDB

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class RealTimeDynamodbConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.subscriptions = []
        self.tableName = kargs.get("tableName") or config.getProperty("tableName")
        self.primaryKey = kargs.get("primaryKey") or config.getProperty("primaryKey")
        self.primaryKeyName = kargs.get("primaryKeyName") or config.getProperty("primaryKeyName")
        self.sortKey = kargs.get("sortKey") or config.getProperty("sortKey")
        self.sortKeyName = kargs.get("sortKeyName") or config.getProperty("sortKeyName")
        self.region = kargs.get("region") or config.getProperty("region")
        self.configColumnName = kargs.get("configColumnName") or config.getProperty("configColumnName")
        self.apiId = kargs.get("apiId") or config.getProperty("apiId")
        self.tableAsConfig = kargs.get("tableAsConfig") or config.getProperty("tableAsConfig")

        self.dynamodbclient = RealTimeDynamoDB(**kargs)
        self.dynamodbclient.subscribe(self.eventCallBack)
        self.response = {}

    def eventCallBack(self,response):
        #response = response.replace("\"","\\\"")
        logger.info("Received updated data "+str(response))
        
        if self.tableAsConfig == "True":
            try:
                self.response.update({
                    response.get(self.primaryKeyName) : {
                        response.get(self.sortKeyName) : response
                    }
                })
            except Exception as e:
                logger.error(str(e))
        else:
            try:
                self.response = response
            except Exception as e:
                logger.error(str(e))

        logger.info(self.response)
        self.publish()

    def refresh(self):
        pass

    def publish(self):
        for subscription in self.subscriptions:
            subscription()

    def getProperty(self,propertyName):
        return self.response.get(propertyName)

    def subscribe(self,callback):
        self.subscriptions.append(callback)
