# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'pypi.schedule.django_pmedien_schedule'
    verbose_name = 'Planer'

    def ready(self):
        from .addons import scheduler
        scheduler.Scheduler()
