# -*- coding: utf-8 -*-
from django.conf import settings

from .conf import settings as cta_settings


def is_select2_enabled():
    is_installed = "django_select2" in settings.INSTALLED_APPS
    return cta_settings.USE_SELECT2 and is_installed


if is_select2_enabled():
    from .fields_select2 import Select2PageSearchField as PageSearchField  # noqa
else:
    from cms.forms.fields import PageSelectFormField as PageSearchField  # noqa
