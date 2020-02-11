from django.urls import path
from django_press.views import PageView, inquiry_view

urlpatterns = [
    path('', PageView.as_view()),
    path('inquiry/<path:path>', inquiry_view, name='Inquiry'),
    path('<path:path>', PageView.as_view(), name='Page'),
]
