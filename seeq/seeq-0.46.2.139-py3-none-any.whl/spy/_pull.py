import concurrent.futures
import datetime
import queue
import string
import threading
import tzlocal

import pandas as pd
import numpy as np

from seeq.sdk import *
from seeq import spy

from . import _common
from . import _config
from . import _login

from ._common import Status


def pull(items, *, start=None, end=None, grid='15min', header='__auto__', group_by=None, shape='auto',
         capsule_properties=None, tz_convert=None, calculation=None, bounding_values=False,
         invalid_values_as=np.nan, errors='raise', quiet=False, status=None, capsules_as=None):
    """
    Retrieves signal, condition or scalar data from Seeq Server and returns it
    in a DataFrame.

    Parameters
    ----------
    items : {pd.DataFrame, pd.Series}
        A DataFrame or Series containing ID and Type columns that can be used
        to identify the items to pull. This is usually created via a call to
        spy.search().

    start : {str, pd.Timestamp}
        The starting time for which to pull data. This argument must be a
        string that pandas.to_datetime() can parse, or a pandas.Timestamp.
        If not provided, 'start' will default to 'end' minus 1 hour. Note
        that Seeq will potentially return one additional row that is earlier
        than this time (if it exists), as a "bounding value" for
        interpolation purposes.

    end : {str, pd.Timestamp}
        The end time for which to pull data. This argument must be a string
        that pandas.to_datetime() can parse, or a pandas.Timestamp. If not
        provided, 'end' will default to now. Note that Seeq will potentially
        return one additional row that is earlier than this time (if it
        exists), as a "bounding value" for interpolation purposes.

    grid : {str, None}, default '15min'
        A period to use for interpolation such that all returned samples
        have the same timestamps. Interpolation will be applied at the server
        to achieve this. If grid=None is specified, no interpolation will
        occur and each signal's samples will be returned untouched. Where
        timestamps don't match, NaNs will be present within a row.
        Interpolation is either linear or step and is set per signal at the
        time of the signal's creation. To change the interpolation type for a
        given signal, change the signal's interpolation or use the appropriate
        'calculation' argument.

    header : str default '__auto__'
        The metadata property to use as the header of each column. Common
        values would be 'ID' or 'Name'. '__auto__' concatenates Path and Name
        if they are present.

    group_by : {str, list(str)}
        The name of a column or list of columns for which to group by. Often
        necessary when pulling data across assets: When you want header='Name',
        you typically need group_by=['Path', 'Asset']

    shape : {'auto', 'samples', 'capsules'}, default 'auto'
        If 'auto', returns capsules as a time series of 0 or 1 when signals are
        also present in the items argument, or returns capsules as individual
        rows if no signals are present. 'samples' or 'capsules' forces the
        output to the former or the latter, if possible.

    capsule_properties : list(str)
        A list of capsule properties to retrieve when shape='capsules'.
        By default, if no signals are present in the items DataFrame, then all
        properties found on a capsule are automatically returned (because
        the nature of the query allows them to be returned "for free").
        Otherwise, you must provide a list of names of properties to retrieve.

    tz_convert : {str, datetime.tzinfo}
        The time zone in which to return all timestamps. If the time zone
        string is not recognized, the list of supported time zone strings will
        be returned in the exception text.

    calculation : {str, pandas.Series, pandas.DataFrame}
        When applying a calculation across assets, the 'calculation' argument
        must be a one-row DataFrame (or a Series) and the 'items' argument must
        be full of assets. When applying a calculation to a signal/condition/
        scalar, calculation must be a string with a single variable in it:
        $signal, $condition or $scalar.

    bounding_values : bool
        If True, extra 'bounding values' will be returned before/after the
        specified query range for the purposes of assisting with interpolation
        to the edges of the range or, in the case of Step or PILinear
        interpolation methods, interpolating to 'now' when appropriate.

    invalid_values_as : object
        Invalid samples and scalars will appear in the returned DataFrame as
        specified in this argument. By default, invalid values will be returned
        as NaNs. Note that specifying a string for this argument (e.g,
        'INVALID') can have significant performance implications on numeric
        signals. You may wish to use a "magic" number like -999999999 if you
        want to be able to discern invalid values but preserve algorithmic
        performance.

    errors : {'raise', 'catalog'}, default 'raise'
        If 'raise', any errors encountered will cause an exception. If
        'catalog', errors will be added to a 'Result' column in the status.df
        DataFrame (errors='catalog' must be combined with
        status=<Status object>).

    quiet : bool
        If True, suppresses progress output.

    status : spy.Status
        If supplied, this Status object will be updated as the command
        progresses.

    capsules_as : str
        Deprecated, use shape argument instead.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the requested data.

    Examples
    --------
    Pull a list of signals and convert the timezone to another timezone

    >>> items = pd.DataFrame([{'ID': '8543F427-2963-4B4E-9825-220D9FDCAD4E', 'Type': 'CalculatedSignal'}])
    >>> spy.pull(items=items, grid='15min', calculation='$signal.toStep()',
    >>>          start='2019-10-5T02:53:45.567Z', end='2019-10-6', tz_convert='US/Eastern')

    Pull a list of capsules

    >>> compressor_on_high = spy.search({'Name': 'Compressor Power on High', 'Workbook': 'Folder 1 >> Workbook 8'})
    >>> spy.pull(compressor_on_high, start='2019-01-01T04:00:00Z', end='2019-01-09T02:00:00Z')

    Pull a list of capsules but apply a condition function in formula first

    >>> comp_high = spy.search({'Name': 'Compressor Power on High', 'Workbook': 'Folder 1 >> Workbook 8'})
    >>> spy.pull(comp_high, start='2019-01-01', end='2019-01-09', calculation='$condition.setMaximumDuration(1d)')

    Pull capsules as a binary signal at the specified grid. 1 when a capsule is
    present, 0 otherwise

    >>> comp_high = spy.search({'Name': 'Compressor Power on High', 'Workbook': 'Folder 1 >> Workbook 8'})
    >>> spy.pull(comp_high, start='2019-01-01T00:00:00Z', end='2019-01-01T12:00:00Z', shape='samples', grid='1h')

    Pull a scalar

    >>> compressor_power_limit = spy.push(
    >>>     metadata=pd.DataFrame(
    >>>         [{ 'Name': 'Compressor Power Limit', 'Type': 'Scalar', 'Formula': '50kW' }]), errors='raise')
    >>> spy.pull(compressor_power_limit)

    Apply a calculation to a signal using the 'calculation' argument

    >>> signal_with_calc = spy.search({'Name': 'Area A_Temperature', 'Datasource Name': 'Example Data'})
    >>> spy.pull(signal_with_calc,
    >>>          start='2019-01-01T00:00:00',
    >>>          end='2019-01-01T03:00:00',
    >>>          calculation='$signal.aggregate(average(), hours(), startKey())', grid=None)

    Convert a linearly interpolated signal into a step interpolated signal
    using the 'calculation' argument:

    >>> items = pd.DataFrame([{'ID': '8543F427-2963-4B4E-9825-220D9FDCAD4E', 'Type': 'CalculatedSignal'}])
    >>> pull(items=items, start='2019-10-5', end='2019-10-6', grid='15min', calculation='$signal.toStep()')

    Interpolate data using the pandas.DataFrame.interpolate method with a
    second order polynomial, with the signal name as the header. Warning:
    pandas.interpolate can be considerably slower than Seeq's interpolation
    functions for large datasets, especially when using complex interpolation
    methods

    >>> search_df = pd.concat((spy.search({'ID': '6A5E44D4-C6C5-463F-827B-474AB051B2F5'}),
    >>>                        spy.search({'ID': '937449C1-16E5-4E20-AC2E-632C5CECC24B'})), ignore_index=True)
    >>> data_df = pull(search_df, grid=None, start='2019-10-5', end='2019-10-6', header='Name')
    >>> data_df.interpolate(method='quadratic')
    """
    # noinspection PyUnresolvedReferences
    _common.validate_argument_types([
        (items, 'items', (pd.DataFrame, pd.Series)),
        # Note we do not validate start/end here because pd.to_datetime will do that for us
        (grid, 'grid', str),
        (header, 'header', str),
        (group_by, 'group_by', (str, list)),
        (shape, 'shape', str),
        (capsule_properties, 'capsule_properties', list),
        (tz_convert, 'tz_convert', (str, datetime.tzinfo)),
        (calculation, 'calculation', (str, pd.DataFrame, pd.Series)),
        (bounding_values, 'bounding_values', bool),
        (errors, 'errors', str),
        (quiet, 'quiet', bool),
        (status, 'status', _common.Status)
    ])

    _login.validate_login()

    if errors == 'catalog' and status is None:
        raise ValueError("status argument must be a valid Status object when errors='catalog'")

    status = Status.validate(status, quiet)
    _common.validate_timezone_arg(tz_convert)
    _common.validate_errors_arg(errors)

    if invalid_values_as is None:
        raise ValueError('invalid_values_as cannot be None (because Pandas treats it the same as NaN)')

    if not (isinstance(items, (pd.DataFrame, pd.Series))):
        raise ValueError('items argument must be a pandas.DataFrame or pandas.Series')

    if not items.index.is_unique:
        raise ValueError("The items DataFrame's index must be unique. Use reset_index(drop=True, inplace=True) "
                         "before passing in to spy.pull().")

    if 'ID' not in items or 'Type' not in items:
        raise ValueError("items DataFrame must include ID and Type columns")

    if isinstance(calculation, pd.DataFrame):
        if len(calculation) != 1:
            raise ValueError("When applying a calculation across assets, calculation argument must be a one-row "
                             "DataFrame, or a Series. When applying a calculation to a signal/condition/scalar, "
                             'calculation must be a string with a signal variable in it: $signal, $condition or '
                             '$scalar.')

        calculation = calculation.iloc[0]

    if isinstance(items, pd.Series):
        items = pd.DataFrame().append(items)

    if shape not in ['auto', 'capsules', 'samples']:
        raise ValueError("shape must be one of 'auto', 'capsules', 'samples'")

    if capsules_as is not None:
        raise ValueError("capsules_as argument is deprecated. Use the following instead:\n"
                         "capsules_as='signal'   -> shape='samples'\n"
                         "capsules_as='capsules' -> shape='capsules'")

    if capsule_properties is not None and not isinstance(capsule_properties, list):
        raise ValueError("capsules_properties must be a list of strings (capsule property names)")

    if group_by:
        if isinstance(group_by, str):
            group_by = [group_by]
        if not isinstance(group_by, list):
            raise ValueError('group_by argument must be a str or list(str)')
        if not all(col in items.columns for col in group_by):
            raise ValueError('group_by columns %s not present in query DataFrame' % group_by)

    pd_start, pd_end = validate_start_and_end(start, end)

    if tz_convert is None:
        # Return the results in the timezone of the start date so that the timestamps tend to make sense to the user
        tz_convert = pd_start.tz

    status_columns = [c for c in ['ID', 'Path', 'Asset', 'Name'] if c in items]

    status.df = items[status_columns].copy()
    status.df['Count'] = 0
    status.df['Time'] = 0
    status.df['Result'] = 'Pulling'

    status.update('Pulling data from %s to %s' % (pd_start, pd_end), Status.RUNNING)

    query_df = items  # type: pd.DataFrame
    output_df = pd.DataFrame()
    at_least_one_signal = len(query_df[query_df['Type'].str.endswith('Signal')]) > 0
    at_least_one_asset = len(query_df[query_df['Type'].str.endswith('Asset')]) > 0
    calculation_is_signal = False

    if at_least_one_asset:
        if calculation is None or not isinstance(calculation, (pd.Series, pd.DataFrame)):
            raise RuntimeError('To pull data for an asset, you must provide a "calculation" argument whose '
                               'value is the metadata of a calculation that is based on a single asset.')

        calculation_series = calculation if isinstance(calculation, pd.Series) else calculation.iloc[0]
        calculation_is_signal = calculation_series['Type'].endswith('Signal')

    if shape == 'auto':
        shape = 'samples' if at_least_one_signal or (at_least_one_asset and calculation_is_signal) else 'capsules'

    # The lifecycle of a pull is several phases. We pull signals before conditions so that, if the conditions are
    # being represented as samples, we have timestamps to map to. Scalars are last because they need to be constant
    # for all rows, and then there is a final step where we re-organize the columns to match the input order as best
    # we can.
    phases = ['signals', 'conditions', 'scalars', 'final']
    if shape == 'capsules':
        phases.remove('signals')

    if shape == 'samples' and (not at_least_one_signal or (at_least_one_asset and not calculation_is_signal)):
        # If we're trying to pull a Condition as a Signal, we need a set of timestamps to use. So the user has to
        # specify a grid and then we create and pull a constant signal just to generate timestamps to which we'll
        # map the condition's 1s and 0s.

        if grid is None:
            raise RuntimeError(
                "Pull cannot include conditions when no signals present with shape='samples' and grid=None")

        placeholder_item_name = '__placeholder__'
        row_result = _pull_signal('0.toSignal(%s)' % grid, list(), placeholder_item_name,
                                  placeholder_item_name, pd_start, pd_end, tz_convert,
                                  threading.Event())

        output_df = row_result.result

    # This dictionary is from item ID to a list of columns, which we use during the final phase to order the columns
    # in the output DataFrame. Each type of pull adds additional entries to this dictionary.
    column_names = dict()

    # This list is assembled during the final phase by going back through all the input rows and adding columns that
    # correspond to the item IDs for those rows.
    final_column_names = list()

    for phase in phases:
        try:
            interrupt_event = threading.Event()

            # Status updates are sent from other threads on this queue, and then the queue is "drained" such that the
            # status DataFrame is updated. (It's important not to manipulate DataFrames from different threads,
            # hence the queue mechanism.)
            status_updates = queue.Queue()

            def _drain_status_updates():
                # noinspection Duplicates
                while True:
                    try:
                        _index, _message, _count, _time = status_updates.get_nowait()

                        status.df.at[_index, 'Result'] = _message
                        status.df.at[_index, 'Count'] = _count
                        status.df.at[_index, 'Time'] = _time
                    except queue.Empty:
                        break

                status.update('Pulling from <strong>%s</strong> to <strong>%s</strong>' % (pd_start, pd_end),
                              Status.RUNNING)

            with concurrent.futures.ThreadPoolExecutor(max_workers=_config.options.max_concurrent_requests) as executor:
                # This dictionary contains a map from the Future object that is returned by the ThreadPoolExecutor to
                # the row_index of the input DataFrame. We use it to wait on completions and map those completions
                # back to the corresponding row.
                to_do = dict()

                index_to_use = output_df.index
                for row_index, row in query_df.iterrows():
                    # noinspection PyBroadException
                    try:
                        if group_by and isinstance(output_df.index, pd.MultiIndex):
                            # When we're doing a group_by, then the output DataFrame may have a MultiIndex as a
                            # result of some activity that has already happened. We need to pare down the output
                            # DataFrame to the rows that should be affected by the next action, which are all the
                            # existing rows that match the current row's group_by cells.
                            index_query = ' and '.join([("%s == '%s'" % (g, row[g])) for g in group_by])
                            index_to_use = output_df.query(index_query).index.levels[0]

                        to_do.update(
                            # _process_query_row was broken out into a function mostly to regain some indentation
                            # space. It's only ever called from this spot. That's why it has a ton of parameters.
                            _process_query_row(at_least_one_signal, calculation, shape,
                                               capsule_properties, grid, header, query_df, index_to_use, row_index,
                                               pd_start, pd_end, phase, executor, status,
                                               status_updates, interrupt_event, tz_convert, bounding_values,
                                               invalid_values_as, column_names, final_column_names))

                    except BaseException:
                        if errors == 'raise':
                            raise

                        status.df.at[row_index, 'Result'] = _common.format_exception()

                # noinspection PyUnresolvedReferences
                while True:
                    try:
                        # Now we wait for all the futures to complete, breaking out every half second to drain status
                        # updates (see TimeoutError except block).
                        for future in concurrent.futures.as_completed(to_do.keys(), 0.5):
                            _drain_status_updates()
                            row_index = to_do[future]
                            del to_do[future]

                            if future.cancelled():
                                status.df.at[row_index, 'Result'] = 'Canceled'
                                continue

                            if future.exception():
                                status.df.at[row_index, 'Result'] = str(future.exception())
                                if errors == 'raise':
                                    raise future.exception()
                                else:
                                    continue

                            row_result = future.result()  # type: RowResult
                            item_row = query_df.loc[row_result.row_index]
                            join_df = row_result.result
                            column_names.update(row_result.column_names)
                            if shape == 'samples':
                                if group_by is None:
                                    item_name = join_df.columns[0]
                                    if item_name in output_df.columns:
                                        raise RuntimeError(
                                            'Column headers not unique. 2+ instances of "%s" found. Use header="ID" '
                                            'to guarantee uniqueness, or alternatively try group_by=["Path", "Asset"] '
                                            'if you are using an asset tree.' % item_name)
                                else:
                                    for group_column in group_by:
                                        join_df[group_column] = item_row[group_column]

                                    join_df.set_index(group_by, inplace=True, append=True)

                            if len(output_df) == 0:
                                existing_columns = output_df.columns
                                output_df = join_df
                                for existing_column in existing_columns:
                                    output_df[existing_column] = np.nan
                            else:
                                if shape == 'capsules':
                                    # When the shape of the output is capsules, it's effectively just a long
                                    # DataFrame with all of the results appended one after the other. The user can
                                    # then choose to sort by one of the columns if they would like.
                                    output_df = output_df.append(join_df)
                                else:
                                    # combine_first has the effect of adding the set of columns from join_df and
                                    # merging the indices, adding NaNs anywhere there are cells from one DataFrame
                                    # that don't match an index entry from another.
                                    output_df = output_df.combine_first(join_df)

                        # We got all the way through the iterator without encountering a TimeoutError, so break
                        break

                    except KeyboardInterrupt:
                        interrupt_event.set()
                        for future in to_do.keys():
                            future.cancel()
                        raise
                    except concurrent.futures.TimeoutError:
                        _drain_status_updates()

        except BaseException as e:
            status.exception(e)

            if isinstance(e, KeyboardInterrupt):
                return None

            raise

    status.update('Pull successful from <strong>%s</strong> to <strong>%s</strong>' % (pd_start, pd_end),
                  Status.SUCCESS)

    # Ensures that the order of the columns matches the order in the metadata
    output_df = output_df[final_column_names]

    return output_df


