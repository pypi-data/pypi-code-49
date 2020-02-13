import requests
import warnings
import json
from jepy.jepy_exceptions import *


class JepyClient():
    def __init__(self, **kwargs):
        if ('user_id' and 'password') in kwargs:
            user_id, password = kwargs['user_id'], kwargs['password']
            self.jwt_token = self._authenticate(user_id, password)
        else:
            warning_msg = ("No credentials supplied, the server will automatically"
                           " deny all requests other than checking status. Use"
                           " keyword arguments user_id and password to make other calls.")
            warnings.warn(warning_msg)

    def _handle_response(self, response):
        if response.status_code != 200:
            raise ServerError(''.join(f'{response.status_code}: {response.reason}'))
        else:
            return json.loads((response.content).decode('utf-8'))

    def _call_status(self):
        url = f'https://je-api.com/v0/status.json'
        response = requests.get(url, verify=True)
        try:
            call = self._handle_response(response)
            return call
        except ServerError as e:
            err_str = str(e)
            return {'message': f'Server did not respond appropriately: {err_str}'}

    def _call_api(self, endpoint, **kwargs):
        url = f'https://je-api.com{endpoint}'
        if 'payload' in kwargs:
            payload = kwargs['payload']
            response = requests.post(url, json=payload, verify=True)
            token_dict = self._handle_response(response)
            if 'access_token' in token_dict:
                return token_dict['access_token']
            elif 'error' in token_dict:
                raise TokenError(token_dict['error'][0])
            else:
                raise ServerError(token_dict)
        elif 'headers' in kwargs:
            response = requests.get(url, headers=kwargs['headers'], verify=True)
            return self._handle_response(response)

    def _authenticate(self, user_id, password):
        payload = {'username': user_id,
                   'password': password}
        jwt_token = self._call_api('/auth', payload=payload)
        return jwt_token
