import os
from distutils.util import strtobool


def bool_getenv(key, default):
    return bool(strtobool(os.environ[key])) if key in os.environ else default
