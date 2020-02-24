# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring
from __future__ import unicode_literals
from collections import OrderedDict
import jmespath
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .functions import Functions


class DataExtractor(models.Model):
    "Abstract model defining rules for extracting data from dicts."
    field_name = models.CharField(_("Input name"), max_length=60)
    omit = models.BooleanField(_("Omit"), blank=True, default=False)
    value = models.TextField(_("Default value"), blank=True, default='')
    expression = models.CharField(_("Expression"), max_length=250, blank=True, default='')
    omit_empty = models.BooleanField(_("Exclude if empty"), blank=True, default=False)

    class Meta:
        abstract = True
        verbose_name = _("Data extractor")
        verbose_name_plural = _("Data extractors")

    def __str__(self):
        return self.field_name

    def get_value(self, data):
        "Extracts data from a data dict."
        if self.omit:
            return None
        if self.value:
            return self.value
        if self.expression:
            options = jmespath.Options(custom_functions=Functions())
            return jmespath.search(self.expression, data, options=options)
        return data.get(self.field_name)

    def get_data(self, data):
        "extracts an ordered dict from data parameter."
        if self.omit:
            return OrderedDict()
        value = self.get_value(data)
        if self.omit_empty and value is None:
            return OrderedDict()
        return OrderedDict([[self.field_name, value]])

    @staticmethod
    def merge_data_extractors(data_extractors, data):
        result = OrderedDict()
        for extractor in data_extractors:
            extracted_data = extractor.get_data(data)
            for key, value in extracted_data.items():
                result[key] = value
        return result