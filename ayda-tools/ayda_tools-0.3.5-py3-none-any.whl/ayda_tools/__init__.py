import os
from getpass import getuser
import json


class AydaConfig:
    def __init__(self):
        username = getuser()
        self.AYDA_CONFIG_PATH = "/home/{}/.ayda/aydarc".format(username)
        self.AYDA_DATA_PATH = ""
        self.CLIENT_KEY_PATH = "/home/{}/.ayda/clientkey".format(username)

        try:
            clientdata = open(self.CLIENT_KEY_PATH, "r").read().splitlines()
            self.server_address = clientdata[0].strip()
            self.server_port = clientdata[1].strip()
            self.mode = clientdata[2].strip()
            self.username = clientdata[3].strip()
            self.pw = clientdata[4].strip()
        except (FileNotFoundError, IndexError):
            pass

        if os.path.exists(self.AYDA_CONFIG_PATH):
            self.update(**json.load(open(self.AYDA_CONFIG_PATH)))

        self.AYDA_DATA_PATH = os.environ.get("AYDA_DATA_PATH", self.AYDA_DATA_PATH)

    def update(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])


config = AydaConfig()
