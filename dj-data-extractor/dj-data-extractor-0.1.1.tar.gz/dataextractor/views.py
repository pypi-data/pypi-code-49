# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	DataExtractor,
)


class DataExtractorCreateView(CreateView):

    model = DataExtractor


class DataExtractorDeleteView(DeleteView):

    model = DataExtractor


class DataExtractorDetailView(DetailView):

    model = DataExtractor


class DataExtractorUpdateView(UpdateView):

    model = DataExtractor


class DataExtractorListView(ListView):

    model = DataExtractor

