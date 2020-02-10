from datetime import timedelta
from configparser import ConfigParser
from typing import TextIO
from uuid import uuid4

from xdg import XDG_DATA_HOME


class Default:
    # Server
    HOST = "127.0.0.1"
    PORT = 8000

    # Database
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_URI = f"sqlite:///{XDG_DATA_HOME}/escarpolette/db.sqlite"

    # Authentication
    REMEMBER_COOKIE_DURATION = timedelta(days=390)  # ~13 months


class Config(Default):
    current_config = None

    def __init__(self, file: TextIO):
        """Read the config from a given file.

        If some values are missing, apply defaults. In any case, write the
        resulting config to the same file.
        """
        config = ConfigParser()
        config.read_file(file)

        if "DATABASE" not in config:
            config["DATABASE"] = {}

        if "MPV" not in config:
            config["MPV"] = {}

        if "SECURITY" not in config:
            config["SECURITY"] = {}

        if "SERVER" not in config:
            config["SERVER"] = {}

        self.HOST = config["SERVER"].get("HOST", self.HOST)
        self.PORT = config["SERVER"].getint("PORT", fallback=self.PORT)
        self.DATABASE_URI = config["DATABASE"].get("URI", self.DATABASE_URI)
        self.MPV_IPC_SOCKET = config["MPV"].get("IPC_SOCKET")
        self.SECRET_KEY = config["SECURITY"].get("SECRET_KEY", str(uuid4()))

        config["DATABASE"] = {"URI": self.DATABASE_URI}

        if self.MPV_IPC_SOCKET is not None:
            config["MVP"] = {"IPC_SOCKET": self.MPV_IPC_SOCKET}

        config["SECURTIY"] = {"SECRET_KEY": self.SECRET_KEY}
        config["SERVER"] = {"HOST": self.HOST, "PORT": str(self.PORT)}

        config.write(file)

        # save a singleton
        Config.current_config = self


def get_current_config():
    return Config.current_config
