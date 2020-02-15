
import os, logging, json
import boto3
from pspring import *

logger = logging.getLogger(__name__)
config = Configuration.getConfig(__name__)

class SecretsManager():
    def __init__(self,*args,**kargs):
        self.secretId = kargs.get("secretId") or config.getProperty("secretId")
        self.region = kargs.get("region") or config.getProperty("region")

        if(self.secretId == None or self.region == None):
            logger.error("secretId required")
            raise Exception("configuration error")

        logger.info("Getting secret : "+self.secretId)

        self.client = boto3.client('secretsmanager',region_name=self.region)
        self.secretResponse = self.getSecret()
        logger.info("Secret status : OK")

    def getSecret(self):
        return self.client.get_secret_value(SecretId=self.secretId)

    def getSecretValue(self):
        secretString = self.secretResponse.get("SecretString")
        return json.loads(secretString)


class SecretValue():
    def __init__(self,*args,**kargs):
        self.secretId = kargs.get("secretId") or config.getProperty("secretId")
        self.region = kargs.get("region") or config.getProperty("region")
        self.column = kargs.get("column") or config.getProperty("column")
        self.columns = kargs.get("columns") or config.getProperty("columns")

        if(self.secretId == None or self.region == None):
            logger.error("secretId required")
            raise Exception("configuration error")

        self.client = boto3.client('secretsmanager',region_name=self.region)

    def __call__(self,classObj):
        def getSecretValue(selfObj):
            logger.info("Getting secret : "+self.secretId)
            self.secretResponse = self.getSecret()
            response = self.client.get_secret_value(SecretId=self.secretId)
            logger.info("Secret status : OK")
            responseData = {}
            columns = self.columns
            column = self.column
            if response != None:
                if columns != None:
                    for column in columns:
                        responseData.update({
                            column : item.get(column)
                        })
                    return responseData
                if column != None:
                    return item.get(column)
            return response

        classObj.getSecretValue = getSecretValue
        return classObj
