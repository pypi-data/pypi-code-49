import json
import boonnano
import urllib3

"""a collection of methods to standardize/isolate http request/response"""

def outgoing_data(response):

    if response.status != 200:
        return False, '{}:{}'.format(response.status, response.reason)
    try:
        content_type = response.headers['Content-Type']
        if content_type == 'application/json':
            if response.data == b'':
                return True, '{}'
            return True, json.loads(response.data.decode('utf-8'))
        elif content_type == 'application/octet-stream':
            return True, response.data
        else:
            return False, "unhandled Content-Type: {}".format(content_type)

    except Exception as e:
        return False, e


def simple_get(nano_handle, get_cmd):

    try:
        response = nano_handle.http.request(
            'GET',
            get_cmd,
            headers={
                'x-token': nano_handle.api_key,
                'Content-Type': 'application/json'
            }
        )
    except Exception as e:
        return False, 'request failed'

    return outgoing_data(response)


def multipart_post(nano_handle, post_cmd, fields=None):

    multi_fields = urllib3.filepost.encode_multipart_formdata(fields)

    try:
        response = nano_handle.http.request(
            'POST',
            post_cmd,
            headers={
                'x-token': nano_handle.api_key
            },
            fields=fields
        )
    except Exception as e:
        return False, 'request failed: {}'.format(e)

    return outgoing_data(response)


def simple_post(nano_handle, post_cmd, body=None):

    try:
        response = nano_handle.http.request(
            'POST',
            post_cmd,
            headers={
                'x-token': nano_handle.api_key,
                'Content-type': 'application/json'
            },
            body=body
        )
    except Exception as e:
        return False, 'request failed: {}'.format(e)

    return outgoing_data(response)


def simple_delete(nano_handle, delete_cmd):

    try:
        response = nano_handle.http.request(
            'DELETE',
            delete_cmd,
            headers={
                'x-token': nano_handle.api_key
            }
        )
    except Exception as e:
        return False, 'request failed: {}'.format(e)

    return outgoing_data(response)
