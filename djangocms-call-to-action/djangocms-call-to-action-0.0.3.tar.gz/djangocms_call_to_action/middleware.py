# -*- coding: utf-8 -*-

from cms.models import Page
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from .conf import settings as cta_settings
from .constants import DENY_PAGES_IDS_CACHE_KEY, USER_GRANTED_PAGES_SESSION_KEY


class CTAFobiFormWidgetRedirectMiddleware(MiddlewareMixin):
    """
        Middleware to support cta fobi form widget redirect to success page.
    """

    def process_response(self, request, response):
        redirect_to_url = getattr(request, "redirect_to_url", None)
        if redirect_to_url is not None:
            return HttpResponseRedirect(redirect_to_url)
        return response


class CTAPagePermissionMiddleware(MiddlewareMixin):
    """
        Middleware to prevent access to cta form redirect page if the user hasn't validate the form.
    """

    def process_request(self, request):
        if request.current_page:
            current_page_id = request.current_page.id
            site = Site.objects.get_current()
            cache_key = DENY_PAGES_IDS_CACHE_KEY.format(site_id=site.id)

            deny_pages_ids = cache.get(cache_key)

            if deny_pages_ids is None:
                deny_pages_draft = (
                    Page.objects.drafts()
                    .on_site(site)
                    .filter(redirect_cta_campaigns__deny_internal_link_access=True)
                )

                deny_pages_ids = list(
                    Page.objects.on_site(site)
                    .filter(
                        publisher_is_draft=False, publisher_public__in=deny_pages_draft
                    )
                    .values_list("pk", flat=True)
                )

                cache.set(
                    cache_key,
                    deny_pages_ids,
                    cta_settings.DENY_PAGES_IDS_CACHE_DURATION,
                )

            if current_page_id in deny_pages_ids:
                user = request.user
                session_key = USER_GRANTED_PAGES_SESSION_KEY.format(
                    page_id=current_page_id
                )
                user_page_granted = request.session.get(session_key, False)
                user_is_granted = any(
                    [user.is_staff, user.is_superuser, user_page_granted]
                )
                if not user_is_granted:
                    raise PermissionDenied()
