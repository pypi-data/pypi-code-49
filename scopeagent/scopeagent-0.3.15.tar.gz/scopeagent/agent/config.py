import json
import logging
from os.path import expanduser

import yaml

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


SCOPE_NATIVE_APP_CONFIG_PATH = expanduser('~/.scope/config.json')
SCOPE_CONFIG_PATH = './scope.yml'
logger = logging.getLogger(__name__)


# We can't use default parameters or @mock.patch won't work
def load_native_app_config_file(path=None):
    """Attempts to read the API endpoint and API key from the native Scope app configuration file."""
    path = path or SCOPE_NATIVE_APP_CONFIG_PATH
    try:
        with open(str(path), 'r') as config_file:
            config = json.load(config_file)
            try:
                profile = config['profiles'][config['currentProfile']]
                logger.debug('autodetected config profile: %s', profile)
                return profile
            # ** TODO ** raise original exception
            except KeyError:
                raise Exception('Invalid format in Scope configuration file at %s' % path)
    except FileNotFoundError:
        return {}


# We can't use default parameters or @mock.patch won't work
def load_scope_config_file(path=None):
    """Attempts to read the configuration file scope.yml"""
    path = path or SCOPE_CONFIG_PATH
    try:
        with open(str(path), 'r') as config_file:
            try:
                config = yaml.load(config_file, Loader=yaml.FullLoader)
                return config
            except yaml.YAMLError:
                raise Exception('Invalid format in scope.yml configuration file at %s' % path)
    except FileNotFoundError:
        return {'scope': {}}
