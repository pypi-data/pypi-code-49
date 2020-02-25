from django.contrib import  auth
from .translitirate import transliterate
import re
from django.contrib.contenttypes.models import ContentType
import bleach
import re


class CommonHelpers:
    @staticmethod
    def get_user__by_request(request):
        if not hasattr(request, '_cached_user'):
            request._cached_user = auth.get_user(request)
        return request._cached_user

    @staticmethod
    def get_slug(_str):
        _str = _str.strip()
        slug = _str

        slug = transliterate(slug)
        slug = slug.lower()
        slug = re.sub(r'[^a-z0-9_-]', r'', slug)

        return slug
