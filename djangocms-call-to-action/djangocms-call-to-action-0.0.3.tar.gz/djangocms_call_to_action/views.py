# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from .conf import settings as cta_settings
from .models import CTAPluginSettings
from .utils import send_ga_event


class CTAPluginRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        cta_plugin_settings = get_object_or_404(CTAPluginSettings, pk=kwargs["pk"])

        campaign = cta_plugin_settings.campaign
        send_ga_event(
            self.request,
            campaign.label,
            cta_settings.CLICKED_USER_GA_LABEL,
            cta_plugin_settings.label,
            campaign.value,
        )

        return cta_plugin_settings.get_form_page_url()
