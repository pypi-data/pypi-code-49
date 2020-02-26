# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django_szuprefix.api.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models
from ..saas.mixins import PartySerializerMixin


class LecturerSerializer(IDAndStrFieldSerializerMixin, PartySerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Lecturer
        exclude = ('party',)
        read_only_fields = ('create_time',)



class VideoSerializer(IDAndStrFieldSerializerMixin, PartySerializerMixin, serializers.ModelSerializer):
    lecturer_name = serializers.CharField(source="lecturer.name", read_only=True)
    class Meta:
        model = models.Video
        exclude = ('party',)
        read_only_fields = ('user', 'create_time')

