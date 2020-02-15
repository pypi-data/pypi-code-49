import json
from pipelinevilma.packer.MetaType import MetaType


class Environment:
    """
    Example of a packet using Environment raw

    {
        "id": _id,
        "x": {
            "sensorId": 1,
            "metaType": "environment",
            "description": "Provide Temperature, Relative Humidity, Pressure and Gas Resistance"
            "dataType": "json",
            "data": "aJsonObj"
            "url": "", // This is going to be filled by Collector
        },
        "y":{
            "true": [], // This is going to be filled by Annotator
            "pred": [] // This is going to be by Estimator
        }
    }
    """
    DESCRIPTION = "Provide Temperature, Relative Humidity, Pressure and Gas Resistance"

    def __init__(self, content, sensor_id):
        self.sensor_id = sensor_id
        self.x = self._set_x(content)
        self.y = self._set_y()

    def _set_x(self, content):
        return {
            "sensorId": self.sensor_id,
            "metaType": MetaType.ENVIRONMENT,
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
        temperature, relative_humidity, pressure, gas_resistance = content
        return json.dumps({
            "temperature": temperature,
            "relativeHumidity": relative_humidity,
            "pressure": pressure,
            "gasResistance": gas_resistance
        })

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
