__version__ = '0.0.4'

import random
from .client_registration import Client
from .data_registration import Data
from .service_registration import Service
import warnings


class DimsClient(object):

    def __init__(self, config={}):
        self.configs = Config
        self.configs.DEFAULT_DIMS_URI = 'http://localhost'
        self.configs.CLIENT_ENDPOINT = 'client'
        self.configs.SERVICE_ENDPOINT = 'service'
        self.configs.DATA_ENDPOINT = 'data'
        self.configs.SERVICE_NUMBER = random.randint(1, 100000)
        self.configs.LOG_ENABLED = False
        self.configs.SERVICE_NAME = 'default_service_name'
        if(config is not None):
            self.init_app(config)

        self.client = Client(self.configs)
        self.service = Service(self.client.config)
        self.data = Data(self.configs)

    def init_app(self, configs):
        """This callback can be used to initialize an application for the
        use with this database setup.  Never use a database in the context
        of an application not initialized that way or connections will
        leak.
        """
        if (
           'DEFAULT_DIMS_URI' not in configs
           ):
            warnings.warn(
                'DEFAULT_DIMS_URI is not set.' \
                'Defaulting DEFAULT_DIMS_URI to "http://localhost".'
            )

        if (
           'SERVICE_NUMBER' not in configs
           ):
            warnings.warn(
                'SERVICE_NUMBER is not set. Defaulting SERVICE_NUMBER to "{}".'.format(str(self.configs.SERVICE_NUMBER))
            )

        if (
           'SERVICE_NAME' not in configs
           ):
            warnings.warn(
                'SERVICE_NAME is not set. Defaulting SERVICE_NAME to "{}".'.format(str(self.configs.SERVICE_NAME))
            )

        self.configs.DEFAULT_DIMS_URI = configs[
            'DEFAULT_DIMS_URI'] if 'DEFAULT_DIMS_URI' in configs else self.configs.DEFAULT_DIMS_URI
        self.configs.CLIENT_ENDPOINT = configs['CLIENT_ENDPOINT'] if 'CLIENT_ENDPOINT' in configs else self.configs.CLIENT_ENDPOINT
        self.configs.SERVICE_ENDPOINT = configs[
            'SERVICE_ENDPOINT'] if 'SERVICE_ENDPOINT' in configs else self.configs.SERVICE_ENDPOINT
        self.configs.DATA_ENDPOINT = configs['DATA_ENDPOINT'] if 'DATA_ENDPOINT' in configs else self.configs.DATA_ENDPOINT
        self.configs.SERVICE_NUMBER = configs['SERVICE_NUMBER'] if 'SERVICE_NUMBER' in configs else self.configs.SERVICE_NUMBER
        self.configs.SERVICE_NAME = configs['SERVICE_NAME'] if 'SERVICE_NAME' in configs else self.configs.SERVICE_NAME
        self.configs.LOG_ENABLED = configs['LOG_ENABLED'] if 'LOG_ENABLED' in configs else self.configs.LOG_ENABLED

    def register_client(self):
        self.client.register_client()

    def register_service(self, service_parameter="", service_unit="", service_numeric="", tags=""):
        self.service.register_service(
            self.configs.SERVICE_NAME, service_parameter, service_unit, service_numeric, tags)

    def send_data(self, value, service_parameter="", service_unit="", service_numeric="", tags=""):
        if not self.client_registered():
            self.register_client()

        if not self.service_registered():
            self.register_service(
                service_parameter, service_unit, service_numeric, tags)

        return self.data.register_data(value)

    def client_registered(self):
        return self.client.client_registered

    def service_registered(self):
        return self.service.service_registered


class Config(dict):
    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value
