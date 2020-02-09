# Import required modules
from netxlib import rest

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Search Infoblox for entries using MAC address filter
def search_by_mac_address(instance, version, username, password, mac, debug=0):
    headers = None
    infoblox_url = 'https://%s/wapi/%s/search?mac_address=%s' % (instance,version,mac)
    status_code, response_headers, cookies, http_response = rest.get_200(infoblox_url, username, password, headers, debug)
    return (status_code, response_headers, http_response)

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Search Infoblox for entries using network filter
def search_by_ip_address(instance, version, username, password, network, debug=0):
    headers = None
    infoblox_url = 'https://%s/wapi/%s/search?address=%s' % (instance,version,network)
    status_code, response_headers, cookies, http_response = rest.get_200(infoblox_url, username, password, headers, debug)
    return (status_code, response_headers, http_response)

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Search Infoblox for entries using network filter
def network(instance, version, username, password, network, debug=0):
    headers = None
    infoblox_url = 'https://%s/wapi/%s/network?network=%s' % (instance,version,network)
    status_code, response_headers, cookies, http_response = rest.get_200(infoblox_url, username, password, headers, debug)
    return (status_code, response_headers, http_response)

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
# Search Infoblox for entries using network filter
def range(instance, version, username, password, network, debug=0):
    headers = None
    infoblox_url = 'https://%s/wapi/%s/range?network=%s&_return_fields=network,member,failover_association,options,comment,extattrs,start_addr,end_addr' % (instance,version,network)
    status_code, response_headers, cookies, http_response = rest.get_200(infoblox_url, username, password, headers, debug)
    return (status_code, response_headers, http_response)

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------
