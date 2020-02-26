import requests
from requests.exceptions import Timeout


class Client(requests.Session):
    def __init__(self, verify_ssl):
        super().__init__()
        self.verify_ssl = verify_ssl

    def request(self, method, url, *args, **kwargs):
        try:
            res = super().request(method, url, verify=self.verify_ssl, *args, **kwargs)
        except Timeout:
            raise Exception(f'Timeout when {method} data to {url}')
        except Exception:
            raise Exception(f'Exception when {method} data to {url}')

        return res
