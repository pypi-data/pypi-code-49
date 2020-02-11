from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_press.views import PageView, inquiry_view

urlpatterns = [
    path('admin', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

    path('', PageView.as_view()),
    path('inquiry/<path:path>', inquiry_view, name='Inquiry'),
    path('<path:path>', PageView.as_view(), name='Page'),
]
