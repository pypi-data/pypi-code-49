#! /usr/bin/env python
#
# Author: Roberto Cuccu - RSS Team - 2018

import os
import re
import glob
import numpy as np
import io
import sys


class L8_Product:

    def __init__(self, product_path):

        # Check if path exist
        if not os.path.exists(product_path):
            raise (IOError('Product path does not exist'))

        # Get L8 product structure
        try:
            self.path = product_path

            file_to_match = 'L*_B1.TIF'
            band_1 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_1 = band_1
            file_to_match = 'L*_B2.TIF'
            band_2 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_2 = band_2
            file_to_match = 'L*_B3.TIF'
            band_3 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_3 = band_3
            file_to_match = 'L*_B4.TIF'
            band_4 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_4 = band_4
            file_to_match = 'L*_B5.TIF'
            band_5 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_5 = band_5
            file_to_match = 'L*_B6.TIF'
            band_6 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_6 = band_6
            file_to_match = 'L*_B7.TIF'
            band_7 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_7 = band_7
            file_to_match = 'L*_B10.TIF'
            band_10 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_10 = band_10
            file_to_match = 'L*_B11.TIF'
            band_11 = glob.glob(os.path.join(product_path, file_to_match))[0]
            self.band_11 = band_11

            self.bands = {
                "b1": band_1,
                "b2": band_2,
                "b3": band_3,
                "b4": band_4,
                "b5": band_5,
                "b6": band_6,
                "b7": band_7,
                "b10": band_10,
                "b11": band_11
            }

        except IndexError:
            os.sys.exit('Error - Not possible to retrieve L8 product structure - Procedure aborted')


