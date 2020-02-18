from cfenv import AppEnv
from config.auth import OAuth2
from config.cf import CF
from config.spring import ConfigClient


class CF3:

    service_name, app_name = None, None

    def __init__(self, service_name, app_name):
        self.service_name = service_name
        self.app_name = app_name

    def load_config(self):
        env = AppEnv().get_service(name=self.service_name)
        config = env.credentials

        client_secret = config.get('client_secret')
        client_id = config.get('client_id')
        access_token = config.get('access_token_uri')
        uri_address = config.get('uri')

        return CF(oauth2=OAuth2(client_secret=client_secret, access_token_uri=access_token, client_id=client_id),
                client=ConfigClient(address=uri_address, app_name=self.app_name), cfenv=None)
