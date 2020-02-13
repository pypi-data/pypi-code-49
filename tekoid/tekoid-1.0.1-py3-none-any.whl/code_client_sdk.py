import jwt
import json
import random
import string
import urllib
from urllib.parse import urlparse, parse_qs
from .base_client_sdk import BaseClientSDK
import base64


class CodeClientSDK(BaseClientSDK):
    def __init__(self, client_id, client_secret, redirect_uri, **kwargs):
        super().__init__(client_id, client_secret, **kwargs)

        self.redirect_uri = redirect_uri
        self.__get_public_keys()

    def __get_public_keys(self):
        jwks = self.client.get(self.base_uri + self.jwks_path).json()
        public_keys = {}
        for jwk in jwks.get('keys'):
            kid = jwk['kid']
            public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(
                json.dumps(jwk))

        self.public_keys = public_keys

    def __random_string(self, len=50):
        pattern = ''.join(
            (string.ascii_uppercase, string.ascii_lowercase, string.digits))
        return ''.join(random.choice(pattern) for _ in range(len))

    def get_authorization_url(self):
        base_uri = self.base_uri
        authorize_path = self.authorize_path
        state = self.__random_string()

        query = urllib.parse.urlencode({
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": ' '.join(self.scope),
            "state": state,
            "nonce": self.__random_string()
        })

        authorization_url = f'{base_uri}{authorize_path}?{query}'
        return authorization_url, state

    def get_token(self, url, state):
        params = parse_qs(urlparse(url).query)
        req_state = params['state'][0]
        code = params['code'][0]
        if (state != req_state):
            raise Exception("invalid state")

        redirect_uri = self.redirect_uri

        body = {
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
            "code": code
        }

        res = self.client.post(self.base_uri + self.token_path,
                               data=body, auth=(self.client_id, self.client_secret))
        return res.json(), res.status_code

    def __decode_token(self, token):
        kid = jwt.get_unverified_header(token).get('kid')
        aud = jwt.decode(token, verify=False, algorithms=[
            'RSA256']).get('aud')
        pubkey = self.public_keys.get(kid)
        payload = jwt.decode(token, key=pubkey, algorithms=[
            "RS256"], audience=aud)
        return payload

    def get_user_info(self, token):
        return self.__decode_token(token)

    def refresh_token(self, refresh_token):

        body = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        res = self.client.post(self.base_uri + self.refresh_token_path,
                               data=body, auth=(self.client_id, self.client_secret))

        return res.json(), res.status_code