def validate_start_and_end(start, end):
    # noinspection PyUnresolvedReferences
    pd_start = pd.to_datetime(start)  # type: pd.Timestamp
    # noinspection PyUnresolvedReferences
    pd_end = pd.to_datetime(end)  # type: pd.Timestamp
    if pd_end is None:
        if pd_start is not None:
            pd_end = pd.to_datetime(pd.datetime.now(tz=pd_start.tz))
        else:
            pd_end = pd.to_datetime(pd.datetime.now())

        if pd_start is not None and pd_start > pd_end:
            # noinspection PyTypeChecker
            pd_end = pd_start + pd.Timedelta(hours=1)

    if pd_start is None:
        if pd_end is not None:
            pd_start = pd_end
        else:
            pd_start = pd.to_datetime(pd.datetime.now())
        pd_start = pd_start - pd.Timedelta(hours=1)

    # Assign the local timezone, otherwise it gets very confusing as to what's being returned.
    if pd_start.tz is None:
        pd_start = pd_start.tz_localize(tzlocal.get_localzone())
    if pd_end.tz is None:
        pd_end = pd_end.tz_localize(tzlocal.get_localzone())

    return pd_start, pd_end


def _process_query_row(at_least_one_signal, calculation, shape, capsule_properties, grid, header, query_df,
                       index_to_use, row_index, pd_start, pd_end, phase, executor, status, status_updates,
                       interrupt_event, tz_convert, bounding_values, invalid_values_as, column_names,
                       final_column_names):
    # _process_query_row was broken out into a function mostly to regain some indentation
    # space from the main pull() function. It's only ever called from one spot. That's why it has a ton of parameters.

    items_api = ItemsApi(_login.client)

    row = query_df.loc[row_index]
    to_do = dict()

    if phase == 'signals' and not _common.present(row, 'ID'):
        status.df.at[row_index, 'Result'] = 'No "ID" column - skipping'
        return to_do

    item_id, item_name, item_type = _get_item_details(header, row)

    calculation_to_use = calculation
    if item_type == 'Asset':
        # If we're pulling assets, then we're actually pulling a calculated item (signal, condition or scalar) that
        # has been swapped to that asset. So use the swap API to find the appropriate item and then use that item's
        # ID instead of the asset's ID. Everything else just works the same as if the user had specified the swap
        # item directly.
        swap_input = SwapInputV1()
        swap_input.swap_in = item_id
        calc_item_id, _, item_type = _get_item_details(header, calculation)

        item_dependency_output = items_api.get_formula_dependencies(
            id=calc_item_id)  # type: ItemDependencyOutputV1

        unique_assets = set(dep.ancestors[-1].id
                            for dep in item_dependency_output.dependencies
                            if len(dep.ancestors) > 0)

        if len(unique_assets) != 1:
            raise RuntimeError('To pull data for an asset, the "calculate" parameter must be a calculated '
                               'item that involves only one asset.')

        swap_input.swap_out = unique_assets.pop()

        swapped_item = items_api.find_swap(id=calc_item_id, body=[swap_input])  # type: ItemPreviewV1

        item_id = swapped_item.id

        # Don't try to apply a calculation later, we've already done it via our swap activity
        calculation_to_use = None

    if phase == 'signals' and \
            'Signal' not in item_type and 'Condition' not in item_type and 'Scalar' not in item_type:
        status.df.at[row_index, 'Result'] = 'Not a Signal, Condition or Scalar - skipping'
        return to_do

    if phase == 'signals' and 'Signal' in item_type:
        parameters = ['signal=%s' % item_id]
        if calculation_to_use is not None:
            formula = calculation_to_use
        else:
            formula = '$signal'

        if grid:
            formula = 'resample(%s, %s)' % (formula, grid)

        to_do[executor.submit(_pull_signal, formula, parameters, item_id, item_name, pd_start, pd_end, tz_convert,
                              interrupt_event, status_updates, row_index, bounding_values,
                              invalid_values_as)] = row_index

    elif phase == 'conditions' and 'Condition' in item_type:
        to_do[executor.submit(_pull_condition, shape, capsule_properties, calculation_to_use, item_id,
                              item_name, header, pd_start, pd_end, tz_convert,
                              row_index, index_to_use, query_df, at_least_one_signal, status_updates,
                              interrupt_event)] = row_index

    elif phase == 'scalars' and 'Scalar' in item_type:
        parameters = ['scalar=%s' % item_id]
        if calculation_to_use is not None:
            formula = calculation_to_use
        else:
            formula = '$scalar'

        to_do[executor.submit(_pull_scalar, formula, parameters, row_index, item_id, item_name, index_to_use,
                              invalid_values_as, status_updates)] = row_index

    elif phase == 'final':
        # Iterate over all the column names that the _pull_xxxx functions added to the DataFrame and put them in an
        # ordered list. This code forces the output DataFrame to be consistent even if the timing of completions is
        # different from run to run.
        if item_id in column_names:
            for column_name in column_names[item_id]:
                if column_name not in final_column_names:
                    final_column_names.append(column_name)

    return to_do


