from django.urls import path
from .views import CodeMirrorTemplate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CodeMirrorTemplate.as_view()),
]
