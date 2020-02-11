import os
from incremental_module_loader import IncrementalModuleLoader

from .auth import AuthModule
from .config import FileConfigStorageProvider, ConfigModule
from .logs import _logger, setup_logging
from .storage import SITE_DATA_DIR
from .spinhub import SpinHubClientModule

from .services.auth0 import SpinHubAuthProvider

logger = _logger('root')

def Spintop(verbose=False, org_id=None, spinhub_url=None):
    # Default factory args
    return SpintopFactory(ephemeral_config=dict(
        verbose=verbose,
        org_id=org_id,
        spinhub_url=spinhub_url
    ))

def SpintopFactory(
            ephemeral_config={},
            logs_factory=setup_logging,
            config_factory=ConfigModule,
            config_storage_factory=FileConfigStorageProvider,
            auth_provider_factory=SpinHubAuthProvider,
            auth_factory=AuthModule, 
            spinhub_factory=SpinHubClientModule,
            final_factory=None
        ):
    
    loader = IncrementalModuleLoader()
    loader.update(
        ephemeral_config=ephemeral_config,
        config_storage=FileConfigStorageProvider(os.path.join(SITE_DATA_DIR, 'spintop.yml'))
    )
    
    loader.load(logs=logs_factory)
    
    config = loader.load(config=config_factory)
    # config.load(ephemeral_config)
    
    loader.load(auth_provider=auth_provider_factory)
    loader.load(auth=auth_factory)
    loader.load(spinhub=spinhub_factory)
    spintop_or_final = loader.load(spintop=SpintopModule)
    
    if final_factory:
        spintop_or_final = loader.load(final_factory)
    
    return spintop_or_final

def SpintopWorkerFactory(worker_cls, **factory_kwargs):
    worker = SpintopFactory(final_factory=worker_cls, **factory_kwargs)
    return worker
    

class SpintopModule(object):
    def __init__(self, config, spinhub, auth):
        self.config = config
        self.spinhub = spinhub
        self.auth = auth
    
    def assert_no_login(self):
        self.auth.assert_no_login()
    
    def login(self, username, password):
        self.assert_no_login()
        self.auth.login(username, password)
        self.auth.save_credentials()
    
    def stored_logged_username(self):
        if self.auth.credentials:
            return self.auth.credentials.get('username')
        else:
            return None
    
    def logout(self):
        return self.auth.logout()
    
    def delete_config(self):
        self.logout()
        self.config.delete_config()
    
    def register_machine(self, name, token, org_id=None):
        return self.spinhub.register_machine(name, token, org_id=org_id)
    
    def get_user_orgs(self):
        user_info = self.spinhub.user_info
        return user_info['organizations']


        
        
    
    
        