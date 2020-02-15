from pipelinevilma.packer.MetaType import MetaType
import base64


class ImageUrl:
    """
    Example of a packet using ImageUrl raw

    {
        "id": _id,
        "x": {
            "sensorId": 1,
            "metaType": "image-url",
            "description": "RGB Image as URL",
            "dataType": "url",
            "data": "http://dataset/image.jpg"
        },
        "y":{
            "true": [], // This is going to be filled by Annotator
            "pred": [] // This is going to be by Estimator
        }
    }
    """
    DESCRIPTION = "RGB Image as URL"

    def __init__(self, content, sensor_id):
        self.sensor_id = sensor_id
        self.x = self._set_x(content)
        self.y = self._set_y()

    def _set_x(self, content):
        return {
            "sensorId": self.sensor_id,
            "metaType": MetaType.IMAGE_URL,
            "description": self.DESCRIPTION,
            "dataType": "string",
            "data": str(content)
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
