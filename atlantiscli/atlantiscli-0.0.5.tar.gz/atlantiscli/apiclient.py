import requests

__version__ = '0.0.2'


class ApiClient(object):

    def __init__(self, url, version='api'):

        if not url:
            raise RuntimeError('ATLANTIS_URL environment variable not set')

        self.atlantis_url = url
        self.api_version = version
        self.session = requests.Session()
        # login salvando token

    def create_user(self, name, email, password):
        url = self._build_url('users')
        try:
            response = requests.post(
                url,
                headers=self._get_headers(),
                data={
                    'name': name,
                    'email': email,
                    'password': password
                })
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e

    def create_client(self, name, redirect_uri, scope):
        url = self._build_url('clients')
        try:
            response = requests.post(
                url,
                headers=self._get_headers(),
                data={
                    'name': name,
                    'redirect_uri': redirect_uri,
                    'scope': scope
                })
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e

    def issue_token(self, code, client_id, client_secret):
        url = self._build_url('token')
        try:
            response = requests.post(
                url,
                headers=self._get_headers(),
                data={
                    'code': code,
                    'client_id': client_id,
                    'client_secret': client_secret
                },
                params={
                    'grant_type': 'authorization_code'
                })
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e

    def get_public_key(self):
        url = self._build_url('key')
        try:
            response = requests.get(
                url,
                headers=self._get_headers())
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e

    def _get_headers(self):
        headers = {
            'User-Agent': 'atlantiscli/{}'.format(__version__),
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
