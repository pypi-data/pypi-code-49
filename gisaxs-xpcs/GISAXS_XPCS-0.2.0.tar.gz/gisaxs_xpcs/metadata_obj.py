#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contains MetaData class which allows to extract image properties such as temperatures and evaporation rates
"""

from typing import List, Optional, Any
import logging
from pathlib import Path

import h5py
import numpy as np

from gisaxs_xpcs.common_tools import get_zaptime_files


class MetaData(object):
    class Property(object):
        def __init__(self, h5name: str, unit: str = '', description: str = '',
                     name: str = None, value: Any = None, abs_time: float = None):
            self.h5name = h5name
            self.name = name or self.h5name
            self.unit = unit
            self.description = description
            self.value = value
            self.abs_time = abs_time

        def get_property(self, value, abs_time: float = None):
            return MetaData.Property(self.h5name, self.unit, self.description, self.name,
                                     value, abs_time)

        def __repr__(self):
            if isinstance(self.value, float):
                return '%s = %.2f (%s): %s. code: %s' % (self.name,
                                                         self.value, self.unit, self.description, self.h5name)
            else:
                return '%s (%s): %s. code: %s' % (self.name, self.unit, self.description, self.h5name)

    ###################################

    PROPERTIES = (Property('SThick', 'nm',
                           '''Film thickness estimated by crystal frequency changing''', 'thickness'),
                  Property('Temp1', '\N{DEGREE SIGN}C', 'PEN temperature of evaporation',
                           'temp_evaporation'),
                  Property('Temp2', '\N{DEGREE SIGN}C', 'Sample temperature', 'temp_sample'),
                  Property('ScalcRate60', 'nm/min', 'Smoothed rate of evaporation (1min average)',
                           'evaporation_rate'))

    ###################################

    class ImageProperties(dict):

        def __init__(self, *args, abs_time: float = None):
            if len(args) != len(MetaData.PROPERTIES):
                raise ValueError('Wrong number of properties passed: %d' % len(args))

            prop_dict = {property_.name: property_.get_property(value, abs_time)
                         for property_, value in zip(MetaData.PROPERTIES, args)}
            if abs_time:
                prop_dict['abs_time'] = abs_time

            super(MetaData.ImageProperties, self).__init__(**prop_dict)

        def __repr__(self):
            return '\n'.join([self.get(property_.name).__repr__() for property_ in MetaData.PROPERTIES])

    ###################################

    def __init__(self, filepath: str = None):
        self.filepath = filepath or Path(__file__).parent / 'metadata.h5'

    def get_image_properties(self, folder_num: int, file_num: int,
                             return_dict: bool = False) -> dict:
        try:
            with h5py.File(self.filepath, 'r') as f:
                common_group = f['common']
                zaptime_dset_name = 'zaptime_%d_abs_time' % folder_num
                image_abs_time = common_group[zaptime_dset_name][file_num]
                abs_time = common_group['abs_time'][()]
                index = np.argmin(np.abs(abs_time - image_abs_time))
                logging.debug('index = %d' % index)
                logging.debug('image_abs_time = %.2f' % image_abs_time)
                properties = [common_group[pr.h5name][index] for pr in self.PROPERTIES]
                if not return_dict:
                    return MetaData.ImageProperties(*properties, abs_time=image_abs_time)
                else:
                    return {pr.name: value for pr, value in zip(self.PROPERTIES, properties)}
        except Exception as err:
            print(err)
            return dict({'error': err})

    def get_first_and_last(self, folder_num: int) -> Optional[List[dict]]:
        files = get_zaptime_files(folder_num)
        if not files:
            return
        else:
            return [self.get_image_properties(folder_num, 0),
                    self.get_image_properties(folder_num, len(files) - 1)]

    def get_latex_title(self, folder_num: int, file_num: int,
                        attrs: dict = None) -> str:
        attrs = attrs or self.get_image_properties(folder_num, file_num)
        return '\n$T_{sample} = %.2f$ %s, $T_{pen} = %.2f$ %s, d = %.1f %s\n' % \
               (attrs['temp_sample'].value, attrs['temp_sample'].unit,
                attrs['temp_evaporation'].value, attrs['temp_evaporation'].unit,
                attrs['thickness'].value, attrs['thickness'].unit)


if __name__ == '__main__':
    from pprint import pprint

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    metadata = MetaData()
    # pprint([p['temp_sample'] for p in metadata.get_first_and_last(16)])
    pprint(metadata.get_image_properties(19, 1300))
