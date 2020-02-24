from django.contrib import admin
from django.urls import path, include
from CustomAuth.urls import handler400, handler401, handler403, handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maintenance-mode/', include('maintenance_mode.urls')),
    path('', include('CustomAuth.urls')),
    path('profile/', profile, name='profile')
] + staticfiles_urlpatterns()
