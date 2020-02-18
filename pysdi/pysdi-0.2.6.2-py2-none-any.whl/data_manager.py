#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Utilities for manage datasets
Author
------
    Roberto A. Real-Rangel (Institute of Engineering UNAM; Mexico)

License
-------
    GNU General Public License
"""
import sys

from collections import OrderedDict
from pathlib2 import Path
import datetime as dt
import numpy as np
import toml
import xarray as xr


class Configurations():
    """
    """
    def __init__(self, config_file):
        self.config_file = config_file
        config = toml.load(config_file)

        for key, value in config.items():
            setattr(self, key, value)


def load_dir(directory):
    """
    Parameters
    ----------
        directory: string
            Full path of the directory to be loaded.
    """
    if not Path(directory).exists():
        create_dir = raw_input(
            "The directory '{}' does not exist.\n"
            "Do you want to create it? [Y] Yes, [N] No. ".
            format(directory)
            )

        if create_dir.lower() == 'y':
            Path(directory).mkdir(parents=True, exist_ok=True)

        else:
            sys.exit("Cannot continue without this directory. Aborting.")

    return(Path(directory))


def drop_array(data, keeplst=False, drop_patt=False):
    """
    Parameters
    ----------
        data
        xyt_vars: dictionary
        drop_patt: bool, optional (default False)
    """
    if keeplst is not False:
        joined_list = ['_'.join(i) for i in keeplst]
        vars_to_drop = [i for i in data.var() if i not in joined_list]

    elif drop_patt is not False:
        vars_to_drop = [
            var
            for var in data.var()
            for pattern in drop_patt
            if pattern in var
            ]

    return(data.drop(vars_to_drop))


def merge_arrays(data, vars_to_merge):
    for merged_variables in vars_to_merge:
        units = list(set([data[i].units for i in merged_variables]))

        if len(units) == 1:
            new_var = '_'.join(merged_variables)
            data[new_var] = sum(
                [data[i] for i in merged_variables]
                ).assign_attrs({'units': units[0]})

        data = data.drop(merged_variables)

    return(data)


def accumulate_time(data, t_acc):
    """Generates a dataset of time-accumulated values.

    Parameters
    ----------
        data: xarray.Dataset
        t_acc: list
    """
    # TODO: This function needs to be modified to consider any temporal
    # resolution of the input data. Currently, it only allows monthly data.
    # Issue #2.
    data_accum = data.copy()

    for var in data_accum.var():
        try:
            if data_accum[var].units == 'kg m-2 s-1':
                data_accum[var] = data_accum[var].rolling(time=t_acc).sum()

            else:
                data_accum[var] = data_accum[var].rolling(time=t_acc).mean()

        except (AttributeError):
            data_accum[var] = data_accum[var].rolling(time=t_acc).sum()

        except (KeyError):
            data_accum = data_accum.drop(var)

    for old_name in data_accum.var():
        new_name = old_name + '_tacc' + str(t_acc)
        data_accum[new_name] = data_accum[old_name].rename(new_name)
        data_accum = data_accum.drop(old_name)

    return(data_accum)


def check_source(raw_dataset, imp_dataset):
    """Import MERRA-2 dataset.

    Parameters
    ----------
    raw_dataset : string
        Local directory where raw (monthly) MERRA-2 datasets are
        stored.
    imp_dataset : string
        Local directory where annualy aggregated datasets will be
        stored.
    """
    # TODO: Check and update the last year dataset if it is out of date.
    # OR always import any missing AND the last/current year.
    print("- Checking imported dataset in '{}'".format(imp_dataset))
    files_list = []

    for ftype in ['**/*.nc', '**/*.nc4']:
        files_list.extend(load_dir(raw_dataset).glob(ftype))

    years = sorted(set([i.stem.split('.')[2][:4] for i in files_list]))

    for year in years:
        yearfiles = list(load_dir(imp_dataset).glob(pattern='*' + year + '*'))

        if (len(yearfiles) == 0) or (year == years[-1]):
            print("  - Importing dataset of {}.".format(year))
            sources = [
                i
                for i in files_list
                if i.stem.split('.')[2][:4] == year
                ]
            xr.open_mfdataset([str(i) for i in sources]).to_netcdf(
                str(load_dir(imp_dataset) / ('M2TMNXLND_' + year + '.nc4'))
                )


def progress_message(current, total, message="- Processing", units=None):
    """Issue messages of the progress of the process.

    Generates a progress bar in terminal. It works within a for loop,
    computing the progress percentage based on the current item
    number and the total length of the sequence of item to iterate.

    Parameters:
        current : integer
            The last item number computed within the for loop. This
            could be obtained using enumerate() in when calling the for
            loop.
        total : integer
            The total length of the sequence for which the for loop is
            performing the iterations.
        message : string (optional; default = "- Processing")
            A word describing the process being performed (e.g.,
            "- Computing", "- Drawing", etc.).
        units : string (optional; default = None)
            Units represented by te loops in the for block (e.g.,
            "cells", "time steps", etc.).
    """
    if units is not None:
        progress = float(current)/total
        sys.stdout.write(
            "\r    {} ({:.1f} % of {} processed)".format(
                message, progress * 100, units
                )
            )

    else:
        progress = float(current)/total
        sys.stdout.write(
            "\r    {} ({:.1f} % processed)".format(message, progress * 100)
            )

    if progress < 1:
        sys.stdout.flush()

    else:
        sys.stdout.write('\n')


def monthly_dataset(date, arrays, title='SDI'):
    """Derivate single monthly outputs from the data cube of the full
    study period.

    Parameters
    ----------
        date : xarray.DataArray
            Date that defines the month from which the data exported.
        arrays : list
            Data to export.
        title : str
            Name of the index exported.
    """
    data_vars = {
        i.attrs['DroughtFeature']: i.sel({'time': date}) for i in arrays
        }
    year = str(date).split('-')[0]
    month = str(date).split('-')[1].zfill(2)
    output_dataset = xr.Dataset(data_vars=data_vars)
    attrs = OrderedDict()
    attrs['Title'] = title
    attrs['TemporalRange'] = year + month
    attrs['SouthernmostLatitude'] = min(output_dataset.lat.values)
    attrs['NorthernmostLatitude'] = max(output_dataset.lat.values)
    attrs['WesternmostLongitude'] = min(output_dataset.lon.values)
    attrs['EasternmostLongitude'] = max(output_dataset.lon.values)
    attrs['LatitudeResolution'] = output_dataset.lat.diff(dim='lat').values[0]
    attrs['LongitudeResolution'] = output_dataset.lon.diff(dim='lon').values[0]
    attrs['SpatialCoverage'] = 'Mexico'
    attrs['History'] = (
        'Original file generated:' + dt.datetime.now().isoformat()
        )
    attrs['Contact'] = ('Roberto A. Real-Rangel (rrealr@iingen.unam.mx)')
    attrs['Institution'] = (
        'Institute of Engineering of the National Autonomous University of'
        'Mexico (II-UNAM)'
        )
    attrs['Format'] = 'NetCDF-4/HDF-5'
    attrs['VersionID'] = '1.0.0'
    output_dataset.attrs = attrs
    return(output_dataset)


def export_nc4(dataset, output_dir='pysdi_out', prefix=None):
    """ Export a given dataset to a NetCDF-4 file (.nc4).

    Parameters:
        dataset : xarray.Dataset
        output_dir : string, optional
        prefix : string (optional; default is None)
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_file = (
        prefix + dataset.attrs['Title'].upper() + '_'
        + dataset.attrs['TemporalRange'] + '.nc4'
        )
    dataset.to_netcdf(str(Path(output_dir) / output_file))


def convert_units(data):
    """
    Converts the original units of MERRA-2 variables to conventional
    units (e.g., kg m-2 s-1 to mm s-1).

    Parameters
    ----------
        data: xarray.Dataset
            Dataset of the values which units are to be
            transformed.

    Returns
    -------
        xarray.Dataset
            Dataset of the transformed values.
    """
    data.time.values = data.time.values.astype('datetime64[M]')
    time_m = data.time.values.astype('datetime64[M]')
    time_s = data.time.values.astype('datetime64[s]')
    seconds = ((time_m + np.timedelta64(1, 'M') - time_s).
               astype('datetime64[s]')).astype(int)

    for var in data.var():
        try:
            if data[var].units == 'kg m-2 s-1':
                data_aux = data[var].values

                for i, val in enumerate(data_aux):
                    data_aux[i] = val * seconds[i]

                data[var].values = data_aux
                data[var].attrs['units'] = 'mm'

            elif data[var].units == 'K':
                data[var].values = data[var].values - 273.15
                data[var].attrs['units'] = 'C'

            elif data[var].units == 'kg m-2':
                data[var].attrs['units'] = 'mm'

            else:
                pass

        except AttributeError:
            pass

    return(data)
