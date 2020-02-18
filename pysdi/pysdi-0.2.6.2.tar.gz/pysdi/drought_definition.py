# -*- coding: utf-8 -*-
"""Definition of drought.
Author
------
    Roberto A. Real-Rangel (Institute of Engineering UNAM; Mexico)

License
-------
    GNU General Public License
"""
from collections import OrderedDict as _OrderedDict
from scipy.stats import norm as _norm
import gdal as _gdal
import numpy as _np
import ogr as _ogr
import sys as _sys
import xarray as _xr
import warnings as _warnings

# Mute warnings. Comments this for debugging.
_warnings.simplefilter(action='ignore', category=FutureWarning)
_warnings.simplefilter(action='ignore', category=RuntimeWarning)


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
        _sys.stdout.write(
            "\r    {} ({:.1f} % of {} processed)".format(
                message, progress * 100, units
                )
            )

    else:
        progress = float(current)/total
        _sys.stdout.write(
            "\r    {} ({:.1f} % processed)".format(message, progress * 100)
            )

    if progress < 1:
        _sys.stdout.flush()

    else:
        _sys.stdout.write('\n')


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
    source_ds = _ogr.Open(utf8_path=vmap)
    source_layer = source_ds.GetLayer(0)

    # Create the destination data source
    cols = len(data.lon.values)
    rows = len(data.lat.values)
    output_source = _gdal.GetDriverByName('MEM').Create(
        '', cols, rows, _gdal.GDT_Byte
        )

    if res > 0:
        xres = res
        yres = res

    else:
        xres = _np.diff(x_coords)[0]
        yres = _np.diff(y_coords)[0]

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
    _gdal.RasterizeLayer(
        dataset=output_source,
        bands=[1],
        layer=source_layer,
        burn_values=[1],
        options=['ALL_TOUCHED=TRUE']
        )
    mask = _xr.DataArray(
        data=_np.flipud(output_band.ReadAsArray()),
        coords={'lat': y_coords, 'lon': x_coords},
        dims=['lat', 'lon']
        )
    trimmed_data = data.loc[dict(lat=mask.lat, lon=mask.lon)]
    masked_data = trimmed_data.where(mask)
    return(masked_data)


def get_time_series(data, month):
    """Slice a given month in the 'time' dimension from a dataset.

    Parameters
    ----------
    data : xarray.Dataset
        A dataset to which it is desired to perform the slicing. Its
        temporal dimension needs to be called 'time'.
    month : int
        The number of the month to slice (e. g., 1 for january, 2 for
        fabruary, etc.)

    Returns
    -------
    xarray.Dataset
        A slice of the original dataset with only the data form the
        month of interest.
    """
    return(data.isel(time=_np.where(data.time.dt.month == month)[0]))


def empirical_probability(X, a=0.44):
    """Computes the empirical probability.

     Empirical probability is computed using the plotting position
     general form as follows:

     P  = (i - a) / (n + 1 - (2 * a))

    where i is the rank of the item, n is the size of the sample and a
    is a coeficient to be proposed. Some values of a found in
    literature are:

        a = 0.000 (Weibull, 1939)
        a = 0.375 (Blom, 1958)
        a = 0.400 (Cunnane, 1978)
        a = 0.440 (Gringorten, 1963)
        a = 0.500 (Hazen, 1913)

    References:
    Blom, Gunnar (1958). Statistical estimates and transformed beta-
        variables. In: Almquist und Wiksell, pp. 68-75, 143-146.
    Cunnane, C. (1978). Unbiased plotting positions - A review. In:
        Journal of Hydrology 37, pp. 205-222. doi: 10.1016/0022-
        1694(79)90120-3.
    Gringorten, Irving I. (1963). A plotting rule for extreme
        probability paper. In: Journal of Geophysical Research 68.3,
        pp. 813. doi: 10.1029/JZ068i003p00813.
    Hazen, Allen (1913). Storage to be provided impounding reservoirs
        for municipal water supply. In: Proceedings of the American
        Society of Civil Engineers 39.9, pp. 1943-2044.
    Weibull, Ernst Hjalmar Waloddi (1939). The Phenomenon of Rupture in
        Solids. Stockholm.

    Parameters
    ----------
    X : numpy.ndarray
        Time series. It contains as many rows as time steps and as many
        columns as variables.
    a : float
        Parameter a in the general formula for plotting possitions.

    Returns
    -------
    numpy.ndarray
        Sequence of values representing the empirical probability
        of each element of the time series.
    """
    n = _np.all(_np.isfinite(X), axis=3).sum(axis=(0))
    i = _np.ndarray((_np.shape(X)[:-1])) * _np.nan

    for m, mat in enumerate(X):
        i[m] = _np.all(X <= mat, axis=3).sum(axis=0)

    return((i - a) / (n + 1 - (2 * a)))


