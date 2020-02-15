import boto3
from appsyncclient import AppSyncClient
import os
import json

import logging, threading

from pspring import Configuration, ConfigurationProvider

logger = logging.getLogger(__name__)

config = Configuration.getConfig(__name__)

class ScheduledS3ConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.region = kargs.get("region") or config.getProperty("region")
        self.bucketId = kargs.get("bucketId") or config.getProperty("bucketId")
        self.objectKey = kargs.get("objectKey") or config.getProperty("objectKey")
        self.period = kargs.get("period") or config.getProperty("period")
        self.period = int(self.period)
        if(self.bucketId == None or self.objectKey == None or self.region == None or self.period == None):
            logger.error("region,bucketId and objectKey required")
            raise Exception("configuration error")

        self.response = {}
        self.subscriptions=[]
        
        self.loop()

    def loop(self):
        self.refresh()
        thread = threading.Timer(self.period,self.loop)
        thread.daemon = True
        thread.start()
    
    def refresh(self):
        logger.info("Getting value")
        client = boto3.client("s3",region_name=self.region)
        file = client.get_object(Bucket=self.bucketId,Key=self.objectKey)
        filecontent = file.get("Body").read().decode("utf-8")
        
        try:
            self.response = json.loads(filecontent)
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