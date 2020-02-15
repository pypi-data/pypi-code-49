import os
from dataclasses import dataclass
from datetime import timedelta
from configparser import ConfigParser
from typing import TextIO
from uuid import uuid4

from xdg import XDG_DATA_HOME


@dataclass
class Default:
    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Database
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_URI: str = f"sqlite:///{XDG_DATA_HOME}/escarpolette/db.sqlite"

    # MPV
    if os.environ.get("ANDROID_DATA") or os.environ.get("ANDROID_ROOT"):
        MPV_IPC_SOCKET: str = "/data/data/com.termux/files/home/.mpv-socket"
    else:
        MPV_IPC_SOCKET: str = "/tmp/mpv-socket"

    # Authentication
    REMEMBER_COOKIE_DURATION: timedelta = timedelta(days=390)  # ~13 months


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
        self.MPV_IPC_SOCKET = config["MPV"].get("IPC_SOCKET", self.MPV_IPC_SOCKET)
        self.SECRET_KEY = config["SECURITY"].get("SECRET_KEY", str(uuid4()))

        config["DATABASE"] = {"URI": self.DATABASE_URI}
        config["MPV"] = {"IPC_SOCKET": self.MPV_IPC_SOCKET}
        config["SECURITY"] = {"SECRET_KEY": self.SECRET_KEY}
        config["SERVER"] = {"HOST": self.HOST, "PORT": str(self.PORT)}

        file.truncate(0)
        config.write(file)

        # save a singleton
        Config.current_config = self


def get_current_config():
    return Config.current_config
