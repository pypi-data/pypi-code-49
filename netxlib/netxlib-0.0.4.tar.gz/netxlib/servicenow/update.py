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
# Update Incident record
def update_inc(ticket_sys_id, payload):
    # construct payload
    data = {
        "comments" : payload
    }

    # Update Incident table from payload
    servicenow_url = 'https://%s.service-now.com/api/now/table/incident/%s' % (servicenow_instance, ticket_sys_id)
    status_code, response_headers, response_cookies, http_response = rest.put_200(servicenow_url, servicenow_user, servicenow_pass, headers, data, cookies, debug)
    time.sleep(2)
    return None

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
