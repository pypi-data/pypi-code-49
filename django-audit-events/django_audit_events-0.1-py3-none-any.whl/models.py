from __future__ import unicode_literals

import uuid

from django.apps import apps
from django.conf import settings as django_settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_audit_events.conf import settings


class AbstractAuditEvent(models.Model):
    uuid = models.UUIDField(verbose_name=_("ID"), default=uuid.uuid4, primary_key=True,)
    timestamp = models.DateTimeField(verbose_name=_("Timestamp"), auto_now_add=True)
    user = models.ForeignKey(
        django_settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name=_("User"),
        blank=True,
        null=True,
    )
    remote_addr = models.GenericIPAddressField(
        verbose_name=_("IP address"), blank=True, null=True,
    )
    url = models.URLField(verbose_name=_("URL"), blank=True, null=True,)
    query_params = JSONField(
        verbose_name=_("Query params"), default=dict, blank=True, null=True,
    )
    post_data = JSONField(
        verbose_name=_("Post data"), default=dict, blank=True, null=True,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    content = JSONField(verbose_name=_("Content"), default=dict,)

    class Meta:
        verbose_name = _("Audit event")
        verbose_name_plural = _("Audit events")
        ordering = ("-timestamp",)
        abstract = True

    @classmethod
    def from_context(cls, context):
        """
        Create an event from audit context

        :type context: django_audit_events.context.AuditContext
        :return: An audit event object
        :rtype: AbstractAuditEvent
        """

        obj = cls()
        obj.user = context.user
        obj.remote_addr = context.remote_addr
        obj.url = context.url
        obj.query_params = context.query_params
        obj.post_data = context.post_data
        return obj


class AuditEvent(AbstractAuditEvent):
    class Meta(AbstractAuditEvent.Meta):
        swappable = "AUDIT_EVENT_MODEL"


def get_audit_event_model():
    try:
        return apps.get_model(settings.AUDIT_EVENT_MODEL)
    except ValueError:
        raise ImproperlyConfigured(
            "AUDIT_EVENT_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "AUDIT_EVENT_MODEL refers to model '%s' that has not been installed"
            % settings.AUDIT_EVENT_MODEL
        )
