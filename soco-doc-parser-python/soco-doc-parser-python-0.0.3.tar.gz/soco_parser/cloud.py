# -*- coding: utf-8 -*-
# Author: Kyusong Lee
# Date: 12/22/19

import uuid

import boto3
import requests

from soco_parser.config import Config


class CloudBucket(object):
    def __init__(self, api_key):
        self.api_key = api_key
        s3_key = self.get_key()
        self._s3 = boto3.resource('s3', aws_access_key_id=s3_key["aws_access_key_id"],
                                  aws_secret_access_key=s3_key["aws_secret_access_key"])

    def _get_header(self):
        return {'Content-Type': 'application/json', "Authorization": self.api_key}

    def get_key(self):
        result = requests.get(url=Config.AUTH_URL, headers=self._get_header()).json()
        if "message" in result and result["message"] == "permission denied":
            print("API_KEY ERROR (Please get your API_KEY at http://app.soco.ai")
            exit()
            return None
        return result["task_info"]

    def upload(self, file, task_id="default"):
        file_name = str(uuid.uuid4())+".pdf"
        try:
            key = '{}/{}/{}'.format("temp", task_id, file_name)
            self._s3.meta.client.upload_file(file, 'soco-knowledge', key) # ExtraArgs={'ACL': 'public-read'}
            return key
        except Exception as e:
            print(e)
            return None

    def deletes(self, files):
        for file in files:
            self._s3.delete_object(Bucket='soco-knowledge', Key=file)


if __name__ == "__main__":
    x = CloudBucket()
    task_id = str(uuid.uuid4())
    x.upload("../resources/1906.09308.pdf",task_id)
