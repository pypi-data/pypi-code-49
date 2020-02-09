# Import required modules
from netxlib import rest

# ------------------------------------- ------------------------------------- ------------------------------------- -------------------------------------

# Update existing network device
def networkdevice(instance, username, password, data, debug=0):

    headers = {
        'content-type':'application/json',
        'accept': 'application/json',
        'X-CSRF-Token' : 'fetch'
    }

    host_name = data['NetworkDevice']['name']

    ise_url = 'https://%s:9060/ers/config/networkdevice?filter=name.CONTAINS.%s' % (instance, host_name)
    status_code, response_headers, cookies, http_response = rest.get_200(ise_url, username, password, headers, debug)
    cookies = None

    if http_response['SearchResult']['resources']:
        ise_put_url = http_response['SearchResult']['resources'][0]['link']['href']
        status_code, response_headers, cookies, http_response = rest.get_200(ise_put_url, username, password, headers, debug)

        token = response_headers['X-CSRF-Token']

        headers = {
            'content-type':'application/json',
            'accept': 'application/json',
            'X-CSRF-Token' : token
        }

        status_code, response_headers, cookies, http_response = rest.put_200(ise_put_url, username, password, headers, data, cookies, debug)
    else:
        status_code = 666
        response_headers = "NoHeaders"
        http_response = "NoResponse"

    return (status_code, response_headers, http_response)

