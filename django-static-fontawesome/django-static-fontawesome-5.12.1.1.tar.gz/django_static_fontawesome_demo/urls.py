from django.urls import path
from django.urls import include
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy("django_static_fontawesome.demo"))),
    path('fontawesome/', include("django_static_fontawesome.urls")),
]
