# -*- coding: utf-8 -*-
# Third party
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import DENY_PAGES_IDS_CACHE_KEY

# Local application / specific library imports
from .models import Campaign


@receiver(post_save, sender=Campaign)
def clear_deny_pages_ids_cache(sender, instance, **kwargs):
    site = Site.objects.get_current()
    cache_key = DENY_PAGES_IDS_CACHE_KEY.format(site_id=site.id)
    cache.delete(cache_key)