def _convert_column_timezone(ts_column, tz):
    ts_column = ts_column.tz_localize('UTC')
    return ts_column.tz_convert(tz) if tz else ts_column


def _pull_condition(shape, capsule_properties, calculation_to_use, item_id, item_name, header,
                    pd_start, pd_end, tz, row_index, index_to_use, query_df,
                    at_least_one_signal, status_updates, interrupt_event):
    result_df = pd.DataFrame(index=index_to_use)
    column_names = dict()

    # noinspection PyBroadException
    timer = _common.timer_start()
    capsule_count = 0
    current_start = pd_start.value
    offset = 0
    while not interrupt_event.is_set():
        # There are two ways we can retrieve capsules: via the Table Builder API or via the Formula API. They each
        # have advantages/disadvantages. When using the Table Builder API, we can efficiently retrieve capsule
        # statistics for a signal just like what is done in Seeq Workbench's Capsule Pane. However, we must manually
        # specify which capsule properties we want to retrieve. When using the Formula API, we can retrieve all
        # properties for a capsule "for free". So we use the former when we have to retrieve capsule summary
        # statistics for a signal, but otherwise use the Formula API.
        if shape == 'capsules' and at_least_one_signal:
            if calculation_to_use is not None:
                raise RuntimeError("If shape='capsules' and at least one signal is present, calculation "
                                   "argument cannot be supplied")

            this_capsule_count, next_start, result_df = _pull_condition_via_table_builder_api(
                capsule_properties, current_start, query_df, item_id, item_name, header, offset, pd_end, tz,
                result_df, column_names, status_updates)
        else:
            this_capsule_count, next_start, result_df = _pull_condition_via_formula_api(
                calculation_to_use, shape, capsule_properties, current_start,
                index_to_use, item_id, item_name, offset, pd_end, tz, result_df, column_names)

        # Note that capsule_count here can diverge from the exact count in the output due to pagination
        capsule_count += this_capsule_count

        if this_capsule_count < _config.options.pull_page_size:
            break

        if next_start == current_start:
            # This can happen if the page is full of capsules that all have the same start time
            offset += _config.options.pull_page_size
        else:
            offset = 0

        current_start = next_start

        status_updates.put((row_index, 'Pulling %s' % _common.convert_to_timestamp(current_start, tz), capsule_count,
                            _common.timer_elapsed(timer)))

    status_updates.put((row_index, 'Success', capsule_count, _common.timer_elapsed(timer)))

    return RowResult(row_index, column_names, result_df)


