from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^likes/add/(?P<target_id>[\d]+)/(?P<target_ct>[\d]+)$',
        views.LikeCreateView.as_view(), name='likes_add'),
]
