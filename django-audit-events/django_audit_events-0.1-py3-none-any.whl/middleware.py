from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

from django_audit_events.context import AuditContext


class AuditEventsMiddleware(MiddlewareMixin):
    # noinspection PyMethodMayBeStatic
    def process_request(self, request):
        assert hasattr(request, "user"), (
            "Audit Events middleware requires authentication middleware "
            "to be installed. Edit your MIDDLEWARE{} setting to insert "
            "'django.contrib.auth.middleware.AuthenticationMiddleware' before "
            "'django_audit_events.middleware.AuditEventsMiddleware'."
        ).format("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.audit_context = SimpleLazyObject(
            lambda: AuditContext.from_request(request)
        )
