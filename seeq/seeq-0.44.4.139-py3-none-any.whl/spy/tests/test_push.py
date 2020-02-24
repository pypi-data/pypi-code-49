import os
import pytest
import pytz
import re

import pandas as pd
import numpy as np

from seeq import spy
from seeq.sdk import *
from seeq.sdk.rest import ApiException

from . import test_common
from .. import _login


def setup_module():
    test_common.login()


@pytest.mark.system
def test_push_to_workbook():
    spy.push(metadata=pd.DataFrame([{
        'Type': 'Signal',
        'Name': 'test_push_to_workbook'
    }]), workbook='test_push_to_workbook >> My Workbook!', worksheet='My Worksheet!')

    search_df = spy.workbooks.search({'Path': 'test_push_to_workbook'})

    assert len(search_df) == 1
    assert search_df.iloc[0]['Name'] == 'My Workbook!'

    workbooks = spy.workbooks.pull(search_df, include_inventory=False)

    assert len(workbooks) == 1
    workbook = workbooks[0]
    assert workbook['Name'] == 'My Workbook!'
    assert len(workbook.worksheets) == 1
    assert workbook.worksheets[0].name == 'My Worksheet!'


@pytest.mark.system
def test_push_signal():
    data_df = pd.DataFrame()

    data_df['Numeric'] = pd.Series([
        1,
        'invalid',
        3,
        None
    ], index=[
        pd.to_datetime('2019-01-01'),
        pd.to_datetime('2019-01-02'),
        pd.to_datetime('2019-01-03'),
        pd.to_datetime('2019-01-04')
    ])

    data_df['String'] = pd.Series([
        'ON',
        'OFF',
        None,
        np.nan,
        np.nan
    ], index=[
        pd.to_datetime('2019-01-01'),
        pd.to_datetime('2019-01-02'),
        pd.to_datetime('2019-01-03'),
        pd.to_datetime('2019-01-04'),
        pd.to_datetime('2019-01-05')  # This timestamp won't show up in the pull
    ])

    with pytest.raises(
            RuntimeError,
            match=re.escape('Column "Numeric" was detected as numeric-valued, but string '
                            'value at (2019-01-02 00:00:00, invalid)')):
        spy.push(data_df)

    push_df = spy.push(data_df, type_mismatches='invalid')

    search_df = spy.search(push_df)

    assert search_df[search_df['Name'] == 'Numeric'].iloc[0]['Value Unit Of Measure'] == ''
    assert search_df[search_df['Name'] == 'String'].iloc[0]['Value Unit Of Measure'] == 'string'

    pull_df = spy.pull(push_df, start='2019-01-01T00:00:00Z', end='2019-01-05T00:00:00Z', grid=None)

    assert len(pull_df) == 4

    assert pull_df.at[pd.to_datetime('2019-01-01'), 'Numeric'] == 1
    assert pd.isna(pull_df.at[pd.to_datetime('2019-01-02'), 'Numeric'])
    assert pull_df.at[pd.to_datetime('2019-01-03'), 'Numeric'] == 3
    assert pd.isna(pull_df.at[pd.to_datetime('2019-01-04'), 'Numeric'])

    assert pull_df.at[pd.to_datetime('2019-01-01'), 'String'] == 'ON'
    assert pull_df.at[pd.to_datetime('2019-01-02'), 'String'] == 'OFF'
    assert pull_df.at[pd.to_datetime('2019-01-03'), 'String'] is None
    assert pd.isna(pull_df.at[pd.to_datetime('2019-01-04'), 'String'])

    with pytest.raises(ValueError,
                       match=re.escape('invalid_values_as cannot be None (because Pandas treats it the same as NaN)')):
        spy.pull(push_df, start='2019-01-01T00:00:00Z', end='2019-01-05T00:00:00Z', grid=None, invalid_values_as=None)

    pull_df = spy.pull(push_df, start='2019-01-01T00:00:00Z', end='2019-01-05T00:00:00Z', grid=None,
                       invalid_values_as='INVALID')

    assert pull_df.at[pd.to_datetime('2019-01-01'), 'Numeric'] == 1
    assert pull_df.at[pd.to_datetime('2019-01-02'), 'Numeric'] == 'INVALID'
    assert pull_df.at[pd.to_datetime('2019-01-03'), 'Numeric'] == 3
    assert pull_df.at[pd.to_datetime('2019-01-04'), 'Numeric'] == 'INVALID'

    assert pull_df.at[pd.to_datetime('2019-01-01'), 'String'] == 'ON'
    assert pull_df.at[pd.to_datetime('2019-01-02'), 'String'] == 'OFF'
    assert pull_df.at[pd.to_datetime('2019-01-03'), 'String'] == 'INVALID'
    assert pd.isna(pull_df.at[pd.to_datetime('2019-01-04'), 'String'])

    pull_df = spy.pull(push_df, start='2019-01-01T00:00:00Z', end='2019-01-05T00:00:00Z', grid=None,
                       invalid_values_as=-999)

    assert pull_df.at[pd.to_datetime('2019-01-01'), 'Numeric'] == 1
    assert pull_df.at[pd.to_datetime('2019-01-02'), 'Numeric'] == -999
    assert pull_df.at[pd.to_datetime('2019-01-03'), 'Numeric'] == 3
    assert pull_df.at[pd.to_datetime('2019-01-04'), 'Numeric'] == -999

    assert pull_df.at[pd.to_datetime('2019-01-01'), 'String'] == 'ON'
    assert pull_df.at[pd.to_datetime('2019-01-02'), 'String'] == 'OFF'
    assert pull_df.at[pd.to_datetime('2019-01-03'), 'String'] == -999
    assert pd.isna(pull_df.at[pd.to_datetime('2019-01-04'), 'String'])


