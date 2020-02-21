#!/bin/env python3
import requests


def get(endpoint, homeserver, **kwargs):
    access_token = kwargs.get('access_token', None)
    data = kwargs.get('data', None)
    params = kwargs.get('params', None)
    headers = kwargs.get('headers', None)
    args = {'url': f'{homeserver}{endpoint}'}
    args['headers'] = {}
    if data is not None:
        args['json'] = data
    if params is not None:
        args['params'] = params
    if headers is not None:
        args['headers'].update(headers)
    if access_token is not None:
        args['headers'].update({"Authorization": f"Bearer {access_token}"})
    request = requests.get(**args)
    return request


def post(endpoint, homeserver, **kwargs):
    access_token = kwargs.get('access_token', None)
    data = kwargs.get('data', None)
    params = kwargs.get('params', None)
    headers = kwargs.get('headers', None)
    args = {'url': f'{homeserver}{endpoint}'}
    args['headers'] = {}
    if data is not None:
        args['json'] = data
    if params is not None:
        args['params'] = params
    if headers is not None:
        args['headers'].update(headers)
    if access_token is not None:
        args['headers'].update({"Authorization": f"Bearer {access_token}"})
    request = requests.post(**args)
    return request
