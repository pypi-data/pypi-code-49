#!/usr/bin/env python2
# -*- coding: utf-8 -*-
__author__ = 'Roberto A. Real-Rangel (Institute of Engineering UNAM)'
__license__ = 'GNU General Public License version 3'

import numpy as np
import gdal
import ogr
import xarray as xr


def trim_data(data, vmap, res, nodata):
    """
    Parameters:
        data : xarray.Dataset
        vmap : string
        res : float
        nodata : float

    Source:
        https://bit.ly/2HxeOng
    """
    x_min = data.lon.min()
    y_max = data.lat.max()
    x_coords = data.lon.values
    y_coords = data.lat.values

    # Open the data source and read in the extent
    source_ds = ogr.Open(utf8_path=vmap)
    source_layer = source_ds.GetLayer(0)

    # Create the destination data source
    cols = len(data.lon.values)
    rows = len(data.lat.values)
    output_source = gdal.GetDriverByName('MEM').Create(
        '', cols, rows, gdal.GDT_Byte
        )

    if res > 0:
        xres = res
        yres = res

    else:
        xres = np.diff(x_coords)[0]
        yres = np.diff(y_coords)[0]

    output_source.SetGeoTransform([
        x_min - (xres / 2),  # X upper left corner of the upper left pixel
        xres,  # pixel width
        0,
        y_max + (yres / 2),  # Y upper left corner of the upper left pixel
        0,
        -yres  # pixel height
        ])
    output_band = output_source.GetRasterBand(1)
    output_band.SetNoDataValue(nodata)

    # Rasterize
    gdal.RasterizeLayer(
        dataset=output_source,
        bands=[1],
        layer=source_layer,
        burn_values=[1],
        options=['ALL_TOUCHED=TRUE']
        )
    mask = xr.DataArray(
        data=np.flipud(output_band.ReadAsArray()),
        coords={'lat': y_coords, 'lon': x_coords},
        dims=['lat', 'lon']
        )
    trimmed_data = data.loc[dict(lat=mask.lat, lon=mask.lon)]
    masked_data = trimmed_data.where(mask)
    return(masked_data)