def compute_npsdi(
        data, temp_scale, index, variable, output_res=0, nodata=-32768,
        trim_vmap=None, interp_method='linear'
        ):
    """Compute non-parametric standardized drought indices (SDI).

    References:
    Edwards, D. C., & McKee, T. B. (1997). Characteristics of 20th
        Century drought in the United States at multiple time scales.
        Atmospheric Science Paper No. 634, May 1–30, 174–174. Retrieved
        from http://oai.dtic.mil/oai/oai?verb=getRecord&metadataPrefix=
        html&identifier=ADA325595
    Hao, Z., & AghaKouchak, A. (2013). Multivariate Standardized
        Drought Index: A parametric multi-index model. Advances in
        Water Resources, 57, 12–18. https://doi.org/10.1016
        /j.advwatres.2013.03.009
    Hao, Z., & AghaKouchak, A. (2014). A Nonparametric Multivariate
        Multi-Index Drought Monitoring Framework. Journal of
        Hydrometeorology, 15(1), 89–101. https://doi.org/10.1175/JHM-D-
        12-0160.1
    McKee, T. B., Doesken, N. J., & Kleist, J. (1993). The relationship
        of drought frequency and duration to time scales. Eighth
        Conference on Applied Climatology, 179–184. American
        Meteorological Society.
    Shukla, S., & Wood, A. W. (2008). Use of a Standardized Runoff
        Index for Characterizing Hydrologic Drought. Geophysical
        Research Letters, 35(2), 1–7. https://doi.org/10.1029
        /2007GL032487

    Parameters
    ----------
    data : xarray.Dataset
        The input datasets of MERRA-2 merged into one data cube (time,
        lat, lon).
    temp_scale : int
        The temporal scale to which the input data is aggregated to
        compute the standardized drought index.
    index : str
        The name of the index to be computed. Valid options are:
            'SPI', to compute the Standardized Precipitation Index
                (McKee et al., 1993, Edwards & McKee, 1997);
            'SRI', to compute the Standardized Runoff Index (Shukla &
                 Wood, 2008);
            'SSI', to compute the Standardized Soil Moisture Index (Hao
                & AghaKouchak, 2013);
            'MSDI-PRERUN', to compute the Multivariate Standardized
                Drought Index for precipitation and runoff (Hao &
                AghaKouchak, 2013; 2014);
            'MSDI-PRESMO', to compute the Multivariate Standardized
                Drought Index for precipitation and soil moisture (Hao
                & AghaKouchak, 2013; 2014); and
            'MSDI-PRESMORUN', to compute the Multivariate Standardized
                Drought Index for precipitation and soil moisture and
                runoff (Hao & AghaKouchak, 2013; 2014).
    variable : sequence
        A list of the MERRA-2's variable(s) name(s) used to compute the
        index. Valid options are:
            [['PRECTOTLAND']], to compute the SPI;
            [['BASEFLOW', 'RUNOFF']], to compute the SRI;
            [['RZMC']], to compute the SSI;
            [['PRECTOTLAND'], ['BASEFLOW', 'RUNOFF']], to compute the
                MSDI-PRERUN;
            [['PRECTOTLAND'], ['RZMC']], to compute the MSDI-PRESMO;
                and
            [['PRECTOTLAND'], ['RZMC'], ['BASEFLOW', 'RUNOFF']], to
                compute the MSDI-PRESMORUN.
    output_res : float, optional
        The spatial resolution used in the output SDI dataset.
    nodata : int, optional
        Value to set in empty cells. Default is -32768.
    trim_vmap : str, optional
        Full path of a shapefile that contains the vector map used to
            trim the output dataset.

    Returns
    -------
    xarray.Dataset
        Dataset of the SDI computed.
    """
    # TODO: Remove the parameter 'variable' from the arguments and
    # define the variables names from the index to compute.

    # Merge mergeable variables.
    if sum([len(i) > 1 for i in variable]) > 0:
        vars_to_merge = variable[
            [
                j
                for j in range(len(variable))
                if [len(i) > 1 for i in variable][j] is True][0]
            ]
        data = merge_arrays(
            data=data,
            vars_to_merge=[vars_to_merge]
            )

    data_clean = drop_array(
        data=data,
        keeplst=variable
        )
    data_scaled = accumulate_time(
        data=data_clean,
        t_acc=temp_scale
        )
    inp_shape = list(
        _np.shape(data_scaled[data_scaled.var().keys()[0]].values)
        )
    intensity_aux = _np.ndarray(inp_shape, dtype='float32') * _np.nan

    for month in range(1, 13):
        t_index = data_scaled.time.dt.month == month
        time_series = get_time_series(
            data=data_scaled,
            month=month
            )

        for v, var in enumerate(time_series.var().iterkeys()):
            var_data = _np.expand_dims(time_series[var].values, axis=3)

            if v == 0:
                rec_arranged = var_data.copy()

            else:
                rec_arranged = _np.concatenate(
                    (rec_arranged, var_data.copy()),
                    axis=3
                    )

        P = empirical_probability(rec_arranged)
        SDI = _norm.ppf(P)
        SDI[_np.isnan(SDI)] = 0   # To fill near sore sea cells.
        intensity_aux[t_index] = SDI
        progress_message(
            current=month,
            total=12,
            message=(
                "- Computing the {} index for a {}-month time scale".format(
                    index.upper(), temp_scale
                    )
                ),
            units='months'
            )

    intensity = _xr.DataArray(
        data=intensity_aux,
        coords={
            'time': data_scaled.time.values,
            'lat': data_scaled.lat.values,
            'lon': data_scaled.lon.values
            },
        dims=['time', 'lat', 'lon']
        )
    intensity = intensity.reindex({'time': sorted(intensity.time.values)})

    if output_res > 0:
        x_min = float(_np.floor(intensity.lon.min())) + (output_res / 2.)
        x_max = float(_np.ceil(intensity.lon.max())) - (output_res / 2.)
        y_min = float(_np.floor(intensity.lat.min())) + (output_res / 2.)
        y_max = float(_np.ceil(intensity.lat.max())) - (output_res / 2.)
        out_lon = _np.arange(x_min, x_max + output_res, output_res)
        out_lat = _np.arange(y_min, y_max + output_res, output_res)
        intensity = intensity.interp(
            lat=out_lat,
            lon=out_lon,
            method=interp_method
            )

    # Trim the intensity dataset.
    if trim_vmap is not None:
        intensity = trim_data(
            data=intensity,
            vmap=trim_vmap,
            res=output_res,
            nodata=nodata
            )

    # Define global attributes
    global_attrs = _OrderedDict()
    global_attrs['DroughtFeature'] = 'Drought_intensity'
    global_attrs['DroughtIndex'] = index
    global_attrs['TemporalScale'] = str(temp_scale) + ' month(s)'
    global_attrs['Units'] = 'None'
    global_attrs['Description'] = 'Nonparametric Standardized Drought Index'
    intensity.attrs = global_attrs

    # Define coordinates attributes
    lat_attrs = _OrderedDict()
    lat_attrs['long_name'] = "latitude"
    lat_attrs['units'] = "degrees_north"
    lat_attrs['standard_name'] = "latitude"
    intensity.lat.attrs = lat_attrs
    lon_attrs = _OrderedDict()
    lon_attrs['long_name'] = "longitude"
    lon_attrs['units'] = "degrees_east"
    lon_attrs['standard_name'] = "longitude"
    intensity.lon.attrs = lon_attrs

    return(intensity)