def _is_capsule_dupe(result_df, item_name, pd_capsule_start, pd_capsule_end):
    return 'Condition' in result_df and \
           'Capsule Start' in result_df and \
           'Capsule End' in result_df and \
           len(result_df.loc[(result_df['Condition'] == item_name) &
                             (result_df['Capsule Start'] == pd_capsule_start) &
                             (result_df['Capsule End'] == pd_capsule_end)])


def _pull_condition_via_formula_api(calculation_to_use, shape, capsule_properties, current_start,
                                    index_to_use, item_id, item_name, offset, pd_end, tz, result_df,
                                    column_names):
    formulas_api = FormulasApi(_login.client)
    parameters = ['condition=%s' % item_id]
    if calculation_to_use is not None:
        formula = calculation_to_use
    else:
        formula = '$condition'

    formula_run_output, _, http_headers = formulas_api.run_formula_with_http_info(
        formula=formula,
        parameters=parameters,
        start='%d ns' % current_start,
        end='%d ns' % pd_end.value,
        offset=offset,
        limit=_config.options.pull_page_size)  # type: FormulaRunOutputV1

    next_start = current_start
    capsules_output = formula_run_output.capsules  # type: CapsulesOutputV1
    check_for_dupes = True
    columns = dict()
    if shape == 'samples':
        # In this case, we are creating a signal-like representation of the condition using 0s and 1s, just like the
        # Excel and OData exports.

        columns[item_name] = pd.Series(0, index_to_use)
        for capsule in capsules_output.capsules:
            pd_capsule_start = _common.convert_to_timestamp(
                capsule.start if capsule.start is not None else 0, tz)
            pd_capsule_end = _common.convert_to_timestamp(
                capsule.end if capsule.end is not None else 7258118400000000000, tz)

            # Mark Derbecker 2019-12-17:
            # I've tried a few ways of making this happen and so far this method seems to be the most efficient: Start
            # with a Series full of zeros (but with the index that corresponds to the already-existing output
            # DataFrame) and use the Series.loc[] indexer to set the values to one if they're within the capsule
            # boundary.
            columns[item_name].loc[(columns[item_name].index >= pd_capsule_start) &
                                   (columns[item_name].index <= pd_capsule_end)] = 1

            for prop in capsule.properties:  # type: ScalarPropertyV1
                # We need to create a column name that is unique for the item / property combination
                colname = '%s - %s' % (item_name, prop.name)
                if colname not in columns:
                    # Here we start with a NaN-filled series, since we're populating property values (not 1s and 0s).
                    columns[colname] = pd.Series(np.nan, index_to_use)

                # Note here that overlapping capsules with different properties will result in "last one wins"
                columns[colname].loc[(columns[colname].index >= pd_capsule_start) &
                                     (columns[colname].index <= pd_capsule_end)] = prop.value

        column_names[item_id] = list()
        for col, series in columns.items():
            result_df[col] = series
            column_names[item_id].append(col)
    else:
        # In this case, we're creating a more straightforward table where each capsule is a row, complete with item
        # properties.

        capsule_df_rows = list()

        for capsule in capsules_output.capsules:  # type: CapsuleV1
            column_names[item_id] = ['Condition', 'Capsule Start', 'Capsule End', 'Capsule Is Uncertain']
            pd_capsule_start = _common.convert_to_timestamp(capsule.start, tz)
            pd_capsule_end = _common.convert_to_timestamp(capsule.end, tz)
            if check_for_dupes and _is_capsule_dupe(result_df, item_name, pd_capsule_start, pd_capsule_end):
                # This can happen as a result of pagination
                continue

            check_for_dupes = False

            capsule_dict = {
                'Condition': item_name,
                'Capsule Start': pd_capsule_start,
                'Capsule End': pd_capsule_end,
                'Capsule Is Uncertain': bool(capsule.is_uncertain)
            }

            for prop in capsule.properties:  # type: ScalarPropertyV1
                if capsule_properties is not None and prop.name not in capsule_properties:
                    continue

                capsule_dict[prop.name] = prop.value
                column_names[item_id].append(prop.name)

            capsule_df_rows.append(capsule_dict)

            if not pd.isna(capsule.start) and capsule.start > next_start:
                next_start = capsule.start

        result_df = result_df.append(capsule_df_rows) if len(result_df) != 0 else pd.DataFrame(capsule_df_rows)

    return len(capsules_output.capsules), next_start, result_df


