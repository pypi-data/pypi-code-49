# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""The utility functions to check the """
import numpy as np
import pandas as pd

from datetime import timedelta
from typing import Any, Dict, List, Optional, Tuple, Union, Set

from azureml.automl.runtime import featurizer

from automl.client.core.common.types import GrainType
from automl.client.core.runtime.time_series_data_frame import TimeSeriesDataFrame
from automl.client.core.runtime.types import DataInputType,\
    DataSingleColumnInputType
from pandas.tseries.frequencies import to_offset
from pandas.tseries.offsets import DateOffset, QuarterEnd, QuarterBegin
from automl.client.core.common.constants import TimeSeriesInternal
from automl.client.core.common.exceptions import ClientException, DataException

FREQUENCY_REJECT_TOLERANCE = 0.90
FREQ = 'freq'
START = 'start'


def get_tsdf_frequency_and_start(
        X: pd.DataFrame,
        y: Optional[DataSingleColumnInputType],
        time_column_Name: str,
        grain_column_names: GrainType
) -> Optional[Tuple[pd.DateOffset, Union[pd.Timestamp, Dict[GrainType, pd.Timestamp]]]]:
    """
    Detect the frequency of a pandas data frame.

    :param X: The data frame used for the frequency inference.
    :param y: The labels for X.
    :param time_column_Name: The column denoting date time.
    :param grain_column_names: The columns defining multiple series.
    :returns: tuple, containing frequency and dictionary with starting time for each grain,
              if different grains have different frequencies or less then FREQUENCY_REJECT_TOLERANCE
              fraction of points can be fit into given frequency.
              If the data frame contain only one grain, the timestamp will be returned instead of a dictionary.
    :raises: DataException
    """
    if y is not None:
        X[TimeSeriesInternal.DUMMY_TARGET_COLUMN] = y
    else:
        X[TimeSeriesInternal.DUMMY_TARGET_COLUMN] = np.NaN
    if grain_column_names is None or grain_column_names == []:
        X[TimeSeriesInternal.DUMMY_GRAIN_COLUMN] = TimeSeriesInternal.DUMMY_GRAIN_COLUMN
        grain_column_names = [TimeSeriesInternal.DUMMY_GRAIN_COLUMN]
    try:
        tsdf = TimeSeriesDataFrame(
            X,
            time_colname=time_column_Name,
            grain_colnames=grain_column_names,
            ts_value_colname=TimeSeriesInternal.DUMMY_TARGET_COLUMN
        )
    except BaseException:
        # We should not fail here if the data frame can not be created, we will fail
        # on the validation step.
        return None
    # Remove added columns.
    drop = [TimeSeriesInternal.DUMMY_TARGET_COLUMN]
    if grain_column_names == [TimeSeriesInternal.DUMMY_GRAIN_COLUMN]:
        drop.append(TimeSeriesInternal.DUMMY_GRAIN_COLUMN)
    X.drop(drop, axis=1, inplace=True)
    tsdf.sort_index(inplace=True)
    freq_offset = tsdf.infer_freq(return_freq_string=False)
    # If frequency is inferred, we already have the solution.
    groupby_ob = tsdf.groupby_grain()

    fixed_frequencies = groupby_ob.apply(
        lambda x: improved_infer_freq_one_grain(
            x, freq_offset, x.name)).reset_index(
        drop=True)
    if len(fixed_frequencies[FREQ].unique()) == 1:
        coverage = groupby_ob.apply(lambda x: check_coverage_one_grain(x, fixed_frequencies)).sum()
        if coverage / len(X) >= FREQUENCY_REJECT_TOLERANCE:
            dict_starts = {}
            for grain, df in groupby_ob:
                df = pd.merge(
                    pd.DataFrame(df),
                    fixed_frequencies,
                    on=df.grain_colnames,
                    how='left',
                    left_index=True,
                    right_index=False)
                df.reset_index(drop=True, inplace=True)
                dict_starts[grain] = df[START][0]
            if len(dict_starts.keys()) == 1 and TimeSeriesInternal.DUMMY_GRAIN_COLUMN in dict_starts.keys():
                return fixed_frequencies[FREQ][0], dict_starts[TimeSeriesInternal.DUMMY_GRAIN_COLUMN]
            return fixed_frequencies[FREQ][0], dict_starts
    return None


