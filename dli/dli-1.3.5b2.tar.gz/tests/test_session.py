import pytest
import unittest
import jwt

from unittest.mock import MagicMock
import httpretty

from dli import __version__
from dli.client.dli_client import Session
from dli.client.exceptions import (
    DatalakeException,
    InsufficientPrivilegesException,
    UnAuthorisedAccessException
)


environ = MagicMock(catalogue='http://catalogue.local', accounts='')
valid_token = jwt.encode({"exp": 9999999999}, 'secret')
expired_token = jwt.encode({"exp": 1111111111}, 'secret')

class SessionTestCase(unittest.TestCase):

    def test_can_decode_valid_jwt_token(self):
        ctx = Session(
            "key",
            environ,
            None,
            valid_token
        )
        self.assertFalse(ctx.has_expired)

    def test_can_detect_token_is_expired(self):
        ctx = Session(
            "key",
            environ,
            None,
            expired_token
        )
        self.assertTrue(ctx.has_expired)


class SessionRequestFactoryTestCase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def session(self):
        self.session = Session(None, environ, None, valid_token)

    @httpretty.activate
    def test_response_403_raises_InsufficientPrivilegesException(self):
        response_text = 'Insufficient Privileges'
        httpretty.register_uri(
            httpretty.GET, 'http://catalogue.local/test',
            status=403, body=response_text
        )

        with self.assertRaises(InsufficientPrivilegesException):
            self.session.get('/test')

    @httpretty.activate
    def test_response_401_raises_UnAuthorisedAccessException(self):
        response_text = 'UnAuthorised Access'
        httpretty.register_uri(
            httpretty.GET, 'http://catalogue.local/test',
            status=401, body=response_text
        )


        with self.assertRaises(UnAuthorisedAccessException):
            self.session.get('/test')

    @httpretty.activate
    def test_response_500_raises_DatalakeException(self):
        response_text = 'Datalake server error'
        httpretty.register_uri(
            httpretty.GET, 'http://catalogue.local/test',
            status=500, body=response_text
        )

        with self.assertRaises(DatalakeException):
            self.session.get('/test')

    @httpretty.activate
    def test_sdk_version_is_included_in_header(self):
        httpretty.register_uri(
            httpretty.GET, 'http://catalogue.local/__api/',
            status=200, body="response"
        )
        # issue a request
        self.session.get('/__api/')

        request = httpretty.last_request()
        self.assertTrue("X-Data-Lake-SDK-Version" in request.headers)
        self.assertEqual(request.headers["X-Data-Lake-SDK-Version"], str(__version__))
