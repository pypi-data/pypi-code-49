import requests

__version__ = '0.0.1'


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
        response = requests.post(
            url,
            headers=self._get_headers(),
            data={
                'name': name,
                'email': email,
                'password': password
            })
        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()


    def create_client(self, name, redirect_uri, scope):
        url = self._build_url('clients')
        response = requests.post(
            url,
            headers=self._get_headers(),
            data={
                'name': name,
                'redirect_uri': redirect_uri,
                'scope': scope
            })
        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()


    def issue_token(self, code, client_id, client_secret):
        url = self._build_url('token')
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
        if not response.status_code == 200:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()


    def get_public_key(self):
        url = self._build_url('key')
        print(url)
        response = requests.get(
            url,
            headers=self._get_headers())
        if not response.status_code == 200:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()


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