def check_coverage_one_grain(one_grain: TimeSeriesDataFrame, freqs: Union[pd.DataFrame, pd.Series]) -> int:
    """
    Get the number of points covered by the given frequency.

    :param one_grain: The data frame denoting one grain.
    :param freq: The proposed frequency of the grain.
    """
    if isinstance(freqs, pd.Series):
        freq = freqs[FREQ]
        start = freqs[START]
    else:
        df = pd.merge(
            pd.DataFrame(one_grain),
            freqs,
            on=one_grain.grain_colnames,
            how='left',
            left_index=True,
            right_index=False)
        df.reset_index(drop=True, inplace=True)
        freq = df[FREQ][0]
        start = df[START][0]
    date_grid = pd.date_range(start=start, end=one_grain.time_index.max(), freq=freq)
    return len([time for time in one_grain.time_index if time in date_grid])


def improved_infer_freq_one_grain(df_grain: TimeSeriesDataFrame, freq_offset: pd.DateOffset, grain: str) -> pd.Series:
    """
    Improved version of frequency inference which can be applied to one grain.

    In this algorithm we first try to use the TimeSeriesDataFrame mechanism if frequency detection,
    build the corresponding frequency grid and if the percentage of data which does not fit the
    grid is within the FREQUENCY_REJECT_TOLERANCE we return this frequency and start date for the given
    grain.
    In case if TimeSeriesDataFrame mechanism left a lot of data points outside the grid, we estimate
    timedeltas between the data points and take the mode of these values. This mode is then used to reconstruct
    the frequency. If the point groups having equal timedelta are separated by some other time interval, we
    consider it to be a different data grid.
    We construct multiple grids and select the dominant one with the percentage
    of non fitted points within FREQUENCY_REJECT_TOLERANCE. We also return the start point used for grid generation.
    If the tiomedeltas remind month, year or quarter we try if these DateOffset s can fit most of data points.
    If neither grid is good enough we return the previous frequency from TimeSeriesDataFrame mechanism.
    :param df_grain: The data frame representing one grain.
    :param freq_offset: The frequency determined by the TimeSeriesDataFrame mechanism.
    :param grain: The name of a given grain.
    :returns: the series with frequency and start date.
              Example: pd.Series{freq=<Days * 7>, start='2019-01-01'}
    """
    # Pandas data frame try to take minimal date range between cells, but if this range is very small,
    # it will result in memory error.
    df_grain.sort_index(inplace=True)
    ix_time = df_grain.time_index
    try:
        time_grid = pd.date_range(start=df_grain.time_index.min(), end=df_grain.time_index.max(), freq=freq_offset)
        time_not_desired = [i for i in ix_time.to_series() if i not in time_grid]
        best_coverage = len(df_grain) - len(time_not_desired)
    except MemoryError:
        best_coverage = 0
    # Can we do better then we have already did?
    if best_coverage / len(df_grain) <= FREQUENCY_REJECT_TOLERANCE:
        # We (1) need another frequency (2) we can not establish the frequency.
        # We want to do subtraction without relation to index.
        timedeltas = (ix_time[1:] - ix_time[:-1]).to_series()
        td_mode = timedeltas.mode()[0]
        # Search for timedelta indexes, where delta is equal to
        # its mode.
        anchor_indexes = np.where(timedeltas == td_mode)[0]
        anchored_freq = None
        first_timestamp = None
        for frequency in get_frequencies_choices(td_mode, ix_time.to_series()):
            # Return freq_offset if dominant difference between points is less them millisecond.
            # In this case timedelta between two dates will be 0,
            # resulting in frequency:DateOffset(days=0).
            if frequency == DateOffset(days=0):
                return _series_freq_start_for_grain(df_grain, freq_offset, ix_time.min(), grain)
            if not has_dominant_frequency(timedeltas, td_mode, frequency, 1 - FREQUENCY_REJECT_TOLERANCE):
                continue
            # There are len(anchor_indexes) possible grids.
            # Theoretically we can have several sets of values separated by uneven time interval.
            # by using this iterations we try to handle this scenario.
            old_ix = -1
            set_checked_start_times = set()
            for i in range(len(anchor_indexes)):
                if old_ix == -1 or anchor_indexes[i] > old_ix + 1:
                    # If previous timedelta index differs by one, that
                    # means we already looked at this grid.
                    start = ix_time[anchor_indexes[i]]
                    if start in set_checked_start_times:
                        # If the start time is the same, we have already covered
                        # this anchor previously because the frequency is the same.
                        continue
                    else:
                        set_checked_start_times.add(start)
                    while df_grain.time_index.min() < start:
                        start -= frequency
                    date_grid = pd.date_range(start=start, end=df_grain.time_index.max(), freq=frequency)
                    covered_points = [i for i in range(len(ix_time)) if ix_time[i] in date_grid]
                    covered_number = len(covered_points)
                    if covered_number > best_coverage:
                        best_coverage = covered_number
                        anchored_freq = to_offset(pd.infer_freq(date_grid))
                        if anchored_freq is None:
                            # For some frequencies pandas mechanism does not work,
                            # the example is DateOffset(months=1) and the anchor
                            # is not the first or last day of the month pandas version 0.23.4.
                            anchored_freq = frequency
                        first_timestamp = ix_time[min(covered_points)]
                    if 2 * covered_number > len(ix_time):
                        # We break the inner loop because in this case we consider date grids
                        # are separated by non equal timedeltas. Given that another grid, using the same frequency
                        # can not cover more data points and hence should not be tried.
                        break
                old_ix = anchor_indexes[i]
        if anchored_freq is not None:
            return _series_freq_start_for_grain(df_grain, anchored_freq, first_timestamp, grain)
    # We were unable to find the better frequency, return what we have.
    return _series_freq_start_for_grain(df_grain, freq_offset, ix_time.min(), grain)


