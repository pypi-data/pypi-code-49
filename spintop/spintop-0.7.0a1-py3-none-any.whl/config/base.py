from copy import deepcopy
from ..errors import SpintopException

from ..logs import _logger

logger = _logger('config')

LOADED_CONFIG = None

class ConfigModule(object):
    def __init__(self, config_storage, ephemeral_config):
        
        self.config_storage = config_storage
        self.ephemeral_config = ephemeral_config
        
        self._config = {}
        self._config_loaded = False
        
        self._profile = None
    
    @property
    def config(self):
        if not self._config:
            self.load(self.ephemeral_config)
        return self._config
    
    def delete_config(self):
        self._config = self.create_empty()
        self.config_storage.delete_spintop_config()
        
    def create_empty(self, default_url=None, profile_name=None, **other_profile_config):
        
        if default_url is None:
            default_url = 'https://dev-api.spinhub.ca'
            
        if profile_name is None:
            profile_name = 'default'
        
        self._config = dict(
            default_profile = profile_name,
            profiles = {},
            credentials = {}
        )
        
        self.create_profile(default_url=default_url, profile_name=profile_name, **other_profile_config)
        
        return self._config
    
    def create_profile(self, machine_id=None, default_url=None, spinhub_url=None, profile_name=None, org_id=None, **_):
        if not spinhub_url:
            spinhub_url = default_url
        
        profile = dict(
            credentials = None,
            spinhub_url = spinhub_url
        )
        self._config['profiles'] = self._config.get('profiles', {})
        self._config['profiles'][profile_name] = profile
        logger.info('Created a profile named %s' % profile_name)
        return profile
    
    
    def update_profile(self, profile_name=None, **kwargs):
        if profile_name is None:
            profile = self._profile
        else:
            profile = self.get_profile(profile_name)
            
        profile.update(kwargs)
    
    def set_credentials(self, key, credentials):
        self._config['credentials'] = self._config.get('credentials', {})
        self._config['credentials'][key] = credentials
        
        profile = self.get_selected_profile()
        if profile.get('credentials_key') is None:
            profile['credentials_key'] = key
            
        
    def remove_credentials(self, key):
        if key in self._config.get('credentials', {}):
            del self._config['credentials'][key]
    
    def get_credentials(self, key=None):
        if key is None:
            key = self.get_selected_profile().get('credentials_key')
        
        if key is None:
            return None
        
        return self._config.get('credentials', {}).get(key, {})
    
    def get_selected_profile(self):
        return self.get_profile()
        
    def load(self, ephemeral_config):
        config = self.get_stored()
        before_load = deepcopy(config)
        
        if not config:
            config = self.create_empty(**ephemeral_config)
        
        self._profile = self.get_profile(**ephemeral_config)
        
        # logger.info('Loaded profile named %s' % self._profile['name'])
        
        if config != before_load:
            self.save()
        
    def get_profile(self, profile_name=None, **other_profile_config):
        if profile_name is None:
            profile_name = self.config.get('default_profile')
        
        profile = self._config.get('profiles', {}).get(profile_name, None)
        
        if profile is not None:
            return profile
        
        # profile not found
        profile = self.create_profile(profile_name=profile_name, **other_profile_config)
        self.save()
        return profile
            
    def get_stored(self):
        if not self._config_loaded:
            self._config = self.config_storage.retrieve_spintop_config()
            self._config_loaded = True
        return self._config
    
    def save(self):
        self._config = self.config_storage.store_spintop_config(self._config)
        self._config_loaded = True
        return self._config
    