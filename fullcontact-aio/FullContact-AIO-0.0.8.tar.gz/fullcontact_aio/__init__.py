import logging

import aiohttp

log = logging.getLogger(__name__)


class FullContactLimitReached(Exception):
    pass


class FullContact(object):
    def __init__(self, api_key):
        self.base_url = 'https://api.fullcontact.com/v3/'
        self.headers = {'Authorization': 'Bearer {}'.format(api_key),
                        'Content-Type': 'application/json'}

    async def _api_get(self, endpoint=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, params=kwargs, headers=self.headers) as request:
                if request.status in (200, 403):
                    return await request.json(), request.status, request.headers.get('X-Rate-Limit-Remaining')
                else:
                    request.raise_for_status()

    async def person(self, **kwargs):
        endpoint = self.base_url + 'person.enrich'
        response, status, _rate_limit_remaining = await self._api_get(endpoint=endpoint, **kwargs)
        if status == 403:
            raise FullContactLimitReached(response.get('message'))
        response.update({'X-Rate-Limit-Remaining': _rate_limit_remaining})
        return response

    async def company(self, **kwargs):
        endpoint = self.base_url + 'company.enrich'
        response, status, _rate_limit_remaining = await self._api_get(endpoint=endpoint, **kwargs)
        if status == 403:
            raise FullContactLimitReached(response.get('message'))
        response.update({'X-Rate-Limit-Remaining': _rate_limit_remaining})
        return response
