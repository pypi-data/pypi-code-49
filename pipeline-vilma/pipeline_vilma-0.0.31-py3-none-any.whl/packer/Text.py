from pipelinevilma.packer.MetaType import MetaType


class Text:
    """
    Example of a packet using Text raw

    {
        "id": _id,
        "x": {
            "sensorId": 1,
            "metaType": "text",
            "description": "Provide a text data (word, sentence)",
            "dataType": "utf8",
            "data": "word"
        },
        "y":{
            "true": [], // This is going to be filled by Annotator
            "pred": [] // This is going to be by Estimator
        }
    }
    """
    DESCRIPTION = "Provide a text data (word, sentence)"

    def __init__(self, content, sensor_id):
        self.sensor_id = sensor_id
        self.x = self._set_x(content)
        self.y = self._set_y()

    def _set_x(self, content):
        return {
            "sensorId": self.sensor_id,
            "metaType": MetaType.TEXT,
            "description": self.DESCRIPTION,
            "dataType": "text",
            "data": content
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
