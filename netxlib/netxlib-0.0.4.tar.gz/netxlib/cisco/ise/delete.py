# Import Modules required for this library
import requests

requests.packages.urllib3.disable_warnings()

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------

# Search Infoblox for entries using MAC address filter
def macadress(instance, version, username, password, mac, debug=0):

    infoblox_url = 'https://%s/wapi/%s/search?mac_address=%s' % (instance,version,mac)

    # Send HTTP GET request to Infoblox
    if debug >= 4:
        print ("DEBUG - Sending Data to Infoblox via: \n" + infoblox_url +"\n")
    response = requests.get(infoblox_url, auth=(username, password), verify=False)

    # Check for HTTP response codes other than 200
    if response.status_code != 200:
        if debug >= 4:
            print('Status:', response.status_code)
            print('Headers:', response.headers)
            print('Error Response:', response.text)
        http_response = response.text
    else:
        http_response = response.json()

    return (response.status_code, response.headers, http_response)

# Search Infoblox for entries using network filter
def network(instance, version, username, password, network, debug=0):

    infoblox_url = 'https://%s/wapi/%s/search?address=%s' % (instance,version,network)

    # Send HTTP GET request to Infoblox
    if debug >= 4:
        print ("DEBUG - Sending Data to Infoblox via: \n" + infoblox_url +"\n")
    response = requests.get(infoblox_url, auth=(username, password), verify=False)

    # Check for HTTP response codes other than 200
    if response.status_code != 200:
        if debug >= 4:
            print('Status:', response.status_code)
            print('Headers:', response.headers)
            print('Error Response:', response.text)
        http_response = response.text
    else:
        http_response = response.json()

    return (response.status_code, response.headers, http_response)
