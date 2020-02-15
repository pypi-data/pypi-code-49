from pipelinevilma.packer.MetaType import MetaType
import base64

class Image:
    """
    Example of a packet using Image raw

    {
        "id": _id,
        "x": {
            "sensorId": 1,
            "metaType": "image",
            "description": "RGB Image",
            "dataType": "base64",
            "data": "aLongBase64String"
            "url": "", // This is going to be filled by Collector
        },
        "y":{
            "true": [], // This is going to be filled by Annotator
            "pred": [] // This is going to be by Estimator
        }
    }
    """
    DESCRIPTION = "RGB Image"

    def __init__(self, content, sensor_id):
        self.sensor_id = sensor_id
        self.x = self._set_x(content)
        self.y = self._set_y()

    def _set_x(self, content):
        return {
            "sensorId": self.sensor_id,
            "metaType": MetaType.IMAGE,
            "description": self.DESCRIPTION,
            "url": "",
            "dataType": "base64",
            "data": base64.b64encode(content).decode('utf-8')
        }

    def _set_y(self):
        return {
            "true": [],
            "pred": []
        }

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
