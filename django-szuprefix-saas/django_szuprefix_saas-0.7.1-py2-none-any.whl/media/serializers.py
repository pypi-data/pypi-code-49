# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django_szuprefix.api.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models
from ..saas.mixins import PartySerializerMixin


class VideoSerializer(IDAndStrFieldSerializerMixin, PartySerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Video
        exclude = ('party',)
        read_only_fields = ('user', 'create_time')


