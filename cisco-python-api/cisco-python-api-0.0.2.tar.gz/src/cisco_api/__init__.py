from .cisco_api import CMXClient

from . import cmx_api

import urllib3
urllib3.disable_warnings()

__all__ = ['CMXClient']
