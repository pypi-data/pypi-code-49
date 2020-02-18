import unittest

from django.test import TestCase
from graphene.test import Client

from tokko_auth.settings import (
    SAMPLES_ARE_ENABLE as using_samples,
    AUTH_API_NAMESPACE as api_namespace,
    AUTH_FULL_DISABLED as is_disabled
)
from tokko_auth.exceptions import TokenNotFound, ScopesNotFound, InsufficientScopes

from .schema import TESTING_SCHEMA
from .crypto import VALID_TOKEN, INVALID_TOKEN_NO_SCOPES
from .context import Context, AuthHeader


class ServiceTest(TestCase):
    """Service Tests"""

    def setUp(self) -> None:
        self.valid_token = VALID_TOKEN
        self.invalid_token_no_scopes = INVALID_TOKEN_NO_SCOPES
        self.gql_client = Client(TESTING_SCHEMA)

    def test_01_request_protected_query(self):
        ctx = Context(headers=AuthHeader(token=self.valid_token).authorization)
        res = self.gql_client.execute("query {protected_query}", context=ctx)
        self.assertEquals(res, {"data": {"protected_query": "You're Authorized!"}})

    def test_02_request_protected_query_without_credentials(self):
        res = self.gql_client.execute("query {protected_query}")
        err_message = res["errors"][0]["message"]
        self.assertEquals(err_message, f"{TokenNotFound()}")
        self.assertEquals(res["data"]["protected_query"], None)

    def test_03_request_protected_query_without_scopes(self):
        ctx = Context(
            headers=AuthHeader(token=self.invalid_token_no_scopes).authorization
        )
        res = self.gql_client.execute("query {protected_query}", context=ctx)
        err_message = res["errors"][0]["message"]
        self.assertEquals(err_message, f"{ScopesNotFound()}")
        self.assertEquals(res["data"]["protected_query"], None)

    def test_04_request_protected_query_without_all_required_scopes(self):
        ctx = Context(headers=AuthHeader(token=self.valid_token).authorization)
        res = self.gql_client.execute(
            "query {protected_query_two_required_scopes}", context=ctx
        )
        err_message = res["errors"][0]["message"]
        self.assertEquals(err_message, f"{InsufficientScopes()}")
        self.assertEquals(res["data"]["protected_query_two_required_scopes"], None)

    def test_05_request_protected_query_one_of_required_scopes(self):
        ctx = Context(headers=AuthHeader(token=self.valid_token).authorization)
        res = self.gql_client.execute(
            "query {protected_query_at_least_one_of_required_scopes}", context=ctx
        )
        self.assertEquals(
            res,
            {
                "data": {
                    "protected_query_at_least_one_of_required_scopes": "You're Authorized!"
                }
            },
        )

    @unittest.skipIf(not using_samples, "Samples are disabled")
    def test_06_request_status_data(self):
        r = self.client.get("/auth/status/")
        _is_enable = r.json()["settings"]["is_enable"]
        _api_namespace = r.json()["settings"]["api_namespace"]
        self.assertEquals(_is_enable, not is_disabled)
        self.assertEquals(_api_namespace, api_namespace)

    @unittest.skipIf(not using_samples, "Samples are disabled")
    def test_07_request_protected_endpoint(self):
        r = self.client.get("/auth/protected/", HTTP_AUTHORIZATION=f'Bearer {self.valid_token}')
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.json(), {"message": "Authorized!"})
