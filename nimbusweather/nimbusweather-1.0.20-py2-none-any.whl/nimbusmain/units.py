# -*- coding: utf-8 -*-
#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

"""Data structures and functions for dealing with units."""

import logging

obs_group_dict = {"altitude": "group_altitude",
                  "cooldeg": "group_degree_day",
                  "heatdeg": "group_degree_day",
                  "gustdir": "group_direction",
                              "vecdir": "group_direction",
                              "windDir": "group_direction",
                              "windGustDir": "group_direction",
                              "interval": "group_interval",
                              "soilMoist1": "group_moisture",
                              "soilMoist2": "group_moisture",
                              "soilMoist3": "group_moisture",
                              "soilMoist4": "group_moisture",
                              "extraHumid1": "group_percent",
                              "extraHumid2": "group_percent",
                              "extraHumid3": "group_percent",
                              "extraHumid4": "group_percent",
                              "extraHumid5": "group_percent",
                              "extraHumid6": "group_percent",
                              "extraHumid7": "group_percent",
                              "inHumidity": "group_percent",
                              "outHumidity": "group_percent",
                              "rxCheckPercent": "group_percent",
                              "altimeter": "group_pressure",
                              "barometer": "group_pressure",
                              "pressure": "group_pressure",
                              "radiation": "group_radiation",
                              "ET": "group_rain",
                              "dayRain": "group_rain",
                              "hail": "group_rain",
                              "hourRain": "group_rain",
                              "monthRain": "group_rain",
                              "rain": "group_rain",
                              "snow": "group_rain",
                              "rain24": "group_rain",
                              "totalRain": "group_rain",
                              "stormRain": "group_rain",
                              "yearRain": "group_rain",
                              "hailRate": "group_rainrate",
                              "rainRate": "group_rainrate",
                              "wind": "group_speed",
                              "windGust": "group_speed",
                              "windSpeed": "group_speed",
                              "windSpeed10": "group_speed",
                              "windgustvec": "group_speed",
                              "windvec": "group_speed",
                              "rms": "group_speed2",
                              "vecavg": "group_speed2",
                              "dewpoint": "group_temperature",
                              "extraTemp1": "group_temperature",
                              "extraTemp2": "group_temperature",
                              "extraTemp3": "group_temperature",
                              "extraTemp4": "group_temperature",
                              "extraTemp5": "group_temperature",
                              "extraTemp6": "group_temperature",
                              "extraTemp7": "group_temperature",
                              "heatindex": "group_temperature",
                              "heatingTemp": "group_temperature",
                              "inTemp": "group_temperature",
                              "leafTemp1": "group_temperature",
                              "leafTemp2": "group_temperature",
                              "leafTemp3": "group_temperature",
                              "leafTemp4": "group_temperature",
                              "outTemp": "group_temperature",
                              "soilTemp1": "group_temperature",
                              "soilTemp2": "group_temperature",
                              "soilTemp3": "group_temperature",
                              "soilTemp4": "group_temperature",
                              "windchill": "group_temperature",
                              "dateTime": "group_time",
                              "leafWet1": "group_count",
                              "leafWet2": "group_count",
                              "UV": "group_uv",
                              "consBatteryVoltage": "group_volt",
                              "heatingVoltage": "group_volt",
                              "referenceVoltage": "group_volt",
                              "supplyVoltage": "group_volt",
                              "cloudbase": "group_altitude",
                              "windrun": "group_distance"}

EnglishUnits = {"group_altitude": "foot",
                "group_count": "count",
                "group_degree_day": "degree_F_day",
                "group_direction": "degree_compass",
                "group_elapsed": "second",
                "group_interval": "minute",
                "group_moisture": "centibar",
                "group_percent": "percent",
                "group_pressure": "inHg",
                "group_radiation": "watt_per_meter_squared",
                "group_rain": "inch",
                "group_rainrate": "inch_per_hour",
                "group_speed": "mile_per_hour",
                "group_speed2": "mile_per_hour2",
                "group_temperature": "degree_F",
                "group_time": "unix_epoch",
                "group_deltatime": "second",
                "group_uv": "uv_index",
                "group_volt": "volt",
                "group_amp": "amp",
                "group_power": "watt",
                "group_energy": "watt_hour",
                "group_volume": "gallon",
                "group_data": "byte",
                "group_distance": "mile",
                "group_length": "inch"}

