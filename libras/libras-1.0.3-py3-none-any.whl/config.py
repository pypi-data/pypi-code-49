from flask import Config
import os
import re
import yaml


class LibConfig(Config):
    regex = r'\S+\.(yaml)|(yml)'

    def from_yaml(self, config_path=os.getcwd()):
        try:
            if config_path and config_path != '/':
                self.scan(config_path)
            addition_path = self.property("resource.addition_path")
            self.scan(addition_path) if addition_path else None
        except FileNotFoundError as e:
            raise FileNotFoundError("Couldn't found file on " + config_path, e)

    def scan(self, config_path):
        if not config_path:
            pass
        for parent, dirname, fileNames in os.walk(config_path, followlinks=True):
            for filename in fileNames:
                file_path = os.path.join(parent, filename)
                match = re.search(self.regex, file_path, re.M | re.I)
                if match:
                    res = self.load_file(file_path)
                    self.update(res)

    def property(self, key: str):
        if not str:
            return None
        value = None
        for x in key.split('.'):
            value = value.get(x) if value else self.get(x)
        return value

    @staticmethod
    def load_file(file):
        print("load yaml file path - %s" % file)
        return yaml.safe_load(open(file))
