from django.test import TestCase

from django_audit_events.conf import DEFAULT_SETTINGS, settings


class SettingsTestCase(TestCase):
    def test_settings_has_defaults(self):
        self.assertEqual(
            settings.AUDIT_EVENT_MODEL, DEFAULT_SETTINGS["AUDIT_EVENT_MODEL"]
        )
