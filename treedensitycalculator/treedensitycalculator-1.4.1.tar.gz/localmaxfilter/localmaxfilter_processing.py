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
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingContext,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFileDestination,)

from qgis.PyQt.QtGui import QIcon
from localmaxfilter.gui.local_max_filter_gui import LocalMaxFilterWidget


class LocalMaxFilterProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    Local Max Filter algorithm returns the tree density using the reflectance values of the local maxima
    of a sliding window going over the input image. It is possible to include an area of interest,
    to create a vonoroi layer or to snap local maxima.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    AREA_LAYER = 'AREA_LAYER'
    WINDOW = 'WINDOW'
    SNAP = 'SNAP'
    VORONOI = 'VORONOI'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return LocalMaxFilterProcessingAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'lumos:local_max_filter'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Tree Density Calculator')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Forestry')

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QIcon(':/lumos')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'forestry'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Local Max Filter algorithm returns the tree density of the input image.")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input image
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT,
                self.tr('Image')
            )
        )

        param_window = QgsProcessingParameterNumber(
                self.WINDOW,
                self.tr('Sliding window size'),
                type=1,           # type=1 is Double, 0 is int
                minValue=0,
                defaultValue=5)
        param_window.setMetadata({'widget_wrapper': {'decimals': 2}})

        self.addParameter(param_window)

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.AREA_LAYER,
                self.tr('Area of interest'),
                optional=True
            )
        )

        param_snap = QgsProcessingParameterNumber(
            self.SNAP,
            self.tr('Snap distance in meters, max half of sliding window size'),
            type=1,  # type=1 is Double, 0 is int
            optional=True,
            minValue=0
            # max value should be max half of the window. It's not possible to make this value
            # depended on another parameter, see: https://gis.stackexchange.com/questions/285570/
            #                   changing-parameter-values-according-to-other-parameter-choice-in-processing-scri
            )
        param_snap.setMetadata({'widget_wrapper': {'decimals': 2}})
        self.addParameter(param_snap)

        self.addParameter(
            QgsProcessingParameterBoolean(
                self.VORONOI,
                self.tr('Voronoi polygons')
            )
        )

        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.OUTPUT,
                self.tr('Output file'),
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Read input values
        image = self.parameterAsRasterLayer(parameters, self.INPUT, context)
        if image is None:
            raise QgsProcessingException('Invalid input layer {}'.format(parameters[self.INPUT]
                                                                         if self.INPUT in parameters else 'INPUT'))
        else:
            image = image.source()
        area = self.parameterAsVectorLayer(parameters, self.AREA_LAYER, context)
        if area:
            area = area.source()
        window = self.parameterAsInt(parameters, self.WINDOW, context)
        out = self.parameterAsFileOutput(parameters, self.OUTPUT, context)
        snap = self.parameterAsDouble(parameters, self.SNAP, context)
        voronoi = self.parameterAsBool(parameters, self.VORONOI, context)

        # Constrains
        if snap > window/2:
            raise QgsProcessingException('Snap distance should be max half of the window length')

        # Execute algorithm
        output_point_path, output_mask_path, output_voronoi_path = LocalMaxFilterWidget.run_algorithm_local_max_filter(
            image, window, feedback.setProgress, feedback.pushInfo, mask_path=area, output_base_path=out,
            snap_distance=snap, voronoi=voronoi,  feedback=feedback, context=context)

        # Open resulting layers in QGIS
        context.addLayerToLoadOnCompletion(
            output_point_path, QgsProcessingContext.LayerDetails(name='Tree Tops', project=context.project()))

        if area:
            context.addLayerToLoadOnCompletion(
                output_mask_path, QgsProcessingContext.LayerDetails(name='Tree Density', project=context.project()))
        if voronoi:
            context.addLayerToLoadOnCompletion(
                output_voronoi_path, QgsProcessingContext.LayerDetails(name='Voronoi', project=context.project()))

        return {'TREE_TOPS_POINT': output_point_path,
                'TREE_DENSITY_POLYGON': output_mask_path,
                'VORONOI_POLYGON': output_voronoi_path}
