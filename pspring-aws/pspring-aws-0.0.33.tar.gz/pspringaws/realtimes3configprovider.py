from pspring import ConfigurationProvider, Configuration
from .realtimes3 import RealTimeS3
import logging
import json

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class RealTimeS3ConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.subscriptions = []
        region = kargs.get("region") or config.getProperty("region")
        apiId = kargs.get("apiId") or config.getProperty("apiId")
        bucketId = kargs.get("bucketId") or config.getProperty("bucketId")
        objectKey = kargs.get("objectKey") or config.getProperty("objectKey")

        self.s3client = RealTimeS3(bucketId=bucketId,objectKey=objectKey,apiId=apiId,region=region)
        self.s3client.subscribe(self.eventCallBack)

    def eventCallBack(self,response):
        logger.info("Received updated data "+str(response))
        self.response = json.loads(response)
        logger.info("After json")
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
