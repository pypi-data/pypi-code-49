# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path

from .views import CTAPluginRedirectView

app_name = "cta"
urlpatterns = [
    path(
        "to-form/<int:pk>/", CTAPluginRedirectView.as_view(), name="cta-plugin-redirect"
    )
]
