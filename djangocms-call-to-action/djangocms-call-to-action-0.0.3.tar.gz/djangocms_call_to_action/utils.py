# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4
import requests
from django.conf import settings

from .conf import settings as cta_settings
from .constants import GA_API_VERSION, GA_USER_SESSION_KEY


def send_ga_event(request, category, action, label, value=None):
    user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")

    headers = {"User-Agent": user_agent}

    ga_user_id = request.session.get(GA_USER_SESSION_KEY, None)

    if ga_user_id is None:
        ga_user_id = str(uuid4())
        request.session[GA_USER_SESSION_KEY] = ga_user_id

    payload = {
        "v": GA_API_VERSION,
        "tid": cta_settings.GA_UA,
        "cid": ga_user_id,
        "t": "event",
        "ec": category,
        "ea": action,
        "el": label,
    }

    if value is not None:
        payload.update({"ev": value})

    ga_url = (
        "https://www.google-analytics.com/debug/collect"
        if settings.DEBUG
        else "https://www.google-analytics.com/collect"
    )
    requests.post(ga_url, headers=headers, data=payload)
