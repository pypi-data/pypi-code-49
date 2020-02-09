# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from django.db import models
from django.utils.functional import cached_property
from django.contrib.contenttypes.fields import GenericForeignKey

from django_szuprefix_saas.saas.models import Party
from django.contrib.auth.models import User
from django_szuprefix.utils import modelutils


class DailyLog(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "日志"

    party = models.ForeignKey(Party, verbose_name=Party._meta.verbose_name, related_name="dailylog_dailylogs",
                              on_delete=models.PROTECT)
    the_date = models.DateField('日期', db_index=True)
    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="dailylog_dailylogs",
                             on_delete=models.PROTECT)
    context = modelutils.JSONField("详情", blank=True, default={})
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    update_time = models.DateTimeField("创建时间", auto_now=True)

    def __unicode__(self):
        return '%s dailylog @ %s' % (self.user, self.the_date.isoformat())
