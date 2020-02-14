import requests

import imis.activity as activity
import imis.demo as demo
import imis.iqa as iqa
import imis.name_fin as name_fin
import imis.party as party
import imis.record as record
import imis.user as user



class ApiError(Exception):
    pass


class AuthError(ApiError):
    pass


class Auth:

    def __init__(self, access_token, token_type, expires_in, user_name):
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.user_name = user_name

    @property
    def authorization_header(self):
        return '{0} {1}'.format(self.token_type, self.access_token)

    @classmethod
    def authenticate(cls, url, username, password):
        data = {
            'grant_type': 'password',
            'username': username,
            'password': password
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=url, data=data, headers=headers)
        if response.status_code == 400:
            data = response.json()
            raise AuthError(data['error_description'])

        data = response.json()
        return cls(access_token=data['access_token'],
                    token_type=data['token_type'],
                    expires_in=data['expires_in'],
                    user_name=data['userName'])


class Client:

    _authenticator = Auth
    _party_manager = party.Manager

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self._auth = Client._authenticator.authenticate(f'{url}/token', username, password)

    @property
    def auth(self):
        if self._auth is None:
            self._auth = Client._authenticator.authenticate(f'{self.url}/token', self.username, self.password)
        return self._auth

    @auth.setter
    def auth(self, val):
        self._auth = val

    @property
    def party(self):
        return Client._party_manager(client=self)

    def demo(self, object_name):
        return demo.Manager(client=self, object_name=object_name)

    def iqa(self, query_name, *parameters, **kwargs):
        for item in iqa.iter_items(self, query_name, 0, *parameters, **kwargs):
            yield record.BasicRecord(**item)

    def create_activity(self, activity_dict):
        return activity.create(self, activity_dict)

    def create_user(self, username, imis_id):
        return user.create(self, username, imis_id)

    def update_renewed_thru(self, imis_id, renewed_thru):
        name_fin.update_renewed_thru(self, imis_id, renewed_thru)
