# coding: utf-8

# In general Geoformat is licensed under an MIT/X style license with the
# following terms:
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# Authors :
#   Guilhain Averlant
#   Eliette Catelin
#   Quentin Lecuire
#   Charlotte Montesinos Chevalley
#   Coralie Rabiniaux

import copy
import os.path
import sys
import zlib

from osgeo import ogr
from osgeo import osr

# predicates
from geoformat_lib.geoprocessing.connectors.predicates import point_intersects_point, point_intersects_segment, \
    point_intersects_bbox, segment_intersects_bbox, segment_intersects_segment, bbox_intersects_bbox, \
    point_position_segment, point_position_segment, ccw_or_cw_segments

# operations
from geoformat_lib.geoprocessing.connectors.operations import coordinates_to_point, segment_to_bbox, coordinates_to_bbox

# conversions
from geoformat_lib.conversion.geometry_conversion import bbox_extent_to_2d_bbox_extent, \
    geometry_type_to_2d_geometry_type, geometry_to_2d_geometry, geolayer_to_2d_geolayer,\
    envelope_to_bbox, bbox_to_envelope

# data printing
from geoformat_lib.explore_data.print_data import print_features_data_table, print_metadata_field_table


__version__ = 20200220

DATA_TYPE = {
    "OFSTBoolean": 1,
    "OFSTFloat32": 3,
    "OFSTInt16": 2,
    "OFSTNone": 0,
    "OFTBinary": 8,
    "OFTDate": 9,
    "OFTDateTime": 11,
    "OFTInteger": 0,
    "OFTInteger64": 12,
    "OFTInteger64List": 13,
    "OFTIntegerList": 1,
    "OFTReal": 2,
    "OFTRealList": 3,
    "OFTString": 4,
    "OFTStringList": 5,
    "OFTTime": 10,
    "OFTWideString": 6,
    "OFTWideStringList": 7
}

GEOMETRY_TYPE = {
    "25Bit": -2147483648,
    "25DBit": -2147483648,
    "CircularString": 8,
    "CircularStringM": 2008,
    "CircularStringZ": 1008,
    "CircularStringZM": 3008,
    "CompoundCurve": 9,
    "CompoundCurveM": 2009,
    "CompoundCurveZ": 1009,
    "CompoundCurveZM": 3009,
    "Curve": 13,
    "CurveM": 2013,
    "CurvePolygon": 10,
    "CurvePolygonM": 2010,
    "CurvePolygonZ": 1010,
    "CurvePolygonZM": 3010,
    "CurveZ": 1013,
    "CurveZM": 3013,
    "GeometryCollection": 7,
    "GeometryCollection25D": -2147483641,
    "GeometryCollectionM": 2007,
    "GeometryCollectionZM": 3007,
    "LineString": 2,
    "LineString25D": -2147483646,
    "LineStringM": 2002,
    "LineStringZM": 3002,
    "LinearRing": 101,
    "MultiCurve": 11,
    "MultiCurveM": 2011,
    "MultiCurveZ": 1011,
    "MultiCurveZM": 3011,
    "MultiLineString": 5,
    "MultiLineString25D": -2147483643,
    "MultiLineStringM": 2005,
    "MultiLineStringZM": 3005,
    "MultiPoint": 4,
    "MultiPoint25D": -2147483644,
    "MultiPointM": 2004,
    "MultiPointZM": 3004,
    "MultiPolygon": 6,
    "MultiPolygon25D": -2147483642,
    "MultiPolygonM": 2006,
    "MultiPolygonZM": 3006,
    "MultiSurface": 12,
    "MultiSurfaceM": 2012,
    "MultiSurfaceZ": 1012,
    "MultiSurfaceZM": 3012,
    "NDR": 1,
    "None": 100,
    "Point": 1,
    "Point25D": -2147483647,
    "PointM": 2001,
    "PointZM": 3001,
    "Polygon": 3,
    "Polygon25D": -2147483645,
    "PolygonM": 2003,
    "PolygonZM": 3003,
    "PolyhedralSurface": 15,
    "PolyhedralSurfaceM": 2015,
    "PolyhedralSurfaceZ": 1015,
    "PolyhedralSurfaceZM": 3015,
    "Surface": 14,
    "SurfaceM": 2014,
    "SurfaceZ": 1014,
    "SurfaceZM": 3014,
    "TIN": 16,
    "TINM": 2016,
    "TINZ": 1016,
    "TINZM": 3016,
    "Triangle": 17,
    "TriangleM": 2017,
    "TriangleZ": 1017,
    "TriangleZM": 3017,
    "Unknown": 0,
    "XDR": 0,
}

DATA_TYPE = {
    "OFSTBoolean": 1,
    "OFSTFloat32": 3,
    "OFSTInt16": 2,
    "OFSTNone": 0,
    "OFTBinary": 8,
    "OFTDate": 9,
    "OFTDateTime": 11,
    "OFTInteger": 0,
    "OFTInteger64": 12,
    "OFTInteger64List": 13,
    "OFTIntegerList": 1,
    "OFTReal": 2,
    "OFTRealList": 3,
    "OFTString": 4,
    "OFTStringList": 5,
    "OFTTime": 10,
    "OFTWideString": 6,
    "OFTWideStringList": 7
}

GEOFORMAT_GEOMETRY_TYPE = {
    'LINESTRING',
    'MULTIPOINT',
    'GEOMETRYCOLLECTION',
    'POINT',
    'GEOMETRY',
    'POLYGON',
    'MULTIPOLYGON',
    'MULTILINESTRING'}

# OGR driver names
OGR_FORMAT_ESRI_SHAPEFILE = "ESRI SHAPEFILE"
OGR_FORMAT_POSTGRESQL = "POSTGRESQL"
OGR_FORMAT_KML = "KML"
OGR_FORMAT_XLSX = "XLSX"
OGR_FORMAT_CSV = "CSV"
OGR_FORMAT_GEOJSON = "GEOJSON"
OGR_DRIVER_NAMES = (OGR_FORMAT_ESRI_SHAPEFILE,
                    OGR_FORMAT_POSTGRESQL,
                    OGR_FORMAT_KML,
                    OGR_FORMAT_XLSX,
                    OGR_FORMAT_CSV,
                    OGR_FORMAT_GEOJSON)


def version(version_value=__version__, verbose=True):
    version_dev = 'Alpha'
    if verbose:
        return '{version_dev} version {version_number}'.format(version_dev=version_dev, version_number=version_value)
    else:
        return version_value


####
#
# CLAUSE
#
# The CLAUSE functions return a directly a list of i_feat or a dict with a list associates to each key of i_feat
###

def clause_where(geolayer, field_name, predicate, values):
    # transform values to iterate variable
    if not isinstance(values, (list, tuple)):
        if isinstance(values, tuple):
            values = list(values)
        else:
            values = [values]
    # init result list
    i_feat_list = []
    # loop on geolayer
    for i_feat in geolayer['features']:
        feature = geolayer['features'][i_feat]
        feature_value = feature['attributes'][field_name]

        # save feature_value in list by default
        if isinstance(feature_value, (list, tuple, set)):
            feature_value_list = feature_value
        else:
            feature_value_list = [feature_value]

        save_i_feat = False
        # loop on feature_value_list
        for feature_value in feature_value_list:
            if '=' in predicate or 'IN' in predicate or predicate == 'LIKE' or predicate == 'BETWEEN':
                if feature_value in values:
                    save_i_feat = True
                    break

            if predicate in '<>' or predicate == 'BETWEEN':
                if predicate == '<>':
                    if feature_value not in values:
                        save_i_feat = True
                else:
                    if (predicate == '>' or predicate == 'BETWEEN') and feature_value > values[0]:
                        save_i_feat = True
                    if (predicate == '<' or predicate == 'BETWEEN') and feature_value < values[-1]:
                        save_i_feat = True

            if 'IS' in predicate:
                if 'NOT' in predicate:
                    if feature_value:
                        save_i_feat = True
                else:
                    if not feature_value:
                        save_i_feat = True

        if save_i_feat:
            i_feat_list.append(i_feat)

    return i_feat_list


def clause_where_combination(geolayer, clause_where_dict):
    """

    example for clause_where_dict :
           clause_where_dict= {'field_predicate': {
                                    'foo_field_name': {
                                        'predicate': '=',
                                        'values': [0, 1, 2]
                                    }
                                }
                            }


    :param geolayer:
    :param clause_where_dict:
    :param field_combination:
    :return:
    """

    def field_predicate(geolayer, field_predicate_dict, field_combination=None):

        i_feat_predicate = {}
        for field_name in field_predicate_dict['field_predicate']:
            field_predicate = field_predicate_dict['field_predicate'][field_name]
            predicate = field_predicate['predicate'].upper()
            if 'values' in field_predicate.keys():
                values = field_predicate['values']
                if not isinstance(values, (list, tuple)):
                    if isinstance(values, tuple):
                        values = list(values)
                    else:
                        values = [field_predicate['values']]

            i_feat_list = []

            for i_feat in geolayer['features']:
                feature = geolayer['features'][i_feat]
                feature_value = feature['attributes'][field_name]

                # save feature_value in list by default
                if isinstance(feature_value, (list, tuple, set)):
                    feature_value_list = feature_value
                else:
                    feature_value_list = [feature_value]

                save_i_feat = False
                # loop on feature_value_list
                for feature_value in feature_value_list:
                    if '=' in predicate or 'IN' in predicate or predicate == 'LIKE' or predicate == 'BETWEEN':
                        if feature_value in values:
                            save_i_feat = True
                            break

                    if predicate in '<>' or predicate == 'BETWEEN':
                        if predicate == '<>':
                            if feature_value not in values:
                                save_i_feat = True
                        else:
                            if (predicate == '>' or predicate == 'BETWEEN') and feature_value > values[0]:
                                save_i_feat = True
                            if (predicate == '<' or predicate == 'BETWEEN') and feature_value < values[-1]:
                                save_i_feat = True

                    if 'IS' in predicate:
                        if 'NOT' in predicate:
                            if feature_value:
                                save_i_feat = True
                        else:
                            if not feature_value:
                                save_i_feat = True

                if save_i_feat:
                    i_feat_list.append(i_feat)

            # save i_feat
            i_feat_predicate[field_name] = i_feat_list

        if field_combination:
            final_i_feat_set = set([])
            for field_name in i_feat_predicate:
                field_name_i_feat_set = set(i_feat_predicate[field_name])
                if field_combination == 'OR':
                    final_i_feat_set.update(field_name_i_feat_set)
                if field_combination == 'AND':
                    if len(final_i_feat_set) == 0:
                        final_i_feat_set = field_name_i_feat_set
                    else:
                        final_i_feat_set.intersection_update(field_name_i_feat_set)

            final_i_feat_list = list(final_i_feat_set)
            return final_i_feat_list
        else:
            return i_feat_list

    if 'field_combination' in clause_where_dict.keys():
        if isinstance(clause_where_dict['field_combination'], str):
            field_combination = clause_where_dict['field_combination']
            i_feat_list = field_predicate(geolayer, clause_where_dict, field_combination)

    # just field_predicate in  clause_where_dict
    else:
        i_feat_list = field_predicate(geolayer, clause_where_dict)

    return i_feat_list


def clause_group_by(geolayer, field_name_list):
    """
    Return a dictionnary with field name list as key and i_feat list from geolayer
    """

    if isinstance(field_name_list, str):
        field_name_list = [field_name_list]

    result_dico = {}
    for i_feat in geolayer['features']:
        feature = geolayer['features'][i_feat]

        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature = eval(feature)

        field_value_tuple = tuple(
            [feature['attributes'][field_name] if field_name in feature['attributes'] else None for field_name in
             field_name_list])

        # convert list value to tuple (if exists) very rare
        field_value_tuple = tuple([tuple(value) if isinstance(value, list) else value for value in field_value_tuple])

        if field_value_tuple in result_dico:
            result_dico[field_value_tuple].append(i_feat)
        else:
            result_dico[field_value_tuple] = [i_feat]

    return result_dico


def clause_order_by(geolayer, order_parameters):
    """
    Send i_feat list in order define in order_parameters

    order_parameters format : 3 poosibilities :
        order_parameters = 'field_name' (order by default is ASC)
        order_parameters = ('field_name', 'ASC' or 'DESC')
        order_parameter = [('field_name_a', 'ASC' or 'DESC'), ('field_name_b', 'ASC' or 'DESC'), ..., ('field_name_n', 'ASC' or 'DESC'
    """

    def insert_in_order_list_by_split(value, i_feat_list, order_by_list):
        # try to insert at extremity of list
        # value is lower of last value in order_by_list
        if value <= order_by_list[0][0]:
            if value == order_by_list[0][0]:
                order_by_list[0][1] = order_by_list[0][0] + i_feat_list
            else:
                order_by_list = [(value, i_feat_list)] + order_by_list
            return order_by_list
        # value is upper of last value in order_by_list
        elif value >= order_by_list[-1][0]:
            if value == order_by_list[-1][0]:
                order_by_list[-1][1] = order_by_list[-1][0] + i_feat_list
            else:
                order_by_list = order_by_list + [(value, i_feat_list)]
            return order_by_list

        # if no insertion we have to split in two
        list_cuter_idx = int(len(order_by_list) / 2)
        if value <= order_by_list[list_cuter_idx-1][0]:
            if value == order_by_list[list_cuter_idx-1][0]:
                order_by_list[list_cuter_idx - 1][1] += i_feat_list
                return order_by_list
            else:
                order_by_list_splited = order_by_list[:list_cuter_idx]
                result = insert_in_order_list_by_split(value, i_feat_list, order_by_list_splited)
                return result + order_by_list[list_cuter_idx:]

        if value >= order_by_list[list_cuter_idx][0]:
            if value == order_by_list[list_cuter_idx][0]:
                order_by_list[list_cuter_idx][1] += i_feat_list
                return order_by_list
            else:
                order_by_list_splited = order_by_list[list_cuter_idx:]
                result = insert_in_order_list_by_split(value, i_feat_list, order_by_list_splited)
                return order_by_list[:list_cuter_idx] + result

        return order_by_list[:list_cuter_idx] + [(value, i_feat_list)] + order_by_list[list_cuter_idx:]


    def order_values(dico_value, field_order):
        """
            This function ordered value in function of field order
        """
        order_by_list = None
        none_value_i_feat = []
        for value in dico_value:
            i_feat_list = dico_value[value]
            if None in value:
                none_value_i_feat += i_feat_list
            else:
                # first iteration
                if not order_by_list:
                    order_by_list = [(value, i_feat_list)]
                else:
                    order_by_list = insert_in_order_list_by_split(value, i_feat_list, order_by_list)

        # reverse order if we are DESC
        if field_order.upper() == 'DESC' and order_by_list:
            order_by_list = sorted(order_by_list, reverse=True)

        # add none value (if exists) in function of order_fields
        if len(none_value_i_feat) > 0:
            if order_by_list:
                if field_order.upper() == 'ASC':
                    order_by_list += [((None,), none_value_i_feat)]
                else:
                    order_by_list = [((None,), none_value_i_feat)] + order_by_list
            else:
                order_by_list = [(None, none_value_i_feat)]

        return order_by_list


    def field_group_by_then_order(geolayer, order_parameters):
        """
        This function is used to realise first a group by and reorder result
        Then it recall it if there is an other field_order_paramenters
        """
        (field_name, field_order) = order_parameters[0]
        gb_field_name = clause_group_by(geolayer, field_name)
        gb_field_name_ordered = order_values(gb_field_name, field_order)
        result_i_feat_list = []
        for value, i_feat_list in gb_field_name_ordered:
            if len(i_feat_list) > 1:
                if len(order_parameters) > 1:
                    new_order_parameters = order_parameters[1:]
                    new_geolayer = create_geolayer_from_i_feat_list(geolayer, i_feat_list, reset_i_feat=False)
                    result_i_feat_list += field_group_by_then_order(new_geolayer, new_order_parameters)
                else:
                    result_i_feat_list += i_feat_list
            else:
                result_i_feat_list += i_feat_list

        return result_i_feat_list

    # verification enters parameters
    if isinstance(order_parameters, (list, tuple)):
        authorised_order_value = set(['ASC', 'DESC'])
        for i_field, field in enumerate(order_parameters):
            if len(field) == 1:
                order_parameters[i_field] = (field, 'ASC')
            elif len(field) == 2:
                if field[1].upper() not in authorised_order_value:
                    print('error you must add "ASC" or "DESC" key in second position')
            else:
                print('error')
    elif isinstance(order_parameters, str):
        order_parameters = [(order_parameters, 'ASC')]
    else:
        print("error: order_parameters must be a list / tuple or str value")

    for (field_name, order_value) in order_parameters:
        if field_name not in geolayer['metadata']['fields']:
            print('error : {field_name} does not exists in geolayer'.format(field_name))

    return field_group_by_then_order(geolayer, order_parameters)