@pytest.mark.system
def test_push_from_csv():
    csv_file = pd.read_csv(
        os.path.join(os.path.dirname(__file__), '..', 'docs', 'Documentation', 'csv_import_example.csv'),
        parse_dates=['TIME(unitless)'],
        index_col='TIME(unitless)')

    spy.options.push_page_size = 5000
    spy.options.max_concurrent_requests = 2

    fewer_signals = csv_file.iloc[:, :-4]

    push_results = spy.push(data=fewer_signals)

    start = pd.to_datetime('2018-07-25T23:31:01.0000000-06:00')
    end = pd.to_datetime('2018-07-25T23:31:07.0000000-06:00')
    expected_df = fewer_signals.loc[start:end]

    pull_df = spy.pull(push_results, start=start, end=end, grid=None, tz_convert=pytz.FixedOffset(-360))
    pull_df.index.name = 'TIME(unitless)'

    assert pull_df.equals(expected_df)


@pytest.mark.system
def test_bad_calculation():
    with pytest.raises(RuntimeError):
        spy.push(metadata=pd.DataFrame([{
            'Type': 'Signal',
            'Name': 'Bad Calc',
            'Formula': 'hey(nothing)'
        }]))


@pytest.mark.system
def test_push_calculated_signal():
    area_a_signals = spy.search({
        'Path': 'Example >> Cooling Tower 1 >> Area A'
    })

    dew_point_calc = spy.push(metadata=pd.DataFrame([{
        'Type': 'Signal',
        'Name': 'Dew Point',
        # From https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html
        'Formula': "$T - ((100 - $RH.setUnits(''))/5)",
        'Formula Parameters': {
            '$T': area_a_signals[area_a_signals['Name'] == 'Temperature'],
            '$RH': area_a_signals[area_a_signals['Name'] == 'Relative Humidity']
        }
    }]))

    assert len(dew_point_calc) == 1
    assert 'ID' in dew_point_calc


@pytest.mark.system
def test_push_scalar():
    metadata = pd.DataFrame([{
        'Type': 'Scalar',
        'Name': 'Negative Number',
        'Formula': np.int64(-12)
    }])

    push_df = spy.push(metadata=metadata)

    search_df = spy.search(push_df, all_properties=True)
    assert search_df.iloc[0]['Formula'] == '-12'

    pull_df = spy.pull(push_df)
    assert pull_df.iloc[0]['Negative Number'] == -12


