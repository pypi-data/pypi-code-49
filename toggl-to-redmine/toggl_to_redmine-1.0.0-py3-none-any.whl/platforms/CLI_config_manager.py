import os
import click
from toggl_to_redmine.app.exceptions import ConfigException
from pathlib import Path


class CLIConfigManager():

    file_path = str(Path.home()) + '/.config/toggl-to-redmine.txt'

    def __init__(self):
        self.config = {}

    def get_config(self) -> dict:
        self.config.clear()
        try:
            path = os.path.abspath(CLIConfigManager.file_path)
            file = open(path, 'r')
            for config_line in file:
                key, value = config_line.split('=')
                self.config[key] = value.strip()
            file.close()
            return self.config
        except OSError:
            raise ConfigException("Config file not found")

    def reset_config(self):
        self.ask_config_from_user()
        self.persist_config()

    def ask_config_from_user(self) -> dict:
        self.config = {
            'redmine_url': click.prompt('URL from Redmine App', type=str),
            'redmine_api_key': click.prompt('API Token from Redmine', type=str),
            'toggl_user': click.prompt('Username or email from Toggl', type=str),
            'toggl_workspace_id': click.prompt('Workspace ID from Toggl', type=str),
            'toggl_api_token': click.prompt('API Token from Toggl', type=str)
        }

    def persist_config(self):
        self.ensure_config_folder_exists()

        path = os.path.abspath(CLIConfigManager.file_path)
        file = open(path, 'w')
        for key, value in self.config.items():
            line = f'{key}={value}\n'
            file.write(line)
        file.close()

    def ensure_config_folder_exists(self):
        config_path = os.path.abspath(str(Path.home()) + '/.config')
        if not os.path.exists(config_path):
            os.mkdir(config_path, mode=0o600)
