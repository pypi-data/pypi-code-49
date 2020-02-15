from pspring import ConfigurationProvider, Configuration
import logging,json

from .dynamodb import DynamoDBTable

import boto3

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class DynamodbConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):

        self.tableName = kargs.get("tableName") or config.getProperty("tableName")
        self.primaryKey = kargs.get("primaryKey") or config.getProperty("primaryKey")
        self.primaryKeyName = kargs.get("primaryKeyName") or config.getProperty("primaryKeyName")
        self.sortKey = kargs.get("sortKey") or config.getProperty("sortKey")
        self.sortKeyName = kargs.get("sortKeyName") or config.getProperty("sortKeyName")
        self.region = kargs.get("region") or config.getProperty("region")
        self.configColumnName = kargs.get("configColumnName") or config.getProperty("configColumnName")

        @DynamoDBTable(
            tableName=self.tableName,
            primaryKey=self.primaryKeyName,
            sortKey=self.sortKeyName,
            region=self.region
        )
        class DynamoTable():
            pass
        self.table = DynamoTable()
        self.config = {}
        self.subscriptions = []
        self.refresh()

    def getProperty(self,propertyName):
        return self.config.get(propertyName)

    def refresh(self):
        dynamoContent = self.table.get(self.primaryKey,sortKey=self.sortKey,column=self.configColumnName)
        try:
            self.config = json.loads(str(dynamoContent))
            self.publish()
        except Exception as er:
            logger.warn(f"Received content from dynamodb was not json {er}")

    def subscribe(self,callback):
        self.subscriptions.append(callback)

    def publish(self):
        for subscription in self.subscriptions:
            subscription()