from django.conf.urls import url

from django_audit_events.views import AuditEventViewSet

urlpatterns = [
    url(r"^events/", AuditEventViewSet.as_view({"get": "list"})),
]
