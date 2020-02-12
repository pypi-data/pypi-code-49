# -*- coding:utf-8 -*-
from __future__ import division, unicode_literals
from django_szuprefix.api.mixins import UserApiMixin
from django_szuprefix.utils.statutils import do_rest_stat_action

from django_szuprefix_saas.saas.mixins import PartyMixin
from .apps import Config
from rest_framework.response import Response

__author__ = 'denishuang'
from . import models, serializers, stats
from rest_framework import viewsets, decorators
from django_szuprefix.api.helper import register


class VideoViewSet(PartyMixin, UserApiMixin, viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    search_fields = ('name',)
    filter_fields = {
        'id': ['in', 'exact'],
        'is_active': ['exact'],
        'owner_type': ['exact'],
        'owner_id': ['exact', 'in'],
    }
    ordering_fields = ('is_active', 'name', 'create_time', 'owner_type')

    @decorators.list_route(['POST'])
    def batch_active(self, request):
        rows = self.filter_queryset(self.get_queryset()) \
            .filter(id__in=request.data.get('id__in', [])) \
            .update(is_active=request.data.get('is_active', True))
        return Response({'rows': rows})

    @decorators.list_route(['POST'])
    def batch_update_media_info(self, request):
        from xyz_qcloud import vod, utils
        ids = request.data.get('id__in', [])
        qset = self.filter_queryset(self.get_queryset())
        rows = 0
        for id in ids:
            v = qset.filter(id=id).first()
            if not v:
                continue
            fid = v.context.get('fileId') or v.context.get('FileId')
            if not fid:
                continue
            v.context = vod.get_media_info(fid)['MediaInfoSet'][0]
            v.cover_url = utils.access(v.context, 'BasicInfo.CoverUrl')
            v.duration = utils.access(v.context, 'MetaData.Duration')
            v.size = utils.access(v.context, 'TranscodeInfo.TranscodeSet.0.Size')
            v.save()
            rows += 1
        return Response({'rows': rows})

    @decorators.list_route(['GET', 'POST'])
    def signature(self, request):
        from xyz_qcloud.vod import gen_signature
        return Response({'signature': gen_signature(extra_params="procedure=流畅")})

    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_video)


register(Config.label, 'video', VideoViewSet)