def _pull_condition_via_table_builder_api(capsule_properties, current_start, query_df, item_id, item_name,
                                          header, offset, pd_end, tz, result_df, column_names, status_updates):
    tables_api = TablesApi(_login.client)

    column_definitions = dict()

    if capsule_properties:
        column_definitions.update({
            cp: '$capsule.getProperty("%s")' % cp for cp in capsule_properties
        })

    signals_df = query_df[query_df['Type'].str.endswith('Signal')]
    for signal_index, signal_row in signals_df.iterrows():
        signal_item_id, signal_item_name, signal_item_type = _get_item_details(header, signal_row)

        statistic = signal_row['Statistic'] if 'Statistic' in signal_row else 'average'
        function = _common.statistic_to_aggregation_function(statistic, allow_condition_stats=False)

        # This construction is the same as what the front-end code does for populating the Capsules Pane
        formula = '$series.%s($capsule) on %s' % (function, signal_item_id.lower())
        column_definitions['%s (%s)' % (signal_item_name, string.capwords(statistic))] = formula

        # We're dealing with the signal by virtue of including it in this table builder call. So just put Success in
        # the status table so that things look right to the user.
        status_updates.put((signal_index, 'Success', None, None))

    table_output = tables_api.build(
        start='%d ns' % current_start,
        end='%d ns' % pd_end.value,
        condition_ids=[item_id],
        column_definitions=list(column_definitions.values()),
        offset=offset,
        limit=_config.options.pull_page_size
    )  # type: TableOutputV1

    # Construct a dictionary to map column names to column indices
    h = {table_output.header[i]: i for i in range(len(table_output.header))}

    next_start = current_start
    table_matrix = table_output.table  # type: list
    check_for_dupes = True

    capsule_df_rows = list()

    for row in table_matrix:
        column_names[item_id] = ['Condition', 'Capsule Start', 'Capsule End', 'Capsule Is Uncertain']
        pd_capsule_start = _common.convert_to_timestamp(row[h['Start']], tz)
        pd_capsule_end = _common.convert_to_timestamp(row[h['End']], tz)
        if check_for_dupes and _is_capsule_dupe(result_df, item_name, pd_capsule_start, pd_capsule_end):
            # This can happen as a result of pagination
            continue

        check_for_dupes = False

        capsule_dict = {
            'Condition': item_name,
            'Capsule Start': pd_capsule_start,
            'Capsule End': pd_capsule_end,
            'Capsule Is Uncertain': row[h['Is Uncertain']]
        }

        for prop_name, column_header in column_definitions.items():
            capsule_dict[prop_name] = row[h[column_header]]
            column_names[item_id].append(prop_name)

        capsule_df_rows.append(capsule_dict)

        if not pd.isna(row[h['Start']]) and row[h['Start']] > next_start:
            next_start = row[h['Start']]

    result_df = result_df.append(capsule_df_rows) if len(result_df) != 0 else pd.DataFrame(capsule_df_rows)

    return len(table_output.table), next_start, result_df


