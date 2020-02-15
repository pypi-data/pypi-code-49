from pspring import ConfigurationProvider, Configuration
from realtimeawssecretsmngr import RealTimeAwsSecretsMngr
import logging
import json

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class RealTimeSecretsMgrConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.subscriptions = []
        secretId = kargs.get("secretId") or config.getProperty("secretId")
        region = kargs.get("region") or config.getProperty("region")
        apiId = kargs.get("apiId") or config.getProperty("apiId")

        self.mgr = RealTimeAwsSecretsMngr(secretId=secretId,apiId=apiId,region=region)
        self.mgr.subscribe(self.eventCallBack)

    def eventCallBack(self,response):
        logger.info("Received updated secret "+str(response))
        self.response = json.loads(response)
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
