from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django_audit_events.context import AuditContext


class AuditContextMixin(object):
    audit_context = AuditContext()

    def __setattr__(self, key, value):
        if key != "audit_context":
            return super(AuditContextMixin, self).__setattr__(key, value)

        if value is None:
            raise ValueError(_("Audit context cannot be None"))

        if not isinstance(value, AuditContext):
            raise TypeError(_("Audit context must be an AuditContext instance"))

        return super(AuditContextMixin, self).__setattr__(key, value)
