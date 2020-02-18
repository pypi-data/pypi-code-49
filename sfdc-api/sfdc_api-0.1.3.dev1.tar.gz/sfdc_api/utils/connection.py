from urllib import request
from urllib import parse
from urllib.error import HTTPError
import json
import ssl
import xml.etree.ElementTree as ET
from .constants import HEADERS, AuthenticationMode
from .string_utils import camel_to_snake_case

sandbox_login_url = 'https://test.salesforce.com/services/oauth2/token'
production_login_url = 'https://login.salesforce.com/services/oauth2/token'


# Defines the general construct for handling connections to Salesforce
# noinspection PyTypeChecker,PyTypeChecker,PyTypeChecker
# TODO: Session refresh not handled
# TODO: Be able to generate different urls for rest and soap resources; e.g.
# TODO: Create mapper function to create generic authentication details
# TODO: Do global ElementTree namespace registration to avoid editing the allocated namespaces for etrees
class Connection:
    ORG_LOGIN_URL = None
    ORG_PASSWORD = None
    ORG_USERNAME = None
    APP_CLIENT_ID = None
    APP_CLIENT_SECRET = None
    VERSION = None
    CONNECTION_DETAILS = dict()
    CONTEXT = ssl.SSLContext()
    HTTPS_HEADERS = HEADERS.copy()
    TIMEOUT = 20
    AUTH_CONFIG = AuthenticationMode.unauthenticated  # TODO: move this to the Session class

    # TODO: create a class to outsource the handling of different response formats in another class
    login_response = None

    def __init__(self, username='', password='', client_key='', client_secret='', org_login_url='https://login.salesforce.com/', version=47.0):
        self.parse_args(locals())

    def login(self):
        response = None
        if self.AUTH_CONFIG == AuthenticationMode.username_password_soap_flow:
            self.login_by_soap()
            response = self.soap_to_oauth()
        elif self.AUTH_CONFIG == AuthenticationMode.username_password_rest_flow:
            response = self.login_by_oauth2()
        else:
            print('Connection configuration not supported')
        return response

    # TODO: consider moving this into the session object to clean up Connection class
    def parse_args(self, args):
        sanitized_args = {key: value for (key, value) in args.items() if value and key != 'self'}  # Clean empty values
        arg_keys = sanitized_args.keys()
        oauth_args = ['username', 'password', 'client_key', 'client_secret']
        soap_args = ['username', 'password']
        is_oauth = all([i in arg_keys for i in oauth_args])
        is_soap = all([i in arg_keys for i in soap_args]) and not is_oauth  # Only true if oauth doesn't pass
        if 'org_login_url' not in arg_keys:
            raise ValueError('Missing org_login_url ')

        self.ORG_LOGIN_URL = self.validate_url(args['org_login_url'])
        self.VERSION = args['version']
        if is_oauth:
            self.AUTH_CONFIG = AuthenticationMode.username_password_rest_flow
            self.ORG_USERNAME = args['username']
            self.ORG_PASSWORD = args['password']
            self.APP_CLIENT_ID = args['client_key']
            self.APP_CLIENT_SECRET = args['client_secret']
        elif is_soap:
            self.AUTH_CONFIG = AuthenticationMode.username_password_soap_flow
            self.ORG_USERNAME = args['username']
            self.ORG_PASSWORD = args['password']
        else:
            raise ValueError('Unknown authentication config: ' + ','.join(arg_keys))

    # TODO: implement JWT login routine
    """
    #Function: login_by_oauth2(self)
    #   Purpose: This function allows for a user to be logged in to Salesforce
    #       -Logs in using an oauth2 configuration
    #       -Gathers user session information that is used for rest of program execution
    #
    #   -TODO: basically, a lot of stuff
    #       - Error logging
    #       - Error handling
    """

    def login_by_oauth2(self):  # TODO: rename this to reflect username-password login
        # print("Logging into " + self.ORG_LOGIN_URL)
        info = {
            'client_id': self.APP_CLIENT_ID,
            'client_secret': self.APP_CLIENT_SECRET,
            'grant_type': 'password',
            'username': self.ORG_USERNAME,
            'password': self.ORG_PASSWORD,
        }
        body = parse.urlencode(info).encode('utf-8')
        self.CONNECTION_DETAILS = self.send_http_request(self.ORG_LOGIN_URL, 'POST',
                                                         self.HTTPS_HEADERS['oauth_login_headers'],
                                                         body=body)
        self.HTTPS_HEADERS["rest_authorized_headers"]["Authorization"] = "Bearer " + self.login_response["access_token"]
        return self.login_response

    def login_by_soap(self):  # TODO: rename this to reflect username-password login
        body = ''.join([
            '<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">',
            '<se:Header/>',
            '<se:Body>',
            '<login xmlns="urn:partner.soap.sforce.com">',
            '<username>' + self.ORG_USERNAME + '</username>',
            '<password>' + self.ORG_PASSWORD + '</password>',
            '</login>',
            '</se:Body>',
            '</se:Envelope>'
        ]).encode('utf-8')
        # TODO: create login response parser
        soap_url = self.ORG_LOGIN_URL + 'services/Soap/u/47.0'
        self.login_response = self.send_http_request(soap_url,
                                                     'POST',
                                                     self.HTTPS_HEADERS['soap_login_headers'],
                                                     body=body)
        return self.login_response

    # convert session to an oauth one; utilize session id as bearer token
    # TODO: improve conversion; maybe replace with a general function to use in all
    def soap_to_oauth(self):
        root = self.login_response
        # print(root.tag)
        tag = root[0][0][0]
        session_id = tag.find('{urn:partner.soap.sforce.com}sessionId').text
        self.HTTPS_HEADERS['rest_authorized_headers']['Authorization'] = 'Bearer ' + session_id
        instance_url = parse.urlparse(tag.find('{urn:partner.soap.sforce.com}serverUrl').text)
        parsed_url = '{uri.scheme}://{uri.netloc}/'.format(uri=instance_url)
        self.login_response = {'instance_url': parsed_url,
                               'session_id': session_id,
                               'metadata_server_url': tag.find('{urn:partner.soap.sforce.com}metadataServerUrl').text}
        for child in root.iter():
            snake_case_key = camel_to_snake_case(child.tag.replace('{urn:partner.soap.sforce.com}', ''))
            if snake_case_key != 'None':
                self.CONNECTION_DETAILS[snake_case_key] = child.text

        # [print(key) for key in self.CONNECTION_DETAILS.keys()]

        self.CONNECTION_DETAILS['instance_url'] = \
            '{uri.scheme}://{uri.netloc}/'.format(uri=parse.urlparse(self.CONNECTION_DETAILS['server_url']))
        # self.CONNECTION_DETAILS['session_id'] = self.CONNECTION_DETAILS.pop('sessionId')
        return self.CONNECTION_DETAILS

    def logout(self):  # TODO:refactor this for session type
        endpoint = "https://test.salesforce.com/services/oauth2/revoke"
        body = parse.urlencode({"token": self.login_response["access_token"]}).encode('utf-8')
        response = self.send_http_request(endpoint, "POST", body=body,
                                          headers=self.HTTPS_HEADERS['oauth_login_headers'])
        return response

    # TODO: add session renewal routine
    def send_http_request(self, endpoint: str, method: str, headers: dict, body=None):
        req = request.Request(endpoint, data=body, headers=headers, method=method)
        try:
            response = request.urlopen(req, timeout=self.TIMEOUT, context=self.CONTEXT)
            return self.handle_http_response(response)
        except HTTPError as e:
            if 300 <= e.getcode() < 400:
                redirect_url = e.headers['Location']
                return self.send_http_request(endpoint=redirect_url, method=method, headers=headers, body=body)
            raise e

    @staticmethod
    def handle_http_response(response):
        content_type = response.info().get('Content-Type')
        response_body = response.read()
        if len(response_body) == 0:
            return ''
        if 'xml' in content_type:
            return ET.fromstring(response_body)
        elif 'json' in content_type:
            return json.loads(response_body)
        else:
            return response_body

    @staticmethod
    def validate_url(url):
        parse.urlparse(url)  # Just to make sure the URL is valid to begin with
        if not url.endswith('/'):
            return url + '/'  # Ensure we can build
        return url


