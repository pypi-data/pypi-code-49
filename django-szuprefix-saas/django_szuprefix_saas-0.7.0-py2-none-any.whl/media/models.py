# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from django.db import models
from django.utils.functional import cached_property
from django.contrib.contenttypes.fields import GenericForeignKey

from django_szuprefix_saas.saas.models import Party
from django.contrib.auth.models import User
from django_szuprefix.utils import modelutils


class Video(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "视频"
        ordering = ('owner_type', 'owner_id', 'name')

    party = models.ForeignKey(Party, verbose_name=Party._meta.verbose_name, related_name="media_videos",
                              on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name=User._meta.verbose_name, related_name="media_videos",
                             on_delete=models.PROTECT)
    owner_type = models.ForeignKey('contenttypes.ContentType', verbose_name='归类', null=True, blank=True,
                                   on_delete=models.CASCADE)
    owner_id = models.PositiveIntegerField(verbose_name='属主编号', null=True, blank=True)
    owner = GenericForeignKey('owner_type', 'owner_id')
    name = models.CharField("名称", max_length=255)
    description = models.CharField("描述", max_length=255, null=True, blank=True, default='')
    url = models.URLField("网址")
    cover_url = models.URLField('封面', blank=True, null=True)
    duration = models.PositiveSmallIntegerField('时长', blank=True, default=0, help_text='单位: 秒.', editable=False)
    size = models.PositiveIntegerField('大小', blank=True, default=0, help_text='单位: 比特Byte', editable=False)
    context = modelutils.JSONField("详情", blank=True, default={})
    is_active = models.BooleanField("有效", blank=False, default=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.name
