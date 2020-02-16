# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'dataextractor'
urlpatterns = [
    url(
        regex="^DataExtractor/~create/$",
        view=views.DataExtractorCreateView.as_view(),
        name='DataExtractor_create',
    ),
    url(
        regex="^DataExtractor/(?P<pk>\d+)/~delete/$",
        view=views.DataExtractorDeleteView.as_view(),
        name='DataExtractor_delete',
    ),
    url(
        regex="^DataExtractor/(?P<pk>\d+)/$",
        view=views.DataExtractorDetailView.as_view(),
        name='DataExtractor_detail',
    ),
    url(
        regex="^DataExtractor/(?P<pk>\d+)/~update/$",
        view=views.DataExtractorUpdateView.as_view(),
        name='DataExtractor_update',
    ),
    url(
        regex="^DataExtractor/$",
        view=views.DataExtractorListView.as_view(),
        name='DataExtractor_list',
    ),
	]
