from inte_ae.admin_site import inte_ae_admin
from django.contrib import admin
from django.urls.conf import path, include

urlpatterns = [
    path("ae/", include("inte_ae.urls")),
    path("admin/", inte_ae_admin.urls),
    path("admin/", admin.site.urls),
]
