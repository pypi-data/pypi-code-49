""" Storage of the access token and refresh token to allow long lived authentication sessions.
"""
import yaml
import os
from pprint import pformat

from ..storage import SITE_DATA_DIR
from .schemas import SpintopMachineConfig

from ..logs import _logger

logger = _logger('config-storage')

class MemoryConfigStorageProvider(object):
    def __init__(self):
        self.config = None

    def store_spintop_config(self, config):
        data = SpintopMachineConfig().dump(config)
        self.config = data
        return data

    def retrieve_spintop_config(self):
        if self.config:
            return SpintopMachineConfig().load(self.config)
        else:
            return {}
        
    def delete_spintop_config(self):
        self.config = None
        
class FileConfigStorageProvider(object):
    def __init__(self, config_filepath):
        self.config_filepath = config_filepath
    
    def store_spintop_config(self, config):
        data = SpintopMachineConfig().dump(config)
        logger.info('Saving config')
        with open(self.config_filepath, 'w+') as machine_file:
            yaml.dump(data, machine_file)
        return data

    def retrieve_spintop_config(self):
        if os.path.exists(self.config_filepath):
            logger.debug('Loading config content')
            with open(self.config_filepath) as machine_file:
                data = yaml.safe_load(machine_file)
                return SpintopMachineConfig().load(data)
        else:
            logger.info('No config file to load')
            return None
        
    def delete_spintop_config(self):
        if os.path.exists(self.config_filepath):
            os.remove(self.config_filepath)
        