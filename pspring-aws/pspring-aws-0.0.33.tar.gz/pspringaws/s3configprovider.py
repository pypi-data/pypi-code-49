from pspring import ConfigurationProvider, Configuration
import logging,json
import yaml
import os
import boto3

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class S3ConfigProvider(ConfigurationProvider):
    def __init__(self,**kargs):
        self.bucketId = kargs.get("bucketId") or config.getProperty("bucketId")
        self.objectKey = kargs.get("objectKey") or config.getProperty("objectKey")
        self.region = kargs.get("region") or config.getProperty("region")
        self.subscriptions = []
        self.refresh()

    def getProperty(self,propertyName):
        return self.config.get(propertyName)

    def refresh(self):
        client = boto3.client("s3",region_name=self.region)
        file = client.get_object(Bucket=self.bucketId,Key=self.objectKey)
        filecontent = file.get("Body").read().decode("utf-8")
        try:
            extn = os.path.splitext(self.objectKey)[1]

            if extn and extn == '.json':
                self.config = json.loads(str(filecontent))
            elif extn and extn in ['.yml', '.yaml']:
                self.config = yaml.safe_load(filecontent)
            else:
                logger.error('File type {} not supported.'.format(extn))
                raise Exception('File type {} not supported.'.format(extn))

            self.publish()
        except Exception as er:
            logger.warn(f"Received content from s3 was not json {er}")

    def subscribe(self,callback):
        self.subscriptions.append(callback)

    def publish(self):
        for subscription in self.subscriptions:
            subscription()