def _series_freq_start_for_grain(
        df_one_grain: TimeSeriesDataFrame,
        freq: pd.DateOffset,
        start: pd.Timestamp,
        grain: str) -> pd.Series:
    """
    The internal function to return frequency and start time in grain aware manner.

    :param df_grain: TimeSeriesDataFrame with only one grain.
    :param freq: The freqiency of this grain.
    :param start: the first timestamp to be used for date grid generation.
    :param grain: The name of a given grain.
    :returns: The Series, containing grains, freq and start times.
    """
    dict_data = {FREQ: freq, START: start}

    if df_one_grain.grain_colnames is not None:
        if not isinstance(grain, tuple):
            dict_data[df_one_grain.grain_colnames[0]] = grain
        else:
            for ord, col in enumerate(df_one_grain.grain_colnames):
                dict_data[col] = grain[ord]
    return pd.Series(dict_data)


def get_frequencies_choices(delta: pd.Timedelta, df_time: pd.Series) -> List[pd.DateOffset]:
    """
    Return possible frequencies for the given timeselta.

    We need this function in case the frequency is special, for example it may
    be a monthly frequencies with some dates missing.
    :param delta: The dominant time delta between data points.
    :param df_time: The series, obtained from data frame time index.
    :returns: The list of frequencies to be tried.
    """
    # The default frequency
    frequencies = []
    dominant_day = df_time.apply(lambda x: x.day).mode()[0]
    dominant_month = df_time.apply(lambda x: x.month).mode()[0]
    if delta in {pd.Timedelta(days=30), pd.Timedelta(days=31)}:
        # Monthly frequency.
        if dominant_day in [30, 31]:
            frequencies.append(to_offset('M'))
        elif dominant_day == 1:
            frequencies.append(to_offset('MS'))
        else:
            frequencies.append(DateOffset(months=1))
    elif delta == pd.Timedelta(days=365):
        # Yearly frequency.

        if dominant_day == 1 and dominant_month == 1:
            frequencies.append(to_offset('YS'))
        elif dominant_day == 31 and dominant_month == 12:
            frequencies.append(to_offset('Y'))
        else:
            frequencies.append(DateOffset(years=1))
    elif delta == pd.Timedelta(days=92):
        # Quarterly frequency.
        start_month = df_time[0].month
        month_counts = df_time.apply(lambda x: x.month).value_counts()
        if start_month not in month_counts[0:4].index:
            start_month = dominant_month
        if dominant_day in [30, 31]:
            frequencies.append(QuarterEnd(startingMonth=start_month))
        elif dominant_day == 1:
            frequencies.append(QuarterBegin(startingMonth=start_month))
    # From timedelta we will get the unanchored frequency for example <7 * Days>.
    frequencies.append(featurizer.transformer.timeseries.forecasting_heuristic_utils.timedelta_to_freq_safe(delta))
    return frequencies


