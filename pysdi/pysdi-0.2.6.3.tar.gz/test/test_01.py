#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Nonparametric Standardized Drought Indices - pySDI main script
Author
------
    Roberto A. Real-Rangel (rrealr@iingen.unam.mx)

License
-------
    GNU General Public License
"""
# Import needed libraries
from pathlib2 import Path
from pysdi import drought_definition as drgt
import numpy as np
import xarray as xr

parent_dir = Path(__file__).parent.absolute()
input_data_file = str(parent_dir/'test_input_data.nc4')
data = xr.open_dataset(filename_or_obj=input_data_file)   # Load sample data.
drought_intensity = drgt.compute_npsdi(   # Compute drought intensity.
    data=data,
    temp_scale=1,
    index='SPI',
    variable=[['PRECTOTLAND']]
    )
drought_magnitude = drgt.compute_magnitude(   # Compute drought magnitude.
    intensity=drought_intensity
    )
date = np.datetime64('2011-08-01T00:30')   # MERRA-2 dates are set to T00:30
arrays = [drought_intensity, drought_magnitude]
data_vars = {
    i.attrs['DroughtFeature']: i.sel({'time': date})
    for i in arrays
    }
output_dataset = xr.Dataset(data_vars=data_vars)
output_dataset.to_netcdf(parent_dir/'test_01_output_data.nc4')
