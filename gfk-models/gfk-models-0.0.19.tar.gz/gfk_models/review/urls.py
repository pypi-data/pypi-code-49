from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reviews/add$', views.ReviewCreateView.as_view(), name='add'),
]