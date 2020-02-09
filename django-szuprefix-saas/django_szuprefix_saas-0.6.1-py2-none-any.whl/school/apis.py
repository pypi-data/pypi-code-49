# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django_szuprefix.auth.authentications import add_token_for_user
from django_szuprefix.utils.statutils import do_rest_stat_action

from .apps import Config

from . import models, mixins, serializers, importers, helper, stats
from rest_framework import viewsets, decorators, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_szuprefix.api.helper import register

__author__ = 'denishuang'


class TeacherViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    # permission_classes = [DjangoModelPermissionsWithView]
    filter_fields = {
        'id': ['in', 'exact'],
        'name': ['exact'],
    }
    search_fields = ('name', 'code')
    ordering_fields = ('name', 'code')

    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_teacher)


register(Config.label, 'teacher', TeacherViewSet)


class GradeViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer


register(Config.label, 'grade', GradeViewSet)


class SessionViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    search_fields = ('name', 'number')
    filter_fields = {'id': ['in', 'exact']}

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.as_saas_worker.party.as_school)


register(Config.label, 'session', SessionViewSet)


class ClazzViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.Clazz.objects.all()
    serializer_class = serializers.ClazzSerializer
    search_fields = ('name', 'code')
    filter_fields = {
        'id': ['in', 'exact'],
        'name': ['exact', 'endswith', 'in'],
        'code': ['in', 'exact'],
        'entrance_session': ['in', 'exact'],
        'grade': ['in', 'exact']
    }


    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ClazzSmallSerializer
        return super(ClazzViewSet, self).get_serializer_class()


    @decorators.list_route(['get'])
    def similar(self, request):
        q = request.query_params.get('q')
        import Levenshtein
        from django.db.models import F
        from django_szuprefix.utils.modelutils import CharCorrelation
        qset = self.filter_queryset(self.get_queryset()).values('name', a=CharCorrelation([F('name'), q])).filter(
            a__gt=0).order_by('-a').values_list('name', 'a')[:10]
        aa = [(Levenshtein.ratio(n, q), c, n) for n, c in qset]
        aa.sort(reverse=True)
        ss = [c for a, b, c in aa if a > 0.5]
        return Response({'similar': ss})

    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_clazz)


register(Config.label, 'clazz', ClazzViewSet)


class MajorViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer
    search_fields = ('name', 'code')
    filter_fields = {
        'code': ['exact'],
        'name': ['exact', 'in'],
        'id': ['in', 'exact'],
    }


register(Config.label, 'major', MajorViewSet)


class CollegeViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.College.objects.all()
    serializer_class = serializers.CollegeSerializer
    search_fields = ('name', 'code')
    filter_fields = ('code', 'name',)


register(Config.label, 'college', CollegeViewSet)


class ClazzCourseViewSet(mixins.PartyMixin, viewsets.ModelViewSet):
    queryset = models.ClazzCourse.objects.all()
    serializer_class = serializers.ClazzCourseSerializer
    search_fields = ('clazz__name', 'course__name')
    filter_fields = {
        'id': ['in', 'exact'],
        'clazz': ['exact'],
        'course': ['exact'],
        'teacher': ['exact']
    }


register(Config.label, 'clazzcourse', ClazzCourseViewSet)


class StudentViewSet(mixins.SchoolMixin, viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    search_fields = ('name', 'number', 'code')
    filter_fields = {
        'id': ['in', 'exact'],
        'grade': ['exact'],
        'clazz': ['exact', 'in'],
        'number': ['exact'],
        'is_active': ['exact'],
        'is_bind': ['exact'],
        'class__id': ['exact', 'in']
    }
    ordering_fields = ('name', 'number', 'create_time', 'grade', 'clazz')


    def get_permissions(self):
        if self.action == 'binding':
            return [IsAuthenticated()]
        return super(StudentViewSet, self).get_permissions()

    @decorators.list_route(['post'])
    def pre_import(self, request):
        importer = importers.StudentImporter(self.school)
        data = importer.clean(importer.get_excel_data(request.data['file']))
        return Response(data)

    @decorators.list_route(['post'])
    def post_import(self, request):
        importer = importers.StudentImporter(self.school)
        student, created = importer.import_one(request.data)
        return Response(self.get_serializer(instance=student).data,
                        status=created and status.HTTP_201_CREATED or status.HTTP_200_OK)

    @decorators.list_route(['POST'])
    def batch_active(self, request):
        rows = self.filter_queryset(self.get_queryset()) \
            .filter(id__in=request.data.get('id__in', [])) \
            .update(is_active=request.data.get('is_active', True))
        return Response({'rows': rows})

    @decorators.list_route(['post'], permission_classes=[IsAuthenticated])
    def binding(self, request):
        serializer = serializers.StudentBindingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            schools = serializer.save()
            data = serializer.data
            data['schools'] = schools
            add_token_for_user(data, request.user)
            return Response(data)
        else:
            return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @decorators.list_route(['POST'])
    def batch_unbind(self, request):
        ids = request.data.get('id__in', [])
        ss = self.filter_queryset(self.get_queryset()).filter(id__in=ids)
        for student in ss:
            helper.unbind(student)
        return Response({'rows': len(ids)})

    @decorators.detail_route(['post'])
    def unbind(self, request):
        helper.unbind(self.get_object())
        return Response({'info': 'success'})

    @decorators.list_route(['get'])
    def stat(self, request):
        return do_rest_stat_action(self, stats.stats_student)


register(Config.label, 'student', StudentViewSet)