MetricUnits = {"group_altitude": "meter",
               "group_count": "count",
               "group_degree_day": "degree_C_day",
               "group_direction": "degree_compass",
               "group_elapsed": "second",
               "group_interval": "minute",
               "group_moisture": "centibar",
               "group_percent": "percent",
               "group_pressure": "mbar",
               "group_radiation": "watt_per_meter_squared",
               "group_rain": "cm",
               "group_rainrate": "cm_per_hour",
               "group_speed": "km_per_hour",
               "group_speed2": "km_per_hour2",
               "group_temperature": "degree_C",
               "group_time": "unix_epoch",
               "group_deltatime": "second",
               "group_uv": "uv_index",
                           "group_volt": "volt",
                           "group_amp": "amp",
                           "group_power": "watt",
                           "group_energy": "watt_hour",
                           "group_volume": "litre",
                           "group_data": "byte",
                           "group_distance": "km",
                           "group_length": "cm"}

conversionDict = {
    'inHg': {'mbar': lambda x: x * 33.86,
             'hPa': lambda x: x * 33.86,
             'mmHg': lambda x: x * 25.4},
    'degree_F': {'degree_C': lambda x: (x - 32.0) * (5.0 / 9.0)},
    'degree_F_day': {'degree_C_day': lambda x: x * (5.0 / 9.0)},
    'mile_per_hour': {'km_per_hour': lambda x: x * 1.609344,
                      'knot': lambda x: x * 0.868976242,
                      'meter_per_second': lambda x: x * 0.44704},
    'mile_per_hour2': {'km_per_hour2': lambda x: x * 1.609344,
                       'knot2': lambda x: x * 0.868976242,
                       'meter_per_second2': lambda x: x * 0.44704},
    'knot': {'mile_per_hour': lambda x: x * 1.15077945,
             'km_per_hour': lambda x: x * 1.85200,
             'meter_per_second': lambda x: x * 0.514444444},
    'knot2': {'mile_per_hour2': lambda x: x * 1.15077945,
              'km_per_hour2': lambda x: x * 1.85200,
              'meter_per_second2': lambda x: x * 0.514444444},
    'inch_per_hour': {'cm_per_hour': lambda x: x * 2.54,
                      'mm_per_hour': lambda x: x * 25.4},
    'inch': {'cm': lambda x: x * 2.54,
             'mm': lambda x: x * 25.4},
    'foot': {'meter': lambda x: x * 0.3048},
    'mmHg': {'inHg': lambda x: x / 25.4,
             'mbar': lambda x: x / 0.75006168,
             'hPa': lambda x: x / 0.75006168},
    'mbar': {'inHg': lambda x: x / 33.86,
             'mmHg': lambda x: x * 0.75006168,
             'hPa': lambda x: x * 1.0},
    'hPa': {'inHg': lambda x: x / 33.86,
            'mmHg': lambda x: x * 0.75006168,
            'mbar': lambda x: x * 1.0},
    'degree_C': {'degree_F': lambda x: x * (9.0 / 5.0) + 32.0},
    'degree_C_day': {'degree_F_day': lambda x: x * (9.0 / 5.0)},
    'km_per_hour': {'mile_per_hour': lambda x: x * 0.621371192,
                    'knot': lambda x: x * 0.539956803,
                    'meter_per_second': lambda x: x * 0.277777778},
    'meter_per_second': {'mile_per_hour': lambda x: x * 2.23693629,
                         'knot': lambda x: x * 1.94384449,
                         'km_per_hour': lambda x: x * 3.6},
    'meter_per_second2': {'mile_per_hour2': lambda x: x * 2.23693629,
                          'knot2': lambda x: x * 1.94384449,
                          'km_per_hour2': lambda x: x * 3.6},
    'cm_per_hour': {'inch_per_hour': lambda x: x * 0.393700787,
                    'mm_per_hour': lambda x: x * 10.0},
    'mm_per_hour': {'inch_per_hour': lambda x: x * .0393700787,
                    'cm_per_hour': lambda x: x * 0.10},
    'cm': {'inch': lambda x: x * 0.393700787,
           'mm': lambda x: x * 10.0},
    'mm': {'inch': lambda x: x * .0393700787,
           'cm': lambda x: x * 0.10},
    'meter': {'foot': lambda x: x * 3.2808399},
    'dublin_jd': {'unix_epoch': lambda x: (x - 25567.5) * 86400.0},
    'unix_epoch': {'dublin_jd': lambda x: x / 86400.0 + 25567.5},
    'second': {'hour': lambda x: x / 3600.0,
               'minute': lambda x: x / 60.0,
               'day': lambda x: x / 86400.0},
    'minute': {'second': lambda x: x * 60.0,
               'hour': lambda x: x / 60.0,
               'day': lambda x: x / 1440.0},
    'hour': {'second': lambda x: x * 3600.0,
             'minute': lambda x: x * 60.0,
             'day': lambda x: x / 24.0},
    'day': {'second': lambda x: x * 86400.0,
            'minute': lambda x: x * 1440.0,
            'hour': lambda x: x * 24.0},
    'gallon': {'litre': lambda x: x * 3.78541,
               'cubic_foot': lambda x: x * 0.133681},
    'litre': {'gallon': lambda x: x * 0.264172,
              'cubic_foot': lambda x: x * 0.0353147},
    'cubic_foot': {'gallon': lambda x: x * 7.48052,
                   'litre': lambda x: x * 28.3168},
    'bit': {'byte': lambda x: x / 8},
    'byte': {'bit': lambda x: x * 8},
    'km': {'mile': lambda x: x * 0.621371192},
    'mile': {'km': lambda x: x * 1.609344}}

