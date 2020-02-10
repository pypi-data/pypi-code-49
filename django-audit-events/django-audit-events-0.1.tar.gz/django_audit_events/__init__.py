# -*- coding: utf-8 -*-
"""Log audit events in Django"""

from __future__ import unicode_literals

try:
    from django_audit_events.version import __version__
except ImportError:
    __version__ = "0.1"

__author__ = "Onur Güzel"
__license__ = "MIT"
__maintainer__ = "Akinon"
__email__ = "dev@akinon.com"

default_app_config = "django_audit_events.apps.DjangoAuditEventsConfig"
