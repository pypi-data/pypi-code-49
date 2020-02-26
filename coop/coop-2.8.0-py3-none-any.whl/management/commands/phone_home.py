import json

import requests
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.text import slugify
from django.utils.timezone import now
from wagtail.core.models import Page, Site

from coop.models import AnalyticsSettings


class Command(BaseCommand):
    help = "Sends a JSON payload to the given url"

    def add_arguments(self, parser):
        parser.add_argument(
            "url",
            type=str,
            nargs="?",
            help="url to send the payload to",)

    def handle(self, *args, **options) -> None:
        url = options['url']

        def get_site_info(site):
            info = dict()
            analytics = AnalyticsSettings.for_site(site)

            if analytics:
                info['google_analytics'] = analytics.google_analytics
                info['google_tag_manager'] = analytics.google_tag_manager
            else:
                info['google_analytics'] = False
                info['google_tag_manager'] = False

            info['hostname'] = site.hostname
            info['name'] = site.site_name

            info['page_count'] = Page.objects.live().count()
            info['update_time'] = now()

            return info

        payload = dict()
        for site in Site.objects.all():
            site_info = get_site_info(site)
            key = slugify(site.site_name)
            payload.update({key: site_info})

        requests.post(url, data=json.dumps(payload, cls=DjangoJSONEncoder))
