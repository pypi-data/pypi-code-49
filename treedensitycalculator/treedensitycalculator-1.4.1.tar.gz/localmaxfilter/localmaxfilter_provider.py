# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------
| Date                : November 2018
| Copyright           : (C) 2018 by Tinne Cahy (Geo Solutions) and Ann Crabbé (KU Leuven)
| Email               : tinne.cahy@geosolutions.be, ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from Local Maximum Filter [C++ software]
|                       Ghent University, Laboratory of Forest Management and Spatial Information Techniques
|                       Lieven P.C. Verbeke
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
| License as published by the Free Software Foundation; either version 3 of the License, or any later version.
| ----------------------------------------------------------------------------------------------------------------
"""
from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon
from localmaxfilter.localmaxfilter_processing import LocalMaxFilterProcessingAlgorithm


class LocalMaxFilterProvider(QgsProcessingProvider):

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(LocalMaxFilterProcessingAlgorithm())

    def id(self, *args, **kwargs):
        """The ID of your plugin, used for identifying the provider.

        This string should be a unique, short, character only string,
        eg "qgis" or "gdal". This string should not be localised.
        """
        return 'lumos'

    def name(self, *args, **kwargs):
        """The human friendly name of your plugin in Processing.

        This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return self.tr('Lumos')

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QIcon(':/lumos')
