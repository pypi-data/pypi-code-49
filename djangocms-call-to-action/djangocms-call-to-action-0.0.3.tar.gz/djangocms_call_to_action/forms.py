# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import Page
from django.contrib.sites.models import Site
from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from djangocms_attributes_field.widgets import AttributesWidget
from fobi.contrib.apps.djangocms_integration.models import FobiFormWidget

from .fields import PageSearchField
from .models import Campaign, CTAPluginSettings


class CampaignForm(ModelForm):
    redirect_internal_link = PageSearchField(
        label=_("Redirect to an internal link"), required=False
    )

    def __init__(self, *args, **kwargs):
        # Prevent circular import
        from .cms_plugins import CTAFobiFormWidgetPlugin

        super(CampaignForm, self).__init__(*args, **kwargs)

        # keep only pages containing the cta fobi plugin
        CTA_PLUGIN_CLASS_NAME = CTAFobiFormWidgetPlugin.__name__
        site = Site.objects.get_current()
        site_pages = Page.objects.drafts().on_site(site)
        form_page_queryset = site_pages.filter(
            placeholders__cmsplugin__plugin_type=CTA_PLUGIN_CLASS_NAME
        )
        self.fields["form_page"].queryset = form_page_queryset

        # Override the redirect_internal_link fields queryset to contains just pages for
        # current site
        # this will work for PageSelectFormField
        self.fields["redirect_internal_link"].queryset = site_pages
        # set the current site as a redirect_internal_link field instance attribute
        # this will be used by the field later to properly set up the queryset
        # this will work for PageSearchField
        self.fields["redirect_internal_link"].site = site
        self.fields["redirect_internal_link"].widget.site = site

    class Meta:
        model = Campaign
        exclude = []


class CTAPluginSettingsForm(ModelForm):
    class Meta:
        model = CTAPluginSettings
        exclude = ("page", "position", "placeholder", "language", "plugin_type")

    def __init__(self, *args, **kwargs):
        super(CTAPluginSettingsForm, self).__init__(*args, **kwargs)
        self.fields["attributes"].widget = AttributesWidget()


class CTAFobiFormWidgetForm(ModelForm):
    class Meta:
        model = FobiFormWidget
        exclude = (
            "hide_form_title",
            "form_title",
            "form_submit_button_text",
            "success_page_template_name",
            "hide_success_page_title",
            "success_page_title",
            "success_page_text",
        )
