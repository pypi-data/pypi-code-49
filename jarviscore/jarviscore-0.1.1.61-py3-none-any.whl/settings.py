from .errors import MissingSetting, ConfigFileNotFound
from pathlib import Path
import yaml
import json


class Settings():
    """Core Settings Class. Reads settings stored in the Common/env YAML file."""
    __settingsData: dict

    def __init__(self, path=None):
        if path is None:
            path = "config.yaml"
        if not Path(path).exists():
            path = "./config.yaml"
        if not Path(path).exists():
            path = "./bots/config.yaml"
        if not Path(path).exists():
            path = "./Common/config.yaml"
        if not Path(path).exists():
            path = "../Common/config.yaml"
        if not Path(path).exists():
            path = "../../Common/config.yaml"
        if path is None:
            path = "config.json"
        if not Path(path).exists():
            path = "./config.json"
        if not Path(path).exists():
            path = "./bots/config.json"
        if not Path(path).exists():
            path = "./Common/config.json"
        if not Path(path).exists():
            path = "../Common/config.json"
        if not Path(path).exists():
            path = "../../Common/config.json"
        if not Path(path).exists():
            raise ConfigFileNotFound("Config file could not be found.")
        self.__settingsData = self.__parse_file(path)
        self.path = path
    
    def get_setting(self, key:str):
        setting = self.__fetchSetting(key, self.__settingsData)
        if setting is None:
            raise MissingSetting(f"Key: '{key}' was not found in the config file '{self.path}'")
        return self.__fetchSetting(key, self.__settingsData)
    
    def __fetchSetting(self, key:str, sublist:dict):
        keynest = key.split(".", 1)
        if len(keynest) == 1:
            try:
                return sublist[keynest[0]]
            except:
                return None
        return self.__fetchSetting(keynest[1], sublist[keynest[0]])
        
    def __parse_file(self, path):
        data = None
        with open(Path(path), 'r') as stream:
            if path.endswith(".yaml"):
                data = yaml.safe_load(stream)
            elif path.endswith(".json"):
                data = json.load(stream)
            else:
                raise ConfigFileNotFound("Config file must be a .yaml or a .json file")
        return data
    
    def get_all_settings(self):
        return self.__settingsData

    def __repr__(self):
        return f"[Settings]: Loaded {len(self.__settingsData)} settings from file: '{self.path}'"

