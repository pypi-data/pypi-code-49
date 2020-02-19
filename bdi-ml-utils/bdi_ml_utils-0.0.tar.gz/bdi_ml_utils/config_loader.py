import json


class ConfigLoader:
    def __init__(self, logger, config_path):
        logger.info("Loading config from {}".format(config_path))
        with open(config_path, 'r') as c:
            self.config = json.load(c)
        logger.info("Config file content: \n{}".format(json.dumps(self.config, indent=4)))

    def get_config(self):
        return self.config