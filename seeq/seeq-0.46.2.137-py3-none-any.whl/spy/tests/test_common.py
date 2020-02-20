import os

from seeq import spy
from seeq.spy import _login


def login(url=None):
    key_path = os.path.join(get_test_data_folder(), 'keys', 'agent.key')
    credentials = open(key_path, "r").read().splitlines()

    spy.login(credentials[0], credentials[1], url=url)


def get_client():
    return _login.client


def get_test_data_folder():
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', 'sq-run-data-dir'))
