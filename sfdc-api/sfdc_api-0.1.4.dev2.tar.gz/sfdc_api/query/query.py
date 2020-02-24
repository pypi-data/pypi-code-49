from sfdc_api.utils import Connection
from urllib.parse import urlencode, quote


class Query:
    _CONNECTION = None

    def __init__(self, conn):
        self._CONNECTION = conn

    def query(self, query):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"] + '/services/data/v' + \
                   str(self._CONNECTION.VERSION) + '/query/?q='+quote(query)
        return self._CONNECTION.send_http_request(endpoint, "GET", self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'])
