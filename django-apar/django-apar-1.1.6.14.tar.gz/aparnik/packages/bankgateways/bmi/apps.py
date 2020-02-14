# -*- coding: utf-8 -*-


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BMIConfig(AppConfig):
    name = 'aparnik.packages.bankgateways.bmi'
    verbose_name = _('BMI')
