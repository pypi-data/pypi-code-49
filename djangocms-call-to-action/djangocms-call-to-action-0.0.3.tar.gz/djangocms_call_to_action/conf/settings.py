# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Third party
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

# The sendgrid API key allowing to register users in mailing lists
SENDGRID_API_KEY = getattr(settings, "DJANGOCMS_CTA_SENDGRID_API_KEY", None)
if not SENDGRID_API_KEY:
    raise ImproperlyConfigured("DJANGOCMS_CTA_SENDGRID_API_KEY must be defined")

# The GA identifier of the GA account to send events into
GA_UA = getattr(settings, "DJANGOCMS_CTA_GA_UA", None)
if not GA_UA:
    raise ImproperlyConfigured("DJANGOCMS_CTA_GA_UA must be defined")

# The list of templates that can be used to render the links of the cms plugin
TEMPLATES = getattr(settings, "DJANGOCMS_CTA_TEMPLATES", (("default.html", _("Link")),))

# See https://github.com/divio/djangocms-link/blob/master/djangocms_link/models.py#L37
HOSTNAME = getattr(settings, "DJANGOCMS_CTA_INTRANET_HOSTNAME_PATTERN", None)

# Allow to use select 2 for cms pages selection in forms.
# Need django-select2 to be installed.
USE_SELECT2 = getattr(settings, "DJANGOCMS_CTA_USE_SELECT2", False)

# Label of the "action" field registered in Google analytics event when the user has displayed the CTA plugin
DISPLAYED_USER_GA_LABEL = getattr(
    settings, "DJANGOCMS_CTA_DISPLAYED_USER_GA_LABEL", "Displayed"
)

# Label of the "action" field registered in Google analytics event when the user has clicked on the CTA plugin
CLICKED_USER_GA_LABEL = getattr(
    settings, "DJANGOCMS_CTA_CLICKED_USER_GA_LABEL", "Clicked"
)

# Label of the "action" field registered in Google analytics event when the user has validated the fobi form
CONVERTED_USER_GA_LABEL = getattr(
    settings, "DJANGOCMS_CTA_CONVERTED_USER_GA_LABEL", "Converted"
)

# A cache value to store the ids of the pages that are denied if the user hasn't validated the form
DENY_PAGES_IDS_CACHE_DURATION = getattr(
    settings, "DJANGOCMS_CTA_DENY_PAGES_IDS_CACHE_DURATION", 60 * 60
)