####
#
# TOOLS
#
###
def sql(path, sql_request):
    data_source = ogr.Open(path)
    return data_source.ExecuteSQL(sql_request)


def field_statistics(geolayer, statistic_field, bessel_correction=True):
    """
    This function return a dictionary with statistics result in it.

        statistic_key : SUM, MEAN, MIN, MAX, RANGE, STD, COUNT, FIRST, LAST, VARIANCE, WEIGHTED_MEAN, COVARIANCE

    INPUT / OUTPUT field type table :
         One field is required :
            SUM : if original field type is real or integer       | output original field type
            MEAN : if original field type is real or integer      | output real
            MIN : if original field type is real or integer       | output original field type
            MAX : if original field type is real or integer       | output original field type
            RANGE : if original field type is real or integer     | output original field type
            STD : if original field type is real or integer       | output real
            COUNT :  original field type doesn't matter           | output integer
            FIRST : original field type doesn't matter            | output original field type
            LAST : original field type doesn't matter             | output original field type
            VARIANCE : if original field type is real or integer  | output real

        Two fields are required :
            WEIGHTED_MEAN : fields type is real or integer        | output real
            COVARIANCE : fields type is real or integer           | output real


    statistic_fields :
        structure example [(field_name_A, statistic_key),
                           ((field_name_a, field_name_c), statistic_key),
                           (...),
                           (field_name_X, statistic_key_1),
                           (field_name_X, statistic_key_2)]

    bassel_correction : if True in case of VARIANCE calculation apply bessel correction :
        https://en.wikipedia.org/wiki/Bessel%27s_correction

    output structure : dict 
        output example : {  field_name_a: {statistic_key: statistic value}
                            (field_name_a, field_name_c) : {statistic_key: statistic value}
                            field_name_x {statistic_key_1: statistic value,
                                         {statistic_key_2: statistic value}
                        }

    :param geolayer:
    :param statistic_field: list of tuples
    :param bessel_correction: boolean
    :return: dict
    """

    valid_field_type = {0, 1, 2, 3, 10, 11, 12, 13}
    statistic_keys = {'SUM', 'MEAN', 'MIN', 'MAX', 'RANGE', 'STD', 'COUNT', 'FIRST', 'LAST', 'VARIANCE',
                      'WEIGHTED_MEAN', 'COVARIANCE'}

    # test if field in statistic_field are valid
    for i_stat, (field_value, statistic_type) in enumerate(statistic_field):
        if isinstance(field_value, str):
            if 'fields' in geolayer['metadata']:
                field_name_type = geolayer["metadata"]['fields'][field_value]['type']
                if field_name_type not in valid_field_type or statistic_type not in statistic_keys:
                    statistic_field[i_stat] = None
        elif isinstance(field_value, (list, tuple, set)):
            for field_name in field_value:
                if isinstance(field_name, str):
                    if 'fields' in geolayer['metadata']:
                        field_name_type = geolayer["metadata"]['fields'][field_name]['type']
                        if field_name_type not in valid_field_type or statistic_type not in statistic_keys:
                            statistic_field[i_stat] = None
        else:
            print('error : field_name type is not correct')

    statistic_field = [value for value in statistic_field if value is not None]

    statistic_result = [0] * len(statistic_field)

    for fid, i_feat in enumerate(geolayer['features']):
        feature = geolayer['features'][i_feat]

        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature = eval(feature)

        for i, (field_name, statistic_type) in enumerate(statistic_field):

            if statistic_type.upper() == 'SUM':
                statistic_result[i] += feature['attributes'][field_name]
            elif statistic_type.upper() == 'MEAN':
                if fid == 0:
                    statistic_result[i] = feature['attributes'][field_name]
                else:
                    statistic_result[i] = (statistic_result[i] * fid + feature['attributes'][field_name]) / (
                            fid + 1)
            elif statistic_type.upper() == 'WEIGHTED_MEAN':
                (field_name_a, field_name_b) = field_name
                value_field_a = feature['attributes'][field_name_a]
                value_field_b = feature['attributes'][field_name_b]
                if fid == 0:
                    statistic_result[i] = (value_field_a * value_field_b, value_field_b)
                else:
                    statistic_result[i] = (statistic_result[i][0] + value_field_a * value_field_b, statistic_result[i][1] +value_field_b)
                # last iteration
                if fid == len(geolayer['features']) - 1:
                    statistic_result[i] = statistic_result[i][0] / statistic_result[i][1]
            elif statistic_type.upper() == 'COVARIANCE':
                (field_name_a, field_name_b) = field_name
                value_a = feature['attributes'][field_name_a]
                value_b = feature['attributes'][field_name_b]
                if fid == 0:
                    product_sum = 0.
                    means = field_statistics(geolayer, [(field_name_a, 'MEAN'), (field_name_b, 'MEAN')])
                    mean_a = means[field_name_a]['MEAN']
                    mean_b = means[field_name_b]['MEAN']
                product = (value_a - mean_a) * (value_b - mean_b)
                product_sum += product

                # if last iteration
                if fid == len(geolayer['features']) - 1:
                    result_value = product_sum / (len(geolayer['features']))
                    statistic_result[i] = result_value

            elif statistic_type.upper() == 'MIN':
                if fid == 0:
                    statistic_result[i] = feature['attributes'][field_name]
                statistic_result[i] = min(statistic_result[i], feature['attributes'][field_name])
            elif statistic_type.upper() == 'MAX':
                if fid == 0:
                    statistic_result[i] = feature['attributes'][field_name]
                statistic_result[i] = max(statistic_result[i], feature['attributes'][field_name])
            elif statistic_type.upper() == 'RANGE':
                if fid == 0:
                    save_min = feature['attributes'][field_name]
                    save_max = feature['attributes'][field_name]
                save_min = min(save_min, feature['attributes'][field_name])
                save_max = max(save_max, feature['attributes'][field_name])
                statistic_result[i] = save_max - save_min

            elif statistic_type.upper() in ['STD', 'VARIANCE']:
                if fid == 0:
                    # saving values in a list
                    statistic_result[i] = [0] * len(geolayer['features'])
                    statistic_result[i][0] = feature['attributes'][field_name]
                else:
                    statistic_result[i][fid] = feature['attributes'][field_name]
                # if last iteration
                if fid == len(geolayer['features']) - 1:
                    nb_value = len(statistic_result[i])
                    mean_value = sum(statistic_result[i]) / nb_value
                    mean_deviation = [(value - mean_value) ** 2 for value in statistic_result[i]]
                    if statistic_type.upper() == 'STD':
                        if bessel_correction:
                            result_value = (sum(mean_deviation) / (nb_value - 1)) ** 0.5
                        else:
                            result_value = (sum(mean_deviation) / (nb_value)) ** 0.5
                    else:
                        if bessel_correction:
                            result_value = (sum(mean_deviation) / (nb_value - 1))
                        else:
                            result_value = (sum(mean_deviation) / nb_value)
                    statistic_result[i] = result_value

            # for all field type
            if statistic_type.upper() == 'COUNT':
                statistic_result[i] += 1
            elif statistic_type.upper() == 'FIRST':
                if fid == 0:
                    statistic_result[i] = feature['attributes'][field_name]
            elif statistic_type.upper() == 'LAST':
                statistic_result[i] = feature['attributes'][field_name]

    # write results in dico result
    dico_result = {}
    for i_stat, (field_name, statistic_type) in enumerate(statistic_field):
        try:
            dico_result[field_name][statistic_type] = statistic_result[i_stat]
        except KeyError:
            dico_result[field_name] = {statistic_type: statistic_result[i_stat]}

    return dico_result


def ogr_geom_type_to_geoformat_geom_type(ogr_geom_type):
    """
    Make transformation between OGR to Geoformat geometry type

    :param ogr_geom_type: (int) OGR geometry type
    :return: (str) Geoformat geometry type
    """
    if ogr_geom_type == 0:
        return 'Geometry'
    if ogr_geom_type == GEOMETRY_TYPE['Point25D']:
        return 'Point25D'
    if ogr_geom_type == GEOMETRY_TYPE['LineString25D']:
        return 'LineString25D'
    if ogr_geom_type == -GEOMETRY_TYPE['Polygon25D']:
        return 'Polygon25D'
    if ogr_geom_type == GEOMETRY_TYPE['MultiPoint25D']:
        return 'MultiPoint25D'
    if ogr_geom_type == GEOMETRY_TYPE['MultiLineString25D']:
        return 'MultiLineString25D'
    if ogr_geom_type == GEOMETRY_TYPE['MultiPolygon25D']:
        return 'MultiPolygon25D'
    if ogr_geom_type == GEOMETRY_TYPE['Point']:
        return 'Point'
    if ogr_geom_type == GEOMETRY_TYPE['LineString']:
        return 'LineString'
    if ogr_geom_type == GEOMETRY_TYPE['Polygon']:
        return 'Polygon'
    if ogr_geom_type == GEOMETRY_TYPE['MultiPoint']:
        return 'MultiPoint'
    if ogr_geom_type == GEOMETRY_TYPE['MultiLineString']:
        return 'MultiLineString'
    if ogr_geom_type == GEOMETRY_TYPE['MultiPolygon']:
        return 'MultiPolygon'
    if ogr_geom_type == GEOMETRY_TYPE['GeometryCollection']:
        return 'GeometryCollection'
    if ogr_geom_type == GEOMETRY_TYPE['None']:
        return 'No Geometry'


def geoformat_geom_type_to_ogr_geom_type(geoformat_geom_type):
    """
    Make transformation between Geoformat geometry type to OGR geometry type

    :param geoformat_geom_type: (str) Geoformat geometry type
    :return: (int) ogr geom type correspondance
    """
    if geoformat_geom_type is None:
        return GEOMETRY_TYPE["None"]
    if geoformat_geom_type.upper() == 'GEOMETRY':  # Geometry
        return GEOMETRY_TYPE['Unknown']
    if geoformat_geom_type.upper() == 'POINT25D':  # Point25D
        return GEOMETRY_TYPE["Point25D"]
    if geoformat_geom_type.upper() == 'LINESTRING25D':  # LineString25D
        return GEOMETRY_TYPE["LineString25D"]
    if geoformat_geom_type.upper() == 'POLYGON25D':  # Polygon25D
        return GEOMETRY_TYPE["Polygon25D"]
    if geoformat_geom_type.upper() == 'MULTIPOINT25D':  # MultiPoint25D
        return GEOMETRY_TYPE["MultiPoint25D"]
    if geoformat_geom_type.upper() == 'MULTILINESTRING25D':  # MultiLineString25D
        return GEOMETRY_TYPE["MultiLineString25D"]
    if geoformat_geom_type.upper() == 'MULTIPOLYGON25D':  # MultiPolygon25D
        return GEOMETRY_TYPE["MultiPolygon25D"]
    if geoformat_geom_type.upper() == 'POINT':  # Point
        return GEOMETRY_TYPE["Point"]
    if geoformat_geom_type.upper() == 'LINESTRING':  # LineString
        return GEOMETRY_TYPE["LineString"]
    if geoformat_geom_type.upper() == 'POLYGON':  # Polygon
        return GEOMETRY_TYPE["Polygon"]
    if geoformat_geom_type.upper() == 'MULTIPOINT':  # MultiPoint
        return GEOMETRY_TYPE["MultiPoint"]
    if geoformat_geom_type.upper() == 'MULTILINESTRING':  # MultiLineString
        return GEOMETRY_TYPE["MultiLineString"]
    if geoformat_geom_type.upper() == 'MULTIPOLYGON':  # MultiPolygon
        return GEOMETRY_TYPE["MultiPolygon"]
    if geoformat_geom_type.upper() == 'GEOMETRYCOLLECTION':  # GeometryCollection
        return GEOMETRY_TYPE["GeometryCollection"]
    if geoformat_geom_type.upper() == 'NO GEOMETRY':  # No Geometry
        return GEOMETRY_TYPE["None"]


def upgrade_geometry(geometry, geometry_type_filter=None):
    """
    Transform a given geometry to a GeometryCollection, all inside geometries are transformed to MULTI geometries.
    Optionally you can add a geometry_type_filter (if you'r geometry input is an GeometryCollection) in this case only 
    filtred geometry type will be return
    """
    if isinstance(geometry, dict):
        if geometry['type'].upper() == 'GEOMETRYCOLLECTION':
            geometry_list = geometry['geometries']
        else:
            geometry_list = [geometry]

    if geometry_type_filter:
        if isinstance(geometry_type_filter, str):
            geometry_type_filter = {geometry_type_filter.upper()}
        elif isinstance(geometry_type_filter, (list, tuple, set)):
            geometry_type_filter = set(geometry_type_filter)
        else:
            print('geometry_type_filter must be a geometry type or a list of geometry type')
    else:
        geometry_type_filter = {'POINT', 'LINESTRING', 'POLYGON', 'MULTIPOINT', 'MULTILINESTRING', 'MULTIPOLYGON', 'GEOMETRY', 'GEOMETRYCOLLECTION'}

    result_geometry_list = []
    for geometry in geometry_list:
        if geometry['type'].upper() in geometry_type_filter:
            result_geometry = dict(geometry)
            if not 'MULTI' in result_geometry['type'].upper():
                result_geometry['coordinates'] = [result_geometry['coordinates']]
                result_geometry['type'] = 'Multi' + result_geometry['type']
            result_geometry_list.append(result_geometry)

    return {'type': 'GeometryCollection', 'geometries': result_geometry_list}


