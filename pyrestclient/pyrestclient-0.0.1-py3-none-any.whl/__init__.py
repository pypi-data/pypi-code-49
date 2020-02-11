import json
from http import HTTPStatus
from urllib.parse import urljoin

import requests
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings, exceptions

from .logger import logger

disable_warnings(exceptions.InsecureRequestWarning)


def json_data(data):
    return json.dumps(data)


def get_header_default(user_agent='ide', content_type='application/json-patch+json', accept='application/json'):
    return {
        'User-Agent': user_agent,
        'Content-Type': content_type,
        'Accept': accept,
        # 'UserAgentInternal': 'webfrontend/1.0'
    }


class Authorization:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def auth_type(self):
        return self.__class__.__name__


class AuthBasic(Authorization):
    """Basic authorization class"""

    def get_base_auth(self):
        return HTTPBasicAuth(self.username, self.password)


class AuthToken(Authorization):
    """Class to get auth token"""

    def __init__(self, client):
        super().__init__(client.username, client.password)
        self.client = client

    @property
    def auth_url(self):
        """Get full authorization URL"""
        return f'{self.client.base_url}/{self.client.auth_uri}'

    @property
    def token(self):
        if self.client.is_service_available:
            try:
                response = requests.post(self.auth_url, json=self.client.auth_payload, verify=False, timeout=7)
                return response.json()['token']
            except json.decoder.JSONDecodeError as err:
                logger.error(err)
                return 'Cannot get token property: {}'.format(err)
            except TypeError as err:
                logger.error(err)
                return 'Endpoint is available but "token" key cannot be retrieved.\n' \
                       'Check credentials.\n{}'.format(err)
        else:
            return f'Host {self.client.host} is unreachable. Check service status'