@pytest.mark.system
def test_edit_existing_calculated_items():
    signals_api = SignalsApi(_login.client)
    conditions_api = ConditionsApi(_login.client)
    scalars_api = ScalarsApi(_login.client)

    area_a_signals = spy.search({
        'Path': 'Example >> Cooling Tower 1 >> Area A'
    })

    formula_parameters = [
        'RH=%s' % area_a_signals[area_a_signals['Name'] == 'Relative Humidity'].iloc[0]['ID'],
        'T=%s' % area_a_signals[area_a_signals['Name'] == 'Temperature'].iloc[0]['ID']
    ]

    # Create a signal, condition and scalar that we will later edit

    signal_input = SignalInputV1()
    signal_input.name = 'test_alter_existing_items Signal'
    signal_input.formula = "$T - ((100 - $RH.setUnits(''))/5)"
    signal_input.formula_parameters = formula_parameters
    signal_output = signals_api.create_signal(body=signal_input)  # type: SignalOutputV1

    condition_input = ConditionInputV1()
    condition_input.name = 'test_alter_existing_items Condition'
    condition_input.formula = "$T.valueSearch(isLessThan(80)).union($RH.valueSearch(isLessThan(40)))"
    condition_input.parameters = formula_parameters
    condition_output = conditions_api.create_condition(body=condition_input)  # type: ConditionOutputV1

    scalar_input = CalculatedItemInputV1()
    scalar_input.name = 'test_alter_existing_items Scalar'
    scalar_input.formula = "$T.average(capsule('2016-12-18')) + $RH.average(capsule('2016-12-18'))"
    scalar_input.parameters = formula_parameters
    scalar_output = scalars_api.create_calculated_scalar(body=scalar_input)  # type: CalculatedItemOutputV1

    created_items = spy.search(pd.DataFrame([{'ID': signal_output.id},
                                             {'ID': condition_output.id},
                                             {'ID': scalar_output.id}]),
                               all_properties=True)

    assert created_items.iloc[0]['Formula'] == "$T - ((100 - $RH.setUnits(''))/5)"
    assert sorted(created_items.iloc[0]['Formula Parameters']) == formula_parameters
    assert created_items.iloc[1]['Formula'] == "$T.valueSearch(isLessThan(80)).union($RH.valueSearch(isLessThan(40)))"
    assert sorted(created_items.iloc[1]['Formula Parameters']) == formula_parameters
    assert created_items.iloc[2]['Formula'] == "$T.average(capsule('2016-12-18')) + $RH.average(capsule('2016-12-18'))"
    assert sorted(created_items.iloc[2]['Formula Parameters']) == formula_parameters

    # Edit them by just changing values in the DataFrame, then push

    created_items.at[0, 'Formula'] = '$T + 100'
    created_items.at[1, 'Formula'] = 'weekends()'
    created_items.at[2, 'Formula'] = '10kW'

    push_df = spy.push(metadata=created_items)

    assert push_df.iloc[0]['ID'] == signal_output.id
    assert push_df.iloc[1]['ID'] == condition_output.id
    assert push_df.iloc[2]['ID'] == scalar_output.id

    pushed_signal = spy.search(pd.DataFrame([{'ID': signal_output.id},
                                             {'ID': condition_output.id},
                                             {'ID': scalar_output.id}]),
                               all_properties=True)

    assert pushed_signal.iloc[0]['Formula'] == '$T + 100'
    assert pushed_signal.iloc[0]['Formula Parameters'] == [formula_parameters[1]]
    assert pushed_signal.iloc[1]['Formula'] == 'weekends()'
    assert pushed_signal.iloc[1]['Formula Parameters'] == []
    assert pushed_signal.iloc[2]['Formula'] == '10kW'
    assert pushed_signal.iloc[2]['Formula Parameters'] == []


