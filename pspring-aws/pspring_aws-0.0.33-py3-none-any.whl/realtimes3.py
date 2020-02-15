import boto3
from appsyncclient import AppSyncClient
import os
import json

import logging, base64

from pspring import Configuration

logger = logging.getLogger(__name__)

config = Configuration.getConfig(__name__)

class RealTimeS3():
    def __init__(self,**kargs):
        self.region = kargs.get("region")
        self.bucketId = kargs.get("bucketId") or config.getProperty("bucketId")
        self.objectKey = kargs.get("objectKey") or config.getProperty("objectKey")
        self.apiId = kargs.get("apiId") or config.getProperty("apiId")

        if(self.bucketId == None or self.objectKey == None or self.region == None):
            logger.error("region,bucketId and objectKey required")
            raise Exception("configuration error")
        self.client = AppSyncClient(region=self.region,apiId=self.apiId)

    def getValue(self):
        client = boto3.client("s3",region_name=self.region)
        file = client.get_object(Bucket=self.bucketId,Key=self.objectKey)
        filecontent = file.get("Body").read().decode("utf-8")
        
        return str(filecontent)

    def subscribe(self,callback):
        contents = self.getValue()
        callback(contents)
        id = "arn:aws:s3:::"+self.bucketId+":"+self.objectKey
        query = json.dumps({"query": "subscription {\n  updatedResource(id:\""+id+"\") {\n    id\n    data\n  }\n}\n"})

        def secretcallback(client, userdata, msg):
            logger.debug("New data received : "+str(msg))

            callbackdatab64 = json.loads(msg.payload).get("data",{}).get("updatedResource",{}).get("data")
            logger.debug(callbackdatab64)
            try:
                callbackdata = base64.b64decode(callbackdatab64.encode("utf-8"))
                logger.debug(f"decoded successfully {callbackdata}")
                callback(callbackdata.decode("utf-8"))
            except Exception as e:
                logger.error(str(e))
                
        response = self.client.execute(data=query,callback=secretcallback)
