"""
A module for storing and retrieving basic application configuration data.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
import os
import pickle


class Singleton(type):
    """Singleton metaclass."""
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Config(metaclass=Singleton):
    """Basic configuration type."""
    def __init__(self):
        """Initializes configuration data from a configuration file."""
        self.data = {}
        self._path = os.path.join(os.getcwd(), 'CONFIG')
        if os.path.exists(self._path):
            with open(self._path, 'rb') as config_file:
                self.data = pickle.load(config_file)

    def save(self):
        """Saves a configuration object to a 'CONFIG' file (overwritten)."""
        if self.data:
            with open(self._path, 'wb') as config_file:
                pickle.dump(self.data, config_file)

    def __repr__(self):
        """Returns the repr() string output of the type."""
        return repr(self.data)
