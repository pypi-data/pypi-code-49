# Import required modules
from netxlib import rest

# Setup common variables
headers = {
    'content-type':'application/json',
    'accept': 'application/json'
}

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Create new network
def network(instance, version, username, password, data, debug=0):
    infoblox_url = 'https://%s/wapi/%s/network' % (instance,version)
    status_code, response_headers, http_response = rest.post_201(infoblox_url, username, password, headers, data, debug)
    return (status_code, response_headers, http_response)

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Create new DHCP Range
def range(instance, version, username, password, data, debug=0):
    infoblox_url = 'https://%s/wapi/%s/range' % (instance,version)
    status_code, response_headers, http_response = rest.post_201(infoblox_url, username, password, headers, data, debug)
    return (status_code, response_headers, http_response)

