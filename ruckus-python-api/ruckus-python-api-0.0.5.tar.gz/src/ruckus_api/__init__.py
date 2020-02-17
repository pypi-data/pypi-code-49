from .smartzone_api import SmartZoneClient
from .vspot_api import VSpotClient

from . import smartzone_api, vspot_api

import urllib3
urllib3.disable_warnings()

__all__ = ['SmartZoneClient', 'VSpotClient']
