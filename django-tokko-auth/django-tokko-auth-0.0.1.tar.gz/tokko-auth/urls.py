from django.conf.urls import url

from authorization.views import auth_status, protected_view
from authorization import settings

# Other auth path
urlpatterns = []

if settings.SAMPLES_ARE_ENABLE:
    urlpatterns += [
        # Samples
        url("status/", auth_status),
        url("protected/", protected_view),
    ]