@pytest.mark.system
def test_push_signal_with_metadata():
    witsml_folder = os.path.dirname(__file__)
    witsml_file = '011_02_0.csv'
    witsml_df = pd.read_csv(os.path.join(witsml_folder, witsml_file))
    timestamp_column = witsml_df.columns[0]
    witsml_df = pd.read_csv(os.path.join(witsml_folder, witsml_file), parse_dates=[timestamp_column])
    witsml_df = witsml_df.drop(list(witsml_df.filter(regex='.*Unnamed.*')), axis=1)
    witsml_df = witsml_df.dropna(axis=1, how='all')
    witsml_df = witsml_df.set_index(timestamp_column)

    metadata = pd.DataFrame({'Header': witsml_df.columns.values})
    metadata['Type'] = 'Signal'
    metadata['Tag'] = metadata['Header'].str.extract(r'(.*)\(')
    metadata['Value Unit Of Measure'] = metadata['Header'].str.extract(r'\((.*)\)')
    metadata['File'] = witsml_file
    metadata['Well Number'] = metadata['File'].str.extract(r'(\d+)_\d+_\d+\.csv')
    metadata['Wellbore ID'] = metadata['File'].str.extract(r'\d+_(\d+)_\d+\.csv')

    metadata = metadata.set_index('Header')

    # Without a Name column, we expect the push metadata to fail
    with pytest.raises(RuntimeError):
        spy.push(data=witsml_df, metadata=metadata)

    metadata['Name'] = "Well_" + metadata['Well Number'] + "_" + "Wellbore_" + \
                       metadata['Wellbore ID'] + "_" + metadata['Tag']

    push_results_df = spy.push(data=witsml_df, metadata=metadata, workbook=None)

    search_results_df = spy.search(push_results_df.iloc[0], workbook=None)

    assert len(search_results_df) == 1
    assert search_results_df.iloc[0]['Name'] == metadata.iloc[0]['Name']
    assert 'Push Result' not in search_results_df
    assert 'Push Count' not in search_results_df
    assert 'Push Time' not in search_results_df

    pull_results_df = spy.pull(search_results_df,
                               start='2016-07-25T15:00:00.000-07:00',
                               end='2019-07-25T17:00:00.000-07:00',
                               grid=None)

    assert len(pull_results_df) == 999

    # noinspection PyUnresolvedReferences
    assert (witsml_df.index == pull_results_df.index).all()

    witsml_list = witsml_df['BITDEP(ft)'].tolist()
    pull_list = pull_results_df['Well_011_Wellbore_02_BITDEP'].tolist()
    assert witsml_list == pull_list


@pytest.mark.system
def test_push_capsules():
    capsule_data = pd.DataFrame([{
        'Capsule Start': pd.to_datetime('2019-01-10T09:00:00.000Z'),
        'Capsule End': pd.to_datetime('2019-01-10T17:00:00.000Z'),
        'Operator On Duty': 'Mark'
    }, {
        'Capsule Start': pd.to_datetime('2019-01-11T09:00:00.000Z'),
        'Capsule End': pd.to_datetime('2019-01-11T17:00:00.000Z'),
        'Operator On Duty': 'Hedwig'
    }])

    try:
        spy.push(data=capsule_data,
                 metadata=pd.DataFrame([{
                     'Name': 'Operator Shifts',
                     'Type': 'Condition'
                 }]))

        assert False, 'Without a Maximum Duration, we expect the push to fail'

    except RuntimeError as e:
        assert 'Maximum Duration' in str(e)

    push_result = spy.push(data=capsule_data,
                           metadata=pd.DataFrame([{
                               'Name': 'Operator Shifts',
                               'Type': 'Condition',
                               'Maximum Duration': '2d'
                           }]))

    assert len(push_result) == 1
    assert push_result.iloc[0]['Name'] == 'Operator Shifts'
    assert push_result.iloc[0]['Push Count'] == 2

    pull_result = spy.pull(push_result, start='2019-01-01T09:00:00.000Z', end='2019-02-01T09:00:00.000Z')

    assert len(pull_result) == 2
    assert pull_result.iloc[0]['Condition'] == 'Operator Shifts'
    assert pull_result.iloc[0]['Capsule Start'] == pd.to_datetime('2019-01-10T09:00:00.000Z')
    assert pull_result.iloc[0]['Capsule End'] == pd.to_datetime('2019-01-10T17:00:00.000Z')
    assert pull_result.iloc[0]['Operator On Duty'] == 'Mark'
    assert pull_result.iloc[1]['Condition'] == 'Operator Shifts'
    assert pull_result.iloc[1]['Capsule Start'] == pd.to_datetime('2019-01-11T09:00:00.000Z')
    assert pull_result.iloc[1]['Capsule End'] == pd.to_datetime('2019-01-11T17:00:00.000Z')
    assert pull_result.iloc[1]['Operator On Duty'] == 'Hedwig'


