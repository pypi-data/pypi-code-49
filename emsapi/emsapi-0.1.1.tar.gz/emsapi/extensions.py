import json
import requests
import logging

from emsapi import emsapi
from datetime import datetime
from datetime import timedelta
from msrest import authentication

class EmsApiAuthError(Exception):
    """
    Generic exception for auth errors
    """
    def __init__(self, msg, original_exception=None):
        message = msg
        if original_exception:
            message = message + f": {original_exception}"
        super(EmsApiAuthError, self).__init__(message)
        self.original_exception = original_exception

class EmsApiTokenAuthentication(authentication.Authentication):
    def __init__(self, user: str, password: str, url: str):
        self.scheme = 'Bearer'
        self.user = user
        self.password = password
        self.url = url
        self.token = None
        self.expiration = None
        self.logger = logging.getLogger(__name__)
        if not self.url.endswith('/'):
            self.url = self.url + '/'

    def set_token(self):
        """
        Retrieves a new token for the EMS API.
        """
        authorization_url = self.url + "token"
        body = "grant_type=password&username=" + self.user +"&password=" + self.password
        try:
            response = requests.post(authorization_url, body)
        except requests.RequestException as e:
            raise EmsApiAuthError("An EMS API authentication error occurred.", e)
        
        if response.ok:
            self.logger.info(f"Retrieved new auth token for {self.url}")
            self.token = json.loads(response.text)
            
            # Subtract 5 seconds from the expiration time to account for long running requests.
            delta_seconds = self.token['expires_in'] - 5
            self.expiration = datetime.now() + timedelta(seconds=delta_seconds)
        else:
            raise EmsApiAuthError(f"The authentication token request failed with the HTTP code {response.status_code}")
            
    def is_expired(self):
        """
        Returns true if the token has expired and needs to be refreshed.
        """
        if self.token is None or self.expiration is None:
            return True
        return datetime.now() > self.expiration
            
    def signed_session(self, session=None):
        """
        Creates a new session, or configures an existing one.
        """
        session = super(EmsApiTokenAuthentication, self).signed_session(session)
        if not self.token or self.is_expired():
            self.set_token()
            
        header = "{} {}".format(self.scheme, self.token['access_token'])
        session.headers['Authorization'] = header
        return session
    
class EmsSystemHelper:
    systems = {}
    
    @staticmethod
    def find_id(client: emsapi, name: str):
        # Cache by base url
        url = client.config.base_url
        cached = EmsSystemHelper.systems.get(url)
        if not cached:
            EmsSystemHelper.systems[url] = client.ems_system.get_ems_systems()
        
        # We don't require an exact match (use find).
        matching = [s 
                    for s in EmsSystemHelper.systems[url]
                    if s.name.lower().find(name.lower()) > -1]

        # But we do require there to be exactly one match, to avoid ambiguity.
        if len(matching) == 0:
            raise ValueError(f"An EMS system was not found with the name {name}")
        elif len(matching) == 1:
            return matching[0].id
        else:
            raise ValueError(f"More than one EMS system was found with the name {name}")