class RESTClient:
    """ Main class for RestAPI """

    def __init__(self,
                 username: str,
                 password: str,
                 protocol: str,
                 host: str,
                 port: int,
                 base_url: str = '',
                 header: str = '',
                 auth_basic: bool = False,
                 auth_uri: str = '',
                 auth_payload: dict = dict,
                 token: str = '',
                 logger_enabled: bool = False):

        # Enable/disable logger
        logger.disabled = not logger_enabled

        # Credentials and settings for api url
        self.username = username
        self.password = password
        self.protocol = protocol or 'https'  # HTTP or HTTPS
        self.host = host
        self.port = port or 80
        self.auth_uri = auth_uri
        self.auth_payload = auth_payload
        self.token = token

        # Default URLs
        self.base_url = base_url or f'{self.protocol}://{self.host}:{self.port}'

        self.header = header or get_header_default()

        # Create auth header
        self.auth_basic = None
        if self.token:
            self.header['Authorization'] = self.token
        elif auth_payload:
            self.auth = AuthToken(self)  # Redeclare self.auth for future usage
            try:
                self.header['Authorization'] = self.auth.token
            except KeyError as err:
                logger.error(f'Cannot get token. {err}')

        # Specify Basic Authorization if enabled
        elif auth_basic:
            self.auth = AuthBasic(username=self.username, password=self.password)
            self.auth_basic = self.auth.get_base_auth()
            self.header = {}
        else:
            self.header = {}

    def __str__(self):

        return f'Object class: {self.__class__.__name__}\n' \
               f'Username: {self.username}\n' \
               f'Password: {self.password}\n' \
               f'Base URL: {self.base_url}\n' \
               f'Authorization: {self.auth.auth_type}\n' \
               f'Token: {self.header["Authorization"]}\n'

    def send_request(self,
                     method: str,
                     url: str = '',
                     full_url: str = '',
                     query_params=None,
                     data=None, files=None,
                     verify=False,
                     extended_header: bool = False,
                     custom_header=None,
                     cookies=None,
                     _request_timeout=None):

        """
        Send common request

        :param cookies:
        :param method: GET, POST, DELETE
        :param url: unified identificator, self.url (BASE) + url
        :param full_url: = Specified full URL
        :param query_params: = Query parameters in the url
        :param data: jsoned data
        :param files: "files: {'licenseFile': (License.name, f)}"
        with open(files, 'rb') as f:
             files = {'licenseFile': (License.name, f)}
        :param verify: Bool
        :param extended_header: Add 'UserAgentInternal': 'webfrontend/1.0' to the header
        :param custom_header: Use specified header
        :param _request_timeout: Time in sec.
        :return: requests.request('POST', url=url, headers=HEADER, files=files, verify=False)

        """

        # Make full url to use in request
        if url and full_url:
            logger.error('"url" and "full_url" parameters cannot be used simultaneously.')
            raise ValueError('"url" and "full_url" parameters cannot be used simultaneously.')

        link = urljoin(self.base_url, url)
        if full_url:
            link = full_url

        method = method.upper()

        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS'], \
            'Specified methods is not compatible.'

        if data and files:
            logger.error('Data parameter cannot be used with files parameter simultaneously.')
            raise ValueError('Data parameter cannot be used with files parameter simultaneously.')

        # Extend header
        if 'Content-Type' not in self.header:
            self.header['Content-Type'] = 'application/json'

        header_ext = None
        if extended_header:
            header_ext = self.header.copy()
            header_ext['UserAgentInternal'] = 'webfrontend/1.0'

        response = 'Invalid requests. Check parameters'

        try:
            # For 'POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE'
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if data and not files:

                    response = requests.request(method=method,
                                                url=link,
                                                auth=self.auth_basic,
                                                headers=self.header,
                                                json=data,
                                                cookies=cookies,
                                                verify=verify,
                                                timeout=_request_timeout)

                    logger.info(f'{method} ' + link)
                    logger.info('PAYLOAD:\n' + json.dumps(data, indent=4))

                elif files:
                    files_header = self.header.copy()
                    del files_header['Content-Type']
                    if custom_header:
                        files_header = custom_header

                    response = requests.request(method=method,
                                                url=link,
                                                auth=self.auth_basic,
                                                headers=files_header,
                                                cookies=cookies,
                                                files=files,
                                                verify=verify,
                                                timeout=_request_timeout)

                    logger.info(f'{method} ' + link)
                    logger.info('PAYLOAD:\n' + json.dumps(data, indent=4))

                elif not files and not data:
                    response = requests.request(method=method,
                                                url=link,
                                                auth=self.auth_basic,
                                                headers=self.header,
                                                cookies=cookies,
                                                verify=verify,
                                                timeout=_request_timeout)

                    logger.info(f'{method} ' + link)
                    logger.info('PAYLOAD:\n' + json.dumps(data, indent=4))

            # For 'GET', 'HEAD' request
            else:
                # For GET with query
                # Add params to requested link
                if query_params:
                    link += '?'
                    params = ''

                    for key, value in query_params.items():
                        if len(params):
                            params += '&'
                        params += str(key) + '=' + str(value)
                    link += params

                # For usual 'GET' without query params
                header = self.header
                if extended_header:  # replace default header with extended one
                    header = header_ext
                elif custom_header:
                    header = custom_header

                logger.info(f'{method} ' + link)

                response = requests.request(method=method,
                                            url=link,
                                            auth=self.auth_basic,
                                            cookies=cookies,
                                            headers=header,
                                            verify=verify,
                                            timeout=_request_timeout)

        except BaseException as err:
            logger.error(err)
            raise err

        return response

    # noinspection PyPep8Naming
    def _GET(self,
             url='',
             full_url='',
             query_params=None,
             extend_header=False,
             cookies=None,
             _request_timeout=None):
        assert any((url, full_url)), 'Provide "URL" or "FULL_URL" parameter.'

        if full_url:
            return self.send_request(
                'GET', full_url=full_url,
                query_params=query_params,
                extended_header=extend_header,
                cookies=cookies,
                _request_timeout=_request_timeout
            )
        return self.send_request(
            'GET', url=url,
            query_params=query_params,
            extended_header=extend_header,
            cookies=cookies,
            _request_timeout=_request_timeout
        )

    # noinspection PyPep8Naming
    def _PUT(self,
             url='',
             full_url='',
             extend_header=False,
             custom_header=None,
             files='',
             _request_timeout=None,
             verify=False):

        header = self.header.copy()

        if files:
            del header['Content-Type']

        if custom_header:
            header = custom_header
        elif extend_header:
            header = extend_header

        if full_url:
            response = self.send_request(
                method='PUT',
                full_url=full_url,
                custom_header=header,
                files=files,
                verify=verify
            )

            return response

        response = requests.request(
            method='PUT',
            url=url,
            auth=self.auth_basic,
            headers=header,
            data=files,
            verify=verify,
            timeout=_request_timeout
        )
        return response

    # noinspection PyPep8Naming
    def _POST(self,
              url='',
              full_url='',
              extend_header=False,
              custom_header=None,
              data='',
              files='',
              _request_timeout=None,
              verify=False):

        header = self.header.copy()

        if custom_header:
            header = custom_header
        elif extend_header:
            header = extend_header

        link = self.base_url + url
        if full_url:
            link = full_url

        if data and not files:

            logger.info(f'POST: ' + link)
            logger.info('PAYLOAD:\n' + json.dumps(data, indent=4))

            return requests.request(
                method='POST',
                url=link,
                auth=self.auth_basic,
                headers=header,
                json=data,
                verify=verify
            )

        elif files:
            del header['Content-Type']
            if custom_header:
                header = custom_header

            logger.info(f'POST: ' + link)
            logger.info('PAYLOAD:\n' + json.dumps(data, indent=4))

            return requests.request(
                method='POST',
                url=link,
                auth=self.auth_basic,
                headers=header,
                files=files,
                verify=verify
            )

        elif not files and not data:

            logger.info(f'POST: ' + link)
            logger.info('PAYLOAD:\n' + json.dumps(data, indent=4))

            return requests.request(
                method='POST',
                url=link,
                auth=self.auth_basic,
                headers=header,
                verify=verify
            )

    @property
    def is_service_available(self):
        """Check base url availability within 30 sec."""

        try:
            response = requests.get(self.base_url, timeout=10, verify=False)
            if response.status_code == 200:
                return True
        except requests.exceptions.Timeout:
            return False
        except requests.exceptions.ConnectionError:
            return False

    def download(self, url, dst):
        """Download file.

        :param url: Full url to file
        :param dst: path to store
        :return:
        """

        response = self.send_request('GET', full_url=url)
        try:
            if response.ok:
                with open(dst, 'wb') as f:
                    f.write(response.content)
                    return True
            else:
                return False
        except (ConnectionError, ConnectionRefusedError) as err:
            logger.error(f'Download failed. {err}')
            return err


class RESTAssertion:
    """Parse requests response to get status code."""

    @staticmethod
    def should_be_success_response_code(response):
        """200 <= status_code < 400"""
        assert response.ok, 'Response code is not success.'

    @staticmethod
    def should_be_ok_response_code(response):
        """OK, 200. Request fulfilled, document follows"""
        assert response.status_code == HTTPStatus.OK, 'Response code is not 200.'

    @staticmethod
    def should_be_not_found_response_code(response):
        """Nothing matches the given URI"""
        assert response.status_code == HTTPStatus.NOT_FOUND, 'Response code is not 404.'

    @staticmethod
    def should_be_bad_request(response):
        """Bad request syntax or unsupported method"""
        assert response.status_code == HTTPStatus.BAD_REQUEST, 'Response code is not 404.'
