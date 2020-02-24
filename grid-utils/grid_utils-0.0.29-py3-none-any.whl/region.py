# -*- coding:utf-8 -*-

import six
import numpy as np
import matplotlib.patches as mpl_patches
from matplotlib.path import Path as MPLPath
import json
from grid_utils.dimension import *
import itertools as it

try:
    from shapely import geometry as sg
    from shapely import wkt as swkt
    HAS_SHAPELY = True
except ImportError:
    HAS_SHAPELY = False

try:
    from django.contrib.gis import geos
    HAS_GEODJANGO = True
except ImportError:
    HAS_GEODJANGO = False


__all__ = ['gen_region_mask']


def gen_region_mask(region, x, y):
    x, y = smart_meshgrid(x, y)
    points = np.array([x.flatten(), y.flatten()]).transpose()
    exteriors, interiors = _region_to_paths(region)
    ext_result = np.vstack([path.contains_points(points) for path in exteriors]).sum(axis=0)
    if len(interiors) > 0:
        int_result = np.vstack([path.contains_points(points) for path in interiors]).sum(axis=0)
        final_result = (ext_result - int_result) > 0
    else:
        final_result = ext_result > 0

    mask = final_result.reshape(x.shape)
    return mask


def _polygon_arr_to_paths(arr):
    exteriors = [MPLPath(arr[0], closed=True)]
    interiors = [MPLPath(ring[::-1], closed=True) for ring in arr[1:]]
    return exteriors, interiors


def _mpolygon_arr_to_paths(arr):
    exteriors = []
    interiors = []
    for a in arr:
        exts, ints = _polygon_arr_to_paths(a)
        exteriors.extend(exts)
        interiors.extend(ints)
    return exteriors, interiors


def _geojson_to_paths(geojson):
    if geojson['type'] == 'MultiPolygon':
        return _mpolygon_arr_to_paths(geojson['coordinates'])
    elif geojson['type'] == 'Polygon':
        return _polygon_arr_to_paths(geojson['coordinates'])
    else:
        raise ValueError("Cannot convert to path. Invalid GeoJSON type: {}".format(geojson['type']))


def _shapely_polygon_to_paths(polygon):
    exteriors = [MPLPath(polygon.exterior, closed=True)]
    interiors = [MPLPath(ring.coords[::-1], closed=True) for ring in polygon.interiors]
    return exteriors, interiors


def _region_to_paths(region):
    if isinstance(region, dict):
        return _geojson_to_paths(region)
    elif isinstance(region, str):
        if region[0] == '{':  # Treat as GeoJSON
            geojson = json.loads(region)
            return _geojson_to_paths(geojson)
        else:  # Treat as WKT
            if HAS_SHAPELY:
                region = swkt.loads(region)
            elif HAS_GEODJANGO:
                region = geos.GEOSGeometry(region)
            else:
                raise NotImplementedError("Native WKT parsing not implemnted!")

    if HAS_SHAPELY:
        if isinstance(region, sg.Polygon):
            return _shapely_polygon_to_paths(region)
        elif isinstance(region, sg.MultiPolygon):
            exteriors = []
            interiors = []
            for p in region.geoms:
                exts, ints = _shapely_polygon_to_paths(p)
                exteriors.extend(exts)
                interiors.extend(ints)
            return exteriors, interiors

    if HAS_GEODJANGO:
        if isinstance(region, geos.Polygon):
            return _polygon_arr_to_paths(region.coords)
        elif isinstance(region, geos.MultiPolygon):
            return _mpolygon_arr_to_paths(region.coords)

    raise ValueError("Cannot convert to path. Invalid region: {}".format(repr(region)))

