from django.conf import settings
from ipware.ip import get_ip
from server_side_matomo.tasks import record_analytic


class MatomoMiddleware(object):
    """ Record every request to piwik """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        SITE_ID = getattr(settings, 'MATOMO_SITE_ID', None)
        if SITE_ID:
            ip = get_ip(request)
            keys_to_serialize = [
                'HTTP_USER_AGENT',
                'REMOTE_ADDR',
                'HTTP_REFERER',
                'HTTP_ACCEPT_LANGUAGE',
                'SERVER_NAME',
                'PATH_INFO',
                'QUERY_STRING',
            ]
            data = {
                'HTTPS': request.is_secure()        
            }
            for key in keys_to_serialize:
                if key in request.META:
                    data[key] = request.META[key]
            user_id = None
            if getattr(settings, 'MATOMO_TRACK_USER_ID', None) and request.user and request.user.pk:
                user_id = request.user.pk
            record_analytic.delay(data, ip, user_id)
        return response
