# -*- coding:utf-8 -*-
from __future__ import division

from django_szuprefix.api.mixins import UserApiMixin
from django_szuprefix_saas.saas.mixins import PartyMixin
from .apps import Config

__author__ = 'denishuang'
from . import models, serializers
from rest_framework import viewsets
from django_szuprefix.api.helper import register
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin


class PersonViewSet(PartyMixin, UserApiMixin,  RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filter_fields = ('gender',)
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PersonListSerializer
        return super(PersonViewSet, self).get_serializer_class()

    # def get_queryset(self):
    #     qset = super(PersonViewSet, self).get_queryset()
    #     user = self.request.user
    #     if user.has_perm('person.view_all_person'):
    #         pass
    #     # elif hasattr(user, 'as_school_teacher'):
    #     #     qset = qset.filter(teacher=user.as_school_teacher)
    #     else:
    #         qset = qset.none()
    #     return qset
register(Config.label, 'person', PersonViewSet)