def geometry_to_geometry_collection(geometry, geometry_type_filter=None, bbox=True):
    """
    Transform a geometry to GeometryCollection
    """
    if geometry_type_filter:
        if isinstance(geometry_type_filter, str):
            geometry_type_filter = {geometry_type_filter.upper()}
        elif isinstance(geometry_type_filter, (list, tuple, set)):
            set_geom_type = set([])
            for geometry_type in geometry_type_filter:
                set_geom_type.update(set([geometry_type.upper()]))
            geometry_type_filter = set_geom_type
        else:
            print('geometry_type_filter must be a geometry type or a list of geometry type')
    else:
        geometry_type_filter = GEOFORMAT_GEOMETRY_TYPE

    geometry_type = geometry['type']
    if geometry_type.upper() != 'GEOMETRYCOLLECTION':
        if geometry_type.upper() in geometry_type_filter:
            geometry_collection = {'type': 'GeometryCollection', 'geometries': [geometry]}
            if bbox:
                if 'bbox' in geometry:
                    bbox = geometry['bbox']
                else:
                    bbox = coordinates_to_bbox(geometry['coordinates'])
                geometry_collection['bbox'] = bbox

            return geometry_collection
        else:
            print('geometry type non compatible with geometry in geoformat_lib :', geometry_type_filter )

    if geometry_type.upper() == 'GEOMETRYCOLLECTION':
        geometry_list = []
        if bbox:
            bbox_geometry_collection = None
        for geometry in geometry['geometries']:
            if geometry['type'].upper() in geometry_type_filter:
                if bbox:
                    if not 'bbox' in geometry:
                        bbox = coordinates_to_bbox(geometry['coordinates'])
                        if not bbox_geometry_collection:
                            bbox_geometry_collection = bbox
                        else:
                            bbox_geometry_collection = bbox_union(bbox_geometry_collection, bbox)
                        geometry['bbox'] = bbox

                geometry_list.append(geometry)
        geometry_collection = {'type': 'GeometryCollection', 'geometries': geometry_list}
        if bbox:
            geometry_collection['bbox'] = bbox_geometry_collection

        return geometry_collection


def multi_geom_to_single_geom(geometry):
    """
    Iterator in given geometry and send single geometry (Point, LineString, Polygon) if geometry is a multigeometry.
    Works with GeometryCollection
    """

    if geometry['type'].upper() == 'GEOMETRYCOLLECTION':  # 'GeometryCollection'
        for inside_geometry in geometry['geometries']:
            for single_geom in multi_geom_to_single_geom(inside_geometry):
                yield single_geom

    elif geometry['type'].upper() in ['MULTIPOINT', 'MULTILINESTRING',
                                      'MULTIPOLGYON']:  # ['MultiPoint', 'MultiLineString', 'MultiPolygon']
        if geometry['type'].upper() == 'MULTIPOINT':  # 'MultiPoint'
            single_geometry_type = 'POINT'  # Point
        elif geometry['type'].upper() == 'MULTILINESTRING':  # 'MultiLineString'
            single_geometry_type = 'LINESTRING'  # 'LineString'
        else:
            single_geometry_type = 'POLYGON'  # 'Polygon'

        multi_coordinates = geometry['coordinates']
        for coordinates in multi_coordinates:
            yield {'type': single_geometry_type, 'coordinates': coordinates}

    else:
        yield geometry


def verify_geom_compatibility(driver_name, metadata_geometry_type):
    """

    OGR Geometry Type List :
        -2147483647: 'Point25D'
        -2147483646: 'LineString25D'
        -2147483645: 'Polygon25D'
        -2147483644: 'MultiPoint25D'
        -2147483643: 'MultiLineString25D'
        -2147483642: 'MultiPolygon25D'
                  0: 'Geometry'
                  1: 'Point'
                  2: 'LineString'
                  3: 'Polygon'
                  4: 'MultiPoint'
                  5: 'MultiLineString'
                  6: 'MultiPolygon'
                  7: 'GeometryCollection'
                100: 'No Geometry'

    [[0],[1], [2, 5], [3, 6], [4], [100]],  # 'Esri Shapefile'
    [[1, 4], [2, 5], [3, 6], [100]],  # TAB 'Mapinfo File'
    [[1, 4], [2, 5], [3, 6], [100]],  # MIF/MID 'Mapinfo File'
    [[1, 2, 3, 4, 5, 6, 7, 100]],  # KML
    [[1, 2, 3, 4, 5, 6, 7, 100]],  # GML
    [[0, 1, 2, 3, 4, 5, 6, 7, 100]],  # GeoJSON
    [[1], [2], [3, 6], [4], [5], [100]],  # Geoconcept
    [[1], [2, 5], [3, 6], [4], [100]],  # FileGDB
    [[1, 2, 3, 4, 5, 6, 7, 100]],  # SQLite
    [[1, 2, 3, 4, 5, 6, 7, 100]],  # POSTGRESQL
    [[1, 2, 3, 4, 5, 6, 7, 100]]   # CSV
    ],

    """

    if isinstance(metadata_geometry_type, str):
        metadata_geometry_type = [metadata_geometry_type.upper()]
    elif isinstance(metadata_geometry_type, (tuple, list, set)):
        metadata_geometry_type = [value.upper() for value in metadata_geometry_type]

    set_geometry_type = set(metadata_geometry_type)

    if driver_name.upper() == OGR_FORMAT_ESRI_SHAPEFILE:
        # POLYGON
        set_polygon = {'NO GEOMETRY', 'POLYGON', 'MULTIPOLYGON'} #set(['No Geometry', 'Polygon', 'MultiPolygon'])
        if len(set_geometry_type) <= 3 and len(set_geometry_type.difference(set_polygon)) == 0:
            return 3
        # LINESTRING
        set_linestring = {'NO GEOMETRY', 'LINESTRING', 'MULTILINESTRING'} #set(['No Geometry', 'LineString', 'MultiLineString'])
        if len(set_geometry_type) <= 3 and len(set_geometry_type.difference(set_linestring)) == 0:
            return 2
        # POINT
        set_point = {'NO GEOMETRY', 'POINT', 'MULTIPOINT'}# set(['No Geometry', 'Point', 'MultiPoint'])
        if len(set_geometry_type) <= 3 and len(set_geometry_type.difference(set_point)) == 0:
            return 1

    if driver_name.upper() == OGR_FORMAT_POSTGRESQL:
        if len(set_geometry_type) > 1:
            return 0
        else:
            return geoformat_geom_type_to_ogr_geom_type(metadata_geometry_type[0])

    if driver_name.upper() == OGR_FORMAT_GEOJSON:
        return 0


def multi_to_single_geom(geometry, bbox=True):
    """
        This function explode a given multi part geometry to single part geometry
    """

    # if geometry collection
    if geometry['type'].upper() == 'GEOMETRYCOLLECTION':  # 'GeometryCollection'
        for under_geom in geometry['geometries']:
            for under_geom_in_under_geom in multi_to_single_geom(under_geom, bbox=bbox):
                yield under_geom_in_under_geom
    # for others geometries
    else:
        # if multipart geometry
        if geometry['type'].upper() in ['MULTIPOINT', 'MULTILINESTRING',
                                        'MULTIPOLYGON']:  # ['MultiPoint', 'MultiLineString', 'MultiPolygon']
            if geometry['type'].upper() == 'MULTIPOINT':  # 'MultiPoint'
                new_geometry = {'type': 'Point'}
            elif geometry['type'].upper() == 'MULTILINESTRING':  # 'MultiLineString'
                new_geometry = {'type': 'LineString'}
            elif geometry['type'].upper() == 'MULTIPOLYGON':  # 'MultiPolygon'
                new_geometry = {'type': 'Polygon'}

            coordinates = geometry['coordinates']
            for under_geom in coordinates:
                return_geometry = dict(new_geometry)
                return_geometry['coordinates'] = under_geom
                if bbox:
                    return_geometry['bbox'] = coordinates_to_bbox(under_geom)
                yield return_geometry

        # if yet single geometry
        else:
            yield geometry


def multi_to_single_geom_geolayer(geolayer):
    # creation de l'output en copiant les metadata de l'input
    geolayer_out = copy.deepcopy(geolayer)

    del geolayer_out['features']
    if geolayer['metadata']['geometry_ref']['type'].upper() == 'MULTIPOINT':  # 'MultiPoint'
        geolayer_out['metadata']['geometry_ref']['type'] = 'Point'
    elif geolayer['metadata']['geometry_ref']['type'].upper() == 'MULTILINESTRING':  # 'MultiLineString'
        geolayer_out['metadata']['geometry_ref']['type'] = 'LineString'
    elif geolayer['metadata']['geometry_ref']['type'].upper() == 'MULTIPOLYGON':  # 'MultiPolygon'
        geolayer_out['metadata']['geometry_ref']['type'] = 'Polygon'

    # boucle et transformation des géométries multi part en single part
    new_i_feat = 0
    geolayer_out['features'] = {}
    for i_feat in geolayer['features']:

        feature = geolayer['features'][i_feat]
        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature = eval(feature)

        geometry = feature['geometry']
        for new_geometry in multi_to_single_geom(geometry):
            new_feature = {'attributes': feature['attributes'],
                           'geometry': new_geometry}

            # if feature is serialized
            if 'feature_serialize' in geolayer['metadata']:
                if geolayer['metadata']['feature_serialize']:
                    new_feature = str(new_feature)

            geolayer_out['features'][new_i_feat] = new_feature
            new_i_feat += 1

    return geolayer_out


def merge_geometries(geom_a, geom_b, bbox=True):
    """
    geom_a
    geom_b
    bbox = True (default) + 5 % time


    Return a merging geometry result of adding two differents geometries
    !! Carfull this function does not "union" two geometry but merge two geometry !!

    Merging Table :

        Single AND Single
            Point + Point = MultiPoint
            LineString + LineString = MultiLineString
            Polygon + Polygon = MultiPolygon

        Single AND Multi
            Point + MultiPoint = MultiPoint
            LineString  + MultiLineString = MultiLineString
            Polygon + MultiPolygon = MultiPolygon

        Mixed Geometries Types and GeometryCollection
            Point + Polygon = GeometryCollection(Point, Polygon)
            GeometryCollection(Polygon + LineString) + LineSting = GeometryCollection(Polygon + MultiLineString)
            GeometryCollection(MultiPolygon, LineString), GeometryCollection(MultiPoint, LineString)
                = GeometryCollection(MultiPolygon, MultiLineString, MultiPoint)



    How does it works ?

        - first if geometry categories are the same

        - if geometry categories are differents or GeometryCollection
            We will have a GeometryCollection

    """
    new_geom = {}

    # if same geometry category (Point, MultiPoint), (LineString, MultiLineString), (Polygon, MultiPolygon)
    if geom_a['type'].replace('Multi', '') == geom_b['type'].replace('Multi', '') and geom_a[
        'type'] != 'GeometryCollection' and geom_b['type'] != 'GeometryCollection':
        new_geom['type'] = str(geom_a['type'])
        new_geom['coordinates'] = list(geom_a['coordinates'])

        if 'Multi' in new_geom['type']:
            if 'Multi' in geom_b['type']:
                for geom_coordinates in geom_b['coordinates']:
                    new_geom['coordinates'].append(geom_coordinates)
            else:
                new_geom['coordinates'].append(geom_b['coordinates'])

        else:
            new_geom['type'] = 'Multi' + new_geom['type']
            if 'Multi' in geom_b['type']:
                geom = [new_geom['coordinates']]
                for geom_coordinates in geom_b['coordinates']:
                    geom.append(geom_coordinates)
                new_geom['coordinates'] = geom
            else:
                new_geom['coordinates'] = [new_geom['coordinates'], geom_b['coordinates']]
    else:
        # new_geom['type'] = 'GeometryCollection'
        if geom_a['type'] == 'GeometryCollection' and geom_b['type'] == 'GeometryCollection':
            # first loop on geom_a geometries
            for i_a, geojson_geometrie_a in enumerate(geom_a['geometries']):
                if i_a == 0:
                    new_geom = geojson_geometrie_a
                else:

                    new_geom = merge_geometries(new_geom, geojson_geometrie_a, bbox=bbox)

            # add geom_ b geometries
            for geojson_geometrie_b in geom_b['geometries']:
                new_geom = merge_geometries(new_geom, geojson_geometrie_b, bbox=bbox)


        elif geom_a['type'] == 'GeometryCollection' or geom_b['type'] == 'GeometryCollection':
            if geom_a['type'] == 'GeometryCollection':
                ori_geom_collect = dict(geom_a)
                ori_geom_simple = dict(geom_b)
            else:
                ori_geom_collect = dict(geom_b)
                ori_geom_simple = dict(geom_a)

            # first loop on ori_geom_collect geometries
            for i_a, geojson_geometrie_a in enumerate(ori_geom_collect['geometries']):
                if i_a == 0:
                    new_geom = geojson_geometrie_a
                else:
                    new_geom = merge_geometries(new_geom, geojson_geometrie_a, bbox=bbox)

            added_geom = False
            # then we see if ori_geom_simple as similar geom type in ori_geom_collect else we had
            for i_geom, geojson_geom in enumerate(new_geom['geometries']):
                if geojson_geom['type'].replace('Multi', '') == ori_geom_simple['type'].replace('Multi', ''):
                    replace_geom = merge_geometries(geojson_geom, ori_geom_simple)
                    new_geom['geometries'][i_geom] = replace_geom
                    added_geom = True
                    # end loop
                    break

            if not added_geom:
                # if not break we had ori_geom_simple to new_geom GEOMETRYCOLLECTION
                new_geom['geometries'] = new_geom['geometries'] + [dict(ori_geom_simple)]

        else:
            new_geom['type'] = 'GeometryCollection'
            new_geom['geometries'] = [dict(geom_a), dict(geom_b)]

    # recompute bbox
    if bbox:
        if new_geom['type'] == 'GeometryCollection':
            for i_geom, geom in enumerate(new_geom['geometries']):
                geom_bbox = coordinates_to_bbox(geom['coordinates'])
                new_geom['geometries'][i_geom]['bbox'] = geom_bbox
                if i_geom == 0:
                    geom_coll_extent = geom_bbox
                else:
                    geom_coll_extent = bbox_union(geom_coll_extent, geom_bbox)

            new_geom['bbox'] = geom_coll_extent

        else:
            new_geom['bbox'] = coordinates_to_bbox(new_geom['coordinates'])
    else:
        if 'bbox' in new_geom:
            del new_geom['bbox']

        if new_geom['type'] == 'GeometryCollection':

            for i_geom, geom in enumerate(new_geom['geometries']):
                if 'bbox' in geom:
                    del new_geom['geometries'][i_geom]['bbox']

    return new_geom