UnitMaps = {'ENGLISH': EnglishUnits,
            'METRIC': MetricUnits}


def convertDict(obs_dict, new_unit_system):
    target_dict = {}
    current_unit_system = obs_dict['units']

    if obs_dict['units'] == new_unit_system:
        return obs_dict

    for obs_type in obs_dict:

        unit_group = obs_group_dict.get(obs_type)

        if unit_group is None:
            continue

        current_unit_type = UnitMaps[current_unit_system].get(unit_group)
        new_unit_type = UnitMaps[new_unit_system].get(unit_group)

        if current_unit_type is None or new_unit_type is None:
            continue

        target_dict[obs_type] = convert(obs_dict[obs_type], current_unit_type, new_unit_type)

    target_dict['units'] = new_unit_system

    return target_dict


def convert(val, current_unit_type, target_unit_type):
    """ Convert a value or a sequence of values between unit systems. """

    if current_unit_type == target_unit_type:
        return val

    try:
        conversion_func = conversionDict[current_unit_type][target_unit_type]
    except KeyError:
        logging.debug("units: Unable to convert from %s to %s" % (current_unit_type, target_unit_type))
        raise

    # Try converting a sequence first. A TypeError exception will occur if
    # the value is actually a scalar:
    try:
        new_val = map(lambda x: conversion_func(x) if x is not None else None, val)
    except TypeError:
        new_val = conversion_func(val) if val is not None else None

    return new_val


def to_ENGLISH(datadict):
    """Convert the units used in a dictionary to US Customary."""
    return convertDict(datadict, 'ENGLISH')


def to_METRIC(datadict):
    """Convert the units used in a dictionary to Metric."""
    return convertDict(datadict, 'METRIC')
