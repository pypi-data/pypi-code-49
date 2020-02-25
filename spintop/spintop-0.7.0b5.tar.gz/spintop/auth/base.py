import click
import requests

from pprint import pprint

from ..errors import SpintopException, AuthUnauthorized, ExpiredAccessToken
from .schemas import credentials_schema

class AuthException(SpintopException):
    pass

REFRESH_MODULE = 'user'

class AuthModule(object):
    scopes = ['openid', 'email', 'profile', 'authorization']
    def __init__(self, auth_provider=None, config=None):
        self.auth_provider = auth_provider
        self.config = config
        
        self._reset_credentials()

    @property
    def credentials(self):
        self._init_check()
        return self._credentials
    
    @credentials.setter
    def credentials(self, value):
        self._credentials = value
    
    @property
    def user_orgs(self):
        access_token = self.credentials.get('access_token', None)
        if access_token:
            return self.attempt_op_with_refresh(lambda: self.auth_provider.get_user_orgs(access_token))
        else:
            return []

    def _reset_credentials(self):
        self._credentials = None
        self._initialized = False

    def _init_check(self):
        if not self._initialized and not self._credentials:
            self.credentials = self.config.get_credentials()
            # Other init stuff should go here
            self._initialized = True
    
    def assert_credentials(self):
        if not self.credentials:
            raise AuthException("No credentials available. Please login.")
    
    def assert_no_login(self):
        if self.credentials:
            raise AuthException("""
You already have credentials stored for %s. \
Spintop currently only support a single user per PC. \
Please logout before logging back in.
""" % self.credentials['username'])

    def login_user_pass(self, username, password, scopes=[]):
        self.assert_no_login()
        content = self.auth_provider.authenticate(username, password, scopes=self.scopes)
        self._save_access_token(content, username=username)

    def _save_access_token(self, content, username):
        self.credentials = credentials_schema.load({
            'username': username,
            'access_token': content.get('access_token'),
            'refresh_token': content.get('refresh_token'),
            'org_id': None,
            'refresh_module': REFRESH_MODULE
        })
        self.save_credentials()
        
    @property
    def credentials_key(self):
        
        key = self.credentials.get('username', None)
            
        if key is None:
            key = self.credentials.get('org_id', None)
            
        return key
        
    def save_credentials(self):
        self.config.set_credentials(self.credentials_key, self.credentials)
        self.config.save()
    
    def attempt_op_with_refresh(self, op):
        try:
            return op()
        except ExpiredAccessToken:
            self.refresh_credentials()
            return op()

    def refresh_credentials(self):
        try:
            self.credentials = self._refresh_credentials_obj(self.credentials)
        except AuthUnauthorized:
            raise AuthException('Unable to refresh credentials.')
        self.save_credentials()
        
    def logout(self):
        # Add SpinHub-related logout stuff
        if self.credentials:
            self.auth_provider.revoke_refresh_token(self.credentials['refresh_token'])
            
        self.config.remove_credentials(self.credentials_key)
        self.config.save()
        self._reset_credentials()
    
    def _refresh_credentials_obj(self, credentials):
        # username and refresh_token both stay valid
        if credentials is None:
            raise AuthUnauthorized()
            
        self._assert_refresh_token_exists(credentials)
        
        username = credentials['username']
        refresh_token = credentials['refresh_token']
        
        content = self.auth_provider.refresh_access_token(refresh_token)
        
        return credentials_schema.load({
            'username': username,
            'refresh_token': refresh_token,
            'access_token': content.get('access_token'),
            'org_id': None,
            'refresh_module': REFRESH_MODULE
        })

    def _assert_refresh_token_exists(self, credentials):
        if not credentials or not credentials['refresh_token']:
            raise AuthUnauthorized('No refresh token exists; unable to execute operation')
        
    def get_auth_headers(self):
        if self.credentials:
            return {
                'Authorization': 'Bearer ' + self.credentials.get('access_token')
            }
        else:
            return {}
        
    
