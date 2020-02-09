from xml.etree import ElementTree

from rtpi.providers import BaseProvider, is_async


class IrishRailProvider(BaseProvider):
    ENDPOINT = "http://api.irishrail.ie/realtime/realtime.asmx/"

    def deserialize(self, response):
        return ElementTree.fromstring(response.content)

    @is_async
    def get_all_stations(self, station_type: str = "all", raw: bool = False):
        """List of all available stations"""
        types = {"all": "A", "mainline": "M", "suburban": "S", "dart": "D"}
        if station_type not in types:
            raise Exception("Station type not available")

        response = self._request(
            "getAllStationsXML_WithStationType",
            {"StationType": types.get(station_type)},
        )
        if raw:
            return response

        stations = []
        for station in response:
            stations.append(
                {
                    "name": station[0].text,
                    "latitude": station[2].text,
                    "longitude": station[3].text,
                    "code": station[4].text,
                    "id": station[5].text,
                }
            )

        return stations
