from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
from django.test import TestCase

from django_audit_events.middleware import AuditEventsMiddleware


class MiddlewareTestMixin:
    request = HttpRequest()

    def reset_request(self):
        self.request = HttpRequest()
        self.request.META = {"SERVER_NAME": "localhost", "SERVER_PORT": 80}

    def apply_middleware(self):
        SessionMiddleware().process_request(self.request)
        AuthenticationMiddleware().process_request(self.request)
        AuditEventsMiddleware().process_request(self.request)


class MiddlewareTestCase(TestCase, MiddlewareTestMixin):
    def setUp(self):
        self.reset_request()

    def test_without_authentication_middleware(self):
        with self.assertRaises(AssertionError):
            AuditEventsMiddleware().process_request(self.request)

    def test_with_authentication_middleware(self):
        self.apply_middleware()
        self.assertTrue(hasattr(self.request, "audit_context"))
        # noinspection PyUnresolvedReferences
        self.assertIsNotNone(self.request.audit_context)
