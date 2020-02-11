from django.conf import settings
from celery import shared_task
from piwikapi.tracking import PiwikTracker
from piwikapi.tests.request import FakeRequest
from urllib.parse import urlencode


class ExtendedPiwikTracker(PiwikTracker):
    """ We have to extend this to add the set_user_id """
    user_id = None

    def set_user_id(self, user_id: str):
        self.user_id = user_id

    def _get_request(self, id_site):
        url = super()._get_request(id_site)
        if self.user_id:
            url = url + '&' + urlencode({'uid': self.user_id})
        return url


@shared_task
def record_analytic(headers: dict, ip: str, user_id: str = None):
    """ Send analytics data to piwik """
    # Use "FakeRequest" because we had to serialize the real request
    request = FakeRequest(headers)
    pt = ExtendedPiwikTracker(settings.MATOMO_SITE_ID, request)
    pt.set_api_url(settings.MATOMO_API_URL)
    if settings.MATOMO_TOKEN_AUTH:
        pt.set_token_auth(settings.MATOMO_TOKEN_AUTH)
        pt.set_ip(ip)
    if getattr(settings, 'MATOMO_TRACK_USER_ID', None) and user_id:
        pt.set_user_id(user_id)
    # Truncate it
    visited_url = request.META['PATH_INFO'][:1000]
    pt.do_track_page_view(visited_url)
