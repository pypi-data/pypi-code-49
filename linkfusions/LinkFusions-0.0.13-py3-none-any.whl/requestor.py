import requests

from .exceptions import BadRequest
from .utils import export_curl


class ApiRequestor:
    def __init__(self, method='POST', endpoint=None, data=None, files=None, token=None, params=None):
        self.token = token
        self.method = method
        self.endpoint = endpoint
        self.data = data
        self.files = files
        self.params = params

    def send(self, as_json=True):
        from LinkFusions import __dev__, get_url
        if not self.data:
            self.data = dict()
        if not self.files:
            self.files = dict()
        if not self.endpoint:
            raise ValueError('No LinkFusions API endpoint provided for request or this method is not '
                             'implemented for this object.')
        url = get_url(self.endpoint)
        method = self.method.lower()
        headers = dict()
        if self.token:
            headers.update({'Authorization': 'Bearer ' + self.token})
        if as_json:
            headers.update({'Content-Type': 'application/json'})
            data_payload = {
                'json': self.data
            }
        else:
            data_payload = {
                'data': self.data
            }
        if method == 'get':
            response = requests.get(url, headers=headers, params=self.params)
        elif method == 'post':
            response = requests.post(url, data=self.data, files=self.files, headers=headers, params=self.params)
        elif method == 'patch':
            response = requests.patch(url, data=self.data, files=self.files, headers=headers, params=self.params)
        elif method == 'put':
            response = requests.put(url, data=self.data, files=self.files, headers=headers, params=self.params)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, params=self.params)
        else:
            raise ValueError('Invalid Method [{}] Provided'.format(method))
        if __dev__:
            export_curl(response)
        if response.status_code == 204:
            return {}
        elif response.status_code in list(range(200, 400)):
            return response.json()
        elif response.status_code == 400:
            raise BadRequest(response.json())
        raise BadRequest(response.text)
