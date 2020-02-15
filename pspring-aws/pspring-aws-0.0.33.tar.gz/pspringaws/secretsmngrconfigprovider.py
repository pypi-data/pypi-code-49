from pspring import ConfigurationProvider, Configuration
from .secretsmngr import SecretsManager
import logging,json

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class SecretsMgrConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        secretId = kargs.get("secretId") or config.getProperty("secretId")
        region = kargs.get("region") or config.getProperty("region")
        self.subscriptions = []
        self.mgr = SecretsManager(secretId=secretId,region=region)
        self.refresh()

    def getProperty(self,propertyName):
        return self.secretValue.get(propertyName)

    def refresh(self):
        self.secretValue = self.mgr.getSecretValue()
        self.publish()

    def subscribe(self,callback):
        self.subscriptions.append(callback)

    def publish(self):
        for subscription in self.subscriptions:
            subscription()