def compute_magnitude(intensity, severity_threshold=1):
    """Computes the drought magnitude for each time step of a drought
    intensity raster map.

    Parameters
    ----------
        intensity : xarray.Dataset
            The values of the drought intensity computed with
            compute.npsdi().
        severity_threshold : float (optional; default: 1)
            A value to divide the resultant drought magnitude (the
            run-sum) in order to express the results as number of
            months of duration if every month of the dry period had the
            threshold value. If negative (positive), deficit magnitudes
            results are positives (negative).

    Returns
    -------
        xarray.DataFrame
            The values of the drought magnitude (the run-sum).
    """
    # TODO: Check how the cumsum of pandas works to apply it here.
    magnitude = intensity.copy()
    intensity_sign = _xr.ufuncs.sign(intensity)
    change_flag = abs(
        intensity_sign.shift(shifts={'time': 1}) - intensity_sign != 0
        )
    magnitude.load()

    for d, date in enumerate(magnitude.time):
        curr = intensity.sel({'time': date}) / severity_threshold

        if d == 0:
            magnitude.loc[date] = curr

        else:
            past = magnitude.shift(shifts={'time': 1}).sel({'time': date})
            magnitude.loc[date] = _xr.where(
                cond=change_flag.loc[date],
                x=curr,
                y=past + curr
                )

        progress_message(
            current=d + 1,
            total=len(magnitude.time),
            message="- Computing the drought magnitude",
            units='time steps'
            )

    attrs = _OrderedDict()
    attrs['DroughtFeature'] = 'Drought_magnitude'
    attrs['DroughtIndex'] = magnitude.attrs['DroughtIndex']
    attrs['TemporalScale'] = magnitude.attrs['TemporalScale']
    attrs['Units'] = 'None'
    attrs['Description'] = (
        'Nonparametric Standardized Drought Index accumulated during a run of'
        'consecutive negative (deficit) or positive (excess) values'
        )
    magnitude.attrs = attrs
    return(magnitude)
