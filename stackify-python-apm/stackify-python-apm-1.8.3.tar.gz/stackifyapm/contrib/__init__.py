import json
import os

from stackifyapm.base import Client
from stackifyapm.conf import constants
from stackifyapm.instrumentation.control import instrument


def make_client(**defaults):
    config = defaults.get("STACKIFY_APM", {})
    defaults['base_dir'] = defaults.get("BASE_DIR") or defaults.get("base_dir") or os.getcwd()
    config_file = defaults.get("CONFIG_FILE") or defaults.get("config_file") or constants.DEFAULT_CONFIG_FILE

    try:
        with open(config_file) as json_file:
            data = json.load(json_file)
            defaults.update(data)
            defaults['base_dir'] = data.get('base_dir') or defaults['base_dir']
    except Exception:
        pass

    defaults['config_file'] = config_file

    return Client(config, **defaults)


class StackifyAPM(object):
    """
    Generic application for StackifyAPM.
    """
    def __init__(self, **defaults):
        self.func_name = None
        self.context = None
        self.client = make_client(**defaults)
        instrument(self.client)

    def clean_up(self):
        self.client.transport.send_all()
