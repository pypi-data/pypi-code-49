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
        unique_together = ('the_date', 'user')

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

class Stat(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "统计"
        unique_together = ('the_date', 'owner_type', 'owner_id', 'metics')

    party = models.ForeignKey(Party, verbose_name=Party._meta.verbose_name, related_name="dailylog_stats",
                              on_delete=models.PROTECT)
    the_date = models.DateField('日期', db_index=True)
    owner_type = models.ForeignKey('contenttypes.ContentType', verbose_name='归类', null=True, blank=True,
                                   on_delete=models.CASCADE)
    owner_id = models.PositiveIntegerField(verbose_name='属主编号', null=True, blank=True)
    owner = GenericForeignKey('owner_type', 'owner_id')
    metics = models.CharField('指标', max_length=128)
    value = models.PositiveIntegerField('数值', default=0)
    user_count = models.PositiveIntegerField('用户数', default=0)
    update_time = models.DateTimeField("创建时间", auto_now=True)