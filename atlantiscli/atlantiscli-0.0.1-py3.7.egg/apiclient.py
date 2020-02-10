import requests
import yaml

__version__ = '0.0.1'


class ApiClient(object):

    def __init__(self, url, version='api'):

        if not url:
            raise RuntimeError('ATLANTIS_URL environment variable not set')

        self.atlantis_url = url
        self.api_version = version
        self.session = requests.Session()
        # login salvando token

    def create_user(self, user):
        url = self._build_url('users')
        response = requests.post(
            url,
            headers=self._get_headers(),
            data=user.encode('utf-8'))
        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()

    def create_client(self, client):
        url = self._build_url('clients')
        response = requests.post(
            url,
            headers=self._get_headers(),
            data=client.encode('utf-8'))
        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()

    def _get_headers(self, content_type='application/x-yaml'):
        headers = {
            'User-Agent': 'atlantiscli/{}'.format(__version__),
            'Content-Type': content_type,
        }
        # token = getattr(self, 'token', None)
        # if token:
        #     headers['Authorization'] = token
        return headers

    def _build_url(self, endpoint):
        return '/'.join([self.atlantis_url, self.api_version, endpoint])


class ApiError(RuntimeError):

    def __init__(self, response):
        message = 'status={} data={}'.format(
            response.status_code, response.json())
        super(ApiError, self).__init__(message)
