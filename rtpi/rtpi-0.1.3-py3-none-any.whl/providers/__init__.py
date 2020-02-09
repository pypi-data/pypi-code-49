from urllib.parse import urljoin

import httpx


def is_async(func):
    def wrapper(self, *args, is_async=False, **kwargs):
        self._async_client = is_async
        return func(self, *args, **kwargs)

    return wrapper


class BaseProvider:
    is_json = True

    def __init__(self, async_client=False):
        self._async_client = async_client

    async def _async_request(self, url, query):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=query)
            return self.deserialize(response)

    def _request(self, url, query=None):
        url = urljoin(self.ENDPOINT, url)

        if self._async_client:
            return self._async_request(url, query)

        response = httpx.get(url, params=query)
        return self.deserialize(response)
