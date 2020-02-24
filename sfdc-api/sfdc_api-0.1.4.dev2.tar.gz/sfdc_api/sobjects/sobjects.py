# from utils import Connection


class Sobjects:
    _CONNECTION = None

    def __init__(self, connection):
        self._CONNECTION = connection

    def global_describe(self):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/sobjects/'
        headers = self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers']
        return self._CONNECTION.send_http_request(endpoint, "GET", headers)
