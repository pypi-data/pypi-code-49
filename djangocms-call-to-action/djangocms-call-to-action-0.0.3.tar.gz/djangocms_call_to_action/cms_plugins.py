# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from fobi.contrib.apps.djangocms_integration.cms_plugins import (
    FobiFormWidgetPlugin,
)  # noqa: 501

from .conf import settings as cta_settings
from .constants import (
    CTA_PLUGIN_SETTINGS_ID_GET_KEY,
    USER_GRANTED_PAGES_SESSION_KEY,
)  # noqa: E501
from .forms import CTAFobiFormWidgetForm, CTAPluginSettingsForm
from .models import CTAPluginSettings
from .utils import send_ga_event

try:
    from urllib.parse import urlparse
except ImportError:  # Python 2 fallback
    from urlparse import urlparse

try:
    from urllib.parse import parse_qs
except ImportError:  # Python 2 fallback
    from urlparse import parse_qs


@plugin_pool.register_plugin
class CTAPlugin(CMSPluginBase):
    model = CTAPluginSettings
    form = CTAPluginSettingsForm
    name = _("Call To Action")
    text_enabled = True
    allow_children = True

    # The plugin must never be cached to ensure that GA events are properly sent
    cache = False

    fieldsets = [
        (None, {"fields": ("name", "template", "campaign", "label")}),
        (_("Link settings"), {"classes": ("collapse",), "fields": (("target",),)}),
        (_("Advanced settings"), {"classes": ("collapse",), "fields": ("attributes",)}),
    ]

    def get_render_template(self, context, instance, placeholder):
        return "djangocms_call_to_action/cta_plugin/{}".format(instance.template)

    def render(self, context, instance, placeholder):
        context["link"] = instance.get_link()
        request = context["request"]

        campaign = instance.campaign

        send_ga_event(
            request,
            campaign.label,
            cta_settings.DISPLAYED_USER_GA_LABEL,
            instance.label,
            campaign.value,
        )

        return super(CTAPlugin, self).render(context, instance, placeholder)


@plugin_pool.register_plugin
class CTAFobiFormWidgetPlugin(FobiFormWidgetPlugin):
    name = _("Call To Action form")
    form = CTAFobiFormWidgetForm

    class Meta:
        proxy = True

    def get_form(self, request, obj=None, **kwargs):
        form = super(CTAFobiFormWidgetPlugin, self).get_form(request, obj, **kwargs)
        form.base_fields["form_entry"].widget.can_add_related = False
        form.base_fields["form_entry"].widget.can_change_related = False
        return form

    def render(self, context, instance, placeholder):
        # Enforce form entry action value with request path + a GET arg to keep a trace on the CTA plugin
        request = context["request"]
        full_path = request.get_full_path()
        parsed = urlparse(full_path)
        get_args = parse_qs(parsed.query)
        cta_plugin_id = get_args.get(CTA_PLUGIN_SETTINGS_ID_GET_KEY)

        if cta_plugin_id is not None:
            instance.form_entry.cta_plugin_id = cta_plugin_id[0]
            instance.form_entry.action = "{}?{}={}".format(
                request.path, CTA_PLUGIN_SETTINGS_ID_GET_KEY, cta_plugin_id[0]
            )

        return super(CTAFobiFormWidgetPlugin, self).render(
            context, instance, placeholder
        )

    def _show_thanks_page(self, request, instance, **kwargs):
        cta_plugin_id = request.GET.get(CTA_PLUGIN_SETTINGS_ID_GET_KEY)

        if cta_plugin_id is not None:
            plugin_settings = CTAPluginSettings.objects.filter(id=cta_plugin_id).first()

            if plugin_settings:
                campaign = plugin_settings.campaign
                if campaign.file_link is not None:
                    instance.form_entry.download_file_url = campaign.file_link.url
                elif campaign.redirect_external_link or campaign.redirect_internal_link:
                    request.redirect_to_url = plugin_settings.get_redirect_link()

                    if campaign.redirect_internal_link:
                        session_key = USER_GRANTED_PAGES_SESSION_KEY.format(
                            page_id=campaign.redirect_internal_link.publisher_public_id
                        )
                        request.session[session_key] = True

                send_ga_event(
                    request,
                    campaign.label,
                    cta_settings.CONVERTED_USER_GA_LABEL,
                    plugin_settings.label,
                    campaign.value,
                )

        return super(CTAFobiFormWidgetPlugin, self)._show_thanks_page(
            request, instance, **kwargs
        )
