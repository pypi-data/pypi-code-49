# -*- coding:utf-8 -*-
from __future__ import division, unicode_literals
from django_szuprefix.api.mixins import UserApiMixin
from django_szuprefix_saas.saas.mixins import PartyMixin
from .apps import Config
from rest_framework.response import Response

__author__ = 'denishuang'
from . import models, serializers
from rest_framework import viewsets, decorators
from django_szuprefix.api.helper import register


class DailyLogViewSet(PartyMixin, UserApiMixin, viewsets.ModelViewSet):
    queryset = models.DailyLog.objects.all()
    serializer_class = serializers.DailyLogSerializer
    filter_fields = {
        'id': ['in', 'exact'],
        'the_date': ['exact', 'gte', 'lte'],
    }

    @decorators.list_route(['POST'])
    def write(self, request):
        user = request.user
        for k, v in request.data.iteritems():
            log, created = self.party.dailylog_dailylogs.get_or_create(user=user, the_date=k)
            log.context.update(v)
            log.save()
        return Response({'detail': 'success'})


register(Config.label, 'dailylog', DailyLogViewSet)