def has_dominant_frequency(
        timedeltas: pd.Series,
        delta_mode: pd.Timedelta,
        dominant_frequency: pd.DateOffset,
        tolerance: float) -> bool:
    """
    Determine if the data set can comply with dominant_frequency.

    *Note:* In this quick test we just test if data set can comply to the frequency according to given
    timedeltas, but it is not guaranteed and actual check if most of data points are in the frequency
    grid should happen afterwards.
    :param timedeltas: The timedeltas from the single series.
    :param delta_mode: The most frequent timedelta in the series.
    :param frequency: The detected dominant frequency to be tested.
    :param tolerance: The allowed percentage of outliers from the expected timedeltas.
    :returns: True if data set can be in this frequency grid, False otherwise.
    """
    allowed_deltas = get_dominant_timedeltas(dominant_frequency, delta_mode)
    non_coompliant = sum(delta not in allowed_deltas for delta in timedeltas)
    return non_coompliant / len(timedeltas) <= tolerance


def get_dominant_timedeltas(frequency: pd.DateOffset, default: pd.Timedelta) -> Set[pd.Timedelta]:
    """
    Get the dominant timedelta for the given frequency.

    :param frequency: The frequency for which the timedelta needs to be estimated.
    :param default: The median time delta present on all returned sets.
    :returns: Dominant timedeltas for given timedelta.
    """
    # Pandas has its own function pd.to_timedelta, but it does not handle frequencies,
    # which does not have 'delta' attribute.
    timedeltas = set()
    if hasattr(frequency, 'delta'):
        timedeltas = {frequency.delta}
    elif isinstance(frequency, pd.offsets.Week) or frequency == DateOffset(weeks=1):
        timedeltas = {pd.Timedelta(days=7)}
    elif isinstance(frequency, pd.offsets.BusinessDay):
        timedeltas = {pd.Timedelta(days=1), pd.Timedelta(days=3)}
    elif isinstance(frequency, pd.offsets.MonthOffset) or frequency == DateOffset(months=1):
        timedeltas = {pd.Timedelta(days=30), pd.Timedelta(days=31),
                      pd.Timedelta(days=28), pd.Timedelta(days=29)}
    elif isinstance(frequency, pd.offsets.YearOffset) or frequency == DateOffset(years=1):
        timedeltas = {pd.Timedelta(days=365), pd.Timedelta(days=366)}
    elif isinstance(frequency, pd.offsets.QuarterOffset):
        timedeltas = {pd.Timedelta(days=90), pd.Timedelta(days=91), pd.Timedelta(days=92)}
    timedeltas.add(default)
    return timedeltas


def fix_df_frequency(X: pd.DataFrame,
                     time_column_name: str,
                     grain_column_names: GrainType,
                     start_times: Union[pd.Timestamp, Dict[GrainType, pd.Timestamp]],
                     freq: pd.DateOffset) -> pd.DataFrame:
    """
    Remove outlier data points from the data frame which does not comply with the given frequency.

    :param X: The data frame used for the frequency inference.
    :param time_column_Name: The column denoting date time.
    :param grain_column_names: The columns defining multiple series.
    :param start_times: The start times for time series. If data set contains multiple grains,
                        it must be a dictionary with start times for each grain. If data set
                        does not contain grains, it is a single timestamp.
    :returns: pd.DateOffset is frequency can be inferred or None otherwise.
    :raises: ClientException
    """
    if (grain_column_names is None) != isinstance(start_times, pd.Timestamp):
        raise ClientException('If the data frame contains multiple data time series, the start times '
                              'should be represented by a dictionary in case of a single '
                              'series, it must be a pd.Timestamp.')
    if grain_column_names is None:
        while start_times > pd.to_datetime(X[time_column_name]).min():
            start_times -= freq
        return fix_frequency_one_grain(X, freq, start_times, time_column_name)
    dfs = []
    for grain, df in X.groupby(grain_column_names, as_index=False, group_keys=False):
        if grain not in start_times.keys():
            # If we do not know the start time we can not fix the data frame.
            dfs.append(df)
        else:
            start_time = start_times[grain]
            while start_time > pd.to_datetime(X[time_column_name]).min():
                start_time -= freq
            dfs.append(fix_frequency_one_grain(
                df,
                freq,
                start_time,
                time_column_name))
    if dfs:
        return_df = pd.concat(dfs)
        return_df.reset_index(inplace=True, drop=True)
        return return_df
    # Return the empty data frame if all data were filtered.
    return X[:0]


