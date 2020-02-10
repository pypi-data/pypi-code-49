from decimal import Decimal
import requests_async as requests

BATTERY_SOC_PERCENT_ENDPOINT = "items/SPPro_BattSocPercent"
POWER_USED_WATTS_ENDPOINT = "items/SPPro_PowerUsed"


class ArvioEmaxxReader():
    """Instance of ArvioEmaxxReader"""

    def __init__(self, host):
        self._host = host.lower()
        self._endpoint_root = f"http://{self._host}:8080/rest/"

    async def battery_soc_percent(self):
        response_json = await self.call_api(BATTERY_SOC_PERCENT_ENDPOINT)
        return Decimal(response_json["state"])

    async def power_used_watts(self):
        response_json = await self.call_api(POWER_USED_WATTS_ENDPOINT)
        return Decimal(response_json["state"])

    async def call_api(self, endpoint):
        """Method to call the Arvio API"""
        response = await requests.get(self._endpoint_root + endpoint, timeout=10, allow_redirects=False,
                                      headers={'Accept': 'application/json'})
        return response.json()