@pytest.mark.system
def test_push_threshold_metric_metadata():
    signals_for_testing = spy.search({
        'Path': 'Example >> Cooling Tower 1 >> Area A'
    })

    # test an expected successful push
    test_dict = {'Type': 'Threshold Metric',
                 'Name': 'push test threshold metric',
                 'Measured Item': signals_for_testing[signals_for_testing['Name'] == 'Temperature']['ID'].iloc[0],
                 'Thresholds': [{'Lo': signals_for_testing[signals_for_testing['Name'] == 'Wet Bulb']['ID'].iloc[0],
                                 '3': 90}]
                 }
    test_metadata = pd.DataFrame(test_dict)

    push_output = spy.push(metadata=test_metadata)

    metrics_api = MetricsApi(spy._login.client)
    confirm_push_output = metrics_api.get_metric(id=push_output['ID'].iloc[0])
    assert confirm_push_output.measured_item.id == test_metadata['Measured Item'].iloc[0]
    tp = [t.priority.level for t in confirm_push_output.thresholds]
    assert confirm_push_output.thresholds[tp.index(-1)].item.id == test_metadata['Thresholds'].iloc[0]['Lo']
    assert confirm_push_output.thresholds[tp.index(3)].value.value == 90

    # Test using metric string levels not defined on the system
    test_metadata['Thresholds'].iloc[0]['9'] = 100
    try:
        spy.push(metadata=test_metadata)
        assert False
    except ApiException as e:
        assert e.status == 400

    # Test using metric string levels that map to multiple values at the same level
    test_metadata.at[0, 'Thresholds'] = {
        'Lo': signals_for_testing[signals_for_testing['Name'] == 'Wet Bulb']['ID'].iloc[0],
        '-1': 90}

    with pytest.raises(RuntimeError):
        spy.push(metadata=test_metadata)

    # Test converting a measured item defined by a dataframe
    temperature_index = signals_for_testing[signals_for_testing['Name'] == 'Temperature'].index.to_list()[0]
    test_dict = [{'Type': 'Threshold Metric',
                  'Name': 'push test threshold metric',
                  'Measured Item': signals_for_testing.iloc[temperature_index].to_dict(),
                  'Thresholds': {'Lo': signals_for_testing[signals_for_testing['Name'] == 'Wet Bulb']['ID'].iloc[0],
                                 '3': 90}}]
    test_metadata = pd.DataFrame(test_dict)

    push_output = spy.push(metadata=test_metadata)
    confirm_push_output = metrics_api.get_metric(id=push_output.at[0, 'ID'])
    assert confirm_push_output.measured_item.name == 'Temperature'

    # Test a threshold defined by a dataframe
    wetbulb_index = signals_for_testing[signals_for_testing['Name'] == 'Wet Bulb'].index.to_list()[0]
    test_dict = [{'Type': 'Threshold Metric',
                  'Name': 'push test threshold metric',
                  'Measured Item': signals_for_testing[signals_for_testing['Name'] == 'Temperature']['ID'].iloc[0],
                  'Thresholds': {'Lo': signals_for_testing.iloc[wetbulb_index].to_dict(),
                                 '3': 90}}]
    test_metadata = pd.DataFrame(test_dict)

    push_output = spy.push(metadata=test_metadata)
    confirm_push_output = metrics_api.get_metric(id=push_output.at[0, 'ID'])
    threshold_items = [t.item.name for t in confirm_push_output.thresholds]
    assert 'Wet Bulb' in threshold_items
