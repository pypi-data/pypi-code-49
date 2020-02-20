# -*- encoding: utf-8 -*-
import os
import yaml

from suite_py.lib.singleton import Singleton


class Config(metaclass=Singleton):
    _config = {}

    def __init__(self):
        pass

    def load(self):
        with open(
            os.path.join(os.environ["HOME"], ".suite_py/config.yml")
        ) as configfile:
            self._config = yaml.safe_load(configfile)

        self._config["user"]["projects_home"] = os.path.join(
            os.environ["HOME"], self._config["user"]["projects_home"]
        )

        self._config["user"].setdefault("review_channel", "#review")

        self._config["user"].setdefault("deploy_channel", "#deploy")

        self._config["user"].setdefault("default_slug", "PRIMA-XXX")

        self._config["user"].setdefault("captainhook_timeout", 30)  # This is in seconds

        self.load_local_config()

        return self._config

    def load_local_config(self):
        local_conf_path = os.path.join(os.curdir, ".suite_py.yml")
        try:
            with open(local_conf_path) as f:
                local_conf = yaml.safe_load(f)

        except FileNotFoundError:
            return

        for key, value in local_conf["user"].items():
            self._config["user"][key] = value
