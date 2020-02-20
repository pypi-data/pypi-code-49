import requests
import json
import re
from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode
from .const import *



class Client:
    def __init__(self, apikey, host):
        self.apikey = apikey
        self.host = host

    def put(self, stream, msg):
        self._validate()

        url = "{host}{path}".format(host=self.host, path=INGEST_SINGLE)

        data = self._generate_single(msg, stream)
        print(data)
        headers = {'X-StreamSQL-Key': self.apikey}

        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(r.text)

    def _validate(self):
        # Check that apikey UUID is correct format
        if not re.match(RE_API_KEY, self.apikey):
            raise ValueError("Invalid Apikey")

    def lookup(self, table, key=None):

        url = "{host}{path}".format(host=self.host, path=GET_TABLE)
        headers = {'X-StreamSQL-Key': self.apikey}

        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)

        query_params['table'] = [table]
        if key:
            query_params['key'] = [key]

        new_query_string = urlencode(query_params, doseq=True)
        url = urlunsplit((scheme, netloc, path, new_query_string, fragment))

        r = requests.get(url=url, headers=headers)
        print(r.text)
        return r.text

    def read(self, stream, num=100):
        pass

    def _generate_single(self, data, stream):
        # Need some validation up in here
        payload = dict()
        payload["data"] = data
        payload["stream"] = stream
        return payload
