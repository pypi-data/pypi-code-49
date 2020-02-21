"""Contains functions that simplify the interface to the probe service."""

import time

import numpy as np
import pandas as pd

from geospin.utilities.decorators import retry
from geospin.utilities.pandas_utils import write_csv


def remove_space(wkts):
    """
    Remove specific spaces from the WKT format to be compatible with probe.

    :param list(str) wkts: List of GPS coordinates in standard WKT format.
    :return list(str): List of corrected GPS coordinates compatible with probe.
    """
    return [wkt.replace(' (', '(') for wkt in wkts]


def parse(result):
    """
    Create pandas.DataFrame from probe output.

    :param ProbeResult result: Unknown iterable (to be specified in probe
        service documentation). Currently the first element of multiple
        timepoints is selected.
    :return pandas.DataFrame: Parsed probe output.
    """
    result = result.__dict__['_Model__dict']
    return pd.DataFrame({feature: [value[0] for value in result[feature]] for
                         feature in result if not feature.startswith('_')})


def store(df, filename):
    """
    Store probed features to csv with dtype information.

    :param pandas.DataFrame df: Probed features and corresponding values.
    :param str filename: Specific name of the output csv file, if None then the
        current datetime string is used as filename (format: Y-m-d_HMS.csv).
    """
    if filename is None:
        filename = '/data/extract/{}.csv'.format(time.strftime(
            '%Y-%m-%d_%H%M%S'))
    write_csv(df, filename=filename, export_dtypes=True)


@retry(Exception)
def request(wkts, source_geometry, source_geometry_mode, probe_mode, version,
            timeseries, radius, source_type):
    """
    Submit a single probing request to the Geode.

    :param list(str) wkts: List of GPS coordinates in standard WKT format.
    :param str source_geometry: The feature name or category to be probed.
    :param str source_geometry_mode: The mode of probe passed to the probe
        service.
    :param object probe_service: An instatiation of the probe service with the
        (hopefully) same version specified as in the version argument.
    :param str version: Version of probe used.
    :param list(str) timeseries: Timeframe of interest passed to probe.
    :param int radius: Radius for the probe operation density.
    :return list(pandas.DataFrame): List of individual results.
    """
    version_major, version_minor, version_patch = version.split('.', 2)

    if int(version_major) > 1:
        raise NotImplementedError('Request is not supported for Probe version'
                                  ' > 1.*.')

    if '5' == version_minor:
        if source_geometry_mode == 'pierce':
            if source_type == 'features':
                result = probe_mode(wkts=wkts,
                                    features=[source_geometry],
                                    timeseries=timeseries)
            else:
                result = probe_mode(wkts=wkts,
                                    categories=[source_geometry],
                                    timeseries=timeseries)
        else:
            if source_type == 'features':
                result = probe_mode(wkts=wkts,
                                    features=[source_geometry],
                                    timeseries=timeseries,
                                    radius=radius)
            else:
                result = probe_mode(wkts=wkts,
                                    categories=[source_geometry],
                                    timeseries=timeseries,
                                    radius=radius)

    if version_minor in ['3', '4']:
        if source_geometry is None:
            result = probe_mode(wkts=wkts)
        else:
            if source_type == 'features':
                result = probe_mode(wkts=wkts, features=[source_geometry])
            else:
                result = probe_mode(wkts=wkts, categories=[source_geometry])

    return result.result()


def chunk(sequence, n_chunks):
    """
    Yield successive maximally n sized chunks from a list.

    :param list sequence: Sequence of GPS coordinates to be split.
    :param int n_chunks: Number of pieces to be split into.
    :return: Sequence of list chunks, in this case GPS coordinates.
    :rtype: iterator

    .. seealso::
       https://stackoverflow.com/questions/312443/
       how-do-you-split-a-list-into-evenly-sized-chunks
    """
    for i in range(0, len(sequence), n_chunks):
        yield sequence[i:i + n_chunks]


def combine(results):
    """
    Combines the individual columns (features) and rows (locations) into a
    single pandas.DataFrame.

    :param list(pandas.DataFrame) results: List of individual results.
    :return pandas.DataFrame: Combined rows and columns in a data frame.
    """
    return pd.concat([pd.concat(result, axis=1) for result in results])


def probe(df, wkt_column, source_geometries, probe_service, version,
          timeseries=None, radius=None, chunksize=1000, filename=None,
          source_type='categories'):
    """
    Probe with the geode based probe service.

    :param pandas.DataFrame df:
    :param list(str) wkt_column: Name of the column that contains GPS
        coordinates in wkt format.
    :param dict source_geometries: List of feature names or feature categories
        passed to probe. Set `source_type` accordingly.
    :param object probe_service: Instance of the probe service.
    :param str version: Version of the probe service used.
    :param list(str) timeseries: Timeframe of interest passed to probe.
    :param int radius: Radius for the probe operation density.
    :param int chunksize: Size of location chunks passed to probe.
    :param str filename: Location where to store the probe result.
    :param str source_type: Defines if features are categories or individual
        features.
    :return pandas.DataFrame df: Data frame that contains original data merged
        with the probed features for all locations (rows).
    """
    mode_map = {'density': probe_service.client.probe.density,
                'pierce': probe_service.client.probe.pierce,
                'nearest': probe_service.client.probe.nearest}

    version_major, version_minor, version_patch = version.split('.', 2)

    if version_major == '1' and int(version_minor) >= 5 and not timeseries:
        raise AttributeError('Parameter timeseries is required for Probe '
                             'version > 1.5.')

    unique_wkts = df[wkt_column].unique()
    unique_wkts_probe_format = remove_space(unique_wkts)

    results = []
    for n, item in enumerate(chunk(unique_wkts_probe_format, chunksize)):
        print(n + 1, 'of', int(np.ceil(len(
            unique_wkts_probe_format) / chunksize)))
        partial_result = []
        for source_geometry, mode in source_geometries.items():
            result = request(item, source_geometry, mode, mode_map[mode],
                             version, timeseries, radius, source_type)
            partial_result.append(parse(result))
        results.append(partial_result)
    results = combine(results)
    results['wkt'] = unique_wkts
    df = df.merge(results, left_on=wkt_column, right_on='wkt', how='left')
    store(df, filename)
    return df
