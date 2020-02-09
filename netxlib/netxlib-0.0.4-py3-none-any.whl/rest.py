"""

Define common functions used for HTTP REST calls

GET
    - 200

PUT
    - 200

POST
    - 201

DELETE
    - 200

"""

# Import required modules
import json
import requests
requests.packages.urllib3.disable_warnings()


# Common HTTP Processing
def process_http(url, response, code, debug):
    if debug >= 4:
        print('DEBUG - URL: %s' % url)
        print('DEBUG - HTTP Status Code: ', response.status_code)
        print('DEBUG - HTTP Response Headers: ', response.headers)
        print('DEBUG - HTTP Response Body: ', response.text)

    if response.status_code != code:
        http_cookies = "EmptyJar"
        return (response.status_code, response.headers, http_cookies, response.text)
    else:
        return (response.status_code, response.headers, response.cookies, response.json())


# Process HTTP GET request, expect response code 200
def get_200(url, username, password, headers, debug):
    response = requests.get(url, auth=(username, password), headers=headers, verify=False)
    r1, r2, r3, r4 = process_http(url, response, 200, debug)
    return (r1, r2, r3, r4)


# Process HTTP PUT request, expect response code 200
def put_200(url, username, password, headers, data, cookies, debug):
    response = requests.put(url, auth=(username, password), headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
    r1, r2, r3, r4 = process_http(url, response, 200, debug)
    return (r1, r2, r3, r4)


# Process HTTP POST request, expect response code 201
def post_201(url, username, password, headers, data, debug):
    response = requests.post(url, auth=(username, password), headers = headers, data = json.dumps(data), verify=False)
    r1, r2, r3, r4 = process_http(url, response, 201, debug)
    return (r1, r2, r3, r4)


# Process HTTP DELETE request, expect response code 200
def delete_200(url, username, password, debug):
    response = requests.delete(url, auth=(username, password), verify=False)
    r1, r2, r3, r4 = process_http(url, response, 200, debug)
    return (r1, r2, r3, r4)
