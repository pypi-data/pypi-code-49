import os
from ruamel.yaml import YAML


ETC_CONFIG_FILE='/etc/rpi.infobot/config.yaml'
HOME_CONFIG_FILE=os.path.join(os.environ.get('HOME'), '.config/rpi.infobot/config.yaml')
TOKEN = 'token'
CHATS = 'chats'


def load(config_file=None):
    config_path = config_file or HOME_CONFIG_FILE
    if os.path.exists(config_path) is not True:
    	config_path = ETC_CONFIG_FILE

    if os.path.exists(config_path) is not True:
    	raise Exception(f"No configuration defined for rpi.infobot in {config_file} or {HOME_CONFIG_FILE} or {ETC_CONFIG_FILE}")
    	
    data = {}

    with open(config_path) as f:
        data = YAML().load(f)

    return Config(data)

class Config:
    def __init__(self, data):
        self.token = data.get(TOKEN)
        self.chats = data.get(CHATS)
