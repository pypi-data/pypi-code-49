import requests
import json
from aiohttp import ClientSession

from . import errors

class GBL:
    """
    API client for Glenn Bot List in Python
    """
    def __init__(self, token: str, *, base: str = "https://glennbotlist.xyz/api/v2/bot/"):
        self.token = token
        self.base = base
        self.session = ClientSession(loop=None)

    async def post_server_count(self, botid: int, servers: int):
        """

        :param botid: Bot ID in which you are posting the stats for
        :param servers: The bots server coint
        """
        if not self.token:
            raise errors.InvalidKey("A token was not supplied")

        r = await self.session.post(url=self.base + f"{botid}/stats", data={"serverCount": servers}, headers={"authorization": self.token})
        if r.status != 200:
            raise errors.InvalidKey("The token provided was not valid")
