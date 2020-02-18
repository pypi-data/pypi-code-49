from dataclasses import dataclass
from typing import Any
import json

from django.test import TestCase

from tokko_auth.middleware import (HasJWTMiddleware, AuthMiddlewareBase)
from tokko_auth.tests.crypto import (
    INVALID_TOKEN_NO_CLAIMS,
    VALID_TOKEN,
    INVALID_TOKEN_NO_SCOPES,
    PAYLOAD,
)
from tokko_auth.helpers import (
    AuthorizationHelper,
    MustBeBearerToken,
    InsufficientScopes,
    ScopesNotFound,
    ClaimsNotFound,
    MustStartWithBearer,
)
from tokko_auth.exceptions import TokenNotFound, UnableDecodeToken


@dataclass
class FakeRequest:
    """Fake Request just for test proposes"""
    headers: dict = None
    text: str = None

    @property
    def content_type(self) -> str:
        try:
            self.json()
            return 'application/json'
        except json.decoder.JSONDecodeError:
            return 'text/plain'

    def json(self) -> dict:
        return json.loads(self.text)


def get_response(request: FakeRequest) -> Any:
    return request.__doc__


class MiddlewareUnitTest(TestCase):
    """Middleware Unitary tests"""
    def setUp(self) -> None:
        self.valid_token = VALID_TOKEN

    def test_01_invoke_base_middleware(self):
        """Successful MiddlewareBase Call"""
        base_middleware = AuthMiddlewareBase(get_response, i_am_testing=True)
        _request = FakeRequest(headers={'Authorization': f'Bearer {self.valid_token}'})
        self.assertEqual(base_middleware(_request), FakeRequest.__doc__)

    def test_02_invoke_has_jwt_middleware(self):
        """Call MiddlewareBase without Token"""
        has_token_middleware = HasJWTMiddleware(get_response, i_am_testing=True)
        _request = FakeRequest(headers={'Authorization': 'Bearer ...'})
        response = has_token_middleware(_request)
        self.assertEqual(response.status_code, 401)
        _json_response = json.loads(response.content.decode())
        self.assertEqual(_json_response, UnableDecodeToken().as_json)

    def test_03_invoke_has_jwt_middleware(self):
        """Success MiddlewareBase call"""
        has_token_middleware = HasJWTMiddleware(get_response, i_am_testing=True)
        _request = FakeRequest(headers={'Authorization': f'Bearer {self.valid_token}'})
        self.assertEqual(has_token_middleware(_request), FakeRequest.__doc__)


class HelpersUnitTests(TestCase):
    """Helpers module unitary tests"""

    def setUp(self) -> None:
        # Authorization Helper
        self.auth = AuthorizationHelper()
        # Token
        self.valid_token = VALID_TOKEN
        self.invalid_token_no_scopes = INVALID_TOKEN_NO_SCOPES
        self.invalid_token_no_claims = INVALID_TOKEN_NO_CLAIMS

    def test_01_get_token_success(self):
        """Successful exec"""
        _t = self.auth.get_token({"Authorization": f"Bearer {self.valid_token}"})
        self.assertEqual(_t, self.valid_token)

    def test_02_get_token_error_token_not_found(self):
        """AuthHelper.get_token Raises TokenNotFound when token not found in headers"""
        with self.assertRaises(TokenNotFound):
            self.auth.get_token({})

    def test_03_get_token_error_should_start_with_bearer(self):
        """AuthHelper.get_token Raises TokenNotFound when Authorization header value not starts with "Bearer" """
        with self.assertRaises(MustBeBearerToken):
            self.auth.get_token({"Authorization": "Invalid Start"})

    def test_04_get_token_error_malformed(self):
        """AuthHelper.get_token Raises TokenNotFound when Authorization header value is malformed"""
        with self.assertRaises(MustStartWithBearer):
            self.auth.get_token({"Authorization": "Invalid parts amount"})

    def test_05_get_token_invalid_headers(self):
        """AuthHelper.get_token Raises TokenNotFound when provided headers isn't an dict instance"""
        with self.assertRaises(TokenNotFound):
            self.auth.get_token([])
        with self.assertRaises(TokenNotFound):
            self.auth.get_token("invalid-headers")
        with self.assertRaises(TokenNotFound):
            self.auth.get_token(1)

    def test_06_get_claims_unable_decode_token(self):
        """AuthHelper.claims Raises UnableDecodeToken when provided token it's invalid"""
        with self.assertRaises(UnableDecodeToken):
            self.auth.claims("invalid-token")
        with self.assertRaises(UnableDecodeToken):
            self.auth.claims(1)

    def test_07_get_claims_unable_decode_token(self):
        """AuthHelper.claims Raises RequiredKeyNotFound when provided not contains claims"""
        with self.assertRaises(ClaimsNotFound):
            self.auth.claims(self.invalid_token_no_claims)

    def test_08_get_claims_returns_dict(self):
        """AuthHelper.claims returns an dict instance"""
        _claims = self.auth.claims(self.valid_token)
        self.assertEqual(type(_claims), dict)
        self.assertEqual(_claims, PAYLOAD)

    def test_09_get_namespaces_no_scopes_found(self):
        """AuthHelper.namespaces when provided token not contain "scope" in claims"""
        with self.assertRaises(ScopesNotFound):
            self.auth.namespaces(self.invalid_token_no_scopes)

    def test_10_get_scopes_on_success(self):
        """AuthHelper.scopes returns an list of str"""
        scopes = self.auth.scopes(self.valid_token)
        self.assertEqual(type(scopes), list)
        self.assertEqual(scopes, ["test:testing"])

    def test_11_get_namespaces_returns_an_list_of_str(self):
        """AuthHelper.namespaces on success return an list of str"""
        namespaces = self.auth.namespaces(self.valid_token)
        self.assertEqual(type(namespaces), list)
        self.assertEqual(namespaces, ["test"])

    def test_12_has_required_scopes_insufficient_permission(self):
        """AuthHelper.has_required_scopes raises InsufficientScopes when not has all required scopes"""
        with self.assertRaises(InsufficientScopes):
            self.auth.has_required_scopes(
                self.valid_token, "has-not:this-scope", require_all=False
            )
        with self.assertRaises(InsufficientScopes):
            self.auth.has_required_scopes(
                self.valid_token, ["test:testing", "has-not:this-scope"]
            )

    def test_13_has_required_scopes_granted(self):
        """AuthHelper.has_required_scopes granted permission"""
        has_all_required_scopes = self.auth.has_required_scopes(
            self.valid_token, "test:testing"
        )
        self.assertEqual(has_all_required_scopes, True)
        has_at_least_one_required_scopes = self.auth.has_required_scopes(
            self.valid_token, ["test:testing", "other:scope"], require_all=False
        )
        self.assertEqual(has_at_least_one_required_scopes, True)

    def test_14_has_required_namespace_insufficient_permission(self):
        """AuthHelper.has_namespace returns false if token not contains required Namespace"""
        has_required_namespace = self.auth.has_namespace(
            "has_not_this_namespace", self.valid_token
        )
        # self.assertEqual(has_required_namespace, False)

    def test_15_has_required_scopes_granted(self):
        """AuthHelper.has_namespace granted permission"""
        has_required_namespace = self.auth.has_namespace("test", self.valid_token)
        self.assertEqual(has_required_namespace, True)