def _pull_signal(formula, parameters, item_id, item_name, pd_start, pd_end, tz,
                 interrupt_event, status_updates=None, row_index=None, bounding_values=False, invalid_values_as=np.nan):
    formulas_api = FormulasApi(_login.client)

    # noinspection PyBroadException
    series = pd.Series()
    timer = _common.timer_start()
    current_start = pd_start
    last_key = 0
    while not interrupt_event.is_set():
        start_string = '%d ns' % current_start.value
        end_string = '%d ns' % pd_end.value
        formula_run_output, status_code, http_headers = formulas_api.run_formula_with_http_info(
            formula=formula,
            parameters=parameters,
            start=start_string,
            end=end_string,
            offset=0,
            limit=_config.options.pull_page_size)  # type: FormulaRunOutputV1

        if formula_run_output.samples is None:
            # noinspection PyStringFormat
            raise RuntimeError('formula_run_output.samples is None.\n'
                               'status_code: %d\nformula: %s\nparameters: %s\n'
                               'start: %s\nend:%s\n'
                               'formula_run_output:\n%s' %
                               (status_code, formula, parameters,
                                start_string, end_string,
                                formula_run_output.__repr__()))

        series_samples_output = formula_run_output.samples  # type: SeriesSamplesOutputV1

        def _keep_sample(_sample_output):
            if _sample_output.key <= last_key:
                return False

            if bounding_values:
                return True

            if _sample_output.key < pd_start.value:
                return False

            if _sample_output.key > pd_end.value:
                return False

            return True

        # Filter out the samples before breaking them into timestamps/values lists. This is the fastest.
        # https://bitbucket.org/seeq12/crab/pull-requests/8872/latest-pypi-changes-up-to-seeq-module-v133/diff#comment-134308908
        filtered_samples = [sample_output for sample_output in series_samples_output.samples if
                            _keep_sample(sample_output)]
        timestamps = [sample.key for sample in filtered_samples]
        values = [sample.value for sample in filtered_samples]

        time_index = _convert_column_timezone(pd.DatetimeIndex(timestamps), tz)

        series = series.append(pd.Series(values, index=time_index))

        if len(series_samples_output.samples) < _config.options.pull_page_size:
            break

        if len(series) > 0:
            last_key = series.index[-1].value

        if time_index[-1].value > current_start.value:
            current_start = time_index[-1]

        if status_updates is not None:
            status_updates.put(
                (row_index, 'Pulling: %s' % str(current_start), len(series), _common.timer_elapsed(timer)))

    if not pd.isna(invalid_values_as):
        series = series.fillna(invalid_values_as)

    if status_updates is not None:
        status_updates.put((row_index, 'Success', len(series), _common.timer_elapsed(timer)))

    return RowResult(row_index, {item_id: [item_name]}, pd.DataFrame({item_name: series}))


