import requests
import json
import re
from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode
from .const import *


class Client:
    """
    Provides access to the StreamSQL client environment.
    Has methods to ingest data and retrieve table results
    """
    def __init__(self, apikey, host):
        self.apikey = apikey
        self.host = host

    def put(self, stream, msg):
        """
        Appends a message to the given data stream
        :param stream:
        Name of the stream to append to
        :param msg:
        A dict() containing the message
        :return:
        None
        """
        self._validate()

        url = "{host}{path}".format(host=self.host, path=INGEST_SINGLE)

        data = self._generate_single(msg, stream)
        headers = {'X-StreamSQL-Key': self.apikey}

        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        if r.status_code >= 400:
            raise ValueError(r.text)

    def _validate(self):
        # Check that apikey UUID is correct format
        if not re.match(RE_API_KEY, self.apikey):
            raise ValueError("Invalid Apikey")

    def lookup(self, table, key=None):
        """
        Returns entire lookup table, or key from lookup table
        :param table:
        Name of lookup table to retrieve from
        :param key:
        (optional) returns specific key in lookup table if provided
        :return:
        dict() of lookup table key: value pairs
        """

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
        if r.status_code >= 400:
            raise ValueError(r.text)
        return json.loads(r.text)

    def read(self, stream, num=100):
        """
        Returns a set number of results from a given stream
        :param stream:
        Stream name
        :param num:
        Number of result to return
        :return:
        Array of stream values
        """
        pass

    def _generate_single(self, data, stream):
        # Need some validation up in here
        payload = dict()
        payload["data"] = data
        payload["stream"] = stream
        return payload