class L8_MTL:

    def __init__(self, MTL_path):

        # Get MTL text file
        MTL_string_match = 'L*_MTL.txt'
        MTL_file_search = glob.glob(os.path.join(MTL_path, MTL_string_match))
        MTL_file = MTL_file_search[0]

        if not os.path.exists(MTL_file):
            raise (IOError('MTL file not found'))

        try:
            self.MTL_path = MTL_path
            self.MTL_file = MTL_file

            # Read MTL file
            MTL_file_open = io.open(MTL_file, 'rU')
            MTL_content = MTL_file_open.read()
            MTL_file_open.close()

            # Get metadata
            # REFLECTANCE MULT BANDS
            string_to_search = 'REFLECTANCE_MULT_BAND_1 =.*'
            reflectance_mult_band_1 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_1 = reflectance_mult_band_1

            string_to_search = 'REFLECTANCE_MULT_BAND_2 =.*'
            reflectance_mult_band_2 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_2 = reflectance_mult_band_2

            string_to_search = 'REFLECTANCE_MULT_BAND_3 =.*'
            reflectance_mult_band_3 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_3 = reflectance_mult_band_3

            string_to_search = 'REFLECTANCE_MULT_BAND_4 =.*'
            reflectance_mult_band_4 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_4 = reflectance_mult_band_4

            string_to_search = 'REFLECTANCE_MULT_BAND_5 =.*'
            reflectance_mult_band_5 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_5 = reflectance_mult_band_5

            string_to_search = 'REFLECTANCE_MULT_BAND_6 =.*'
            reflectance_mult_band_6 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_6 = reflectance_mult_band_6

            string_to_search = 'REFLECTANCE_MULT_BAND_7 =.*'
            reflectance_mult_band_7 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_7 = reflectance_mult_band_7

            string_to_search = 'RADIANCE_MULT_BAND_10 =.*'
            reflectance_mult_band_10 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_10 = reflectance_mult_band_10

            string_to_search = 'RADIANCE_MULT_BAND_11 =.*'
            reflectance_mult_band_11 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_mult_band_11 = reflectance_mult_band_11

            string_to_search = 'K1_CONSTANT_BAND_10 =.*'
            reflectance_k1_band_10 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_k1_band_10 = reflectance_k1_band_10

            string_to_search = 'K1_CONSTANT_BAND_11 =.*'
            reflectance_k1_band_11 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_k1_band_11 = reflectance_k1_band_11

            self.reflectance_mult_factors = {
                "REFLECTANCE_MULT_BAND_1": reflectance_mult_band_1,
                "REFLECTANCE_MULT_BAND_2": reflectance_mult_band_2,
                "REFLECTANCE_MULT_BAND_3": reflectance_mult_band_3,
                "REFLECTANCE_MULT_BAND_4": reflectance_mult_band_4,
                "REFLECTANCE_MULT_BAND_5": reflectance_mult_band_5,
                "REFLECTANCE_MULT_BAND_6": reflectance_mult_band_6,
                "REFLECTANCE_MULT_BAND_7": reflectance_mult_band_7,
                "RADIANCE_MULT_BAND_10": reflectance_mult_band_10,
                "RADIANCE_MULT_BAND_11": reflectance_mult_band_11,
                "K1_CONSTANT_BAND_10": reflectance_k1_band_10,
                "K1_CONSTANT_BAND_11": reflectance_k1_band_11
            }

            # REFLECTANCE ADD BANDS
            string_to_search = 'REFLECTANCE_ADD_BAND_1 =.*'
            reflectance_add_band_1 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_1 = reflectance_add_band_1

            string_to_search = 'REFLECTANCE_ADD_BAND_2 =.*'
            reflectance_add_band_2 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_2 = reflectance_add_band_2

            string_to_search = 'REFLECTANCE_ADD_BAND_3 =.*'
            reflectance_add_band_3 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_3 = reflectance_add_band_3

            string_to_search = 'REFLECTANCE_ADD_BAND_4 =.*'
            reflectance_add_band_4 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_4 = reflectance_add_band_4

            string_to_search = 'REFLECTANCE_ADD_BAND_5 =.*'
            reflectance_add_band_5 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_5 = reflectance_add_band_5

            string_to_search = 'REFLECTANCE_ADD_BAND_6 =.*'
            reflectance_add_band_6 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_6 = reflectance_add_band_6

            string_to_search = 'REFLECTANCE_ADD_BAND_7 =.*'
            reflectance_add_band_7 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_7 = reflectance_add_band_7

            string_to_search = 'RADIANCE_ADD_BAND_10 =.*'
            reflectance_add_band_10 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_10 = reflectance_add_band_10

            string_to_search = 'RADIANCE_ADD_BAND_11 =.*'
            reflectance_add_band_11 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_add_band_11 = reflectance_add_band_11

            string_to_search = 'K2_CONSTANT_BAND_10 =.*'
            reflectance_k2_band_10 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_k2_band_10 = reflectance_k2_band_10

            string_to_search = 'K2_CONSTANT_BAND_11 =.*'
            reflectance_k2_band_11 = get_mtl_value(MTL_content, string_to_search)
            self.reflectance_k2_band_11 = reflectance_k2_band_11

            self.reflectance_add_factors = {
                "REFLECTANCE_ADD_BAND_1": reflectance_add_band_1,
                "REFLECTANCE_ADD_BAND_2": reflectance_add_band_2,
                "REFLECTANCE_ADD_BAND_3": reflectance_add_band_3,
                "REFLECTANCE_ADD_BAND_4": reflectance_add_band_4,
                "REFLECTANCE_ADD_BAND_5": reflectance_add_band_5,
                "REFLECTANCE_ADD_BAND_6": reflectance_add_band_6,
                "REFLECTANCE_ADD_BAND_7": reflectance_add_band_7,
                "RADIANCE_ADD_BAND_10": reflectance_add_band_10,
                "RADIANCE_ADD_BAND_11": reflectance_add_band_11,
                "K2_CONSTANT_BAND_10": reflectance_k2_band_10,
                "K2_CONSTANT_BAND_11": reflectance_k2_band_11
            }

            # SUN ELEVATION and ZENITH angles
            string_to_search = 'SUN_ELEVATION =.*'
            sun_elevation = get_mtl_value(MTL_content, string_to_search)
            sun_zenith = 90.0 - np.float(sun_elevation)
            self.sun_elevation_angle = sun_elevation
            self.sun_zenith_angle = sun_zenith

        except IndexError:
            os.sys.exit('Error - Not possible to retriev MTL metadata - Procedure aborted')


def get_mtl_value(MTL, pattern2match):
    check = re.compile(pattern2match)
    match = (check.findall(MTL))
    if match:
        mtl_value = (match[0].split('='))[1].replace('"', '').replace(' ', '')
    else:
        mtl_value = 'no match'
    return mtl_value

