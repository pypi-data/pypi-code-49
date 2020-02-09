import requests
import httpx
import enum

from telegram_bot_sdk.controller import controller


class HttpVerbs(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5
    HEAD = 6
    CONNECT = 7
    OPTIONS = 8
    TRACE = 9


class NetworkAsync:
    def __init__(self, my_config):
        self.config = my_config
        self.async_client = httpx.Client()

    async def make_request(self, *, verb, call, params=None, data=None):
        response = None

        if verb == HttpVerbs.GET:
            response = await self.async_client.get(self.config.vars["URL"] + call, params=params)
        if verb == HttpVerbs.POST:
            response = await self.async_client.post(self.config.vars["URL"] + call, params=params, data=data)

        return controller.control_response_level_network(response)


class Network:
    def __init__(self, my_config):
        self.config = my_config
        self.session = requests.Session()

    def make_request(self, *, verb, call, params=None, data=None, files=None, timeout=None):
        response = None

        if verb == HttpVerbs.GET:
            response = self.session.get(self.config.vars["URL"] + call, params=params, timeout=timeout)
        if verb == HttpVerbs.POST:
            response = self.session.post(self.config.vars["URL"] + call, params=params, data=data, files=files, timeout=timeout)

        return controller.control_response_level_network(response)
