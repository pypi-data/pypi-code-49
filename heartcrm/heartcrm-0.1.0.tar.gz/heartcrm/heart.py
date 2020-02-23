"""Establishes a connection to HEART CRM via OAUTH2 or username/password/token
and uses that connection to make Salesforce API calls."""
import requests
from simple_salesforce import Salesforce

from heartcrm.conf import read_heartrc


class HeartCRM(Salesforce):
    def __init__(self, **kwargs):
        connected = self._try_username_password(**kwargs)

        # Read in the configuration file, but allow the kwargs
        # to take precedence over the conigs.
        if not connected:
            config = read_heartrc()
            if config:
                for key in config:
                    if key not in kwargs:
                        kwargs[key] = config[key]
            self._try_oauth(**kwargs)

    def _try_username_password(self, **kwargs):
        """Attempts to connect with username and password."""
        connected = False

        username = kwargs.pop('username', None)
        password = kwargs.pop('password', None)
        security_token = kwargs.pop('security_token', None)
        instance = kwargs.pop('instance', None)
        domain = kwargs.pop('domain', None)

        if any([username, password, security_token]):
            if not all([username, password, security_token]):
                raise ValueError('Authentication with username/password '
                                 'requires a username, a password, and a '
                                 'security_token.')

            super().__init__(username=username,
                             password=password,
                             security_token=security_token,
                             instance=instance,
                             domain=domain)
            connected = True
        return connected

    def _try_oauth(self, **kwargs):
        """Attempts to connect to Salesforce using OAUTH2."""
        connected = False

        redirect_uri = kwargs.pop('redirect_uri', None)
        client_id = kwargs.pop('client_id', None)
        client_secret = kwargs.pop('client_secret', None)
        access_code = kwargs.pop('access_code', None)
        sandbox = kwargs.pop('sandbox', False)

        if any([redirect_uri, client_id, client_secret, access_code]):
            if not all([redirect_uri, client_id, client_secret, access_code]):
                raise ValueError('OAUTH2 authentication requires a '
                                 'redirect_uri, a client_id, a client_secret '
                                 'and an access_code.')

            access_token, instance_url = _get_access_token(redirect_uri,
                                                           client_id,
                                                           client_secret,
                                                           access_code,
                                                           sandbox)

            super().__init__(session_id=access_token,
                             instance_url=instance_url)
            connected = False
        return connected


def _get_access_token(redirect_uri, client_id, client_secret,
                      access_code, sandbox=False):
    """Retrieves an access code from the Salesforce OAUTH2 enpoint.

    Parameters
    ----------
    redirect_uri : str
        the redirect URI that is registered in the Salesforce ConnectedApp
    client_id : str
        the consumer key for the Salesforce ConnectedApp
    client_secret : str
        the consumer secret for the Salesforce ConnectedApp
    access_code : str
        the access code generated in the query parameter of the redirect URI
        after authenticating
    sandbox : bool
        uses test.salesforce.com if True, otherwise uses login.salesforce.com

    Returns
    -------
    access_token : str
        the access token that can be used to make subsequent Salesforce
        API calls
    instance_url : str
        the instance URL for the Salesforce account
    """
    data = {'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': access_code,
            'client_id': client_id,
            'client_secret': client_secret}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    subdomain = 'test' if sandbox else 'login'
    access_token_url = 'https://{}.salesforce.com/services/oauth2/token'
    access_token_url = access_token_url.format(subdomain)
    req = requests.post(access_token_url, data=data, headers=headers)
    response = req.json()
    return response['access_token'], response['instance_url']