def line_merge(geometry, bbox=True):
    """
    Returns a (set of) LineString(s) formed by sewing together the constituent line work of a MULTILINESTRING.

    """

    def merge_loop_over_single_linestring(multilinestring):
        """
        This function define :
            * start_dict store each start point of a line part -> at each point you store the geom position in
            coordinates list.
            * end_dict store each end point point of a line part -> at each point you store the geom position in
            coordinates list.

            * hub_point with this two dictionaries we create hub_point that store for each unique point the counting
            number of times this point appears in the multinlinestring.

            * we loop on each point in hub point and we try to know, if this point appears in two line, its position
            (start / end) for each of the lines to which it belongs. At this time you have 3 possibilities :
                # 2 points in start_dict
                # 2 points in end_dict
                # 1 point in start_dict and 1 point in end_dict

                * we initialize some variables :
                    [before loop}
                    - final_coordinates (list) [before loop] : store each part to create a new geometry in output.
                    - computed_idx_geom (set) [before loop] : for each point on which we loop we store the under
                     geometry index.
                    - reloop (bool) [before loop] : if condition above (pass_point is True) then reloop is True.

                    [reinitialize at each loop step's]
                    - for_point_computed_idx_geom : store for each of two points the under geometry index. If we have
                    just one index inside it means we've processed a line that starts and ends at the same place
                    (a loop). In this case we do not in this case we don't change the geometry.
                    - result_part_coordinates (list) : store part new geometry.
                    - pass_point (bool) : if the geometry to which the point belongs has already been modified,
                     then it is not modified and pass_point is True.

                for each of 3 possibilites we create a new under geometry (result_part_coordinates) that we store step
                by step in final_ordinates if pass_point is False and for_point_computed_idx_geom.

            * Then we recreate a new geometry with data in final_coordinates and we add non concerned, by merging, geometries (geometries
            that are'nt in computed_idx_geom.
        """

        start_dict = {}
        end_dict = {}
        single_geom_list = list(multi_to_single_geom(multilinestring, bbox=False))

        for i_part_geom, single_geom in enumerate(single_geom_list):
            # begin
            start_point = tuple(single_geom['coordinates'][0])
            try:
                start_dict[start_point].update({i_part_geom})
            except KeyError:
                start_dict[start_point] = {i_part_geom}

            # end
            end_point = tuple(single_geom['coordinates'][-1])
            try:
                end_dict[end_point].update({i_part_geom})
            except KeyError:
                end_dict[end_point] = {i_part_geom}

            # count points occurrence
            # if count > 2 then we cannot merge geometries
            hub_point = {point: len(start_dict[point]) for point in start_dict}
            for end_point in end_dict:
                if end_point in hub_point:
                    hub_point[end_point] = hub_point[end_point] + len(end_dict[end_point])
                else:
                    hub_point[end_point] = len(end_dict[end_point])

        computed_idx_geom = set([])
        final_coordinates = []
        reloop = False

        for i_point, point in enumerate(hub_point):
            if hub_point[point] == 2:
                # here three configuration are possible
                # 2 points in start_dict
                # 2 points in end_dict
                # 1 point in start_dict and 1 point in end_dict
                # As it possible to have a point in both dict (third configuration) and a point is always located between
                # end of first geom and begin of second geom we begin with end_dict then start_dict

                result_part_coordinates = []
                pass_point = False
                for_point_computed_idx_geom = set([])
                if point in end_dict:
                    if end_dict[point] & computed_idx_geom:
                        reloop = True
                        pass_point = True
                    else:
                        for i_idx, i_part_geom in enumerate(end_dict[point]):
                            for_point_computed_idx_geom.update({i_part_geom})
                            geom = multilinestring['coordinates'][i_part_geom]
                            if i_idx == 0:
                                result_part_coordinates += geom
                            else:
                                # reverse geom
                                geom.reverse()
                                # add to result
                                result_part_coordinates = result_part_coordinates + geom[1:]

                if point in start_dict:
                    if start_dict[point] & computed_idx_geom:
                        reloop = True
                        pass_point = True
                    else:
                        for i_idx, i_part_geom in enumerate(start_dict[point]):
                            # add i_part_geom to computed_idx_geom
                            for_point_computed_idx_geom.update({i_part_geom})
                            geom = multilinestring['coordinates'][i_part_geom]
                            if i_idx == 0:
                                result_part_coordinates += geom[1:]
                            else:
                                # reverse geom
                                geom.reverse()
                                # add to result
                                result_part_coordinates = geom + result_part_coordinates

                # add result_part_coordinates to final_coordinates
                if result_part_coordinates and not pass_point:
                    if len(for_point_computed_idx_geom) == 2:
                        final_coordinates.append(result_part_coordinates)
                    else:
                        i_part_geom = list(for_point_computed_idx_geom)[0]
                        geom = multilinestring['coordinates'][i_part_geom]
                        final_coordinates.append(geom)

                # if this point is not passing we add geom part in computed_idx_geom
                if not pass_point:
                    computed_idx_geom.update(for_point_computed_idx_geom)

        # add non-computed idx geom
        for i_part_geom, single_geom in enumerate(single_geom_list):
            if not {i_part_geom} & computed_idx_geom:
                final_coordinates.append(single_geom['coordinates'])

        if len(final_coordinates) == 1:
            final_geometry = {'type': 'LineString', 'coordinates': final_coordinates[0]}
            # we do not have to reloop
            reloop = False
        else:
            final_geometry = {'type': 'MultiLineString', 'coordinates': final_coordinates}

        if reloop:
            return merge_loop_over_single_linestring(final_geometry)
        else:
            return final_geometry

    # save bbox info
    if bbox and 'bbox' in geometry:
        bbox_output = geometry['bbox']
    else:
        bbox_ouput = None

    # force input geometry to geometry collection
    geometry_collection = geometry_to_geometry_collection(geometry)
    # loop on each geometry
    new_geometry_collection = {'type': 'GeometryCollection', 'geometries': list(geometry_collection['geometries'])}
    for i_geom, geometry in enumerate(geometry_collection['geometries']):
        # if there is linestring in geometry type we launch a line_merge
        if "MULTILINESTRING" in geometry['type'].upper():
            merged_geometry = merge_loop_over_single_linestring(geometry)
        else:
            merged_geometry = geometry

        # add bbox geometry if required
        if bbox:
            if not 'bbox' in merged_geometry:
                merged_geometry['bbox'] = coordinates_to_bbox(merged_geometry['coordinates'])
            if i_geom == 0:
                bbox_geometry_collection = merged_geometry['bbox']
            else:
                bbox_geometry_collection = bbox_union(bbox_geometry_collection, merged_geometry['bbox'])

        new_geometry_collection['geometries'][i_geom] = merged_geometry


    if bbox:
        new_geometry_collection['bbox'] = bbox_geometry_collection

    # return output
    if len(new_geometry_collection['geometries']) > 1:
        return new_geometry_collection
    else:
        return new_geometry_collection['geometries'][0]


def euclidean_distance(point_a, point_b):
    """
    retunn Euclidean distance between two points

    :param point_a:
    :param point_b:
    :return: Euclidean distance between two points
    """
    (x_a, y_a) = point_a
    (x_b, y_b) = point_b
    return ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5


