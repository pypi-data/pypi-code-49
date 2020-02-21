from __future__ import absolute_import, unicode_literals

import logging

from mezzanine import template

from ..models import Access, GraphAPIError

logger = logging.getLogger(__name__)
register = template.Library()


@register.as_tag
def fbfeed_photos(name=None, limit=10):
    """
    Put a list of Facebook photos into the template context.
    """
    if name is None:
        access = Access.objects.first()
    else:
        try:
            access = Access.objects.get(name=name)
        except Access.DoesNotExist:
            return []

    try:
        return access.get_photos(limit=limit)
    except GraphAPIError:
        logger.exception("Facebook API error while rendering photos in template")
        return []
