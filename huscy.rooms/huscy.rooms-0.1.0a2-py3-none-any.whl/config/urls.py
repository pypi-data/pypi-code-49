from django.contrib import admin
from django.urls import include, path

from huscy.rooms.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
