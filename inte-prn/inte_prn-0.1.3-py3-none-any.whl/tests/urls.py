from django.contrib import admin
from django.urls.conf import path, include

from ..admin_site import inte_prn_admin

urlpatterns = [
    path("inte_prn/", include("inte_prn.urls")),
    path("admin/", inte_prn_admin.urls),
    path("admin/", admin.site.urls),
]
