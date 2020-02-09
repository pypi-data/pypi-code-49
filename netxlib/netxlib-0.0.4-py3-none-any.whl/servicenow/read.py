# Import libraries
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

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# retrieve CMDB CI record from Incident ticket

def cmdb_from_inc(ticket_sys_id):
    # Read Incident record
    servicenow_url = 'https://%s.service-now.com/api/now/table/incident/%s?sysparm_display_value=true' % (servicenow_instance, ticket_sys_id)
    status_code, response_headers, response_cookies, http_response = rest.get_200(servicenow_url, servicenow_user, servicenow_pass, headers, debug)
    time.sleep(2)

    # Read CMDB record using fields retrievd from Incident record
    cmdb_servicenow_url = http_response['result']['cmdb_ci']['link']
    short_description = http_response['result']['short_description']

    status_code, response_headers, response_cookies, http_response = rest.get_200(cmdb_servicenow_url, servicenow_user, servicenow_pass, headers, debug)
    time.sleep(2)

    cmdb_ci_name = http_response['result']['name']
    cmdb_ci_ip_address = http_response['result']['ip_address']
    cmdb_ci_sys_id = http_response['result']['sys_id']

    print ("Host is: %s - IP is %s" %(cmdb_ci_name, cmdb_ci_ip_address))
    return (cmdb_ci_name, cmdb_ci_ip_address, cmdb_ci_sys_id, short_description)

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
