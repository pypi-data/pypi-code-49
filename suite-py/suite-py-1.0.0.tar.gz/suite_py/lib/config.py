# -*- encoding: utf-8 -*-
import yaml
import os

from suite_py.lib.singleton import Singleton


class Config(metaclass=Singleton):
    _config = {}

    def __init__(self):
        pass

    def load(self):
        with open(os.path.join(os.environ['HOME'], '.suite_py/config.yml')) as configfile:
            self._config = yaml.safe_load(configfile)

        self._config['user']['projects_home'] = os.path.join(
            os.environ['HOME'], self._config['user']['projects_home'])

        if not self._config['user'].get('notify_channel'):
            self._config['user']['notify_channel'] = '#review'

        if not self._config['user'].get('default_slug'):
            self._config['user']['default_slug'] = "PRIMA-XXX"

        if not self._config['user'].get('captainhook_timeout'):
            self._config['user']['captainhook_timeout'] = 10  # This is in seconds

        return self._config
