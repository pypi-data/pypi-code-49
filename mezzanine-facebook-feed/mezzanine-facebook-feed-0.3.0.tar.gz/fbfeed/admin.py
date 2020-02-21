# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect, get_object_or_404

from mezzanine.utils.urls import admin_url

from .models import Access, FacebookSettingError, GraphAPIError


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    readonly_fields = ["token", "token_type", "expires"]

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        Don't render the change view until the Facebook settings are set
        """
        access = get_object_or_404(Access, id=object_id)
        try:
            access.app_id
            access.app_secret
        except FacebookSettingError as e:
            self.message_user(request, str(e))
            return redirect("admin:conf_setting_changelist")
        return super(AccessAdmin, self).change_view(
            request, object_id, form_url=form_url, extra_context=extra_context
        )

    def redirect_endpoint(self, request):
        """
        Process the request after the user has logged into Facebook
        """
        code = request.GET.get("code")
        access = get_object_or_404(Access, id=request.GET.get("state", 0))
        try:
            access.get_token_from_code(code)
        except (GraphAPIError, FacebookSettingError) as e:
            self.message_user(request, str(e))
        else:
            self.message_user(request, "Access token updated")

        return redirect(admin_url(Access, "change", access.id))

    def get_urls(self):
        urls = [
            url(
                r"^redirect/$",
                self.admin_site.admin_view(self.redirect_endpoint),
                name="fbfeed_redirect_endpoint",
            )
        ]
        return urls + super(AccessAdmin, self).get_urls()
