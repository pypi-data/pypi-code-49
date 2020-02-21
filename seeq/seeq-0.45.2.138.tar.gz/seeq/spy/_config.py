import configparser
import os
import textwrap

from enum import Enum

from seeq.base import system
from seeq.sdk.rest import Configuration

file_config = None


class Options:
    _DEFAULT_SEARCH_PAGE_SIZE = 1000
    _DEFAULT_PULL_PAGE_SIZE = 1000000
    _DEFAULT_PUSH_PAGE_SIZE = 100000
    _DEFAULT_MAX_CONCURRENT_REQUESTS = 8

    def __init__(self):
        self.search_page_size = self._DEFAULT_SEARCH_PAGE_SIZE
        self.pull_page_size = self._DEFAULT_PULL_PAGE_SIZE
        self.push_page_size = self._DEFAULT_PUSH_PAGE_SIZE
        self.max_concurrent_requests = self._DEFAULT_MAX_CONCURRENT_REQUESTS

    @property
    def retry_timeout_in_seconds(self):
        return Configuration().retry_timeout_in_seconds

    @retry_timeout_in_seconds.setter
    def retry_timeout_in_seconds(self, value):
        Configuration().retry_timeout_in_seconds = value

    def help(self):
        help_string = """\
            Assign a new value to the following variables if you would like to adjust them.
            
            E.g.:
               spy.options.concurrent_requests = 3
                    
            Available Options
            -----------------
            
            spy.options.search_page_size (default: %s)
            
                The number of items retrieved on each round-trip to the Seeq Server during
                a spy.search() call. If you have a fast system and fast connection, you can
                make this higher.
            
            spy.options.pull_page_size (default: %s)
            
                The number of samples/capsules retrieved on each round-trip to the Seeq
                Server during a spy.pull() call. If you have a slow system or slow
                connection, you may wish to make this lower. It is not recommended to
                exceed 1000000.
                 
            spy.options.push_page_size (default: %s)
            
                The number of samples/capsules uploaded during each round-trip to the Seeq
                Server during a spy.push() call. If you have a slow system or slow
                connection, you may wish to make this lower. It is not recommended to
                exceed 1000000.
                
            spy.options.max_concurrent_requests (default: %s)
            
                The maximum number of simultaneous requests made to the Seeq Server during
                spy.pull() and spy.push() calls. The higher the number, the more you can
                monopolize the Seeq Server. If you keep it low, then other users are less
                likely to be impacted by your activity. 
                
            spy.options.retry_timeout_in_seconds (default: %s)
            
                The amount of time to spend retrying a failed Seeq Server API call in an
                attempt to overcome network flakiness. 
        """

        print(textwrap.dedent(help_string % (self._DEFAULT_SEARCH_PAGE_SIZE,
                                             self._DEFAULT_PULL_PAGE_SIZE,
                                             self._DEFAULT_PUSH_PAGE_SIZE,
                                             self._DEFAULT_MAX_CONCURRENT_REQUESTS,
                                             Configuration().DEFAULT_RETRY_TIMEOUT_IN_SECONDS)))


options = Options()


class Setting(Enum):
    CONFIG_FOLDER = {'env': 'SEEQ_SPY_CONFIG_FOLDER', 'ini': None}
    CONFIG_FILENAME = {'env': 'SEEQ_SPY_CONFIG_FILENAME', 'ini': None}
    SEEQ_URL = {'env': 'SEEQ_SERVER_URL', 'ini': 'seeq_server_url'}
    SEEQ_CERT_PATH = {'env': 'SEEQ_CERT_PATH', 'ini': 'seeq_cert_path'}
    SEEQ_KEY_PATH = {'env': 'SEEQ_KEY_PATH', 'ini': 'seeq_key_path'}
    AGENT_KEY_PATH = {'env': 'AGENT_KEY_PATH', 'ini': 'agent_key_path'}

    def get_env_name(self):
        return self.value['env']

    def get_ini_name(self):
        return self.value['ini']

    def get(self):
        setting = os.environ.get(self.get_env_name())
        if not setting and self.get_ini_name():
            config = get_file_config()
            setting = config.get('spy', self.get_ini_name(), fallback=None)
        return setting

    def set(self, value):
        os.environ[self.get_env_name()] = value

    def unset(self):
        del os.environ[self.get_env_name()]


def get_config_folder():
    """
    This is the config folder for the SPy library, which is where any additional configuration files for SPy must be
    stored. The default location is the same as the Seeq global folder.
    :return: Location of the config folder
    """
    config_folder = Setting.CONFIG_FOLDER.get()
    if not config_folder:
        if system.is_windows():
            config_folder = os.path.join(os.environ["ProgramData"], 'Seeq')
        else:
            config_folder = os.path.join(system.get_home_dir(), '.seeq')

    system.create_folder_if_necessary_with_correct_permissions(config_folder)

    return config_folder


def set_config_folder(path):
    Setting.CONFIG_FOLDER.set(path)


def get_config_filename():
    filename = Setting.CONFIG_FILENAME.get()
    return filename if filename else "spy.ini"


def get_config_path():
    return os.path.join(get_config_folder(), get_config_filename())


def get_seeq_url():
    url = Setting.SEEQ_URL.get()
    return url if url else 'http://localhost:34216'


def set_seeq_url(url):
    Setting.SEEQ_URL.set(url)


def unset_seeq_url():
    Setting.SEEQ_URL.unset()


def get_api_url():
    return '{0}/api'.format(get_seeq_url())


def get_seeq_cert_path():
    path = Setting.SEEQ_CERT_PATH.get()
    return path if path else os.path.join(get_config_folder(), 'seeq-cert.pem')


def get_seeq_key_path():
    path = Setting.SEEQ_KEY_PATH.get()
    return path if path else os.path.join(get_config_folder(), 'seeq-key.pem')


def get_file_config():
    global file_config
    if not file_config:
        file_config = configparser.ConfigParser()
        file_config.read(get_config_path())
    return file_config
