""" This file exposes endpoints from the SWS Identity Service
"""
import datetime

from requests.auth import HTTPBasicAuth

from sws_py_sdk.service import Service

class Identity(Service):

    def __init__(self, sws):
        super().__init__(sws)
        self.service_uri = sws.service_uris['id']

    def token_refresh(self, refresh_token):
        """ Endpoint for refreshing access tokens
            refresh_token : string
                Refresh token for user that proves they deserve a new access token.
        """
        return self.fetch(
            auth=None,
            endpoint='/api/v1/tokens/refresh',
            body={'refresh_token': refresh_token},
            method='POST'
        )

    def token_exchange(self, grant_type, code, redirect_uri):
        """ POST exchange an authorization code for access and refresh tokens via /tokens/exchange endpoint
            grant_type : str
                authorization_code
            code : str
                Authorization code
            redirect_uri : str
                The redirect URI supplied when the authorization code was issued
        """
        endpoint = '/api/v1/tokens/exchange'
        return self.fetch(
            auth=HTTPBasicAuth(username=self.sws.app_id, password=self.sws.secret),
            endpoint=endpoint,
            body={
                'grant_type': grant_type,
                'code': code,
                'redirect_uri': redirect_uri
            },
            method='POST'
        )

    def login(self, email_address, password, device_id='', device_name=''):
        """ Logs user in with Basic auth
            email_address : str
                User's email address
            password : str
                User's password
            device_id : str
                Some identifier of the machine
            device_name : str
                Human readable name of machine
        """
        return self.fetch(
            auth=HTTPBasicAuth(username=self.sws.app_id, password=self.sws.secret),
            endpoint='/api/v1/login',
            body={
                'email_address': email_address,
                'password': password,
                'device_id': device_id,
                'device_name': device_name
            },
            method='POST'
        )

    def logout(self, refresh_token='', refresh_token_ids=''):
        """ Logs user out via /me/logout endpoint
            refresh_token : string
                Refresh token for user that proves they deserve a new access token.
            refresh_token_ids : string
                A comma separated list of refresh token IDs.
        """
        endpoint = '/api/v1/me' if self.sws.user_id == 0 else '/api/v1/users/' + str(self.sws.user_id)
        endpoint += '/logout'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={ "refresh_token": refresh_token, "refresh_token_ids": refresh_token_ids },
            method='POST',
        )

    
    def post_users(self, email_address, password, first_name=None, last_name=None, locale=None):
        """ Creates user via the /users endpoint
            email_address : str
                User's email address
            password : str
                User's password
            timestamp : datetime
                The time now, in ISO 8601 format
            first_name : str
                User's first name
            last_name : str
                User's last name
            locale : str
                Either the two letter ISO 639-1 language code,
                or the language code followed by an underscore,
                then the ISO 3166-1 alpha-2 country code.
        """
        return self.fetch(
            auth=HTTPBasicAuth(username=self.sws.app_id,
                               password=self.sws.secret),
            endpoint='/api/v1/users',
            body={
                'email_address': email_address,
                'password': password,
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'first_name': first_name,
                'last_name': last_name,
                'locale': locale
            },
            method='POST'
        )

    def post_groups(self, group_name):
        """ Adds the authenticated client user to a user group
            group_name : str
                User group name
        """
        endpoint = '/api/v1/me' if self.sws.user_id == 0 else '/api/v1/users/' + str(self.sws.user_id)
        endpoint += '/groups'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={
                "group_name": group_name
            },
            method='POST'
        )

    def get_user(self):
        """ Get user detail via /api/v1/me, /api/v1/users/{user_id} endpoint
        """
        endpoint = '/api/v1/me' if self.sws.user_id == 0 else '/api/v1/users/'+ str(self.sws.user_id)
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={},
            method='GET'
        )

    def get_users(self, email_address='', ga_client_id='', app_session_cookie=''):
        """ Get list of users via /api/v1/users endpoint
            email_address : str
                User's email address
            ga_client_id : str
                Google Client ID
            app_session_cookie : str    
                application session cookie value        
        """
        endpoint = '/api/v1/users'
        return self.fetch(
            auth=HTTPBasicAuth(username=self.sws.app_id, password=self.sws.secret),
            endpoint=endpoint,
            body={
                'email_address': email_address
            },
            method='GET'
        )

    def delete_user(self):
        """ DELETE  create user deactivation request.
        """
        endpoint = '/api/v1/me' 
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={},
            method='DELETE'
        )

    def reset_password(self, email_address):
        """ POST reset user password via /sendresetpassword endpoint
            email_address : str
                User's email address
        """
        endpoint = '/api/v1/sendresetpassword'
        return self.fetch(
            auth=HTTPBasicAuth(username=self.sws.app_id, password=self.sws.secret),
            endpoint=endpoint,
            body={
                'email_address': email_address
            },
            method='POST'
        )

    def verify_email_address(self, email_address, redirect_uri):
        """ Post send an email to verify a change in this user's email address 
            via /me/sendverifyemailaddress, /users/{user_id}/sendverifyemailaddress
            email_address : str
                User's email address
            redirect_uri : str
                URI to redirect to after an email is sent
        """
        endpoint = '/api/v1/me' if self.sws.user_id == 0 else '/api/v1/users/'+ str(self.sws.user_id)
        endpoint += '/sendverifyemailaddress'
        return self.fetch(
            auth='bearer',
            endpoint=endpoint,
            body={
                'email_address': email_address,
                'redirect_uri': redirect_uri
            },
            method='POST'
        )

    def post_user_gaclientid(self, ga_client_id):
        """ POST add a Google Client ID association to a user
            ga_client_id : str
                Google Client ID
        """
        endpoint = '/api/v1/users/'+ str(self.sws.user_id) + '/gaclientid'
        return self.fetch(
            auth=HTTPBasicAuth(username=self.sws.app_id, password=self.sws.secret),
            endpoint=endpoint,
            body={
                'ga_client_id': ga_client_id
            },
            method='POST'
        )