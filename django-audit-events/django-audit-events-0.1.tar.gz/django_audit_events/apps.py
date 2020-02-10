from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoAuditEventsConfig(AppConfig):
    name = "django_audit_events"
    verbose_name = _("Django Audit Event")
