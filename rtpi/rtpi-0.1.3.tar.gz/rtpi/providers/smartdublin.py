from typing import Optional

from rtpi.providers import BaseProvider, is_async


class SmartDublinProvider(BaseProvider):
    ENDPOINT = "https://data.smartdublin.ie/cgi-bin/rtpi/"

    def deserialize(self, response):
        return response.json()

    @is_async
    def realtime_bus_information(
        self,
        stopid: int,
        routeid: Optional[str] = None,
        operator: Optional[str] = None,
        maxresults: Optional[int] = None,
    ) -> dict:
        """Real time bus information for a given stop number and route"""
        query = {
            "stopid": stopid,
            "routeid": routeid,
            "operator": operator,
        }

        if maxresults:
            query["maxresults"] = maxresults

        return self._request("realtimebusinformation", query)
