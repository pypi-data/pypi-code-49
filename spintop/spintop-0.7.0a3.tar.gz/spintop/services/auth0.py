
import json
import jwt
import requests

from json.decoder import JSONDecodeError

from simple_memory_cache import GLOBAL_CACHE

from ..errors import AuthUnauthorized


class Auth0Provider(object):
    def __init__(self, domain, audience, client_id, jwks_url, user_info_url):
        self.domain = domain
        self.audience = audience
        self.client_id = client_id
        self.jwks_url = jwks_url
        self.user_info_url = user_info_url

        self.cached_jwks = GLOBAL_CACHE.MemoryCachedVar('auth_jwks')
        self.cached_jwks.on_first_access(self._retrieve_jwks)

    def _retrieve_jwks(self):
        return requests.get(self.jwks_url).json()
    
    def get_user_info(self, access_token):
        return requests.get(self.user_info_url, headers={'Authorization': 'Bearer ' + access_token}).json()

    def authenticate(self, username, password, scopes=[]):
        return self._execute_request('/oauth/token',
            grant_type = 'password',
            username = username,
            password = password,
            audience = self.audience,
            client_id = self.client_id,
            scope = 'offline_access ' + ' '.join(scopes) # Special scope to receive a refresh token
        )
    
    def _execute_request(self, url_path, **data):
        URL = 'https://' + self.domain  + url_path
        resp = requests.post(URL, data = data)
        content = self._handle_errors_in_content(resp)
        return content
    
    def _handle_errors_in_content(self, resp):
        try:
            content = resp.json()
        except JSONDecodeError:
            content = {}
            
        if resp.status_code >= 400:
            desc = content.get('error_description', None)
            if desc:
                raise AuthUnauthorized(desc)
            else:
                raise AuthUnauthorized(str(content))
    
        return content
    
    def refresh_access_token(self, refresh_token):
        return self._execute_request('/oauth/token',
            grant_type = 'refresh_token',
            client_id = self.client_id,
            refresh_token = refresh_token
        )

    def revoke_refresh_token(self, refresh_token):
        self._execute_request('/oauth/revoke',
            client_id = self.client_id,
            token = refresh_token
        )
    
    def get_jwks_key(self, access_token):
        jwks = self.cached_jwks.get()
        public_keys = {}
        for jwk in jwks['keys']:
            kid = jwk['kid']
            public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
            
        kid = jwt.get_unverified_header(access_token)['kid']
        key = public_keys[kid]
        return key

    def jwt_verify(self, access_token):
        try:
            payload = self.decode(access_token)
        except jwt.PyJWTError:
            # invalidate jwks cache and try ONCE more.
            self.cached_jwks.invalidate()
            payload = self.decode(access_token)
        return payload
    
    def decode(self, access_token):
        key = self.get_jwks_key(access_token)
        return jwt.decode(access_token, key=key, algorithms=['RS256'], audience=[self.client_id, self.audience])
    

class SpinHubAuthProvider(Auth0Provider):
    def __init__(self):
        domain = "spinhub.auth0.com"
        super(SpinHubAuthProvider, self).__init__(
            domain = domain,
            audience = "https://app.spinhub.ca/api",
            client_id = "fYeWIlWMD99S6eJi86pKN7oa2ll2k7lE",
            jwks_url = 'https://' + domain + '/.well-known/jwks.json',
            user_info_url = 'https://' + domain + '/userinfo'
        )
    
    
