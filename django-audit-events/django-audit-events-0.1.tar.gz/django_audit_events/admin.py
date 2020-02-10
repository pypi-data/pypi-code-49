from django.contrib import admin

from django_audit_events.models import AuditEvent


@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_display = ("uuid", "user", "content_object", "timestamp")
