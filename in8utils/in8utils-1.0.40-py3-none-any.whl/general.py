import inspect
import os
import time

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


def load_config_to_env(ref: str, project: str, config_url: str = 'http://buscamax-data.buscamilhas.com', force_az: str = None, headers: dict = {}):
    az = Aws.get_az() or force_az

    if not az:
        try:
            root_path = os.path.dirname(os.path.abspath((inspect.stack()[1])[1]))
            dotenv.load_dotenv(f"{root_path}/.env")
        except:
            pass
        return

    i = 1
    while True:
        try:
            ambient = 'prod' if az.upper() in ['2B', '2C', '2A'] else 'homolog'
            resp = requests.get(f"{config_url}/config/{ambient}/{az}/{project}/{ref}", headers=headers)

            print(f"""
resp.status_code = {resp.status_code}
resp.url = {resp.url}
resp.content = {resp.content}
            """)

            config: dict = resp.json()

            for key, value in config.items():
                os.environ[key] = str(value)

            return
        except:
            print(f"fail in get config. retry in {i} seconds")
            time.sleep(i)
            i *= 2
