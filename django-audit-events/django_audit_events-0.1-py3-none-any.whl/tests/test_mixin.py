from django.test import TestCase

from django_audit_events.context import AuditContext
from django_audit_events.mixin import AuditContextMixin


class TestClass(AuditContextMixin):
    dummy_attribute = "Dummy"


class TestWithDunder(AuditContextMixin):
    dummy_attribute = "Dummy"

    def __setattr__(self, key, value):
        setattr(self, key, value)


class MixinTestCase(TestCase):
    def test_has_audit_context(self):
        instance = TestClass()
        self.assertTrue(hasattr(instance, "audit_context"))

    def test_set_audit_context(self):
        instance = TestClass()
        context = AuditContext()
        instance.audit_context = context
        self.assertTrue(hasattr(instance, "audit_context"))

    def test_set_audit_context_none(self):
        instance = TestClass()
        with self.assertRaises(ValueError):
            instance.audit_context = None

    def test_set_audit_context_noninstance(self):
        instance = TestClass()
        with self.assertRaises(TypeError):
            instance.audit_context = "Not Acceptable"

    # noinspection PyMethodMayBeStatic
    def test_set_another_existing_attribute(self):
        instance = TestClass()
        instance.dummy_attribute = "Acceptable"

    def test_with_dunder_setattr(self):
        instance = TestClass()
        with self.assertRaises(ValueError):
            instance.audit_context = None

        with self.assertRaises(TypeError):
            instance.audit_context = "Not Acceptable"

        instance.dummy_attribute = "Acceptable"
