""" Constants used throughout this package """

VERSION = '1.0.1'

USER_AGENT = 'f5-teem-python/%s' % (VERSION)
HTTP = {
    'VERIFY': False,
    'TIMEOUT': {
        'DEFAULT': 60
    },
    'STATUS_CODES': {
        'OK': 200,
        'ACCEPTED': 202
    }
}

ENVIRONMENTS = {
    'published': ['production', 'staging'],
    'env_var': 'F5_TEEM_API_ENVIRONMENT'
}
ENDPOINTS = {
    'anonymous': {
        'production': {
            # this endpoint and API key should be updated when prod endpoint is available
            'endpoint': 'product-tst.apis.f5networks.net',
            'api_key': 'Q8fX4FZtkQoHElKvwKjOv27nD8NEWECQ'
        },
        'staging': {
            'endpoint': 'product-tst.apis.f5networks.net',
            'api_key': 'Q8fX4FZtkQoHElKvwKjOv27nD8NEWECQ'
        }
    }
}
