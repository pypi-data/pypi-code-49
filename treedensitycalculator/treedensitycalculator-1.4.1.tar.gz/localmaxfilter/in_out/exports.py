# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------
| Date                : March 2019
| Copyright           : (C) 2018 by Tinne Cahy, Louis Put (Geo Solutions) and Ann Crabbé (KU Leuven)
| Email               : tinne.cahy@geosolutions.be, ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from Local Maximum Filter [C++ software]
|                       Ghent University, Laboratory of Forest Management and Spatial Information Techniques
|                       Lieven P.C. Verbeke
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
| License as published by the Free Software Foundation; either version 3 of the License, or any later version.
| ----------------------------------------------------------------------------------------------------------------
"""
import os
import tempfile
from osgeo import ogr
from localmaxfilter.in_out import check_path
from qgis.PyQt.QtWidgets import QWidget


def write_point_layer(output_path, points_dict, geo_transform, srs, mask_path=None, feedback=None, context=None):
    """ Convert the input point dictionary to a vector point layer using the image metadata (srs and geo_transform).
        The points are clipped to fit the given mask.
        https://gis.stackexchange.com/questions/268395/converting-raster-tif-to-point-shapefile-using-python

    :param output_path: the absolute path to the output vector file
    :param points_dict: a dictionary containing the raster values and pixel locations
        Keys: RasterVal, Pixel with keys x and y
    :param mask_path: the absolute path to the mask file for clipping
    :param geo_transform: geo transformation coefficients
    :param srs: spatial reference system
    :param feedback: necessary for the processing tool
    :param context: necessary for the processing tool
    """

    if mask_path:
        # temporary file before clip
        tempdir = tempfile.mkdtemp()
        output = os.path.join(tempdir, 'points.shp')
    else:
        output = output_path

    # create empty layer
    driver = ogr.GetDriverByName('ESRI Shapefile')
    data_source = driver.CreateDataSource(output)
    # if the layer exists in memory, add '(1)'
    description = "point layer"
    while data_source.GetLayerByName(description):
        description = description + ' (1)'
    layer = data_source.CreateLayer(description, srs=srs, geom_type=ogr.wkbPoint)
    layer_definition = layer.GetLayerDefn()
    layer.CreateField(ogr.FieldDefn("RasterVal", ogr.OFTInteger))

    # add points from dictionary to layer
    origin_x = geo_transform[0]
    origin_y = geo_transform[3]
    pixel_width = geo_transform[1]
    pixel_height = geo_transform[5]

    point = ogr.Geometry(ogr.wkbPoint)

    for element in points_dict:
        coord_x = origin_x + pixel_width * element['Pixel']['x'] + pixel_width / 2
        coord_y = origin_y + pixel_height * element['Pixel']['y'] + pixel_height / 2
        point.AddPoint(coord_x, coord_y)
        out_feature = ogr.Feature(layer_definition)
        out_feature.SetGeometry(point)
        out_feature.SetField("RasterVal", int(element['RasterVal']))
        layer.CreateFeature(out_feature)
        out_feature.Destroy()

    driver = None
    del layer, data_source

    if mask_path:
        # use processing in qgis session
        import processing
        processing.run(
            "native:intersection",
            {'INPUT': output, 'INPUT_FIELDS': [], 'OUTPUT': output_path, 'OVERLAY': mask_path, 'OVERLAY_FIELDS': []},
            feedback=feedback,
            context=context
        )
        # todo problem: input of this function cannot be destroyed afterwards


def write_mask_layer(output_path, mask_path, trees_path):
    """ Copy the input mask to a new shapefile, and add an extra attributes:
        - field 'Area_ha' contains the area of the polygon
        - field 'TreeCount' contains the number of trees found in that polygon
        - field 'TreeDens' contains the number of trees per ha

    :param output_path: the absolute path to the output Shapefile
    :param mask_path: the absolute path to the input vector file
    :param trees_path: the absolute path to the input point vector file
    """

    check_path(mask_path)
    check_path(trees_path)

    # copy vector file to new shapefile
    mask_data = ogr.Open(mask_path)
    mask_layer = mask_data.GetLayer()

    driver = ogr.GetDriverByName('ESRI Shapefile')
    output_data = driver.CreateDataSource(output_path)
    output_layer = output_data.CopyLayer(mask_layer, output_path, ['OVERWRITE=YES'])

    # open the point layer
    point_data = driver.Open(trees_path)
    point_layer = point_data.GetLayer()

    # get the id field. if any id's are empty, return None
    point_fields = [x.lower() for x in point_layer.GetFeature(0).keys()]
    if 'id' in point_fields:
        id_field = 'id'
    elif 'fid' in point_fields:
        id_field = 'fid'
    else:
        id_field = None

    point_count = point_layer.GetFeatureCount()
    if id_field:
        for i in range(0, point_count):
            if point_layer.GetFeature(i).GetField(id_field) is None:
                id_field = None
                break

    # get the point count per polygon
    point_count_per_polygon = {}
    point_wkts = []
    if id_field:
        for i in range(0, point_count):
            polygon_id = point_layer.GetFeature(i).GetField(id_field)
            point_count_per_polygon[polygon_id] = point_count_per_polygon.get(polygon_id, 0) + 1
    else:
        point_wkts = [point_feature.GetGeometryRef().ExportToWkt() for point_feature in point_layer]

    # add fields to output layer. 'TreeDensity' is too long, therefore 'TreeDens'
    field_config = {
        "Area_ha": {'width': 32, 'precision': 4},
        "TreeCount": {'width': 32, 'precision': 0},
        "TreeDens": {'width': 32, 'precision': 2}
    }
    for field_name in field_config.keys():
        if output_layer.GetLayerDefn().GetFieldIndex(field_name) <= 0:
            field = ogr.FieldDefn(field_name, ogr.OFTReal)
            field.SetWidth(field_config[field_name]['width'])
            field.SetPrecision(field_config[field_name]['precision'])
            output_layer.CreateField(field)

    # for each polygon, add tree density information
    polygon_count = output_layer.GetFeatureCount()
    for i in range(0, polygon_count):
        # area
        polygon_feature = output_layer.GetFeature(i)
        geom = polygon_feature.GetGeometryRef()
        area = geom.GetArea() / 10000
        polygon_feature.SetField("Area_ha", area)

        # tree count
        count = 0
        # Select the intersecting features
        if id_field:
            count = point_count_per_polygon[polygon_feature.GetField(id_field)]
        else:
            for point_wkt in point_wkts:
                if ogr.CreateGeometryFromWkt(point_wkt).Intersects(polygon_feature.GetGeometryRef()):
                    count += 1

        polygon_feature.SetField("TreeCount", count)

        # tree density
        polygon_feature.SetField("TreeDens", count/area)

        output_layer.SetFeature(polygon_feature)

        # print result
        print("Polygon {0} is {1} ha and has {2} trees in total or {3} trees/ha.".format(i + 1, area, count, count/area))


def write_voronoi_layer(output_path, point_path, mask_path=None, feedback=None, context=None):
    """ Convert the input point vector to a Voronoi polygon layer and clip it by the mask layer

    :param output_path: the absolute path to the output voronoi vector file
    :param point_path: the absolute path to the input point vector file
    :param mask_path: the absolute path to the overlay vector file
    :param feedback: necessary for the processing tool
    :param context: necessary for the processing tool
    """

    check_path(point_path)
    tempdir = tempfile.mkdtemp()

    if mask_path:
        # temporary file before clip
        output = os.path.join(tempdir, 'voronoi.shp')
    else:
        output = output_path

    # check geometry: in case multipoint --> point
    try:
        driver = ogr.GetDriverByName('ESRI Shapefile')
        data = driver.Open(point_path)
        layer = data.GetLayer()
        feature = layer.GetFeature(0)
        geom = feature.GetGeometryRef().ExportToWkt()
    except Exception as e:
        raise Exception(str(e))

    if 'MULTIPOINT' in geom:
        tempdir_pt = os.path.join(tempdir, 'point.shp')

        # use processing in QGIS session
        import processing
        processing.run(
            'qgis:convertgeometrytype',
            {'INPUT': point_path, 'OUTPUT': tempdir_pt, 'TYPE': 0},
            feedback=feedback,
            context=context
        )

        point_path = tempdir_pt

    # use processing in QGIS session
    import processing
    processing.run(
        "qgis:voronoipolygons",
        {'BUFFER': 0, 'INPUT': point_path, 'OUTPUT': output},
        feedback=feedback,
        context=context
    )

    if mask_path:
        # use processing in qgis session
        import processing
        processing.run(
            "native:intersection",
            {'INPUT': output, 'INPUT_FIELDS': [], 'OUTPUT': output_path, 'OVERLAY': mask_path, 'OVERLAY_FIELDS': []},
            feedback=feedback,
            context=context
        )


class EmittingStream:
    """ QObject to catch the terminal output and send it along with q pyqtSignal. """

    def __init__(self, tab_widget):

        self.tab_widget = tab_widget
        self.log_index = tab_widget.indexOf(tab_widget.findChild(QWidget, 'tab_log'))
        self.log_widget = tab_widget.findChild(QWidget, 'logBrowser')

    def write(self, text):
        self.log_widget.append(text)
        self.tab_widget.setCurrentIndex(self.log_index)

    def flush(self):
        pass
