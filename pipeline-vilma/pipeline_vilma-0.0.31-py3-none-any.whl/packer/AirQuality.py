import json
from pipelinevilma.packer.MetaType import MetaType


class AirQuality:
    """
    Example of a packet using AirQuality raw

    {
        "id": _id,
        "x": {
            "sensorId": 1,
            "metaType": "airQuality",
            "description": "Provide C02 Gas PPM, Temperature and Relative Humidity",
            "dataType": "json",
            "data": "aJsonObj"
        },
        "y":{
            "true": [], // This is going to be filled by Annotator
            "pred": [] // This is going to be by Estimator
        }
    }
    """
    DESCRIPTION = "Provide C02 Gas PPM, Temperature and Relative Humidity"

    def __init__(self, content, sensor_id):
        self.sensor_id = sensor_id
        self.x = self._set_x(content)
        self.y = self._set_y()

    def _set_x(self, content):
        return {
            "sensorId": self.sensor_id,
            "metaType": MetaType.AIR_QUALITY,
            "description": self.DESCRIPTION,
            "dataType": "json",
            "data": self._json_encode(content)
        }

    def _set_y(self):
        return {
            "true": [],
            "pred": []
        }

    def _json_encode(self, content):
        co2, temperature, relative_humidity = content
        return json.dumps({
            "co2": co2,
            "temperature": temperature,
            "relativeHumidity": relative_humidity
        })

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
