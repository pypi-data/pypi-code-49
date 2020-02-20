from django.conf.urls import url

from tokko_auth.views import auth_status, protected_view
from tokko_auth import settings

# Other auth path
urlpatterns = []

if settings.SAMPLES_ARE_ENABLE:
    urlpatterns += [
        # Samples
        url("status/", auth_status),
        url("protected/", protected_view),
    ]
