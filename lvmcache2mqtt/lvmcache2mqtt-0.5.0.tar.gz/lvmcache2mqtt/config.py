import yaml

class Config():
    def __init__(self, config_file):
        self._config = yaml.load(open(config_file, 'r'), yaml.BaseLoader)

    def get_devices(self):
        return self._config['devices']

    def get_mqtt(self):
        return self._config['mqtt']

