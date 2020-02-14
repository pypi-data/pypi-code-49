#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
This module provides authorization generator described in
http://gollum.baidu.com/IamApiServiceGuide
Author: dengxiaochao@baidu.com
"""
import datetime
import hashlib
import hmac
import urllib


class ClassBceSigner(object):
    """
    request to be signed with an BCE signature
    """

    def __init__(self, access_key, secret_key):
        self.access_key = access_key.encode()
        self.secret_key = secret_key.encode()

    def gen_authorization(self, request, timestamp=None, expire_period=180000):
        """
        generate authorization string
        if not specify timestamp, then use current time;
        """
        signedheaders = []
        if 'headers' in request:
            signedheaders = list(
                key.lower() for key in request["headers"].keys() if key != ''
            )
            signedheaders.sort()
        authorization = build_authorization(
            self.access_key, signedheaders, expire_period, timestamp
        )
        signingkey = self._calc_signingkey(authorization)
        signature = self._calc_signature(signingkey, request, signedheaders)
        authorization["signature"] = signature
        return serialize_authorization(authorization)

    def gen_signature(self, request, timestamp=None, expire_period=180000):
        """
        genreate signature string
        """
        signedheaders = []
        if "headers" in request:
            signedheaders = list(
                key.lower() for key in request["headers"].keys() if key != ''
            )
            signedheaders.sort()
        authorization = build_authorization(
            self.access_key,
            signedheaders, expire_period, timestamp
        )
        signingkey = self._calc_signingkey(authorization)
        return signingkey

    def authenticate(self, authorization, request):
        """
        autenticate a request.
        calcaulate request signature, and compare with authorization
        """
        signingkey = self._calc_signingkey(authorization)
        signature = self._calc_signature(
            signingkey, request, authorization['signedheaders']
        )
        return signature == authorization['signature']

    @staticmethod
    def get_utf8_value(value):
        """
        Get the UTF8-encoded version of a value.
        """
        if not isinstance(value, (str, unicode)):
            value = str(value)
        if isinstance(value, unicode):
            return value.encode('utf-8')
        else:
            return value

    @staticmethod
    def canonical_qs(params):
        """
        Construct a sorted, correctly encoded query string
        """
        keys = list(params)
        keys.sort()
        pairs = []
        for key in keys:
            if key == "authorization":
                continue
            val = ClassBceSigner.normalized(params[key])
            pairs.append(urllib.quote(key, safe='') + '=' + val)
        return '&'.join(pairs)

    @staticmethod
    def canonical_header_str(headers, signedheaders=None):
        """
        calculate canonicalized header string
        """
        headers_norm_lower = dict()
        for (key, value) in headers.iteritems():
            key_norm_lower = ClassBceSigner.normalized(key.lower())
            value_norm_lower = ClassBceSigner.normalized(value.strip())
            headers_norm_lower[key_norm_lower] = value_norm_lower
        keys = list(headers_norm_lower)
        keys.sort()
        if "host" not in keys:
            raise MissingHeaderError()
        header_list = []
        default_signed = (
            'host', 'content-length', 'content-type', 'content-md5'
        )
        if signedheaders:
            for key in signedheaders:
                key = ClassBceSigner.normalized(key.lower())
                if key not in keys:
                    raise MissingHeaderError()
                if headers_norm_lower[key]:
                    header_list.append(key + ':' + headers_norm_lower[key])
        else:
            for key in keys:
                if key.startswith('x-bce-') or key in default_signed:
                    header_list.append(key + ':' + headers_norm_lower[key])
        return '\n'.join(header_list)

    @staticmethod
    def normalized_uri(uri):
        """
        Construct a normalized(except slash '/') uri
        eg. /json-api/v1/example/ ==> /json-api/v1/example/
        """
        return urllib.quote(ClassBceSigner.get_utf8_value(uri), safe='-_.~/')

    @staticmethod
    def normalized(msg):
        """
        Construct a normalized uri
        """
        return urllib.quote(ClassBceSigner.get_utf8_value(msg), safe='-_.~')

    def _calc_signingkey(self, auth):
        """ Get a a signing key """
        string_to_sign = '/'.join(
            (
                auth['version'], auth['access'],
                auth['timestamp'], auth['period']
            )
        )
        signingkey = hmac.new(
            self.secret_key, self.get_utf8_value(string_to_sign),
            hashlib.sha256
        ).hexdigest()
        return signingkey

    def _calc_signature(self, key, request, signedheaders):
        """Generate BCE signature string."""
        if not request.get('method'):
            raise EmptyMethodError()
        if not request.get('uri'):
            raise EmptyURIError()
        # Create canonical request
        params = {}
        headers = {}
        if 'params' in request:
            params = request['params']
        if 'headers' in request:
            headers = request['headers']
        crs = '\n'.join(
            (
                request['method'].upper(),
                self.normalized_uri(request['uri']),
                self.canonical_qs(params),
                ClassBceSigner.canonical_header_str(headers, signedheaders)
            )
        )
        signature = hmac.new(key, crs, hashlib.sha256).hexdigest()
        return signature


def load_authorization(auth_str):
    """ return a dict contains version, access, timestamp, period
        param: auth: Authorization string
    """
    auth_split = auth_str.split('/')
    if len(auth_split) != 6:
        raise InvalidAuthorizationError()
    version = auth_split[0]
    access = auth_split[1]
    timestamp = auth_split[2]
    period = auth_split[3]
    signedheaders = []
    if auth_split[4]:
        signedheaders = auth_split[4].split(';')
    signature = auth_split[5]

    if version != "bce-auth-v1":
        raise InvalidAuthorizationError()
    if not is_utc_timestamp(timestamp):
        raise InvalidAuthorizationError()
    if not is_integer(period):
        raise InvalidAuthorizationError()

    req_datetime = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    now_datetime = datetime.datetime.utcnow()
    if now_datetime - req_datetime > datetime.timedelta(seconds=int(period)):
        raise RequestExpiredError()

    auth = {}
    auth['version'] = version
    auth['access'] = access
    auth['timestamp'] = timestamp
    auth['period'] = period
    auth['signedheaders'] = signedheaders
    auth['signature'] = signature
    return auth


def serialize_authorization(auth):
    """
    serialize Authorization object to authorization string
    """
    val = "/".join(
        (auth['version'], auth['access'], auth['timestamp'], auth['period'],
            ";".join(auth['signedheaders']), auth['signature'])
    )
    return ClassBceSigner.get_utf8_value(val)


def build_authorization(accesskey, signedheaders, period=1800, timestamp=None):
    """
    build Authorization object
    """
    auth = {}
    auth['version'] = "bce-auth-v1"
    auth['access'] = accesskey
    if not timestamp:
        auth['timestamp'] = datetime.datetime.utcnow().strftime(
            '%Y-%m-%dT%H:%M:%SZ'
        )
    else:
        auth['timestamp'] = timestamp
    auth['period'] = str(period)
    auth['signedheaders'] = signedheaders
    return auth


def is_utc_timestamp(timestamp):
    """
    check if timestamp is with utc format
    """
    try:
        datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        return True
    except ValueError:
        return False


def is_integer(value):
    """
    check if value is an interger
    """
    try:
        val = int(value)
        return True
    except ValueError:
        return False


class ValidationError(Exception):
    """
    base Error class
    """
    def __init__(self, message):
        self.message = message
        super(ValidationError, self).__init__(message)


class MissingHeaderError(ValidationError):
    """
    missing required headers
    """
    def __init__(self):
        self.message = "missing signing headers"
        super(MissingHeaderError, self).__init__(self.message)


class EmptyMethodError(ValidationError):
    """
    method is empty
    """
    def __init__(self):
        self.message = "method is empty"
        super(EmptyMethodError, self).__init__(self.message)


class EmptyURIError(ValidationError):
    """
    uri is empty
    """
    def __init__(self):
        self.message = "uri is empty"
        super(EmptyURIError, self).__init__(self.message)


class InvalidAuthorizationError(ValidationError):
    """
    invalid authorization string
    """
    def __init__(self):
        self.message = "invalid authorization string"
        super(InvalidAuthorizationError, self).__init__(self.message)


class RequestExpiredError(ValidationError):
    """
    request has expired
    """
    def __init__(self):
        self.message = "Request Expired"
        super(RequestExpiredError, self).__init__(self.message)


def get_utc_time():
    """
    get utc time
    """
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
