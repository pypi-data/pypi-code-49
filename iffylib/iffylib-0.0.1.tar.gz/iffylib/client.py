import math
from iffylib import schema
import requests
import time


class GiphyAPIClientError(Exception):
    pass

class APICLient(object):
    def __init__(self, apikey):
        self.apikey = apikey

    def _param_prep(self, **params):
        # Remove params set to None, inject apikey
        final_params = dict()
        for k in params.keys():
            if params[k] is None:
                continue
            final_params[k] = params[k]
        final_params['api_key'] = self.apikey
        return final_params

    def search(
            self, query,
            limit=None, offset=None, rating=None, lang=None, random_id=None):

        params = self._param_prep(
            q=query, limit=limit, offset=offset, rating=rating, lang=lang,
            random_id=random_id)

        return requests.get(
            "http://api.giphy.com/v1/gifs/search",
            params=params)

    def get(self, gif_id, random_id=None):
        params = self._param_prep(random_id=random_id)

        return requests.get(
            "http://api.giphy.com/v1/gifs/{gid}".format(gid=gif_id),
            params=params)


class Giphy(object):
    def __init__(self, apikey):
        self.apikey = apikey
        self.api = APICLient(apikey)

    def search(
            self, query, limit=25, offset=0, rating="g", lang="en",
            random_id=None):

        r = self.api.search(
            query, limit=limit, offset=offset, rating=rating, lang=lang,
            random_id=random_id)

        return schema.SearchResponse(r.json())

    def autopaging_search(
            self, query, limit=25, offset=0, rating="g", lang="en",
            random_id=None, yield_cooldown=.1):

        '''
        Returns a generator that yields complete results, paging through
        subsequent calls as necessary
        '''

        r = self.api.search(
            query, limit=limit, offset=offset, rating=rating, lang=lang,
            random_id=random_id)

        data = schema.SearchResponse(r.json())

        total_iterations = math.ceil(data.pagination.total_count / limit)
        for i in range(total_iterations):
            yield data
            time.sleep(yield_cooldown)
            current_start += limit
            r = self.api.search(
                query, limit=limit, offset=offset, rating=rating, lang=lang,
                randomid=randomid)
            data = schema.SearchResponse(r.json())

    def get(self, gif_id, random_id=None):
        r = self.api.get(gif_id, random_id=random_id)
        return schema.GetResponse(r.json())
