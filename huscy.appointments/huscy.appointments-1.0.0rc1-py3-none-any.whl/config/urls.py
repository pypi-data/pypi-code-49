from django.contrib import admin
from django.urls import include
from django.urls import path

from huscy.appointments.feed import AppointmentFeed
from huscy.appointments.feed import get_feed_url
from huscy.appointments.urls import router as appointments_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(appointments_router.urls)),
    path('feed/<str:token>', AppointmentFeed(), name='feed'),
    path('feedurl/', get_feed_url, name='feed-url'),

]
