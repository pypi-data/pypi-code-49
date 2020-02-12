import importlib
import os

__author__ = 'Whirldata Cloud Agnostic Services'
__version__ = '0.0.1'


def _get_default_service(*args, **kwargs):
    """
    """
    return CAUtil(*args, **kwargs)

def resource(*args, **kwargs):
    """
    """
    return _get_default_service(*args, **kwargs).resource()


class CAUtil(object):
    def __init__(self, service_name, config):
        self.service_name = service_name
        self.config = config

    def __validate_resource(self):
        if(self.service_name not in os.listdir('./cautil/utils')):
            raise ServiceNotFoundException(
                "Service `{}` is not defined".format(self.service_name))
        elif(not isinstance(self.config, dict)):
            raise ConfigDataException("Configuration data should be of type `dict`")
        elif( self.service_name not in self.config):
            raise ConfigDataException("Service `{}` has no configuration info".format(self.service_name))
        elif( 'vendor' not in self.config[self.service_name]):
            raise ConfigDataException("Service `{}` has no configuration vendor".format(self.service_name))
        
    def __create_resource_object(self):
        service = importlib.import_module('cautil.utils.{0}'.format(self.service_name))
        module_class = getattr(service, '{0}'.format(self.service_name.capitalize()))
        module_object = module_class(self.service_name, self.config)
        return module_object.get_service()
        
    def resource(self):
        self.__validate_resource()
        return self.__create_resource_object()


class ServiceNotFoundException(Exception):
    """
    """
    def __init__(self, msg):
        pass


class ConfigDataException(Exception):
    """
    """
    def __init__(self, msg):
        pass
