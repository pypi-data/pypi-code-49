"""Python module containing helper http utility functions """

import json
import requests
from requests.auth import HTTPBasicAuth

from f5teem import constants
from f5teem.exceptions import HTTPError

def make_request(host, uri, **kwargs):
    """Make HTTP request (HTTP/S)

    Parameters
    ----------
    uri : str
        the URI where the request should be made
    **kwargs :
        optional keyword arguments

    Keyword Arguments
    -----------------
    port : int
        the port to use
    method : str
        the HTTP method to use
    headers : str
        the HTTP headers to use
    body : str
        the HTTP body to use
    body_content_type : str
        the HTTP body content type to use
    bool_response : bool
        return boolean based on HTTP success/failure
    basic_auth : dict
        use basic auth: {'user': 'foo', 'password': 'bar'}

    Returns
    -------
    dict
        a dictionary containing the status code, JSON response
        {
            'response': {},
            'status_code': 200
        }
    """

    port = kwargs.pop('port', 443)
    method = kwargs.pop('method', 'GET').lower()
    headers = {'User-Agent': constants.USER_AGENT}
    # add any supplied headers, allow the caller to override default headers
    headers.update(kwargs.pop('headers', {}))

    # check for body, normalize
    body = kwargs.pop('body', None)
    body_content_type = kwargs.pop('body_content_type', 'json')  # json (default), raw
    if body and body_content_type == 'json':
        headers.update({'Content-Type': 'application/json'})
        body = json.dumps(body)

    # check for auth options
    auth = None
    basic_auth = kwargs.pop('basic_auth', None)
    if basic_auth:
        auth = HTTPBasicAuth(basic_auth['user'], basic_auth['password'])

    url = 'https://%s:%s%s' % (host, port, uri)

    # make request
    response = requests.request(
        method,
        url,
        headers=headers,
        data=body,
        auth=auth,
        timeout=constants.HTTP['TIMEOUT']['DEFAULT'],
        verify=constants.HTTP['VERIFY']
    )

    # return boolean response, if requested
    if kwargs.pop('bool_response', False):
        return response.ok

    status_code = response.status_code
    status_reason = response.reason

    # determine response body using the following logic
    # 1) if the content-length header exists and is 0: set to empty dict
    # 2) response is valid JSON: decode JSON to native python object (dict, list)
    headers = response.headers
    if (status_code == 204) or \
            ('content-length' in headers.keys() and headers['content-length'] == '0'):
        response_body = None
    else:
        response_body = response.json()


    # raise exception on 4xx and 5xx status code(s)
    if str(status_code)[:1] in ['4', '5']:
        raise HTTPError({
            'message': 'Failed HTTP Request',
            'url': url,
            'status_code': status_code,
            'status_reason': status_reason,
            'response': response_body
        })

    # finally, simply return
    return {'response': response_body, 'status_code': status_code}
