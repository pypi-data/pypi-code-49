from copy import deepcopy

from django.http import QueryDict
from django.test import override_settings
from django.utils.http import urlencode

from django_audit_events.context import MASK_VALUE, AuditContext
from django_audit_events.models import AuditEvent
from django_audit_events.tests.test_middleware import MiddlewareTestMixin
from django_audit_events.tests.test_models import TestModelMixin


class ContextTestCase(TestModelMixin, MiddlewareTestMixin):
    def setUp(self):
        self.reset_request()
        super(ContextTestCase, self).setUp()

    # noinspection PyMethodMayBeStatic
    def test_create_blank(self):
        # Assert creating blank context not raises any exceptions
        AuditContext()

    def test_create_from_request(self):
        self.apply_middleware()
        # Assert creating context from request not raises any exceptions
        AuditContext.from_request(self.request)

    def test_context_is_immutable(self):
        context = AuditContext()

        with self.assertRaises(NotImplementedError):
            context.url = ""

        with self.assertRaises(NotImplementedError):
            # noinspection PyDunderSlots,PyUnresolvedReferences
            context.extra_data = {}

    @override_settings(AUDIT_INCLUDE_POST_DATA=True)
    def test_mask_post_data_fields(self):
        # Test static method without audit context
        data = {"foo": "bar", "password": "secret"}
        masked = AuditContext.mask_fields(deepcopy(data), ["password"])
        self.assertEqual(masked["foo"], "bar")
        self.assertEqual(masked["password"], MASK_VALUE)
        self.assertEqual(data["password"], "secret")

        # Test inside audit context
        self.request.POST = QueryDict(query_string=urlencode(data))
        self.apply_middleware()
        self.assertIsNotNone(self.request.audit_context.post_data)
        self.assertEqual(self.request.audit_context.post_data["foo"], "bar")
        self.assertEqual(self.request.audit_context.post_data["password"], MASK_VALUE)

    def test_new_event(self):
        self.apply_middleware()
        event = self.request.audit_context.new_event()
        self.assertIsInstance(event, AuditEvent)

    def test_create_event(self):
        self.apply_middleware()

        event = self.request.audit_context.create_event(self.poll, foo="bar")
        self.assertIsInstance(event, AuditEvent)
        AuditEvent.objects.get(pk=event.pk)
        self.assertIn("foo", event.content)
        self.assertEqual(event.content["foo"], "bar")

    def test_create_event_with_extra(self):
        self.apply_middleware()
        self.request.audit_context.extra_data["marco"] = "polo"

        event = self.request.audit_context.create_event(self.poll, foo="bar")
        self.assertIsInstance(event, AuditEvent)
        AuditEvent.objects.get(pk=event.pk)
        self.assertIn("marco", event.content)
        self.assertEqual(event.content["marco"], "polo")
        self.assertIn("foo", event.content)
        self.assertEqual(event.content["foo"], "bar")

    def test_create_event_with_extra_override(self):
        self.apply_middleware()
        self.request.audit_context.extra_data["foo"] = "bar"

        event = self.request.audit_context.create_event(self.poll, foo="baz")
        self.assertIsInstance(event, AuditEvent)
        AuditEvent.objects.get(pk=event.pk)
        self.assertIn("foo", event.content)
        self.assertEqual(event.content["foo"], "baz")

    def test_create_fields_event(self):
        self.apply_middleware()

        event = self.request.audit_context.create_fields_event(
            self.poll, "question", foo="bar"
        )
        self.assertIsInstance(event, AuditEvent)
        AuditEvent.objects.get(pk=event.pk)
        self.assertIn("foo", event.content)
        self.assertEqual(event.content["foo"], "bar")
        self.assertIn("question", event.content)
        self.assertEqual(event.content["question"], self.poll.question)
