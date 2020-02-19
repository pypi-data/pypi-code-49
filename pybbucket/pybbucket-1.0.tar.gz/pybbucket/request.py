import inspect
import json

import requests
from requests.auth import HTTPBasicAuth

import pybbucket.log as logger

log = logger.setup_custom_logger('root')


def print_request_details(url, headers, params=None, data=None, description=None):
    caller_function_name = inspect.stack()[1][3]
    if description is not None:
        log.info("{} - {} request to {}".format(description, caller_function_name.upper(), url))
    else:
        log.info("{} request to {}".format(caller_function_name.upper(), url))
    log.debug("Headers: {}".format(json.dumps(headers, indent=2)))
    if caller_function_name is "get":
        log.debug("Params: {}".format(json.dumps(params, indent=2)))
    elif caller_function_name in ["post", "put", "patch"]:
        log.debug("Payload: {}".format(json.dumps(json.loads(data), indent=2)))


def print_response_details(response):
    log.debug("Response code: {}".format(response.status_code))
    try:
        log.debug("Response body: {}".format(json.dumps(json.loads(response.text), indent=2)))
    except:  # TODO: add a specific exception here
        log.debug("Response body: {}".format(response.text))


def get(url, headers, params=None, credentials=None, description=None):
    print_request_details(url=url, headers=headers, params=params, description=description)
    if credentials is None:
        response = requests.get(url=url, params=params, headers=headers)
    else:
        response = requests.get(url=url, params=params, headers=headers, auth=HTTPBasicAuth(credentials[0],
                                                                                            credentials[1]))
    print_response_details(response)
    return response


def post(url, data, headers, credentials=None, description=None):
    print_request_details(url=url, headers=headers, data=data, description=description)
    if credentials is None:
        response = requests.post(url=url, data=data, headers=headers)
    else:
        response = requests.post(url=url, data=data, headers=headers, auth=HTTPBasicAuth(credentials[0],
                                                                                         credentials[1]))
    print_response_details(response)
    return response


def put(url, data, headers, credentials=None, description=None):
    print_request_details(url=url, headers=headers, data=data, description=description)
    if credentials is None:
        response = requests.put(url=url, data=data, headers=headers)
    else:
        response = requests.put(url=url, data=data, headers=headers, auth=credentials)
    print_response_details(response)
    return response


def patch(url, data, headers, description=None):
    print_request_details(url=url, headers=headers, data=data, description=description)
    response = requests.patch(url=url, data=data, headers=headers)
    print_response_details(response)
    return response


def delete(url, headers, description=None):
    print_request_details(url=url, headers=headers, description=description)
    response = requests.delete(url=url, headers=headers)
    print_response_details(response)
    return response
