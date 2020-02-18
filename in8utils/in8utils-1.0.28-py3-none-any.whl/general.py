import inspect
import os
import dotenv
import requests
import json

from .aws import Aws


def dumps(to_dump):
    def dump(obj):
        return obj.__dict__

    return json.dumps(to_dump, indent=4, default=dump, ensure_ascii=False)


class AtomicCounter:
    def __init__(self):
        self.counter = 0

    def count(self):
        self.counter += 1
        return self.counter


def load_config_to_env(ref: str, config_url: str = 'http://10.10.17.211:9005', force_az: str = None):
    az = Aws.get_az() or force_az

    if not az:
        try:
            root_path = os.path.dirname(os.path.abspath((inspect.stack()[1])[1]))
            dotenv.load_dotenv(f"{root_path}/.env")
        except:
            pass
        return

    ambient = 'prod' if az in ['2B', '2C', '2A'] else 'staging'
    config: dict = requests.get(f"{config_url}/config/{ambient}/{az}/{ref}").json()

    for key, value in config.items():
        os.environ[key] = str(value)
