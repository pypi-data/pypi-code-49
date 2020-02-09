# Import required modules
from netxlib import rest

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Delete new network
def object(instance, version, username, password, data, debug=0):
    infoblox_url = 'https://%s/wapi/%s/%s' % (instance,version, data)
    status_code, response_headers, http_response = rest.delete_200(infoblox_url, username, password, debug)
    return (status_code, response_headers, http_response)
