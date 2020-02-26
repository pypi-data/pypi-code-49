__author__ = "Wytze Bruinsma"

import re
from io import BytesIO
from dataclasses import dataclass

import requests
from PIL import Image

from vaknl_gcp.Storage import StorageClient


@dataclass
class Image:
    url: str  # default
    bucket_url: str  # default
    width: int  # default
    height: int  # default
    bytes_size: int  # default


class ImageClient(object):

    def __init__(self, project_id):
        self.project_id = project_id
        self.storage_client = StorageClient(project_id=project_id)

    @staticmethod
    def get_image(image_url, auth=None):
        for i in range(3):  # try 3 times if necessary
            try:
                response = requests.get(image_url, auth=auth)
                if response.status_code <= 204:
                    data = response.content
                    with Image.open(BytesIO(data)) as img:
                        width, heigth = img.size
                        size = len(img.fp.read())
                        return width, heigth, size, data
            except Exception as e:
                print(e)
        return None, None, None, None

    def upload_image_to_storage(self, id, bucket_name, image_url):
        width, heigth, byte_size, image = self.get_image(image_url)
        if image:
            bucket = self.storage_client.get_bucket(f'{bucket_name}-{self.project_id}')
            blob = bucket.blob(f"{id}/{self.get_image_name_from_url(image_url)}")
            new_image_url = self.storage_client.upload_from_string(blob, image)
            return width, heigth, byte_size, new_image_url
        else:
            return None, None, None, None

    @staticmethod
    def get_image_name_from_url(image_url):
        return re.search(r'[^/]+$', image_url).group()
