import pytest
import jwt

from http import HTTPStatus
from unittest import TestCase
from unittest.mock import MagicMock, patch

from dli.client.exceptions import AuthenticationFailure, DatalakeException
from dli.client.dli_client import Session

valid_token = jwt.encode({"exp": 9999999999}, 'secret')

class TestAuth(TestCase):

    @pytest.fixture(autouse=True)
    def session(self):
        environ = MagicMock(catalogue='http://test.local/', accounts='')
        self.session = Session('api_key', environ, None, valid_token)

    def test_auth(self):
        self.session.send = MagicMock()
        self.session._get_auth_key()
        prep_request = self.session.send.call_args[0][0]
        assert prep_request.headers['Authorization'] == (
            'Bearer api_key'
        )

    def test_handle_auth_error(self):
        self.session.post = MagicMock()
        self.session.post.side_effect = MagicMock(
            side_effect=DatalakeException
        )

        with self.assertRaises(AuthenticationFailure) as cm:
            self.session._get_auth_key()