def manhattan_distance(point_a, point_b):
    """
    return Manhattan distance between to points

    :param point_a:
    :param point_b:
    :return: Manhattan distance between to points
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return float(abs(x1 - x2) + abs(y1 - y2))


def segment_length(segment, distance_type='EUCLIDEAN'):
    """
    Calculate length of a given segment
    """
    (point_a, point_b) = segment
    if distance_type.upper() == 'EUCLIDEAN':
        return euclidean_distance(point_a, point_b)
    elif distance_type.upper() == 'MANHATTAN':
        return manhattan_distance(point_a, point_b)
    else:
        print('type of distance : {distance_type} does not exists'.format(distance_type=distance_type))


def geometry_length(geometry, distance_type='EUCLIDEAN'):

    geometry = geometry_to_geometry_collection(geometry, geometry_type_filter=GEOFORMAT_GEOMETRY_TYPE)
    if geometry:
        length = 0
        for coordinates_list in geometry_to_coordinates_list(geometry):
            for segment in coordinates_to_segment(coordinates_list):
                length += segment_length(segment, distance_type=distance_type)

        return length


def line_parameters(segment):
    """
    Deduces from a segment lines (slope and  y-intercept) parameters passing through this segment

    :param segment: input segment
    :return: a dict with two linears parameters : slope AND y_intercept
    """

    ((x_a, y_a), (x_b, y_b)) = segment
    if x_b != x_a:
        a = (y_b - y_a) / (x_b - x_a)
        b = y_a - (x_a * a)
    else:
        a = 'VERTICAL'
        b = y_b

    return {'slope': a, 'y-intercept': b}


def perpendicular_line_parameters(line_parameters, point):
    """
    Gives perpendicular lines parameters of a line passing through a point from an original line parameters

    :param line_parameters: original line parameter
    :param point: point of origin which serves as a pivot for calculating the parameters of perpendicular lines
    :return:
    """

    a = line_parameters['slope']
    b = line_parameters['y-intercept']

    x_a, y_a = point
    if a == 0:
        a_bis = 'VERTICAL'
        b_bis = b
    elif a == 'VERTICAL':
        a_bis = 0
        b_bis = b
    else:
        a_bis = -1 / a
        b_bis = y_a - (x_a * a_bis)

    return {"slope": a_bis, 'y-intercept': b_bis}


def point_at_distance_with_line_parameters(point, line_parameters, distance, offset_distance=None):
    """
    Returns an point at distance to a input_point with a direction define by line parameters
    optional: add an offset distance (perpendicular to line_parameters value)

    :param point: input point
    :param line_parameters: line parameter that define direction to the new point
    :param distance: distance between input point to output point
    :param offset_distance: in option you can add a perpendicular offset input point
    :return: output point
    """

    a = line_parameters['slope']
    b = line_parameters['y-intercept']

    x_a, y_a = point
    if a == 'VERTICAL':
        x_b = x_a
        y_b = y_a + distance
    else:
        x_b = x_a + (distance / ((1 + a ** 2) ** 0.5))
        y_b = a * x_b + b

    ouput_point = x_b, y_b

    if offset_distance:
        perpendicular_parameter = perpendicular_line_parameters(line_parameters, ouput_point)
        offset_x, offset_y = point_at_distance_with_line_parameters(ouput_point, perpendicular_parameter,
                                                                    distance=offset_distance, offset_distance=None)
        ouput_point = offset_x, offset_y

    return ouput_point


def point_on_segment_range(segment, step_distance, offset_distance=None):
    """
    Iterator send point coordinates on a segment at a given step distance.
    optional: add an offset distance (perpendicular to line_parameters value)

    :param segment:
    :param step_distance:
    :param offset_distance:
    :return:
    """
    start_point, end_point = segment
    native_step_distance = step_distance
    line_parameter = line_parameters((start_point, end_point))
    # test because direction of the linestring can be different from the direction of an affine line
    if euclidean_distance(start_point,
                          point_at_distance_with_line_parameters(end_point, line_parameter, step_distance,
                                                                 offset_distance=offset_distance)) < euclidean_distance(
        start_point, end_point):
        step_distance = -step_distance

    distance = euclidean_distance(start_point, end_point)

    while distance > native_step_distance:
        start_point = point_at_distance_with_line_parameters(start_point, line_parameter, step_distance,
                                                             offset_distance=offset_distance)
        yield start_point
        distance = euclidean_distance(start_point, end_point)


def points_on_linestring_distance(linestring, step_distance, offset_distance=None):
    """
    Return a point geometry that is a point on a given linestring at a given step_distance
    optional: add an offset distance (perpendicular to line_parameters value)

    :param linestring: LineString or MultiLineString geometrie
    :param step_distance: distance between each steps
    :param offset_distance: if you want you can add an offset to final on point value
    :return: Point geometrie
    """

    def points_on_linestring_part(coordinates, step_distance, offset_distance=None):

        # note about remaining_distance
        # remaining_distance is the distance that remain after a new vertex (because when there is a new vertex we have
        # to recompute the step_distance remaining

        # loop on each coordinate
        for i_point, point in enumerate(coordinates):
            if i_point == 0:
                previous_point = point
                # init remaining distance
                remaining_distance = 0
            else:
                remaining_step_distance = step_distance - remaining_distance
                segment = (previous_point, point)

                # yield first point
                if i_point == 1:
                    if offset_distance:
                        line_parameter = line_parameters(segment)
                        perp_parameter = perpendicular_line_parameters(line_parameter, previous_point)
                        first_point = point_at_distance_with_line_parameters(previous_point, perp_parameter,
                                                                             distance=offset_distance)
                        yield {'type': 'Point', 'coordinates': first_point}
                    else:
                        yield {'type': 'Point', 'coordinates': previous_point}

                # for just one iteration
                for new_point in point_on_segment_range(segment, remaining_step_distance, offset_distance=None):
                    remaining_distance = 0
                    # reinit values
                    previous_point = new_point
                    segment = (previous_point, point)
                    # here we cannot use offset_distance directly in point_on_segment_range used above because we have
                    # to keep initial segment direction. Then we recompute offset new_point.
                    if offset_distance:
                        line_parameter = line_parameters(segment)
                        perp_parameter = perpendicular_line_parameters(line_parameter, new_point)
                        new_point = point_at_distance_with_line_parameters(new_point, perp_parameter,
                                                                           distance=offset_distance)
                    yield {'type': 'Point', 'coordinates': new_point}
                    break  # just one iteration

                # pass_on_loop check if we iterate on loop below
                pass_on_loop = False
                for new_point in point_on_segment_range(segment, step_distance, offset_distance=None):
                    remaining_distance = euclidean_distance(new_point, point)
                    pass_on_loop = True
                    # here we cannot use offset_distance directly in point_on_segment_range used above because we have
                    # to calculate the remain distance on non offseted point before. Then we recompute offset new_point
                    if offset_distance:
                        line_parameter = line_parameters(segment)
                        perp_parameter = perpendicular_line_parameters(line_parameter, new_point)
                        new_point = point_at_distance_with_line_parameters(new_point, perp_parameter,
                                                                           distance=offset_distance)
                    yield {'type': 'Point', 'coordinates': new_point}

                # if no iteration en loop above we recalculate remaining distance for next point on coordinates
                if not pass_on_loop:
                    remaining_distance += euclidean_distance(point, previous_point)

                previous_point = point

    # force coordinates to MULTI
    coordinates = linestring['coordinates']
    if 'MULTI' not in linestring['type'].upper():
        coordinates = [coordinates]

    for linestring_part in coordinates:
        for point in points_on_linestring_part(linestring_part, step_distance, offset_distance=offset_distance):
            yield point


def reproject_geometry(geometry, in_crs, out_crs, bbox_extent=True):
    """
    Reproject a geometry with an input coordinate reference system to an output coordinate system

    * GDAL/OSR dependencie :
        AssignSpatialReference()
        ImportFromEPSG()
        SpatialReference()
        TransformTo()
    *

    :param geometry: input geometry
    :param in_crs: input coordinate reference system
    :param out_crs: output coordinate system
    :return: output geometry
    """
    ogr_geometry = geojson_to_ogr_geom(geometry)

    # Assign spatial ref
    ## Input
    if isinstance(in_crs, int):
        in_proj = osr.SpatialReference()
        in_proj.ImportFromEPSG(in_crs)
    elif isinstance(in_crs, str):
        in_proj = osr.SpatialReference(in_crs)
    else:
        print('crs value must be a ESPG code or a  OGC WKT projection')

    ## Output
    if isinstance(out_crs, int):
        out_proj = osr.SpatialReference()
        out_proj.ImportFromEPSG(out_crs)
    elif isinstance(out_crs, str):
        out_proj = osr.SpatialReference(out_crs)
    else:
        print('crs value must be a ESPG code or a  OGC WKT projection')

    ogr_geometry.AssignSpatialReference(in_proj)
    ogr_geometry.TransformTo(out_proj)

    geometry = ogr_geom_to_geojson(ogr_geometry)
    if bbox_extent:
        geometry['bbox'] = coordinates_to_bbox(geometry['coordinates'])

    return geometry


def reproject_geolayer(geolayer, out_crs, in_crs=None, bbox_extent=True):

    if not in_crs:
        in_crs = geolayer['metadata']['geometry_ref']['crs']

    # change metadata
    geolayer['metadata']['geometry_ref']['crs'] = out_crs

    if bbox_extent:
        geolayer['metadata']['geometry_ref']['extent'] = None

    # reproject geometry
    for i_feat in geolayer['features']:
        feature = geolayer['features'][i_feat]

        # if geometry in feature
        if 'geometry' in feature.keys():
            feature_geometry = feature['geometry']
            new_geometry = reproject_geometry(feature_geometry, in_crs, out_crs, bbox_extent)
            if geolayer['metadata']['geometry_ref']['extent'] is None:
                geolayer['metadata']['geometry_ref']['extent'] = new_geometry['bbox']
            else:
                bbox_extent = geolayer['metadata']['geometry_ref']['extent']
                geolayer['metadata']['geometry_ref']['extent'] = bbox_union(bbox_extent, new_geometry['bbox'])

            # assign new geometry
            feature['geometry'] = new_geometry

    if bbox_extent:
        geolayer['metadata']['geometry_ref']['extent'] = bbox_extent

    return geolayer


def extent_bbox(bbox, extent):
    (x_min, y_min, x_max, y_max) = bbox
    x_min = x_min - extent
    y_min = y_min - extent
    x_max = x_max + extent
    y_max = y_max + extent

    return x_min, y_min, x_max, y_max


def bbox_union(bbox_a, bbox_b):
    """ realize union between to given bbox"""
    (x_min_a, y_min_a, x_max_a, y_max_a) = bbox_a
    (x_min_b, y_min_b, x_max_b, y_max_b) = bbox_b

    return min(x_min_a, x_min_b), min(y_min_a, y_min_b), max(x_max_a, x_max_b), max(y_max_a, y_max_b)


def bbox_to_polygon_coordinates(bbox):
    """
    This function send polygon coordinates from a gives bbox
    :param bbox:
    :return:
    """
    (x_min, y_min, x_max, y_max) = bbox

    return [[(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min), (x_min, y_min)]]


def union_by_split(geometry_list, split_factor=2):
    """
    Union geometry list with split list method (split_factor default 2 by 2)
    * OGR dependencie : Union *
    """

    len_list = len(geometry_list)
    if len_list > split_factor:
        union_geom_list = []
        for i in range(split_factor):
            # first iteration
            if i == 0:
                split_geometry_list = geometry_list[:int(len_list / split_factor)]
            # last iteration
            elif i == split_factor - 1:
                begin = int(len_list / split_factor) * i
                split_geometry_list = geometry_list[begin:]
            # others iterations
            else:
                begin = int(len_list / split_factor) * i
                end = (int(len_list / split_factor)) * (i + 1)
                split_geometry_list = geometry_list[begin:end]

            # adding union to geom list
            union_geom_list.append(union_by_split(split_geometry_list, split_factor))

        for i, union_geom in enumerate(union_geom_list):
            if i == 0:
                ogr_geom_unioned = geojson_to_ogr_geom(union_geom)
            else:
                temp_geom = geojson_to_ogr_geom(union_geom)
                ogr_geom_unioned = ogr_geom_unioned.Union(temp_geom)

        geojson_unioned = ogr_geom_to_geojson(ogr_geom_unioned)

        return geojson_unioned

    else:
        if len(geometry_list) > 1:

            for i, union_geom in enumerate(geometry_list):
                if i == 0:
                    ogr_geom_unioned = geojson_to_ogr_geom(union_geom)
                else:
                    temp_geom = geojson_to_ogr_geom(union_geom)
                    ogr_geom_unioned = ogr_geom_unioned.Union(temp_geom)

            geojson_unioned = ogr_geom_to_geojson(ogr_geom_unioned)

            return geojson_unioned

        else:
            return geometry_list[0]


def geometry_to_coordinates_list(geometry, geometry_type_filter=None):
    """
    Return an iterator as a coordinate list from a given geometry.
    Each list is a part of geometry
    """

    def iterate_over_coordinates(coordinates):

        if isinstance(coordinates[0][0], (int, float)):
            yield coordinates
        elif isinstance(coordinates, (list, tuple)):
            for coordinate_list in coordinates:
                for deeper_coordinates_list in iterate_over_coordinates(coordinate_list):
                    yield deeper_coordinates_list
        else:
            print('error your geometry in input is not correct')

    geometry_collection = geometry_to_geometry_collection(geometry)
    for geometry in geometry_collection['geometries']:
        coordinates = geometry['coordinates']
        for coordinates_list in iterate_over_coordinates(coordinates):
            yield coordinates_list


def coordinates_to_segment(coordinates):
    """
    This function yield
    :param coordinates:
    :return:
    """

    for i, point in enumerate(coordinates_to_point(coordinates)):
        if i == 0:
            pass
        else:
            yield (save_point, point)
        save_point = point


def grid_index_to_geolayer(grid_index, name='grid_index', crs=None, features_serialize=False):
    geolayer = {'features': {}, 'metadata': {'name': name, 'geometry_ref': {'type': 'Polygon'}, }}

    if crs:
        geolayer['metadata']['geometry_ref']['crs'] = crs

    # create field
    geolayer['metadata']['fields'] = {'g_id': {'type': 4, 'width': 254, 'precision': 0, 'index': 0},
                                      'i_feat_list': {'type': 1, 'width': 0, 'precision': 0, 'index': 1}}
    # add feature
    for i_feat, g_id in enumerate(grid_index['index']):
        feature = {
            'attributes': {'g_id': g_id, 'i_feat_list': grid_index['index'][g_id]},
            'geometry': {
                'type': 'Polygon',
                'coordinates': bbox_to_polygon_coordinates(
                    g_id_to_bbox(
                        g_id,
                        mesh_size=grid_index['metadata']['mesh_size'],
                        x_grid_origin=grid_index['metadata']['x_grid_origin'],
                        y_grid_origin=grid_index['metadata']['y_grid_origin']
                    )
                )
            }
        }

        if features_serialize:
            feature = str(feature)

        geolayer['features'][i_feat] = feature

    return geolayer


def ogr_geom_to_geojson(ogr_geometry, bbox=True):
    def coordinates_loop(geom, bbox_launch):

        bbox = ()

        # if geometry collection
        if geom.GetGeometryType() == 7:
            geom_collection_list = []
            for i, under_geom in enumerate(geom):
                geom_geojson = ogr_geom_to_geojson(under_geom, bbox_launch)
                geom_collection_list.append(geom_geojson)

                if bbox_launch:
                    if i == 0:
                        bbox = geom_geojson['bbox']
                    else:
                        bbox = bbox_union(bbox, geom_geojson['bbox'])

            return geom_collection_list, tuple(bbox)

        # if point
        elif geom.GetGeometryType() == 1:
            return [geom.GetX(), geom.GetY()], (geom.GetX(), geom.GetY(), geom.GetX(), geom.GetY())

        # for linestring, polygon, multipoint, multilinestring, multipolygon
        else:
            # iterate over geometries
            if geom.GetGeometryCount() > 0:
                coordinates_list = [0] * geom.GetGeometryCount()
                for j, under_geom in enumerate(geom):
                    # linearring compose polygon if j > 0 then j is a hole.
                    # Hole is inside polygon so we do not need to loop on this coordinate
                    if under_geom.GetGeometryName() == 'LINEARRING' and j > 0:
                        bbox_launch = False
                    else:
                        bbox_launch = True

                    coordinates_list[j], under_bbox = coordinates_loop(under_geom, bbox_launch)
                    if bbox_launch:
                        # bbox
                        if j == 0:
                            bbox = under_bbox
                        else:
                            bbox = bbox_union(bbox, under_bbox)

                return coordinates_list, tuple(bbox)

            # iterate over points
            if geom.GetPointCount() > 0:
                coordinates_list = [0] * geom.GetPointCount()
                for i in range(geom.GetPointCount()):
                    # coordinates
                    point = geom.GetPoint(i)
                    coordinates_list[i] = [point[0], point[1]]
                    # bbox
                    if bbox_launch:
                        if i == 0:
                            bbox = [point[0], point[1], point[0], point[1]]
                        else:
                            if point[0] < bbox[0]:
                                bbox[0] = point[0]
                            if point[0] > bbox[2]:
                                bbox[2] = point[0]
                            if point[1] < bbox[1]:
                                bbox[1] = point[1]
                            if point[1] > bbox[3]:
                                bbox[3] = point[1]

                return coordinates_list, tuple(bbox)

    dico = {}
    ogr_geom_type = ogr_geometry.GetGeometryType()
    dico['type'] = ogr_geom_type_to_geoformat_geom_type(ogr_geom_type)

    # adding bbox
    if bbox == True:
        coordinates, bbox = coordinates_loop(ogr_geometry, True)
        dico['bbox'] = bbox
    else:
        coordinates, bbox = coordinates_loop(ogr_geometry, False)

    # adding coordinates for geometries
    # if GeometryCollection
    if ogr_geom_type != 7:
        dico['coordinates'] = coordinates
    # for others geometries
    else:
        dico['geometries'] = coordinates

    return dico


def geojson_to_ogr_geom(geojson):
    def coordinates_loop(coordinates, ogr_geom):
        """
        2D ONLY -- if 3D change AddPoint_2D by AddPoint and add 3D type in GetGeometryType test.
        """

        # if geometry collection
        if ogr_geom.GetGeometryType() == 7:
            for geojson_geom in coordinates:
                new_ogr_geom = geojson_to_ogr_geom(geojson_geom)
                ogr_geom.AddGeometry(new_ogr_geom)

            return ogr_geom

        # if point
        elif ogr_geom.GetGeometryType() == 1:
            ogr_geom.AddPoint_2D(coordinates[0], coordinates[1])
            return ogr_geom

        # for linestring, polygon, multipoint, multilinestring, multipolygon
        else:
            if ogr_geom.GetGeometryType() == 4:
                under_ogr_geom = ogr.Geometry(ogr.wkbPoint)
            elif ogr_geom.GetGeometryType() == 6:
                under_ogr_geom = ogr.Geometry(ogr.wkbPolygon)
            elif ogr_geom.GetGeometryType() == 3:
                under_ogr_geom = ogr.Geometry(ogr.wkbLinearRing)
            elif ogr_geom.GetGeometryType() == 5:
                under_ogr_geom = ogr.Geometry(ogr.wkbLineString)

            for i, coordinates_list in enumerate(coordinates):
                if ogr_geom.GetGeometryType() == 2:
                    if i == 0:
                        if ogr_geom.GetGeometryName() == 'LINESTRING':
                            ogr_geom = ogr.Geometry(ogr.wkbLineString)
                        else:
                            ogr_geom = ogr.Geometry(ogr.wkbLinearRing)
                    ogr_geom.AddPoint_2D(coordinates_list[0], coordinates_list[1])

                else:
                    if i == 0 and ogr_geom.GetGeometryType() == 3:
                        ogr_geom = ogr.Geometry(ogr.wkbPolygon)
                    new_geom = coordinates_loop(coordinates_list, under_ogr_geom)
                    ogr_geom.AddGeometry(new_geom)

            return ogr_geom

    geo_type = geojson['type']
    if geo_type.upper() == 'POINT':
        ogr_geom = ogr.Geometry(ogr.wkbPoint)
    elif geo_type.upper() == 'LINESTRING':
        ogr_geom = ogr.Geometry(ogr.wkbLineString)
    elif geo_type.upper() == 'POLYGON':
        ogr_geom = ogr.Geometry(ogr.wkbPolygon)
    elif geo_type.upper() == 'MULTIPOINT':
        ogr_geom = ogr.Geometry(ogr.wkbMultiPoint)
    elif geo_type.upper() == 'MULTILINESTRING':
        ogr_geom = ogr.Geometry(ogr.wkbMultiLineString)
    elif geo_type.upper() == 'MULTIPOLYGON':
        ogr_geom = ogr.Geometry(ogr.wkbMultiPolygon)
    elif geo_type.upper() == 'GEOMETRYCOLLECTION':
        ogr_geom = ogr.Geometry(ogr.wkbGeometryCollection)
    elif geo_type.upper() == 'NO GEOMETRY':
        ogr_geom = ogr.Geometry(ogr.wkbNone)
    elif geo_type.upper() == 'GEOMETRY':
        ogr_geom = ogr.Geometry(ogr.wkbUnknown)

    if geo_type != 'NO GEOMETRY':
        if geo_type != 'GEOMETRYCOLLECTION':
            ogr_geom = coordinates_loop(geojson['coordinates'], ogr_geom)
        else:
            ogr_geom = coordinates_loop(geojson['geometries'], ogr_geom)

    return ogr_geom


def ogr_layer_to_geolayer(path, layer_id=None, field_name_filter=None, driver_name=None, bbox_extent=True,
                          bbox_filter=None, feature_serialize=False, feature_limit=None, feature_offset=None):
    """
    'ogr_layer_to_geolayer' permet d'ouvrier un fichier sig externe (attributaire ou géométrique), de le lire et de
    stocker des informations filtrées. Il faut lui renseigner un chemin vers le fichier (obligatoirement).

    :param path: chemin d'accès au fichier + nom fichier ; Format : string ; ex : "C:\dataPython\com.shp"
    :param layer_id: identifiant ou nom table concernée ; Format : string ou integer ou none
    :param field_name_filter: liste noms des champs filtrant ; Format : StringList  ou none
    :param driver_name: format du fichier en lecture, le script peu le déterminer ; Format : string (majuscule) ou none
    :param bbox_extent: if you want to add bbox for each geometry and extent in metadata
    :param bbox_filter if wout want make a bbox filter when you import data


    :return: geolayer : layer au format geoformat basé sur le fichier path renseigné en entrée filtrées par field_name_filter
    """

    # création de la layer geolayer (conteneur de base)
    geolayer = {}

    # ouvert la data source avec ou sans driver défini
    if driver_name:
        driver = ogr.GetDriverByName(driver_name)
        data_source = driver.Open(path)
    else:
        # détection du driver compris dans la fonction ogr.Open()
        data_source = ogr.Open(path)

    # open layer (table) - condition valable pour les databases notamment
    if not layer_id:
        # si pas d'identifiant de layer
        layer = data_source.GetLayer()
    else:
        if isinstance(layer_id, str):
            # si l'identifiant est un string : le nom de la layer
            layer = data_source.GetLayerByName(layer_id)
        elif isinstance(layer_id, int):
            # si l'identifiant est un nombre
            layer = data_source.GetLayer(layer_id)

    # récupération de la LayerDefn() via la fonction ogr
    layer_defn = layer.GetLayerDefn()

    # creation du dictionnaire des métadonnées des champs et ajout du nombre de champ dans la layer
    metadata = {'fields': {}}
    # boucle sur la structure des champs de la layer en entree
    if field_name_filter:
        # gestion de la correspondance de la case champs/field_name_filtres
        field_name_filter_up = [field_name.upper() for field_name in field_name_filter]
        # création liste vide pour stocker après le nom de champ initiaux de la table en entrée
        field_name_ori = []
        # récupération éléments pour chaque champ compris dans la layer definition

    if field_name_filter:
        # si field_name_filter on réinitialize l'ordre d'apparition des champs à 0
        i_field_filter = 0
    for i_field in range(layer_defn.GetFieldCount()):
        field_defn = layer_defn.GetFieldDefn(i_field)
        field_name = field_defn.GetName()
        field_type = field_defn.GetType()
        field_width = field_defn.GetWidth()
        field_precision = field_defn.GetPrecision()

        # ecriture de la metadata des champs du filtre dans les metadonnees des champs
        write_metadata = True
        # vérification si field_name_filter renseigné
        if field_name_filter:
            # si field_name est dans field_name_filter (gestion de la case)
            if field_name.upper() not in field_name_filter_up:
                write_metadata = False
            else:
                field_name_ori.append(field_name)
        if write_metadata:
            # si oui : écriture chaque informatation dans la métadonnée
            if field_name_filter:
                # on écrit les caractéristiques des champs et on remets à jour la variable index
                metadata['fields'][field_name] = {'type': field_type, 'width': field_width,
                                                  'precision': field_precision, 'index': i_field_filter}
                i_field_filter += 1
            else:
                # on écrit les caractéristiques des champs
                metadata['fields'][field_name] = {'type': field_type, 'width': field_width,
                                                  'precision': field_precision, 'index': i_field}

    # if geometry
    if layer.GetGeomType() != 100:
        # add geometry metadata
        metadata['geometry_ref'] = {'type': ogr_geom_type_to_geoformat_geom_type(layer.GetGeomType())}
        if layer.GetSpatialRef():
            metadata['geometry_ref']['crs'] = layer.GetSpatialRef().ExportToWkt()
        else:
            metadata['geometry_ref']['crs'] = None

        if bbox_extent:
            metadata['geometry_ref']['extent'] = None

    # nom de la layer
    metadata['name'] = layer.GetName()

    if feature_serialize:
        metadata['feature_serialize'] = True

    # ajout des metadadonnees dans geolayer
    geolayer['metadata'] = metadata

    # creation des features indépendamment les unes des autres, création structure attributaire pour chaque feature
    geolayer['features'] = {}

    #
    # i_feat : feature_id in input layer
    # i_feat_writed : feature_id in output layer
    # write_feature : True|False say if a feature can or cannot be written this depending on
    # filters option setting :
    #                           bbox_filter
    #                           feature_limit
    #                           feature_offset
    i_feat_writed = 0
    # set who list unique geometry type in layer
    geom_type_set = set([])
    for i_feat, feature in enumerate(layer):
        # init
        write_feature = True
        # test feature offset and limit
        if feature_offset:
            if i_feat < feature_offset:
                write_feature = False

        if feature_limit:
            # stop loop if feature_limit is reached
            if i_feat_writed == feature_limit:
                break

        if write_feature:
            # creation d'un dictionnaire vide pour chaque entité
            new_feature = {}

            ################################################################################################################
            #
            #   geometry
            #
            ################################################################################################################

            # test if geom in feature
            geom = feature.GetGeometryRef()
            if geom:
                # get geometry type
                if geom.GetGeometryType() != geoformat_geom_type_to_ogr_geom_type(
                        metadata['geometry_ref']['type']) or ogr_geom_type_to_geoformat_geom_type(
                    geom.GetGeometryType()) not in geom_type_set:
                    geom_type_set = set(
                        [ogr_geom_type_to_geoformat_geom_type(geom.GetGeometryType())] + list(geom_type_set))

                # recuperation des geometries / ajout dans le dictionnaire des features
                temp_bbox_extent = False
                if bbox_filter is not None:
                    temp_bbox_extent = True

                # bbox and extent must be computed
                if bbox_extent or temp_bbox_extent:
                    geom_json = ogr_geom_to_geojson(geom, True)
                    if bbox_extent:
                        # modify extent in metadata
                        if geolayer['metadata']['geometry_ref']['extent'] is None:
                            geolayer['metadata']['geometry_ref']['extent'] = geom_json['bbox']
                        else:
                            extent_bbox = geolayer['metadata']['geometry_ref']['extent']
                            extent_bbox = bbox_union(extent_bbox, geom_json['bbox'])
                            geolayer['metadata']['geometry_ref']['extent'] = extent_bbox
                else:
                    geom_json = ogr_geom_to_geojson(geom, False)

                if bbox_filter:
                    feat_bbox = geom_json['bbox']
                    if bbox_intersects_bbox(bbox_filter, feat_bbox):
                        if bbox_extent:
                            new_feature['geometry'] = geom_json
                        else:
                            del geom_json['bbox']
                            new_feature['geometry'] = geom_json
                    else:
                        write_feature = False
                else:
                    new_feature['geometry'] = geom_json

        ################################################################################################################
        #
        #   attributes
        #
        ################################################################################################################
        if write_feature:
            # ajout des données attributaires
            new_feature['attributes'] = {}
            # recuperation des informations attributaires pour les features
            # si option filtre sur champ
            if field_name_filter:
                for field_name in field_name_ori:
                    new_feature['attributes'][field_name] = feature.GetField(field_name)

            else:
                # récupérer la valeur du nom des champs
                for field_name in geolayer['metadata']['fields']:
                    new_feature['attributes'][field_name] = feature.GetField(field_name)

            if feature_serialize:
                # new_feature = zlib.compress(cPickle.dumps(new_feature))
                # new_feature = zlib.compress(str(new_feature))
                new_feature = str(new_feature)

            geolayer['features'][i_feat_writed] = new_feature
            i_feat_writed += 1

    ## Check layer metadata

    # GEOMETRY METADATA
    # if there is a difference between layer metadata geom type and scan
    if 'geometry_ref' in metadata:
        if geom_type_set != set(metadata['geometry_ref']['type']):
            if len(geom_type_set) == 0:
                metadata['geometry_ref']['type'] = 'No Geometry'
            elif len(geom_type_set) == 1:
                metadata['geometry_ref']['type'] = list(geom_type_set)[0]
            else:
                metadata['geometry_ref']['type'] = list(geom_type_set)

    return geolayer


# -----------------------------------------------------------------------------------------------------------------------

def ogr_layers_to_geocontainer(path, field_name_filter=None, driver_name=None, bbox_extent=True, bbox_filter=None,
                               feature_limit=None, feature_serialize=False):
    """
    'ogr_layers_to_geocontainer' crée une géodatasource comprenant des géolayers (format geoformat). Elle requiere
    la fonction layer_to_geoformat car elle boucle sur la fonction layer_to_geoformat, ce qui permet de récupérer les
    différentes géolayer et de les encapsuler dans une datasource.

    :param path: chemin d'accès au fichier + nom fichier ; Format : string ou list
    :param field_name_filter: liste noms des champs filtrant, même filtre pour tous; Format : StringList  ou none
    :param driver_name: format(s) fichier en lecture, script peu le déterminer ; Format : string (majuscule) ou liste ou none
    :param bbox_extent: if you want to add bbox for each geometry and extent in metadata
    :param bbox_filter: if you want filter input feature with a given bbox


    :return: géodatasource : un conteneur de layer au geoformat, filtrées par le fiel_name_filter
    """

    # fonction qui permet de boucler sur la 'layer_to_geoformat'
    def loop_list_layer(path, field_name_filter=None, driver_name=None, bbox_extent=None, bbox_filter=None,
                        feature_serialize=False):
        """
        'loop_list_layer' permet de lancer en boucle la fonction ogr_layer_to_geolayer.

        :param path: chemin d'un fichier
        :param field_name_filter: liste noms des champs filtrant
        :param driver_name: format fichier en lecture
        :return: yield de géolayer
        """

        if driver_name:
            # si driver_name renseigné
            driver = ogr.GetDriverByName(driver_name)
            data_source = driver.Open(path)


        else:
            # détection interne du driver via la fonction ogr.open()
            data_source = ogr.Open(path)

        # lancement de la fonction ogr_layer_to_geolayer() et récupération des layers au fur et à mesure
        for layer_id, layer in enumerate(data_source):
            geolayer = ogr_layer_to_geolayer(path, layer_id, field_name_filter=field_name_filter,
                                             driver_name=driver_name, bbox_extent=bbox_extent, bbox_filter=bbox_filter,
                                             feature_limit=feature_limit, feature_serialize=feature_serialize)
            yield geolayer

    # création du conteneur de layers
    geocontainer = {'layers': {}, 'metadata': {}}

    # init parameters
    temp_layer_path, temp_field_name_filter, temp_driver_name, temp_bbox_extent, temp_bbox_filter = None, None, None, None, None

    # test si le path est une liste, si oui : boucle pour chaque élément de la liste
    if isinstance(path, str):
        path = [path]

    for i_path, temp_layer_path in enumerate(path):

        if not isinstance(temp_layer_path, str):
            sys.exit('path must be a string')

        temp_field_name_filter = None
        # test si field_name_filter renseigné
        if field_name_filter:
            if isinstance(field_name_filter[i_path], str):
                temp_field_name_filter = field_name_filter
            else:
                temp_field_name_filter = field_name_filter[i_path]
        temp_driver_name = None

        # test driver_name
        if driver_name:
            temp_driver_name = driver_name[i_path]
            if isinstance(driver_name, list):
                temp_driver_name = driver_name[i_path]
            else:
                temp_driver_name = driver_name

        # test bbox extent
        if bbox_extent:
            if isinstance(bbox_extent, list):
                temp_bbox_extent = bbox_extent[i_path]
            else:
                temp_bbox_extent = bbox_extent

        # si bbox filter
        if bbox_filter:
            if isinstance(bbox_extent, list):
                temp_bbox_filter = bbox_extent[i_path]
            else:
                temp_bbox_filter = bbox_filter

        # lancement de la fonction loop_list_layer
        for i_geolayer, geolayer in enumerate(
                loop_list_layer(temp_layer_path, temp_field_name_filter, temp_driver_name, temp_bbox_extent,
                                temp_bbox_filter, feature_serialize)):
            # stockage des returns yield de la fonction loop
            geolayer_name = geolayer['metadata']['name']
            geocontainer['layers'][geolayer_name] = geolayer
            if temp_bbox_extent:
                geolayer_extent = geolayer['metadata']['geometry_ref']['extent']
                if i_geolayer == 0:
                    geocontainer_extent = geolayer_extent
                else:
                    geocontainer_extent = bbox_union(geocontainer_extent, geolayer_extent)
                geocontainer['metadata']['extent'] = geocontainer_extent

    # # test si path est en string, on lance le loop mais elle tournera qu'une fois
    # elif isinstance(path, str):
    #     for geolayer in loop_list_layer(path, field_name_filter, driver_name, bbox_extent, bbox_filter, feature_serialize):
    #         # stockage du return yield de la fonction loop
    #         geolayer_name = geolayer['metadata']['name']
    #         geocontainer['layers'][geolayer_name] = geolayer

    # # message d'erreur
    # else:
    #     sys.exit('erreur format path non valide')

    return geocontainer


# -----------------------------------------------------------------------------------------------------------------------

def geolayer_to_ogr_layer(geolayer, path, driver_name, ogr_options=None, order_fields=False, feature_serialize=False):
    """
    'geolayer_to_ogr_layer' exports a geolayer to several formats:
        - esri shapefile
        - kml
        - xlsx
        - postgresql
        - geojson

    The geolayer can be #TODO translate "attributaire et/ou géométrique"

    Example ogr_options : ogr_options=['OVERWRITE=YES']

    :param geolayer: layer
    :param path: export path
    :param driver_name: output format
    :param ogr_options: TODO
    :param order_fields: TODO
    :param feature_serialize: TODO
    """

    # création de l'ensemble des informations pour créer un fichier au format SIG
    # création d'un driver
    if driver_name.upper() not in OGR_DRIVER_NAMES:
        raise ValueError("The given driver name {} is not correct.".format(driver_name))
    driver = ogr.GetDriverByName(driver_name)

    # récupération du path en 2 parties : la racine et l'extension
    (root, ext) = os.path.splitext(path)

    # test si il y a pas une extension
    if ext == '':
        # alors c'est un dossier ou l'adresse d'une base de données
        # recupération du nom de la layer
        layer_name = geolayer['metadata']['name']
        # si le chemin est bien un dossier existant
        if os.path.isdir(root):
            # récupération de l'extension suivant le driver_name
            # TODO add other drivers
            if driver_name.upper() == OGR_FORMAT_ESRI_SHAPEFILE:
                # if geometry in geolayer
                if 'geometry_ref' in geolayer["metadata"]:
                    new_ext = '.shp'
                # else we write only dbf
                else:
                    new_ext = '.dbf'
            elif driver_name.upper() == OGR_FORMAT_KML:
                new_ext = '.kml'
            elif driver_name.upper() == OGR_FORMAT_XLSX:
                new_ext = '.xlsx'
            elif driver_name.upper() == OGR_FORMAT_CSV:
                new_ext = '.csv'
            elif driver_name.upper() == OGR_FORMAT_GEOJSON:
                new_ext = '.geojson'
            else:
                sys.exit('format non pris en compte')
            new_path = root + layer_name + new_ext
        else:
            # Then we suppose that is a datasource
            if ogr.Open(root) is not None:
                if driver_name.upper() == OGR_FORMAT_POSTGRESQL:
                    new_path = path
                else:
                    raise ValueError("Given file is a datasource but the driver_name is not {}".format(OGR_FORMAT_POSTGRESQL))
            else:
                raise FileNotFoundError("Your path does not exists or is invalid")
        data_source = driver.CreateDataSource(new_path)
    else:
        if driver_name == OGR_FORMAT_XLSX:
            # on test s'il existe
            data_source = driver.Open(path, 1)
            if not data_source:
                data_source = driver.CreateDataSource(path)
        else:
            # alors c'est un fichier
            data_source = driver.CreateDataSource(path)

    # récupération dans geolayer des informations nécessaires à la création d'une layer : nom, projection, geometry_type
    layer_name = geolayer['metadata']['name']
    layer_crs = None
    layer_ogr_geom_type = geoformat_geom_type_to_ogr_geom_type(geoformat_geom_type=None)

    if 'geometry_ref' in geolayer['metadata']:
        layer_crs = None
        if 'crs' in geolayer['metadata']['geometry_ref']:
            crs_data = geolayer['metadata']['geometry_ref']['crs']
            # from EPSG
            if crs_data is None:
                layer_crs = None
            elif isinstance(crs_data, int):
                layer_crs = osr.SpatialReference()
                layer_crs.ImportFromEPSG(crs_data)
            # from OGC WKT
            elif isinstance(crs_data, str):
                try:
                    layer_crs = osr.SpatialReference(crs_data)
                except:
                    # si le format n'est pas reconnu tant pis pas de ref spatiale
                    print('WARNING: projection not recognized')
            else:
                print('WARNING: crs value must be an ESPG code or a OGC WKT projection')

        if 'type' in geolayer['metadata']['geometry_ref']:
            layer_ogr_geom_type = verify_geom_compatibility(driver_name, geolayer['metadata']['geometry_ref']['type'])
        else:
            raise ValueError("A type shall be found in geometry_ref.")

    if 'feature_serialize' in geolayer['metadata']:
        feature_serialize = geolayer['metadata']['feature_serialize']

    # création réelle de la layer
    if ogr_options:
        layer = data_source.CreateLayer(layer_name,
                                        srs=layer_crs,
                                        geom_type=layer_ogr_geom_type,
                                        options=ogr_options)
    else:
        layer = data_source.CreateLayer(layer_name,
                                        srs=layer_crs,
                                        geom_type=layer_ogr_geom_type)

    # création des fields (structure du fichier)
    # si l'on souhaite que l'ordre d'apparition des champs soit conservée
    if 'fields' in geolayer['metadata']:
        if order_fields:
            field_name_list = [0] * len(geolayer['metadata']['fields'])
            for field_name in geolayer['metadata']['fields']:
                field_name_list[geolayer['metadata']['fields'][field_name]['index']] = field_name
        else:
            field_name_list = list(geolayer['metadata']['fields'].keys())

        for field_name in field_name_list:
            # récupération des informations nécessaire à la création des champs
            field_type = geolayer['metadata']['fields'][field_name]['type']
            field_width = geolayer['metadata']['fields'][field_name]['width']
            field_precision = geolayer['metadata']['fields'][field_name]['precision']

            # création de la définition du champ (type, longueur, precision)
            field = ogr.FieldDefn(field_name, field_type)
            field.SetWidth(field_width)
            field.SetPrecision(field_precision)

            # création du champ
            layer.CreateField(field)

        # creation table de correspondance [au cas où la taille des champs est réduite lors de la création de la layer]
        # example DBF = 10 char maximum
        # if layerDefn() is define
        try:
            ct_field_name = {}
            for i in range(layer.GetLayerDefn().GetFieldCount()):
                ct_field_name[field_name_list[i]] = layer.GetLayerDefn().GetFieldDefn(i).GetName()
        except:
            ct_field_name = {field_name: field_name for field_name in field_name_list}

    # création des features
    for i_feat in geolayer['features']:
        try:
            feature_ogr = ogr.Feature(layer.GetLayerDefn())
        except:
            feature_ogr = ogr.Feature()

        feature_geoformat = geolayer['features'][i_feat]
        if feature_serialize:
            feature_geoformat = eval(feature_geoformat)

        # if geometry in feature
        if 'geometry' in feature_geoformat:
            # get geometry in geojson format like
            geom_json = feature_geoformat['geometry']
            # transform geometry to ogr geometry
            geom_ogr = geojson_to_ogr_geom(geom_json)
            # add geometry in ogr feature object
            feature_ogr.SetGeometry(geom_ogr)

        # test if attributes data in feature
        if 'attributes' in feature_geoformat:
            # loop on each layer [metadata] fields
            for field_name in geolayer['metadata']['fields']:
                # we recuperate true field name [in case it has been truncated]
                true_field_name = ct_field_name[field_name]
                value_field = feature_geoformat['attributes'].get(field_name)
                # if field value exists and is not NULL
                if value_field is not None:
                    # write data if error change field_value to string
                    try:
                        feature_ogr.SetField(true_field_name, value_field)
                    except NotImplementedError:
                        feature_ogr.SetField(true_field_name, str(value_field))

        layer.CreateFeature(feature_ogr)

    data_source.Destroy()


# -----------------------------------------------------------------------------------------------------------------------

def geocontainer_to_ogr_format(geocontainer, path, driver_name, export_layer_list=None, ogr_options=None,
                               order_fields=False, feature_serialize=False):
    """
    'geocontainer_to_ogr_format' est une procedure qui permet d'exporter une sélection ou l'ensemble des layers d'une
    datasource aux formats voulus. Le path renseignée peut être un dossier, une datasource, ou un fichier. On peut
    renseigner une liste ou un nom de layer pour filtrer l'export.

    :param geocontainer: la géodatasource complete
    :param path: chemin où aller sauvegarder (il peut être une liste ou un str)
    :param driver_name: le nom du drive peut etre une liste ou un seul qu'on applique à tous
    :param export_layer_list: liste des layers de la datasource a exporter, peut être list ou str. Si export_layer_list
    non rempli alors on exporte toutes les layers, si export layer_list rempli = on exporte que ces layers là.
    Variable possible pour cette list : 'tc', 'ref_a', 'ref_b' (seulement)
    """

    if export_layer_list:
        # test si il y a une liste des layers à exporter
        if isinstance(export_layer_list, list):
            for i_layer, export_layer_name in enumerate(export_layer_list):
                # test si la layer fait partie de la liste des layers à sauvegarder
                if export_layer_name in geocontainer['layers'].keys():
                    geolayer = geocontainer['layers'][export_layer_name]
                    if isinstance(path, list):
                        # path = fichier en dur
                        if isinstance(driver_name, list):
                            geolayer_to_ogr_layer(geolayer, path[i_layer], driver_name[i_layer],
                                                  ogr_options=ogr_options[i_layer], order_fields=order_fields,
                                                  feature_serialize=feature_serialize)
                        else:
                            geolayer_to_ogr_layer(geolayer, path[i_layer], driver_name, ogr_options=ogr_options,
                                                  order_fields=order_fields, feature_serialize=feature_serialize)
                    else:
                        # path = dossier ou database
                        if isinstance(driver_name, list):
                            geolayer_to_ogr_layer(geolayer, path, driver_name[i_layer],
                                                  ogr_options=ogr_options[i_layer], order_fields=order_fields,
                                                  feature_serialize=feature_serialize)
                        else:
                            geolayer_to_ogr_layer(geolayer, path, driver_name, ogr_options=ogr_options,
                                                  order_fields=order_fields, feature_serialize=feature_serialize)

        # si export_layer_list n'est pas une liste, elle contient qu'une valeur
        elif isinstance(export_layer_list, str):
            geolayer = geocontainer['layers'][export_layer_list]
            geolayer_to_ogr_layer(geolayer, path, driver_name, ogr_options=ogr_options, order_fields=order_fields,
                                  feature_serialize=feature_serialize)  # il y aura alors que 1 path et 1 driver name


    # si export_layer_list=None alors on exporte l'ensemble des layers de la geocontainer
    else:
        for i_layer, layer_name in enumerate(geocontainer['layers']):
            geolayer = geocontainer['layers'][layer_name]
            # si le path est une liste :
            if isinstance(path, list):
                # et si le driver_name est une liste
                if isinstance(driver_name, list):
                    geolayer_to_ogr_layer(geolayer, path[i_layer], driver_name[i_layer],
                                          ogr_options=ogr_options[i_layer], order_fields=order_fields,
                                          feature_serialize=feature_serialize)
                # si non utiliser toujours le même driver
                else:
                    geolayer_to_ogr_layer(geolayer, path[i_layer], driver_name, ogr_options=ogr_options,
                                          order_fields=order_fields, feature_serialize=feature_serialize)
            # sinon utiliser le même dossier
            else:
                # test sur le driver_name pour voir lequel on donne
                if isinstance(driver_name, list):
                    geolayer_to_ogr_layer(geolayer, path, driver_name[i_layer], ogr_options=ogr_options[i_layer],
                                          order_fields=order_fields, feature_serialize=feature_serialize)
                else:
                    geolayer_to_ogr_layer(geolayer, path, driver_name, ogr_options=ogr_options, order_fields=order_fields,
                                          feature_serialize=feature_serialize)


# -----------------------------------------------------------------------------------------------------------------------

def create_pk(geolayer, pk_field_name):
    """
    'create_pk' est un dictionnaire qui permet de faire le lien entre les itérateurs features et la valeur d'un champ.

    :param geolayer: la layer au géoformat
    :param pk_field_name: le nom du champs à "indexer"
    :return: géolayer avec une contrainte de pk avce la clé du champs rajouté
    """
    # création du dictionnaire vide
    pk_dico = {}

    # récupération de la value du champs à indexer
    for i_feat in geolayer['features']:
        feature = geolayer['features'][i_feat]

        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature = eval(feature)

        pk_field_value = feature['attributes'][pk_field_name]
        # vérification que les valeurs sont uniques
        if pk_field_value in pk_dico:
            sys.exit('le champ indiqué contient des valeurs non unique')
        else:
            # récupération de la valeur de l'itérateur
            pk_dico[pk_field_value] = i_feat

    # affectation du dictionnaire dans les métadonnées de la géolayer
    # geolayer['metadata']['constraints'] = {'pk': {}}
    # geolayer['metadata']['constraints']['pk'][pk_field_name] = pk_dico

    return pk_dico


def create_attribute_index(geolayer, field_name):
    index_dict = {'type': 'hashtable', 'index': {}}

    # récupération de la valeur du champs à indexer
    for i_feat in geolayer['features']:
        feature = geolayer['features'][i_feat]

        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature = eval(feature)

        field_value = feature['attributes'][field_name]

        try:
            index_dict['index'][field_value].append(i_feat)
        except KeyError:
            index_dict['index'][field_value] = [i_feat]

    return index_dict


def pairwise(iterable):
    """
    from https://stackoverflow.com/questions/5764782/iterate-through-pairs-of-items-in-a-python-list?lq=1
    iterable = [s0, s1, s2, s3, ...]
    return ((s0,s1), (s1,s2), (s2, s3), ...)

    """
    import itertools

    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def len_coordinates(coordinates):
    """
    Return number of coordinates on a coordinates list
    """

    coordinates_count = 0
    for point in coordinates_to_point(coordinates):
        coordinates_count += 1

    return coordinates_count


def len_coordinates_in_geometry(geometry):
    """
    Return number of coordinates on a given geometry
    """
    geometry_collection = geometry_to_geometry_collection(geometry)
    coordinates_count = 0
    for geometry in geometry_collection['geometries']:
        coordinates_count += len_coordinates(geometry['coordinates'])

    return coordinates_count


def get_geocontainer_extent(geocontainer):
    if 'metadata' in geocontainer.keys():
        if 'extent' in geocontainer['metadata']:
            return geocontainer['metadata']['extent']
    else:
        for i_layer, geolayer in enumerate(geocontainer['layers']):
            geolayer_bbox = None
            if 'geometry_ref' in geolayer['metadata']:
                if 'extent' in geolayer['metadata']['geometry_ref']:
                    geolayer_bbox = geolayer['metadata']['geometry_ref']['extent']
            else:
                # no geometry in geolayer
                return None

            if not geolayer_bbox:
                for i_feat in geolayer['features']:
                    feature_bbox = None
                    if 'geometry' in geolayer['features'][i_feat].keys():
                        if 'bbox' in geolayer['features'][i_feat]['geometry']:
                            feature_bbox = geolayer['features'][i_feat]['geometry']['bbox']

                        else:
                            feature_bbox = coordinates_to_bbox(geolayer['features'][i_feat]['geometry'])
                    else:
                        # no geometry in geolayer
                        return None

                    if i_feat == 0:
                        geolayer_bbox = feature_bbox
                    else:
                        geolayer_bbox = bbox_union(geolayer_bbox, feature_bbox)

            if i_layer == 0:
                geocontainer_extent = geolayer_bbox
            else:
                geocontainer_extent = bbox_union(geocontainer_extent, geolayer_bbox)

    return geocontainer_extent


def point_bbox_position(point, bbox):
    """
    Return point position and sector (NW, N, NE, W, E, SW, S, SE) in regard to given bbox.

    Diagram showing sectors's position around a bbox :

       NW  |   N  |  NE
    -------+------+-------
        W  | bbox |   E
    -------+------+-------
       SW  |   S  |  SE

    3 position possibilities and sectors configuration :
        * Boundary : and side of bbox boundary (N, S, E, W) or corner (NW, NE, SW, SE)
        * Exterior : (NW, N, NE, W, E, SW, S, SE)
        * Interior : None

    """

    (pt_x, pt_y) = point
    (x_min, y_min, x_max, y_max) = bbox

    # North
    if (pt_x > x_min and pt_x < x_max) and (pt_y >= y_max):
        if pt_y == y_max:
            position = ('Boundary', 'N')
        else:
            position = ('Exterior', 'N')
    # South
    elif (pt_x > x_min and pt_x < x_max) and (pt_y <= y_min):
        if pt_y == y_min:
            position = ('Boundary', 'S')
        else:
            position = ('Exterior', 'S')
    # Est
    elif pt_x >= x_max and (pt_y > y_min and pt_y < y_max):
        if pt_x == x_max:
            position = ('Boundary', 'E')
        else:
            position = ('Exterior', 'E')
    # West
    elif pt_x <= x_min and (pt_y > y_min and pt_y < y_max):
        if pt_x == x_min:
            position = ('Boundary', 'W')
        else:
            position = ('Exterior', 'W')
    # North-West
    elif pt_x <= x_min and pt_y >= y_max:
        if pt_x == x_min and pt_y == y_max:
            position = ('Boundary', 'NW')
        else:
            position = ('Exterior', 'NW')
    # North-Est
    elif pt_x >= x_max and pt_y >= y_max:
        if pt_x == x_max and pt_y == y_max:
            position = ('Boundary', 'NE')
        else:
            position = ('Exterior', 'NE')
    # South-Est
    elif pt_x >= x_max and pt_y <= y_min:
        if pt_x == x_max and pt_y == y_min:
            position = ('Boundary', 'SE')
        else:
            position = ('Exterior', 'SE')
    # South-West
    elif pt_x <= x_min and pt_y <= y_min:
        if pt_x == x_min and pt_y == y_min:
            position = ('Boundary', 'SW')
        else:
            position = ('Exterior', 'SW')
    # Point in bbox
    else:
        position = ('Interior', None)

    return position


def coordinates_to_centroid(coordinates, precision=None):
    """
    Return the centroid of given coordinates list or tuple

    :param coordinates: (list or tuple) coordinates list or tuple
    :param precision: (int) precision of coordinates (number of decimal places)
    :return: (tuple) centroid
    """

    for i_point, point in enumerate(coordinates_to_point(coordinates)):
        if i_point == 0:
            mean_point = list(point)
        else:
            mean_point[0] += point[0]
            mean_point[1] += point[1]

    nb_coordinates = i_point + 1
    centroid = (mean_point[0] / nb_coordinates, mean_point[1] / nb_coordinates)
    if precision:
        centroid = (round(centroid[0], precision), round(centroid[1], precision))

    return centroid


########################################################################################################################
#
# GRID INDEX
#
########################################################################################################################
def bbox_to_g_id(bbox, mesh_size, x_grid_origin=0., y_grid_origin=0.):
    """
    This function allow to find, with bbox coordinates, grid index identifier (g_id) to witch it begins.

    :param bbox [list/tuple]: bbox
    :param mesh_size [int]: mesh size
    :param x_grid_origin: x-coordinates of the original point from which the index is constructed
    :param y_grid_origin: y-coordinates of the original point from which the index is constructed

    :return: g_id [tuple] : grid id of grid mesh intersecting given bbox
    """
    # split bbox coordinates
    (x_min, y_min, x_max, y_max) = bbox
    # deduc g_id of bbox extremity
    id_x_min = int((x_min - x_grid_origin) / mesh_size) - 1
    id_x_max = int((x_max - x_grid_origin) / mesh_size)
    id_y_min = int((y_min - y_grid_origin) / mesh_size) - 1
    id_y_max = int((y_max - y_grid_origin) / mesh_size)
    # beacuse integer rounding testing if id_x_min and id_y_min are in given bbox
    # testing id_x_min
    point = x_min, y_max
    g_id = (id_x_min, id_y_max)
    g_id_bbox = g_id_to_bbox(g_id, mesh_size, x_grid_origin=x_grid_origin, y_grid_origin=y_grid_origin)
    point_position, point_direction = point_bbox_position(point, g_id_bbox)
    if point_position == 'Exterior':
        id_x_min += 1
    # testing id_y_min
    point = x_max, y_min
    g_id = (id_x_max, id_y_min)
    g_id_bbox = g_id_to_bbox(g_id, mesh_size, x_grid_origin=x_grid_origin, y_grid_origin=y_grid_origin)
    point_position, point_direction = point_bbox_position(point, g_id_bbox)
    if point_position == 'Exterior':
        id_y_min += 1
    # double loop sending all g_id intersecting bbox
    for x_step in range(id_x_min, id_x_max + 1):
        for y_step in range(id_y_min, id_y_max + 1):
            yield x_step, y_step


def point_to_g_id(point, mesh_size, x_grid_origin=0., y_grid_origin=0.):
    """
    This function return grid id (g_id) for a given point

    :param point: 
    :param mesh_size: 
    :param x_grid_origin: 
    :param y_grid_origin: 
    :return: 
    """
    bbox = point + point

    for g_id in bbox_to_g_id(bbox, mesh_size, x_grid_origin, y_grid_origin):
        yield g_id


def g_id_to_point(g_id, mesh_size, position='center', x_grid_origin=0., y_grid_origin=0.):
    """
    This function return a coordinates point to given g_id (g_id). Obviously since it is a grid, the position of the
    point can be specified between this values ('center', 'NE', 'NW', 'SE',  'SW').

    If the grid origin is different to 0. you have to indicate the origin's coordinates (x_grid_origin or y_grid_origin)
    """

    x_min, y_min, x_max, y_max = g_id_to_bbox(g_id, mesh_size)

    if position.upper() == 'CENTER':
        x, y = (x_min + x_max) / 2., (y_min + y_max) / 2.
    if position.upper() == 'NE':
        x, y = x_max, y_max
    if position.upper() == 'NW':
        x, y = x_min, y_max
    if position.upper() == 'SE':
        x, y = x_max, y_min
    if position.upper() == 'SW':
        x, y = x_min, y_min

    if x_grid_origin != 0.0 or y_grid_origin != 0.:
        x += x_grid_origin
        y += y_grid_origin

    return x, y


def g_id_to_bbox(g_id, mesh_size, x_grid_origin=0., y_grid_origin=0.):
    """
    This fucntion return the bbox associate to a given g_id (grid id).
    If the grid origin is different to 0. you have to indicate the origin's coordinates (x_grid_origin or y_grid_origin)

    :param g_id:
    :param mesh_size:
    :param x_grid_origin:
    :param y_grid_origin:
    :return:
    """
    (x_id, y_id) = g_id
    x_id, y_id = float(x_id), float(y_id)
    bbox_x_min = x_id * mesh_size
    bbox_x_max = (x_id + 1) * mesh_size
    bbox_y_min = y_id * mesh_size
    bbox_y_max = (y_id + 1) * mesh_size

    if x_grid_origin != 0. or y_grid_origin != 0.:
        bbox_x_min = x_grid_origin + bbox_x_min
        bbox_x_max = x_grid_origin + bbox_x_max
        bbox_y_min = y_grid_origin + bbox_y_min
        bbox_y_max = y_grid_origin + bbox_y_max
    return bbox_x_min, bbox_y_min, bbox_x_max, bbox_y_max


def create_grid_index(geolayer, mesh_size=None, x_grid_origin=0, y_grid_origin=0):
    """
    Create a grid index for a geolayer at a mesh size (deduce automatically or given in input).
    You have also possibility to determine the origin point of the frame on which the grid is constructed (by default
    0, 0).

    This function return a dictionnary with this structure : {
        'metadata : {
            'type' :  type of index
            'mesh_size': size of mesh (like in parameters or computed by this function if uninformed)
            'x_grid_origin': grid frame x origin coordinates
            'y_grid_origin': grid frame y origin coordinates
        'index' : {
            (coordinates of mesh): [list with geolayer i_feat where bbox intersects mesh]
        }

    :param geolayer:
    :param mesh_size: size of mesh
    :param x_grid_origin: x origin of grid frame
    :param y_grid_origin: y origin of grid frame
    :return: grid index dict (structure describe above)
    """
    
    # first define mesh size if not yet define
    if not mesh_size:
        # we deduce mean hight and width for all features
        size_x, size_y = 0, 0
        first_point = False
        for i, i_feat in enumerate(geolayer['features']):
            feature = geolayer['features'][i_feat]

            # if feature is serialized
            if 'feature_serialize' in geolayer['metadata']:
                if geolayer['metadata']['feature_serialize']:
                    feature = eval(feature)
            # get bbox
            try:
                bbox = feature['geometry']['bbox']
            except KeyError:
                bbox = coordinates_to_bbox(feature['geometry']['coordinates'])
                feature['geometry']['bbox'] = bbox

            # if geometry type is point there is no dimension in same bbox (no lenght / no width) we have to compare
            #  with others points bbox
            if feature['geometry']['type'] == 'Point':
                if not first_point:
                    old_point_bbox = bbox
                    first_point = True
                else:
                    size_x += abs(bbox[2] - old_point_bbox[2])
                    size_y += abs(bbox[3] - old_point_bbox[3])
                    old_point_bbox = bbox

            else:
                size_x += bbox[2] - bbox[0]
                size_y += bbox[3] - bbox[1]

        mesh_size = max(size_x / len(geolayer['features']), size_y / len(geolayer['features']))

    index_dict = {}
    index_dict['metadata'] = {'type': 'grid',
                              'mesh_size': mesh_size,
                              'x_grid_origin': x_grid_origin,
                              'y_grid_origin': y_grid_origin}
    index_dict['index'] = {}

    for i_feat in geolayer['features']:
        feature = geolayer['features'][i_feat]

        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature = eval(feature)

        geom = feature['geometry']

        if 'bbox' in geom.keys():
            bbox_geom = geom['bbox']
        else:
            coordinates = geom['coordinates']
            bbox_geom = coordinates_to_bbox(coordinates)

        # for each grid identifier (g_id) we add in grid_idx_dico entity identifier (i_feat)
        for g_id in bbox_to_g_id(bbox_geom, mesh_size, x_grid_origin=x_grid_origin, y_grid_origin=y_grid_origin):
            try:
                index_dict['index'][g_id].append(i_feat)
            except KeyError:
                index_dict['index'][g_id] = [i_feat]

    return index_dict


def g_id_neighbor_in_grid_index(g_id, grid_index, nb_mesh=1):
    """
    Return g_id neigbhor if exists in given grid index at a distance of n mesh
    """

    (x_g_id, y_g_id) = g_id

    x_min = x_g_id - nb_mesh
    x_max = x_g_id + nb_mesh + 1
    y_min = y_g_id - nb_mesh
    y_max = y_g_id + nb_mesh + 1
    for x_g_id in range(x_min, x_max):
        for y_g_id in range(y_min, y_max):
            neighbor_g_id = x_g_id, y_g_id
            if neighbor_g_id in grid_index['index']:
                yield neighbor_g_id


########################################################################################################################
#
# Adjacency matrix
#
########################################################################################################################

def i_feat_to_adjacency_neighbor(i_feat, adjacency_matrix, neighbor_set=None):
    """
    Use adjacency matrix to find all i_feat neighbor's
    """

    if not neighbor_set:
        neighbor_set = set([i_feat])

    # set store i_feat neighbor's
    i_feat_neighbor_set = set(adjacency_matrix[i_feat])
    # difference result between the list of neighbors already scanned and i_feat neighbors
    # Anyway, it's the list of new neighbors we haven't scanned yet.
    new_neighbor_set = set(i_feat_neighbor_set.difference(neighbor_set))
    # copy previous set
    new_neighbor_set_copy = set(new_neighbor_set)

    i = 0
    while new_neighbor_set_copy:
        # Loop scan every new neighbor
        for neighbor in new_neighbor_set:
            # set store i_feat neighbor's
            i_feat_neighbor_set = set(adjacency_matrix[neighbor])
            # new set of neighbors who have never been scanned before
            new_new_neighbor_set = i_feat_neighbor_set.difference(neighbor_set)
            # add the neighbor to the result list
            neighbor_set.update(set([neighbor]))
            # we add the new neighbors never scanned before
            new_neighbor_set_copy.update(new_new_neighbor_set)

            # we delete the scanned neighbor
            new_neighbor_set_copy = new_neighbor_set_copy.difference(set([neighbor]))

            i += 1
        # adding to new_neighbor_set ew neighbors that have never been scanned before
        new_neighbor_set = set(new_neighbor_set_copy)

    return list(neighbor_set)


def create_adjacency_matrix(geolayer, mesh_size=None):
    """
    Creating an adjacency matrix

    * GDAL/OGR dependencie :
        Intersects
    *
    """

    matrix_dict = {}

    try:
        input_grid_idx = geolayer['metadata']['constraints']['index']['geometry']
    except:
        input_grid_idx = create_grid_index(geolayer, mesh_size=mesh_size)

    mesh_size = input_grid_idx['metadata']['mesh_size']

    # Création de la clé unique du dictionnaire de résultat (préparation du stockage des résultats)
    matrix_dict['matrix'] = {i_feat: [] for i_feat in geolayer['features']}

    for i_feat in geolayer['features']:
        feature_a = geolayer['features'][i_feat]

        # if feature is serialized
        if 'feature_serialize' in geolayer['metadata']:
            if geolayer['metadata']['feature_serialize']:
                feature_a = eval(feature_a)

        # get bbox
        try:
            feature_a_bbox = feature_a['geometry']['bbox']
        except KeyError:
            feature_a_bbox = coordinates_to_bbox(feature_a['geometry']['coordinates'])
            feature_a['geometry']['bbox'] = feature_a_bbox

        # Récupération des identifiants de mailles présent dans l'index
        g_id_list = list(bbox_to_g_id(feature_a_bbox, mesh_size))

        # Pour chaque identifiant de maille de l'index on récupère l'identifant des autres polygones voisins de l'entité
        # en cours (s'ils existent)
        neighbour_i_feat_list = []
        for g_id in g_id_list:
            # récupération de la liste des clefs primaires des entités présentes dans la maille de l'index
            neighbour_i_feat_list += input_grid_idx['index'][g_id]

        # suppression de la clef primaire du polyone en cours et d'éventuels doublons
        neighbour_i_feat_list = [value for value in list(set(neighbour_i_feat_list)) if value != i_feat]

        # création  de la géométrie du feature A
        feature_a_ogr_geom = geojson_to_ogr_geom(feature_a['geometry'])
        # Même procédé que précédemment pour l'objet B
        for neighbour_i_feat in neighbour_i_feat_list:
            # si le i_feat n'est pas déjà compris dans la matrice de proximité du voisin :
            #  si c'est le cas alors cela veut dire que l'on a déjà fait un test d'intersection enrte les deux
            #  géométries auparavant (car pour avoir un voisin il faut etre deux)

            if i_feat not in matrix_dict['matrix'][neighbour_i_feat]:
                feature_b = geolayer['features'][neighbour_i_feat]

                # if feature is serialized
                if 'feature_serialize' in geolayer['metadata']:
                    if geolayer['metadata']['feature_serialize']:
                        feature_b = eval(feature_b)

                feature_b_ogr_geom = geojson_to_ogr_geom(feature_b['geometry'])

                if feature_a_ogr_geom.Intersects(feature_b_ogr_geom):
                    matrix_dict['matrix'][i_feat].append(neighbour_i_feat)
                    matrix_dict['matrix'][neighbour_i_feat].append(i_feat)

    matrix_dict['metadata'] = {'type': 'adjacency'}

    return matrix_dict


def create_layer_from_i_feat_list(geolayer, i_feat_list, feature_serialize=False, reset_i_feat=True):
    """ DEPRECATED """
    return create_geolayer_from_i_feat_list(geolayer,
                                            i_feat_list,
                                            feature_serialize=feature_serialize,
                                            reset_i_feat=reset_i_feat)


def create_geolayer_from_i_feat_list(geolayer, i_feat_list, feature_serialize=False, reset_i_feat=True):
    """
    Create a new layer with i_feat_list from an input layer
    """
    new_layer = {
        'metadata': dict(geolayer['metadata'])
    }

    if feature_serialize:
        geolayer['metadata']['feature_serialize'] = True

    new_layer['features'] = {}
    for new_i_feat, i_feat in enumerate(i_feat_list):
        if i_feat in geolayer['features']:
            if feature_serialize:
                new_feature = str(geolayer['features'][i_feat])
            else:
                new_feature = geolayer['features'][i_feat]

        if reset_i_feat:
            new_layer['features'][new_i_feat] = new_feature
        else:
            new_layer['features'][i_feat] = new_feature

    return new_layer


# -----------------------------------------------------------------------------------------------------------------------

# def export_geolayer_to_csv(save_path, geocontainer):
#     """
#     'export_geolayer_to_csv' permet d'exporter la table de correspondance dans un fichier au format csv.
#     Elle exporte que la tc de la geocontainer mais on pourrait rajouter aussi l'export dans autres layers.
#     On peut donner l'ordre des champs pour écrire dans le fichier en sortie.
#     'wb' et pas 'w' pour supprimer l'interligne vide entre chaque feature.
#     extrasaction='ignore' : permet d'ignorer si certains champs de la layer ne sont pas compris dans la sélection des
#     field_name renseigné.
#     field_name : permet de donner les champs et leur ordre d'écriture dans la layer_out
#
#     :param save_path: chemin + nom du fichier + extension du fichier en sortie
#     :param geocontainer: datasource de référence
#     """
#
#     layer_tc = geocontainer['layers']['tc']
#
#     with open(save_path, 'wb') as csvfile:
#         field_name = ('CODE_REF', 'EXIST_A', 'EXIST_B', 'ETAT_TC', 'REF_A', 'REF_B')
#         writer = csv.DictWriter(csvfile, fieldnames=field_name, extrasaction='ignore')
#         writer.writeheader()
#         for i_feat in layer_tc['features']:
#             writer.writerow(layer_tc['features'][i_feat]['attributes'])

# -----------------------------------------------------------------------------------------------------------------------

def save(geolayer, path, output_type='TXT'):
    """
    'save' est une procedure de sauvegarde des layers au geoformat_lib. Elle prend en compte plusieurs formats (txt, bin ou
    zip). Pour autant, le binaire proposé ici n'est pas exactement du binaire, cela reste à vérifier.

    :param geolayer: nom du directionnaire / géolayer à enregistrer
    :param path: chemin d'enregistrement + le nom du fichier qu'on veut en sortie + l'extension
    :param output_type: format de sauvegarde : texte, binaire, ou compressé
    """
    # save au format txt
    if output_type == 'TXT':
        with open(path, 'w') as geolayer_txt:
            geolayer_txt.write(str(geolayer))

    # save au format binaire
    # attention wb permet pas d'enregistré en binaire
    elif output_type == 'BIN':
        with open(path, 'wb') as geolayer_bin:
            geolayer_bin.write(str(geolayer))

    # save au format binaire compressé
    elif output_type == 'ZIP':
        save_zip = zlib.compress(str(geolayer))
        with open(path, 'wb') as geolayer_zip:
            geolayer_zip.write(save_zip)

    # message error si format de save pas reconnu
    else:
        sys.exit("error output_type not recognize")


# -----------------------------------------------------------------------------------------------------------------------

def load(path, input_type='TXT'):
    """
    'load' est une fonction de téléchargement de layers au geoformat. Elle permet de lire plusieurs formats (txt, bin ou
    zip). Pour autant, le binaire proposé ici n'est pas exactement du binaire, cela reste à vérifier.

    :param load_path: chemin du fichier à télécharger
    :param input_type: format du fichier à télécahrger
    """

    try:
        # load format txt
        if input_type == 'TXT':
            with open(path, 'r') as load_txt:
                file_load = load_txt.read()

        # load format bin
        elif input_type == 'BIN':
            with open(path, 'rb') as load_bin:
                file_load = load_bin.read()

        # load format zip
        elif input_type == 'ZIP':
            with open(path, 'rb') as load_txt_compress:
                file_load = zlib.decompress(load_txt_compress.read())

    # message d'erreur
    except:
        print('Error : savefile_type and input are not same')

    return eval(file_load)

# -----------------------------------------------------------------------------------------------------------------------
