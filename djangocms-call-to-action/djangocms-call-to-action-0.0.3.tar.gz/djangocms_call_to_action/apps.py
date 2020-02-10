# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangocmsCallToActionConfig(AppConfig):
    label = "djangocms_call_to_action"
    name = "djangocms_call_to_action"
    verbose_name = _("CTA CMS plugin")

    def ready(self):
        from . import receivers  # noqa: F401
