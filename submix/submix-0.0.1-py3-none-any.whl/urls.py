from django.contrib import admin
from django.urls import path

from .views import IndexView, NodesView

urlpatterns = [
    path('', IndexView.as_view()),
    path('nodes', NodesView.as_view()),
    path('admin/', admin.site.urls),
]
