# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import sendgrid

from .conf import settings as cta_settings


def get_sendgrid_client():
    return sendgrid.SendGridAPIClient(cta_settings.SENDGRID_API_KEY)


def get_sendgrid_lists():
    sg = get_sendgrid_client()
    response = sg.client.contactdb.lists.get()
    data = json.loads(response.body)
    return data["lists"]
