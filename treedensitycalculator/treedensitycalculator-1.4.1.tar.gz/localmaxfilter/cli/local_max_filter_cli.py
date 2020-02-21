# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------
| Date                : August 2018
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
import os
import argparse
from localmaxfilter.scripts.local_max_filter import LocalMaxFilter
from localmaxfilter.in_out.imports import import_image, import_vector_as_image
from localmaxfilter.in_out.exports import EmittingStream, write_mask_layer, write_point_layer, write_voronoi_layer


# Include code to work with processing algorithms
# ===============================================
import sys
from qgis.core import QgsApplication
from qgis.analysis import QgsNativeAlgorithms

if not os.environ.get('QGIS_PREFIX_PATH'):
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.environ['QGIS_PREFIX_PATH'] = '/usr'
    else:
        os.environ['QGIS_PREFIX_PATH'] = os.path.join("C:", os.sep, "OSGeo4W64", "apps", "qgis")

QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX_PATH'], True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
# Ubuntu Linux for example the prefix path is: /usr  and plugins: (qgis_prefix)/share/qgis/python/plugins
sys.path.append(os.path.join(os.environ['QGIS_PREFIX_PATH'], 'share', 'qgis', 'python', 'plugins'))  # unix, mac
# On Windows for example the prefix path is: C:\\OSGeo4W\\apps\\qgis\\ and plugins: (qgis_prefix)\\python\\plugins
sys.path.append(os.path.join(os.environ['QGIS_PREFIX_PATH'], 'python', 'plugins'))  # windows

import processing
from processing.core.Processing import Processing

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())


def create_parser():

    parser = argparse.ArgumentParser(description=LocalMaxFilter.__doc__)

    parser.add_argument('image', metavar='image', type=str, help='input reflectance image path')

    parser.add_argument('window', metavar='sliding_window', type=int,
                        help='length of the sliding window, in meters (default 5 m), '
                             'should be a multiple of the image pixel size')

    parser.add_argument('-m', '--mask', metavar='\b', type=str,
                        help='overlapping vector mask path')

    parser.add_argument('-v', '--voronoi', action='store_true', default=False,
                        help='create a Voronoi shapefile based on the tree locations (default off)')

    parser.add_argument('-s', '--snap', metavar='\b', type=float,
                        help='give distance [m] for the snap tool, should be max half of the window size, '
                             'tree tops which are closer to each other than the given distance will be taken as one')

    parser.add_argument('-o', '--output', metavar='\b',
                        help='path for output files, give base without extension '
                             '(default: in same folder with extension _window_{}.shp)')

    return parser


def run_local_max(args):
    """
    Documentation: localmaxfilter -h
    """

    # image and window are obligatory arguments and cannot be none. No test required.
    # get path of mask
    if args.mask:
        mask_path = args.mask
    else:
        mask_path = None

    # get raster (clipped by mask) and its metadata
    img, img_srs, img_gt = import_image(args.image, mask_path, args.window)

    # get area of interest as raster
    area_raster = import_vector_as_image(mask_path, img_gt, img.shape, img_srs, args.window) if mask_path else None

    # convert the window size from meters to number of pixels (odd number)
    pixel_size = img_gt[1]
    window_px = int((args.window / pixel_size) // 2 * 2 + 1)
    if window_px == 1:
        window_px = 3

    # Print in the log the size of the window in pixels
    print('The window is built out of {0} by {0} pixels'.format(window_px))

    # convert the snap distance from meters to number of pixels
    if args.snap:
        if args.snap > args.window/2:
            raise Exception('Snap distance should be max half of the window size')
        snap_distance = int(args.snap / pixel_size)
    else:
        snap_distance = None

    # Run LMF
    lmf_result = LocalMaxFilter(window_px).execute(img, area_raster, snap_distance, img_gt)

    # base name for output files
    if not args.output:
        output_base_path, _ = os.path.splitext(args.image)
    else:
        output_base_path, _ = os.path.splitext(args.output)

    output_base_path = '{0}_window_{1}'.format(output_base_path, args.window)

    # point layer
    output_point_path = output_base_path + '_point.shp'
    write_point_layer(output_point_path, lmf_result, img_gt, img_srs, mask_path)
    print("Resulting point shapefile: {}".format(output_point_path))

    # Output mask in case it was given:
    if mask_path:
        output_mask_path = output_base_path + '_mask.shp'
        write_mask_layer(output_mask_path, mask_path, output_point_path)
        print("Resulting mask shapefile: {}".format(output_mask_path))
    else:
        print("Number of trees counted: {} ".format(len(lmf_result)))

    # write point layer to Voronoi polygon layer
    if args.voronoi:
        output_voronoi_path = output_base_path + '_voronoi.shp'
        write_voronoi_layer(output_voronoi_path, output_point_path, mask_path)
        print("Resulting voronoi shapefile: {}".format(output_voronoi_path))


def main():
    parser = create_parser()
    run_local_max(parser.parse_args())


if __name__ == '__main__':
    main()
