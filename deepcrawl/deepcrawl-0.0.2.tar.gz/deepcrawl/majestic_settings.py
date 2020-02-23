from requests.auth import HTTPBasicAuth
import json

from .api_endpoints import *
from .api_requests import *


class MajesticSettings:
    def __init__(self, majestic_settings):
        
        majestic_settings_fields = ['enabled', 'max_rows', 'use_historic_data', 'use_root_domain']
        
        for key, value in majestic_settings.items():
            if key in majestic_settings_fields:
                setattr(self, key, value)


