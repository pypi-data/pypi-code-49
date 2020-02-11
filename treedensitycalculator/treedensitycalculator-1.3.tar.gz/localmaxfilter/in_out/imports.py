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
import osgeo.gdal as gdal
import osgeo.ogr as ogr
import osgeo.osr as osr
from localmaxfilter.in_out import check_path


def import_image(image_path, mask_path=None, window_size=None, reflectance=False, feedback=None, context=None):
    """ Get an input image as array from file path. If a vector layer path is given, the raster is clipped,
    using a 2*window_size buffer. Also return the the spatial reference system and the geo_transform.

    :param image_path: the absolute path to the input image
    :param mask_path: the absolute path to the polygon file
    :param window_size: the size of the sliding window, only required if mask is given
    :param reflectance: return reflectance values instead of DN between 0 and 255
    :param feedback: necessary for the processing tool
    :param context: necessary for the processing tool
    :return: numpy array [#bands x #rows x #columns], ogr srs and geo_transform
    """

    check_path(image_path)
    gdal.UseExceptions()

    try:

        # get CRS and Geo Transform coefficients
        image_data = gdal.Open(image_path)
        image_srs = osr.SpatialReference(wkt=image_data.GetProjection())
        image_epsg = image_srs.GetAuthorityCode(None)

        if not image_srs.IsProjected() or image_srs.GetAttrValue('projcs') is None:
            raise Exception('Raster has no projection.')

        if not image_srs.GetAttrValue('unit').lower() in ['metre', 'meter', 'metres', 'meters']:
            raise Exception('The projected crs must be in metres in order to calculate the tree density.')

        # get array
        if not mask_path:
            # no mask? get array directly
            array = image_data.ReadAsArray()
            image_geo_transform = image_data.GetGeoTransform()
        else:
            # window_size must be given
            if not window_size:
                raise Exception('Window size is obligatory in case of mask.')

            # mask? (1) buffer mask (2) buffer extent (3) clip raster based on extent (4) get array
            mask_data = ogr.Open(mask_path)
            layer = mask_data.GetLayer()
            mask_srs = layer.GetSpatialRef()
            mask_epsg = mask_srs.GetAuthorityCode(None)

            if not image_epsg == mask_epsg:
                raise Exception('Raster and Shapefile have different projections. \n' +
                                'Image srs: ' + image_srs.ExportToWkt() + '\n' +
                                'Mask srs:  ' + mask_srs.ExportToWkt())

            # (1) buffer mask
            tempdir = tempfile.mkdtemp()
            tempdir_buffer = os.path.join(tempdir, 'buffer.shp')
            distance = window_size * 2
            import processing
            processing.run(
                "native:buffer",
                {
                    'DISSOLVE': False, 'DISTANCE': distance, 'END_CAP_STYLE': 0, 'INPUT': mask_path, 'JOIN_STYLE': 0,
                    'MITER_LIMIT': 2, 'OUTPUT': tempdir_buffer, 'SEGMENTS': 5
                },
                feedback=feedback,
                context=context
            )

            # (2) buffer extent
            buffer_data = ogr.Open(tempdir_buffer, 0)
            buffer_layer = buffer_data.GetLayer()
            extent = ', '.join(['{}'.format(e) for e in buffer_layer.GetExtent()])  # comma separated string

            # (3) clip raster by extent
            tempdir_clip = os.path.join(tempdir, 'clip.tif')
            import processing
            processing.run(
                "gdal:cliprasterbyextent",
                {'INPUT': image_path, 'NODATA': -1, 'OPTIONS': '', 'OUTPUT': tempdir_clip, 'PROJWIN': extent},
                feedback=feedback,
                context=context
            )

            # (4) get array
            image_data = gdal.Open(tempdir_clip)
            array = image_data.ReadAsArray()
            image_geo_transform = image_data.GetGeoTransform()
        # end else

        # turn array into reflectance values
        if reflectance:
            array = array / float(255)  # adjust to reflectance values

        return array, image_srs, image_geo_transform

    except Exception as e:
        raise Exception(str(e))


def import_vector_as_image(path, geo_transform, image_size, image_srs, window_size, feedback=None, context=None):
    """ Browse for a vector file and return it as a raster after buffering with window_size.

    :param path: the absolute path to the vector file
    :param geo_transform: 6 geo transformation coefficients
    :param image_size: size of the image
    :param image_srs: OSR spatial reference system object
    :param window_size: the size of the sliding window
    :param feedback: necessary for the processing tool
    :param context: necessary for the processing tool
    :return: numpy array
    """

    check_path(path)
    gdal.UseExceptions()

    try:
        # check image and vector have same epsg
        image_epsg = image_srs.GetAuthorityCode(None)
        mask_data = ogr.Open(path)
        layer = mask_data.GetLayer()
        mask_srs = layer.GetSpatialRef()
        mask_epsg = mask_srs.GetAuthorityCode(None)

        if not image_epsg == mask_epsg:
            raise Exception('Raster and Shapefile have different projections. \n' +
                            'Image srs: ' + image_srs.ExportToWkt() + '\n' +
                            'Mask srs:  ' + mask_srs.ExportToWkt())

        # create vector buffer
        tempdir = tempfile.mkdtemp()
        tempdir_buffer = os.path.join(tempdir, 'buffer.shp')
        distance = window_size * 2
        import processing
        processing.run(
            "native:buffer",
            {
                'DISSOLVE': False, 'DISTANCE': distance, 'END_CAP_STYLE': 0, 'INPUT': path, 'JOIN_STYLE': 0,
                'MITER_LIMIT': 2, 'OUTPUT': tempdir_buffer, 'SEGMENTS': 5
            },
            feedback=feedback,
            context=context
        )

        # open buffer as layer
        data = ogr.Open(tempdir_buffer)
        layer = data.GetLayer()

        # create raster based on buffer
        driver = gdal.GetDriverByName('MEM')
        memory_raster = driver.Create('', image_size[1], image_size[0], 1, gdal.GDT_Float32)
        memory_raster.SetGeoTransform(geo_transform)
        memory_raster.SetProjection(image_srs.ExportToWkt())
        gdal.RasterizeLayer(memory_raster, [1], layer,  burn_values=[1])  # , options=['ALL_TOUCHED=TRUE']
        array = memory_raster.ReadAsArray()

        return array

    except Exception as e:
        raise Exception(str(e))
