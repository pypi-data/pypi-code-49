import json
import os
from urllib.parse import urlencode

import requests

from .helpers import get_million_timestamp, generate_random_str, get_b64md5, sign


class HttpClientBase(object):
    def __init__(self, app_id=None, key_id=None, private_key=None, public_key=None):
        params = {
            "_app_id": app_id,
            "_key_id": key_id,
            "_private_key": private_key,
            "_public_key": public_key,
        }
        self._set_attr(params)

    def _set_attr(self, params):
        for key in params:
            value = params[key]
            if not value:
                key_str = key[1:]
                value = os.environ.get(key_str)
                if key_str == 'public_key' and not value:
                    continue
                if not value:
                    raise Exception('invalid params', key_str)
            setattr(self, key, value)

    def _http_get(self, url, query_dict=None, proxies=None):
        set_auth_header = self.__set_auth_header(dict_param=query_dict)

        headers = {}
        headers.update(set_auth_header)

        try:
            req = requests.session()
            req.proxies = proxies
            req.keep_alive = False
            response = req.get(url,
                               params=query_dict,
                               headers=headers,
                               timeout=5)

            if response.status_code in [200, 401]:
                reply = response.json()
                return reply, True

        except Exception as e:
            print(e)
        return {}, False

    def _http_post(self, url, body_dict=None, proxies=None):
        add_to_headers = self.__set_header('POST', json.dumps(body_dict))

        headers = {"Content-Type": "application/raw"}

        headers.update(add_to_headers)

        try:
            req = requests.session()
            req.proxies = proxies
            req.keep_alive = False
            response = req.post(url,
                                data=json.dumps(body_dict),
                                headers=headers,
                                timeout=5)
            if response.status_code in [200, 401]:
                reply = response.json()
                return reply, True

        except Exception as e:
            print(e)
        return {}, False

    def __set_auth_header(self, verb='GET', dict_param=None):
        encode_params = ''
        if dict_param:
            sorted_dict = sorted(dict_param.items(), key=lambda d: d[0])
            encode_params = urlencode(sorted_dict).replace("+", "%20").replace("*", "%2A").replace("%7E", "~")
        add_to_headers = self.__set_header(verb=verb, source_content=encode_params)
        return add_to_headers

    def __set_header(self, verb, source_content=''):
        timestamp_str = get_million_timestamp()
        nonce = generate_random_str()

        b64md5 = get_b64md5(source_content)

        sign_str = verb + '\n' \
                   + str(timestamp_str) + '\n' \
                   + self._app_id + '\n' \
                   + nonce + '\n' \
                   + b64md5

        signature = sign(self._private_key, sign_str)

        auth = 'SHA256-RSA {}:{}'.format(self._key_id, signature)
        header = self._init_header(timestamp_str, nonce)
        header['Authorization'] = auth
        return header

    def _init_header(self, timestamp_str, nonce):
        header_dict = {
            'X-Request-Timestamp': str(timestamp_str),
            'X-Request-AppId': self._app_id,
            'X-Request-Nonce': str(nonce)
        }
        return header_dict
