# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .forms import CampaignForm
from .models import Campaign


class CampaignAdmin(admin.ModelAdmin):
    form = CampaignForm
    list_display = ("label",)
    search_fields = ("label",)

    fieldsets = [
        (None, {"fields": ("label",)}),
        (_("Form"), {"fields": ("form_page",)}),
        (
            _("Conversion settings"),
            {
                "fields": (
                    (
                        "redirect_external_link",
                        "redirect_internal_link",
                        "deny_internal_link_access",
                    ),
                    "file_link",
                )
            },
        ),
        (_("Advanced settings"), {"classes": ("collapse",), "fields": ("value",)}),
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(CampaignAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["form_page"].widget.can_add_related = False
        form.base_fields["form_page"].widget.can_change_related = False
        return form


admin.site.register(Campaign, CampaignAdmin)