def _pull_scalar(formula, parameters, row_index, item_id, item_name, index_to_use, invalid_values_as, status_updates):
    formulas_api = FormulasApi(_login.client)
    timer = _common.timer_start()

    formula_run_output, _, http_headers = formulas_api.run_formula_with_http_info(
        formula=formula,
        parameters=parameters)  # type: FormulaRunOutputV1

    status_updates.put((row_index, 'Success', 1, _common.timer_elapsed(timer)))

    if len(index_to_use) == 0:
        index_to_use = pd.Series([0])

    result_df = pd.DataFrame(index=index_to_use)
    value = invalid_values_as if formula_run_output.scalar.value is None else formula_run_output.scalar.value
    result_df[item_name] = value
    return RowResult(row_index, {item_id: [item_name]}, result_df)


class RowResult:
    def __init__(self, row_index, column_names, result):
        self.row_index = row_index
        self.column_names = column_names
        self.result = result


def _get_item_details(header, row):
    # This is a somewhat complex function that tries its best to pick a column header (item_name) for the output
    # DataFrame by either honoring the user's "header" argument or auto-picking something that makes sense.

    items_api = ItemsApi(_login.client)

    item_id = _common.get(row, 'ID')

    # noinspection PyTypeChecker
    item = None

    if _common.present(row, 'Type'):
        item_type = _common.get(row, 'Type')
    else:
        item = items_api.get_item_and_all_properties(id=item_id)  # type: ItemOutputV1
        item_type = item.type

    if header.upper() == 'ID':
        item_name = item_id
    elif _common.present(row, header):
        item_name = _common.get(row, header)
    else:
        if not item:
            item = items_api.get_item_and_all_properties(id=item_id)  # type: ItemOutputV1

        item_name = ''
        if header == '__auto__' and _common.present(row, 'Path'):
            item_name = _common.get(row, 'Path') + ' >> '
            if _common.present(row, 'Asset'):
                item_name += _common.get(row, 'Asset') + ' >> '

        if header in ['__auto__', 'Name']:
            item_name += item.name
        elif header == 'Description':
            item_name += item.description
        else:
            prop = [p.value for p in item.properties if p.name == header]
            if len(prop) == 0:
                raise ValueError(f'header argument invalid: Property "{header}" not found')
            else:
                item_name += prop[0]

    return item_id, item_name, item_type