def fix_frequency_one_grain(X: pd.DataFrame,
                            freq: pd.DateOffset,
                            start: pd.Timestamp,
                            time_column_name: str) -> pd.DataFrame:
    """
    Remove outlier data points from the data frame which does not comply with the given frequency.

    :param X: Tha time series data frame to be used during fitting.
    :param freq: The frequency to be used for fixing X.
    :param start: The starting point of grid to tilter data frame.
    :param time_column_name: The column denoting date time.
    :returns: the dataframe with corrected frequency.
    """
    X[time_column_name] = pd.to_datetime(X[time_column_name])
    # Make a date grid in the time frame of a data frame X.
    data_grid = pd.date_range(start=start, end=X[time_column_name].max(), freq=freq)
    grid_df = data_grid.to_frame(index=False)
    grid_df.rename({grid_df.columns[0]: time_column_name}, axis=1, inplace=True)
    # Do an inner join to remove all outliers.
    return grid_df.merge(X, 'inner', on=time_column_name)


def check_types(X: pd.DataFrame,
                y: Optional[DataSingleColumnInputType]) -> None:
    """
    Raise the exception if X or y has incorrect type, also convert y to np.ndarray.

    :param X: The data frame used for the frequency inference.
    :param y: The labels for X.
    :returns: tuple with X and y.
    :raises: DataException
    """
    if not isinstance(X, pd.DataFrame):
        raise DataException('X must be of a DataFrame type.')
    if y is not None and not isinstance(y, np.ndarray):
        raise DataException('y must be of a numpy.ndarray type.')


def fix_data_set_regularity_may_be(
        X: pd.DataFrame,
        y: Optional[DataSingleColumnInputType],
        time_column_name: str,
        grain_column_names: GrainType) -> Tuple[pd.DataFrame, Optional[DataSingleColumnInputType], bool, bool]:
    """
    The helper function to fix the data frame frequency.

    :param X: The data frame used for the frequency inference.
    :param y: The labels for X.
    :param time_column_name: The column denoting date time.
    :param grain_column_names: The columns defining multiple series.
    :rerturns: The corrected data frame, corresponding y, and two flags showing
               if the frequency inference failed and if data set was modified.
    """
    # At this point we already converted y to np.ndarray.
    check_types(X, y)
    X[time_column_name] = pd.to_datetime(X[time_column_name])
    results = get_tsdf_frequency_and_start(
        X, y,
        time_column_name, grain_column_names)
    if results is None:
        # We are unable to get frequency, giving up.
        # Do not print any guard rails because we will fail later on data set verification.
        return X, y, True, False

    new_freq, starts = results
    if y is not None:
        # If y was provided, align it with X.
        X[TimeSeriesInternal.DUMMY_TARGET_COLUMN] = y
    X_fixed = fix_df_frequency(X,
                               time_column_name,
                               grain_column_names,
                               starts,
                               new_freq)
    y_fixed = None
    if y is not None:
        X.drop(TimeSeriesInternal.DUMMY_TARGET_COLUMN, inplace=True, axis=1)
        y_fixed = X_fixed.pop(TimeSeriesInternal.DUMMY_TARGET_COLUMN).values
    return X_fixed, y_fixed, False, X_fixed.shape[0] != X.shape[0]
