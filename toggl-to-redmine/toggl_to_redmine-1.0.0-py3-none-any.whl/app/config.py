from .exceptions import ConfigException
from datetime import date


class AppConfig():

    redmine_config_keys = ['redmine_url', 'redmine_api_key']

    toggl_config_keys = ['toggl_user', 'toggl_workspace_id',
                         'toggl_start_date', 'toggl_api_token']

    def __init__(self, config):
        self.config = config
        self.config['toggl_start_date'] = str(date.today())
        AppConfig.__check_config_integrity(self.config)

    def get(self, config_name):
        return self.config.get(config_name)

    def set_start_date(self, date: str):
        self.config['toggl_start_date'] = date

    def redmine_config(self):
        return self.__get_config_from_keys(AppConfig.redmine_config_keys)

    def toggl_config(self):
        return self.__get_config_from_keys(AppConfig.toggl_config_keys)

    def __get_config_from_keys(self, keys: list):
        config = {}
        for key in keys:
            config[key] = self.get(key)
        return config

    @staticmethod
    def __check_config_integrity(config):
        config_keys = ['toggl_user', 'toggl_workspace_id', 'toggl_start_date',
                    'toggl_api_token', 'redmine_url', 'redmine_api_key']
        for key in config_keys:
            if config.get(key) == None:
                raise ConfigException("There's a key missing in the configuration")
