# Import libraries
import json
import time

from django.conf import settings
from netxlib import rest

# Global variables
servicenow_user = settings.SERVICENOW_USER
servicenow_pass = settings.SERVICENOW_PASS
servicenow_instance = settings.SERVICENOW_INSTANCE
debug = settings.DEBUG_LEVEL

headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}

cookies = ''

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
