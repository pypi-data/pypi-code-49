from datetime import datetime

import requests
from requests.exceptions import RequestException
import jwt


class AppStoreConnectException(Exception):
    pass


class AppStoreConnect:
    def __init__(self, key_id: str, issuer_id: str, private_key: bytes) -> None:
        self.key_id = key_id
        self.issuer_id = issuer_id
        self.private_key = private_key
        self.headers = {
            'alg': 'ES256',
            'kid': self.key_id,
            'typ': 'JWT'
        }
        self.base_url = 'https://api.appstoreconnect.apple.com/v1'

    def _prep_headers(self):
        payload = {
            'iss': self.issuer_id,
            'exp': int(datetime.now().strftime("%s")) + 60 * 5,
            'aud': 'appstoreconnect-v1'
        }
        token = jwt.encode(payload, self.private_key, algorithm='ES256', headers=self.headers)
        return {'Authorization': 'Bearer %s' % token.decode('utf-8')}

    def add_device(self, udid, name):
        url = '{}/devices'.format(self.base_url)
        data = {
            'data': {
                'type': 'devices',
                'attributes': {
                    'name': name,
                    'udid': udid,
                    'platform': 'IOS'
                }
            }
        }
        req = requests.post(url, headers=self._prep_headers(), json=data)
        if req.status_code != 201:
            raise AppStoreConnectException(req.status_code)

    def list_devices(self):
        url = '{}/devices'.format(self.base_url)
        req = requests.get(url, headers=self._prep_headers())
        print(req.status_code)
        print(req.json())

    def get_device_info(self, dev_id):
        url = '{}/devices/{}'.format(self.base_url, dev_id)
        req = requests.get(url, headers=self._prep_headers())
        print(req.text)

    def apps(self):
        url = '{}/apps'.format(self.base_url)
        print(url)
        print(self._prep_headers())
        try:
            req = requests.get(url, headers=self._prep_headers())
            if req.status_code != 200:

                raise AppStoreConnectException
        except RequestException as e:
            raise AppStoreConnectException(e)


if __name__ == '__main__':
    pass
