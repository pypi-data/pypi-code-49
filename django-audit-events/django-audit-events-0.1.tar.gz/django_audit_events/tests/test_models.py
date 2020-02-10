from django.db import IntegrityError
from django.http import QueryDict
from django.test import TestCase, override_settings

from django_audit_events.context import AuditContext
from django_audit_events.models import AuditEvent
from django_audit_events.tests.test_middleware import MiddlewareTestMixin
from django_audit_events.tests.utils.models import Poll


class TestModelMixin(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(
            question="Is it possible to create an audit event easily?"
        )


class AuditEventModelTestCase(TestModelMixin, MiddlewareTestMixin):
    def test_require_content_object(self):
        context = AuditContext()
        event = AuditEvent.from_context(context)
        self.assertIsInstance(event, AuditEvent)
        with self.assertRaises(IntegrityError):
            event.save()

    def test_create_from_empty_context(self):
        context = AuditContext()
        event = AuditEvent.from_context(context)
        self.assertIsInstance(event, AuditEvent)

        event.content_object = self.poll

        # Event is not saved to the DB yet.
        # noinspection PyTypeChecker
        with self.assertRaises(AuditEvent.DoesNotExist):
            AuditEvent.objects.get(pk=event.pk)

        event.save()
        # Assert fetching from DB not raises DoesNotExist exception
        AuditEvent.objects.get(pk=event.pk)

    @override_settings(AUDIT_INCLUDE_QUERY_PARAMS=True)
    def test_create_from_context(self):
        self.reset_request()
        self.request.GET = QueryDict("foo=bar")
        self.apply_middleware()

        event = AuditEvent.from_context(self.request.audit_context)
        self.assertIsInstance(event, AuditEvent)
        self.assertIn("foo", event.query_params)
        self.assertEqual(
            self.request.audit_context.query_params["foo"], event.query_params["foo"]
        )

        event.content_object = self.poll
        event.save()
        # Assert fetching from DB not raises DoesNotExist exception
        AuditEvent.objects.get(pk=event.pk)
