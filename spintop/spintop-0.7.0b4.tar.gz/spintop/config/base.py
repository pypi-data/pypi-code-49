from copy import deepcopy

from .schemas import SpinhubProfile


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
    
    @property
    def profile_name(self):
        profile = self.ephemeral_config.get('profile')
        if not profile:
            profile = self.config.get('default_profile')
        return profile

    def delete_config(self):
        self._config = self.create_empty()
        self.config_storage.delete_spintop_config()
        
    def create_empty(self, profile=None, spinhub_url=None):
        
        
        self._config = dict(
            default_profile = profile,
            profiles = {},
            credentials = {}
        )
        
        self.create_profile(profile=profile, spinhub_url=spinhub_url)
        
        return self._config
    
    def create_profile(self, profile=None, spinhub_url=None):
        if spinhub_url is None:
            spinhub_url = 'https://dev-api.spinhub.ca'
            
        if profile is None:
            profile = 'default'

        profile_content = dict(
            credentials_key = None,
            spinhub_url = spinhub_url,
            name = profile
        )
        self.config['profiles'] = self.config.get('profiles', {})
        self.config['profiles'][profile] = SpinhubProfile().dump(profile_content)
        logger.info('Created a profile named %s' % profile)
        return profile_content
    
    def update_profile(self, **kwargs):
        profile = self.get_selected_profile()
            
        profile.update(kwargs)
    
    def set_credentials(self, key, credentials):
        self.config['credentials'] = self.config.get('credentials', {})
        self.config['credentials'][key] = credentials
        
        profile = self.get_selected_profile()
        if profile.get('credentials_key') is None:
            profile['credentials_key'] = key
            
        
    def remove_credentials(self, key):
        if key in self.config.get('credentials', {}):
            del self.config['credentials'][key]

        for _, content in self.config.get('profiles', {}).items():
            if content.get('credentials_key') == key:
                content['credentials_key'] = None
    
    def get_credentials(self, key=None):
        if key is None:
            key = self.get_selected_profile().get('credentials_key')
        
        if key is None:
            return None
        
        return self.config.get('credentials', {}).get(key, {})
    
    def get_selected_profile(self):
        return self.get_profile()
        
    def load(self, ephemeral_config):
        config = self.get_stored()
        before_load = deepcopy(config)
        
        profile_config = dict(
            spinhub_url=ephemeral_config.get('spinhub_url'),
            profile=ephemeral_config.get('profile'),
        )

        if not config:
            config = self.create_empty(**profile_config)
        
        self._profile = self.get_profile(**profile_config)
        
        if config != before_load:
            self.save()
        
    def get_profile(self, profile=None, **other_profile_config):
        if profile is None:
            profile = self.profile_name
        
        profile_content = self.config.get('profiles', {}).get(profile, None)
        
        if profile_content is not None:
            return profile_content
        else:
            profile_content = self.create_profile(profile=profile, **other_profile_config)
            self.save()
            return profile_content
            
    def get_stored(self):
        if not self._config_loaded:
            self._config = self.config_storage.retrieve_spintop_config()
            self._config_loaded = True
        return self._config
    
    def save(self):
        self._config = self.config_storage.store_spintop_config(self._config)
        self._config_loaded = True
        return self._config
    