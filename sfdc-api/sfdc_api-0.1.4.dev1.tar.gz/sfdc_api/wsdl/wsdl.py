from urllib import request
from ..utils import Connection
from http.cookies import SimpleCookie


class WSDL:
    _CONNECTION: Connection = None
    ORG_URL = None
    SESSION_ID = None

    def __init__(self, connection: Connection):
        self._CONNECTION = connection
        self.ORG_URL = connection.ORG_LOGIN_URL
        self.SESSION_ID = connection.CONNECTION_DETAILS['session_id']

    def get_metadata_wsdl(self):
        url = self.ORG_URL + 'services/wsdl/metadata'
        req = self.create_wsdl_request(url)
        response = request.urlopen(req)
        return self._CONNECTION.handle_http_response(response)

    def get_tooling_wsdl(self):
        url = self.ORG_URL + 'services/wsdl/tooling'
        req = self.create_wsdl_request(url)
        response = request.urlopen(req)
        return self._CONNECTION.handle_http_response(response)

    # TODO: Confirm that this works within a rest session
    def create_wsdl_request(self, wsdl_url):
        sid_cookie = SimpleCookie()
        sid_cookie['sid'] = self.SESSION_ID
        sid_header = sid_cookie.output(header='')
        headers = {'content-type': 'text/xml', 'Cookie': sid_header}
        req = request.Request(url=wsdl_url, method='GET', headers=headers)
        return req
