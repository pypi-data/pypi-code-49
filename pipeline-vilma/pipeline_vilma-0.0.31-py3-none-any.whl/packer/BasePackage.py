import json
import base64
import time
from pipelinevilma.packer.ImageBase64 import ImageBase64
from pipelinevilma.packer.ImageUrl import ImageUrl
from pipelinevilma.packer.AirQuality import AirQuality
from pipelinevilma.packer.Heatmap import Heatmap
from pipelinevilma.packer.Environment import Environment
from pipelinevilma.packer.Text import Text
from pipelinevilma.packer.MetaType import MetaType


class BasePackage:
    def __init__(self, data_type, content, sensor_id):
        if data_type == MetaType.IMAGE_URL:
            self.data = ImageUrl(content, sensor_id)
        elif data_type == MetaType.IMAGE_BASE64:
            self.data = ImageBase64(content, sensor_id)
        elif data_type == MetaType.AIR_QUALITY:
            self.data = AirQuality(content, sensor_id)
        elif data_type == MetaType.HEATMAP:
            self.data = Heatmap(content, sensor_id)
        elif data_type == MetaType.ENVIRONMENT:
            self.data = Environment(content, sensor_id)
        elif data_type == MetaType.TEXT:
            self.data = Text(content, sensor_id)

    def pack(self):
        return json.dumps({
            "x": self.data.get_x(),
            "y": self.data.get_y(),
            "createdAt": int(time.time())
        })
