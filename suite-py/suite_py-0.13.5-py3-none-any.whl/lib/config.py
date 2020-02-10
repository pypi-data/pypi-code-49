from __future__ import print_function, unicode_literals
from .singleton import Singleton
import os
import yaml


class Config(metaclass=Singleton):
    _config = {}

    def __init__(self):
        pass

    def load(self):
        with open(os.path.join(os.environ['HOME'], '.suite_py/config.yml')) as configfile:
            self._config = yaml.safe_load(configfile)

        self._config['user']['projects_home'] = os.path.join(
            os.environ['HOME'], self._config['user']['projects_home'])
        return self._config
