# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import CMSPlugin, Page
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from djangocms_attributes_field.fields import AttributesField
from filer.fields.file import FilerFileField

from .conf import settings as cta_settings
from .constants import CTA_PLUGIN_SETTINGS_ID_GET_KEY
from .validators import IntranetURLValidator

TARGET_CHOICES = (
    ("_blank", _("Open in new window")),
    ("_self", _("Open in same window")),
    ("_parent", _("Delegate to parent")),
    ("_top", _("Delegate to top")),
)


@python_2_unicode_compatible
class Campaign(models.Model):
    url_validators = [IntranetURLValidator(intranet_host_re=cta_settings.HOSTNAME)]

    label = models.CharField(verbose_name=_("Label"), max_length=100)

    form_page = models.ForeignKey(
        Page,
        verbose_name=_("Page containing CTA form"),
        on_delete=models.CASCADE,
        related_name="form_cta_campaigns",
    )

    # Url to redirect user to once form complete
    redirect_external_link = models.CharField(
        verbose_name=_("Redirect to an external link"),
        blank=True,
        max_length=2040,
        validators=url_validators,
        help_text=_(
            "Provide a link to an external source to redirect the user to once form validated."
        ),
    )

    redirect_internal_link = models.ForeignKey(
        Page,
        verbose_name=_("Redirect to an internal link"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_(
            "If provided, overrides the external link to redirect the user to once form validated."
        ),
        related_name="redirect_cta_campaigns",
    )

    deny_internal_link_access = models.BooleanField(
        _(
            "Deny access to the internal link redirect page if the user hasn't validate the form"
        ),
        default=False,
        db_index=True,
    )

    # File to download once form complete
    file_link = FilerFileField(
        verbose_name=_("File link"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_("If provided links a file from the filer app."),
    )

    value = models.PositiveIntegerField(
        verbose_name=_("Value"),
        null=True,
        blank=True,
        help_text=_('A positive integer used in the "value" field of Google Analytics'),
    )

    def __str__(self):
        return "{}".format(self.label)

    class Meta:
        verbose_name = _("Campaign")
        app_label = "djangocms_call_to_action"

    def clean(self):
        super(Campaign, self).clean()
        field_names = ("redirect_external_link", "redirect_internal_link", "file_link")

        link_fields = {key: getattr(self, key) for key in field_names}
        link_field_verbose_names = {
            key: force_text(self._meta.get_field(key).verbose_name)
            for key in link_fields.keys()
        }
        provided_link_fields = {
            key: value for key, value in link_fields.items() if value
        }

        if len(provided_link_fields) > 1:
            # Too many fields have a value.
            verbose_names = sorted(link_field_verbose_names.values())
            error_msg = _("Only one of {0} or {1} may be given.").format(
                ", ".join(verbose_names[:-1]), verbose_names[-1]
            )
            errors = {}.fromkeys(provided_link_fields.keys(), error_msg)
            raise ValidationError(errors)

        if self.redirect_internal_link is None and self.deny_internal_link_access:
            raise ValidationError(
                _(
                    'You can\'t check the field "{deny_internal_link_access}", if no redirect page is defined in the field "{redirect_internal_link}"'
                ).format(
                    redirect_internal_link=force_text(
                        self._meta.get_field("redirect_internal_link").verbose_name
                    ),
                    deny_internal_link_access=force_text(
                        self._meta.get_field("deny_internal_link_access").verbose_name
                    ),
                ),
                code="invalid-use-of-deny_internal_link_access",
            )


@python_2_unicode_compatible
class CTAPluginSettings(CMSPlugin):
    # used by django CMS search
    search_fields = ("name",)

    name = models.CharField(verbose_name=_("Display name"), blank=True, max_length=255)

    template = models.CharField(
        verbose_name=_("Template"),
        choices=cta_settings.TEMPLATES,
        default=cta_settings.TEMPLATES[0][0],
        max_length=100,
    )

    campaign = models.ForeignKey(
        Campaign, verbose_name=_("Campaign"), on_delete=models.CASCADE
    )

    label = models.CharField(
        verbose_name=_("Label"),
        max_length=100,
        help_text=_("ex: Top page button"),
        default=_("Button"),
    )

    # advanced options
    target = models.CharField(
        verbose_name=_("Target"), choices=TARGET_CHOICES, blank=True, max_length=255
    )

    attributes = AttributesField(
        verbose_name=_("Attributes"),
        blank=True,
        excluded_keys=["href", "target", "rel"],
    )

    def get_link(self):
        return reverse("cta:cta-plugin-redirect", kwargs={"pk": self.pk})

    def get_form_page_url(self):
        link = self._get_internal_link(self.campaign.form_page)
        link = "{}?{}={}".format(link, CTA_PLUGIN_SETTINGS_ID_GET_KEY, self.id)
        return link

    def get_redirect_link(self):
        link = None
        campaign = self.campaign
        if campaign.redirect_internal_link:
            ref_page = campaign.redirect_internal_link
            link = self._get_internal_link(ref_page)

        elif campaign.redirect_external_link:
            link = campaign.redirect_external_link

        return link

    def _get_internal_link(self, ref_page):
        link = ref_page.get_absolute_url()

        # simulate the call to the unauthorized CMSPlugin.page property
        cms_page = self.placeholder.page if self.placeholder_id else None

        # first, we check if the placeholder the plugin is attached to
        # has a page. Thus the check "is not None":
        if cms_page is not None:
            if getattr(cms_page, "node", None):
                cms_page_site_id = getattr(cms_page.node, "site_id", None)
            else:
                cms_page_site_id = getattr(cms_page, "site_id", None)
        # a plugin might not be attached to a page and thus has no site
        # associated with it. This also applies to plugins inside
        # static placeholders
        else:
            cms_page_site_id = None

        # now we do the same for the reference page the plugin links to
        # in order to compare them later
        if cms_page is not None:
            if getattr(cms_page, "node", None):
                ref_page_site_id = ref_page.node.site_id
            else:
                ref_page_site_id = ref_page.site_id
        # if no external reference is found the plugin links to the
        # current page
        else:
            ref_page_site_id = Site.objects.get_current().pk

        if ref_page_site_id != cms_page_site_id:
            ref_site = Site.objects._get_site_by_id(ref_page_site_id).domain
            link = "//{}{}".format(ref_site, link)

        return link
