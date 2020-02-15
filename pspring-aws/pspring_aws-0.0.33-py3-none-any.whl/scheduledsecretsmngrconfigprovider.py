import boto3
from appsyncclient import AppSyncClient
import os
import json

import logging, threading

from pspring import Configuration, ConfigurationProvider

logger = logging.getLogger(__name__)

config = Configuration.getConfig(__name__)

class ScheduledSecretsMngrConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.region = kargs.get("region") or config.getProperty("region")
        self.secretId = kargs.get("secretId") or config.getProperty("secretId")
        self.period = kargs.get("period") or config.getProperty("period")
        self.period = int(self.period)
        if(self.secretId == None or self.region == None or self.period == None):
            logger.error("region,bucketId and objectKey required")
            raise Exception("configuration error")

        self.response = {}
        self.subscriptions=[]
        self.client = boto3.client('secretsmanager',region_name=self.region)
        
        self.loop()

    def loop(self):
        self.refresh()

        thread = threading.Timer(self.period,self.loop)
        thread.daemon = True
        thread.start()
    
    def refresh(self):
        logger.info("Getting value")
        
        secretResponse = self.client.get_secret_value(SecretId=self.secretId)
        content = secretResponse.get("SecretString")
        
        try:
            self.response = json.loads(content)
        except Exception as jsonerror:
            logger.error("Error while loading json..")
        self.publish()

    def publish(self):
        for subscription in self.subscriptions:
            subscription()

    def getProperty(self,propertyName):
        return self.response.get(propertyName)

    def subscribe(self,callback):
        self.subscriptions.append(callback)