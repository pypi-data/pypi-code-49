import requests
import json
import aiohttp
from . import errors

class GBL:
    """
    API client for Glenn Bot List in Python
    """
    def __init__(self, token: str, *, base: str = "https://glennbotlist.xyz/api/v2/bot/"):
        self.token = token
        self.base = base

    async def post_server_count(self, botid: int, servers: int):
        """

        :param botid: Bot ID in which you are posting the stats for
        :param servers: The bots server coint
        """
        if not self.token:
            raise errors.InvalidKey("A token was not supplied")

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.base + f"{botid}/stats",
                headers={"authorization": self.token},
                data = {"serverCount": servers}) as resp:
                resp.raise_for_status()