import pytest
import os
from spintop.errors import SpintopException
from spintop.auth import AuthModule, AuthException
from spintop.spinhub import SpinHubClientModule

from mock import patch

CREDENTIALS_FILE_MOCK = 'tempcredentials.json'

@pytest.fixture
def auth_module():
    return AuthModule()

@pytest.fixture
def spinhub_module(auth_module, integration_config):
    if not integration_config:
        return None
    else:
        return SpinHubClientModule(url=integration_config.api_url, auth_module=auth_module)

@pytest.mark.integration
def test_login(auth_module, integration_config):
    store.delete_credentials() # make sure none exist
    
    auth_module.login(integration_config.username, integration_config.password)
    
    assert os.path.exists(CREDENTIALS_FILE_MOCK)
    
@pytest.mark.integration
def test_refuse_second_login(auth_module, integration_config):
    assert auth_module.credentials.username == integration_config.username
    
    with pytest.raises(AuthException):
        auth_module.login(integration_config.username, integration_config.password)

@pytest.mark.integration
def test_private_api_endpoint(spinhub_module):
    spinhub_module.test_private_endpoint()
    
@pytest.mark.integration
def test_bad_access_token_causes_refresh(auth_module, spinhub_module):
    auth_module.credentials.access_token = auth_module.credentials.access_token[0:-4]
    spinhub_module.test_private_endpoint()
    
@pytest.mark.integration
def test_bad_access_and_bad_refresh(auth_module, spinhub_module):
    # re-corrupt access
    auth_module.credentials.access_token = auth_module.credentials.access_token[0:-4]
    # corrupt refresh
    auth_module.credentials.refresh_token = auth_module.credentials.refresh_token[0:-4]
    
    with pytest.raises(SpintopException):
        spinhub_module.test_private_endpoint()

@pytest.mark.integration
def test_logout(auth_module):
    auth_module.logout()
    assert not os.path.exists(CREDENTIALS_FILE_MOCK)
    
    
    
