# -*- coding:utf-8 -*-
from __future__ import division, unicode_literals
from django_szuprefix.api.mixins import UserApiMixin, BatchActionMixin
from django_szuprefix.utils.statutils import do_rest_stat_action

from django_szuprefix_saas.saas.mixins import PartyMixin
from .apps import Config
from rest_framework.response import Response

__author__ = 'denishuang'
from . import models, serializers, stats, helper
from rest_framework import viewsets, decorators
from django_szuprefix.api.helper import register


class LecturerViewSet(PartyMixin, viewsets.ModelViewSet):
    queryset = models.Lecturer.objects.all()
    serializer_class = serializers.LecturerSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
    }


register(Config.label, 'lecturer', LecturerViewSet)


class VideoViewSet(PartyMixin, UserApiMixin, BatchActionMixin, viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
        'is_active': ['exact'],
        'owner_type': ['exact'],
        'owner_id': ['exact', 'in'],
        'lecturer': ['exact', 'in'],
    }
    ordering_fields = ('is_active', 'name', 'create_time', 'owner_type')

    @decorators.list_route(['POST'])
    def batch_active(self, request):
        return self.do_batch_action('is_active', True)

    @decorators.list_route(['POST'])
    def batch_update_media_info(self, request):
        return self.do_batch_action(helper.sync_qcloud_vod_info)

    @decorators.list_route(['GET', 'POST'])
    def signature(self, request):
        from xyz_qcloud.vod import gen_signature
        return Response({'signature': gen_signature(extra_params="procedure=流畅")})

    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_video)


register(Config.label, 'video', VideoViewSet)
