import pytest

import pandas as pd

from seeq import spy
from seeq.sdk import *
from seeq.sdk.rest import ApiException

from . import test_common

from .. import _config


def setup_module():
    test_common.login()


@pytest.mark.system
def test_simple_search():
    search_results = spy.search({
        'Name': 'Area A_Temper'
    })

    assert len(search_results) == 1

    search_results = spy.search(pd.DataFrame([{
        'Name': 'Area A_Temper'
    }]))

    # Nothing will be returned because we use a equal-to comparison when a DataFrame is passed in
    assert len(search_results) == 0

    search_results = spy.search(pd.DataFrame([{
        'Name': 'Area A_Temperature'
    }]))

    assert len(search_results) == 1

    search_results = spy.search(pd.DataFrame([{
        'Name': 'Area A_Temperature'
    }]), all_properties=True)

    assert len(search_results) == 1
    assert 'Maximum Interpolation' in search_results.iloc[0]


@pytest.mark.system
def test_dataframe_single_row_with_id():
    search_results = spy.search({
        'Name': 'Area A_Temper'
    })

    search_results = spy.search(search_results.iloc[0])

    assert len(search_results) == 1
    assert search_results.iloc[0]['Name'] == 'Area A_Temperature'
    assert search_results.iloc[0]['Data ID'] == '[Tag] Area A_Temperature.sim.ts.csv'


@pytest.mark.system
def test_dataframe_multi_row():
    search_results = spy.search(pd.DataFrame([{
        'Name': 'Area A_Relative Humidity',
        'Datasource Name': 'Example Data'
    }, {
        'Name': 'Area A_Temperature',
        'Datasource Name': 'Example Data'
    }, {
        'Path': 'Example >> Cooling Tower 1 >> Area A',
        'Name': 'Relative Humidity'
    }]))

    assert len(search_results) == 3
    assert len(search_results[search_results['Name'] == 'Area A_Temperature']) == 1
    assert len(search_results[search_results['Name'] == 'Area A_Relative Humidity']) == 1
    assert len(search_results[search_results['Name'] == 'Relative Humidity']) == 1


@pytest.mark.system
def test_dataframe_warnings_and_duplicates():
    status = spy.Status()
    search_results = spy.search([{
        'Name': 'Humid',
        'Path': 'Example >> Cooling Tower 1'
    }, {
        'Name': 'Area A_',
        'Datasource Name': 'Example Data'
    }, {
        'Name': 'Area A_',
        'Datasource Name': 'Example Data'
    }], status=status)

    # Make sure the duplicates will have been dropped
    assert len(search_results) == 14

    assert '6 duplicates removed' in status.message

    search_results.drop(columns=['ID'], inplace=True)

    status = spy.Status()
    search_results2 = spy.search(search_results, status=status)

    # There will be a warning because 'Value Unit Of Measure' will be part of the DataFrame but it can't be searched on
    assert 'Warning' in status.message

    assert len(search_results2) == 14

    unique_ids = search_results2['ID'].drop_duplicates().to_list()
    assert len(unique_ids) == 14


@pytest.mark.system
def test_path_with_datasource():
    search_results = spy.search({
        'Name': 'Area ?_*',
        'Datasource Name': 'Example Data'
    })

    push_df = search_results.copy()
    push_df['Reference'] = True
    push_df['Path'] = 'test_path_with_datasource-tree >> branch-alpha'
    push_df['Asset'] = push_df['Name'].str.extract(r'(Area .)_.*')
    push_df['Name'] = push_df['Name'].str.extract(r'Area ._(.*)')

    spy.push(metadata=push_df, datasource={
        'Datasource Class': 'test_path_with_datasource-class',
        'Datasource Name': 'test_path_with_datasource-name-1'
    })

    push_df['Path'] = 'test_path_with_datasource-tree >> branch-bravo'

    spy.push(metadata=push_df, datasource={
        'Datasource Class': 'test_path_with_datasource-class',
        'Datasource Name': 'test_path_with_datasource-name-2'
    })

    search_results = spy.search({
        'Path': 'test_path_with_datasource-tree',
    }, recursive=False)

    paths = search_results['Path'].drop_duplicates().dropna().tolist()
    assets = search_results['Asset'].drop_duplicates().tolist()
    names = sorted(search_results['Name'].tolist())
    types = search_results['Type'].drop_duplicates().tolist()

    assert len(paths) == 0
    assert assets == ['test_path_with_datasource-tree']
    assert names == ['branch-alpha', 'branch-bravo']
    assert types == ['Asset']

    search_results = spy.search({
        'Path': 'test_path_with_datasource-tree',
    }, recursive=True)

    assert len(search_results) > 100
    types = sorted(search_results['Type'].drop_duplicates().tolist())
    assert types == ['Asset', 'CalculatedSignal']
    assert len(search_results[search_results['Asset'] == 'branch-alpha']) > 0
    assert len(search_results[search_results['Asset'] == 'branch-bravo']) > 0

    search_results = spy.search({
        'Path': 'test_path_with_datasource-tree >> branch-alpha',
    }, recursive=True)

    assert len(search_results[search_results['Asset'] == 'branch-alpha']) > 0
    assert len(search_results[search_results['Asset'] == 'branch-bravo']) == 0

    search_results = spy.search({
        'Path': 'test_path_with_datasource-tree >> branch-*',
    }, recursive=True)

    assert len(search_results[search_results['Asset'] == 'branch-alpha']) > 0
    assert len(search_results[search_results['Asset'] == 'branch-bravo']) > 0

    search_results = spy.search({
        'Path': 'test_path_with_datasource-* >> branch-bravo',
    }, recursive=True)

    assert len(search_results[search_results['Asset'] == 'branch-alpha']) == 0
    assert len(search_results[search_results['Asset'] == 'branch-bravo']) > 0

    search_results = spy.search({
        'Path': 'test_path_with_datasource-* >> branch-bravo',
        'Datasource Name': 'test_path_with_datasource-name-1'
    }, recursive=True)

    assert len(search_results) == 0

    search_results = spy.search({
        'Path': 'test_path_with_datasource-* >> branch-alpha',
        'Datasource Name': 'test_path_with_datasource-name-1'
    }, recursive=True)

    assert len(search_results[search_results['Asset'] == 'branch-alpha']) > 0
    assert len(search_results[search_results['Asset'] == 'branch-bravo']) == 0


@pytest.mark.system
def test_dataframe_bad_datasource():
    with pytest.raises(RuntimeError):
        spy.search(pd.DataFrame([{
            'Name': 'Area A_Temperature',
            'Datasource Name': 'Bad Datasource'
        }]))


@pytest.mark.system
def test_type_search():
    search_results = spy.search({
        'Datasource Class': 'Time Series CSV Files',
        'Type': 'Signal'
    })

    assert 150 < len(search_results) < 200

    datasource_names = set(search_results['Datasource Name'].tolist())
    assert len(datasource_names) == 1
    assert datasource_names.pop() == 'Example Data'

    types = set(search_results['Type'].tolist())
    assert len(types) == 1
    assert types.pop() == 'StoredSignal'

    search_results = spy.search({
        'Datasource Class': 'Time Series CSV Files',
        'Type': 'Condition'
    })

    assert len(search_results) == 0

    search_results = spy.search({
        'Datasource Class': 'Time Series CSV Files',
        'Type': 'Scalar'
    })

    assert len(search_results) == 0

    search_results = spy.search({
        'Datasource Class': 'Time Series CSV Files',
        'Type': 'Asset'
    })

    assert 5 < len(search_results) < 20

    # Multiple types
    search_results = spy.search({
        'Datasource Class': 'Time Series CSV Files',
        'Type': ['Signal', 'Asset']
    })

    assert 160 < len(search_results) < 300
    assert 5 < len(search_results[search_results['Type'] == 'Asset']) < 20
    assert 150 < len(search_results[search_results['Type'].str.contains('Signal')]) < 200


@pytest.mark.system
def test_path_search_recursive():
    search_results = spy.search({
        'Path': 'Non-existent >> Path'
    })

    assert len(search_results) == 0

    search_results = spy.search({
        'Path': 'Example >> Cooling Tower 1'
    })

    assert 40 < len(search_results) < 60

    search_results = spy.search({
        'Path': '*xamp* >> Cooling Tower *',
        'Name': '*Compressor*'
    }, workbook=None)

    names = search_results['Name'].drop_duplicates().tolist()
    assert len(names) == 2
    assert 'Compressor Power' in names
    assert 'Compressor Stage' in names
    paths = search_results['Path'].drop_duplicates().tolist()
    assert len(paths) == 2
    assert 'Example >> Cooling Tower 1' in paths
    assert 'Example >> Cooling Tower 2' in paths

    search_results = spy.search({
        'Path': 'Example >> /Cooling Tower [2]/',
        'Name': '*Compressor*'
    }, workbook=None)

    names = search_results['Name'].drop_duplicates().tolist()
    assert len(names) == 2
    assert 'Compressor Power' in names
    assert 'Compressor Stage' in names
    paths = search_results['Path'].drop_duplicates().tolist()
    assert len(paths) == 1
    assert 'Example >> Cooling Tower 2' in paths


@pytest.mark.system
def test_path_search_non_recursive():
    search_results = spy.search({
        'Path': 'Exampl',
        'Type': 'Asset'
    }, recursive=None)

    assert len(search_results) == 0

    search_results = spy.search({
        'Path': 'Example',
        'Type': 'Asset'
    }, recursive=None)

    assert len(search_results) == 2

    search_results = spy.search({
        'Path': 'Example >> Cooling Tower 1',
        'Name': '/Area [ABC]/'
    }, recursive=False, workbook=None)

    assert len(search_results) == 3
    types = search_results['Type'].drop_duplicates().tolist()
    assert len(types) == 1
    assert types[0] == 'Asset'

    search_results = spy.search({
        'Path': 'Example >> Cooling Tower *',
        'Asset': 'Area A',
        'Name': '*Compressor*'
    }, recursive=False, workbook=None)

    assert len(search_results) == 2
    names = search_results['Name'].tolist()
    assert len(names) == 2
    assert 'Compressor Power' in names
    assert 'Compressor Stage' in names
    paths = search_results['Path'].drop_duplicates().tolist()
    assert len(paths) == 1
    assert paths[0] == 'Example >> Cooling Tower 1'


@pytest.mark.system
def test_path_search_pagination():
    # This tests the 'Path' finding code to make sure we'll find a path even if pagination
    # is required.
    original_page_size = _config.options.search_page_size
    try:
        _config.options.search_page_size = 1
        search_results = spy.search({
            'Path': 'Example >> Cooling Tower 1 >> Area G'
        }, recursive=False, workbook=None)

        assert len(search_results) == 6
    finally:
        _config.options.search_page_size = original_page_size


@pytest.mark.system
def test_datasource_name_search():
    with pytest.raises(RuntimeError):
        spy.search({
            'Datasource Name': 'Non-existent'
        })

    search_results = spy.search({
        'Datasource Name': 'Example Data'
    })

    assert 150 < len(search_results) < 200


@pytest.mark.system
def test_search_pagination():
    original_page_size = _config.options.search_page_size
    try:
        _config.options.search_page_size = 2
        search_results = spy.search({
            'Name': 'Area A_*'
        })

        assert len(search_results) == 6

    finally:
        _config.options.search_page_size = original_page_size


@pytest.mark.system
def test_search_bad_workbook():
    with pytest.raises(RuntimeError):
        spy.search({
            'Name': 'Area A_*'
        }, workbook='bad')


@pytest.mark.system
def test_search_workbook_guid():
    # The workbook won't be found, so we'll get an access error
    with pytest.raises(ApiException):
        spy.search({
            'Name': 'Area A_*'
        }, workbook='A0B89103-E95D-4E32-A809-390C1FAE9D2F')


@pytest.mark.system
def test_include_archived():
    search_df = spy.search({'Name': 'Area A_*', 'Datasource ID': 'Example Data'})
    area_a_ids = search_df['ID'].tolist()
    area_a_count = len(area_a_ids)
    items_api = ItemsApi(test_common.get_client())

    def _do_archive(archive):
        for _id in area_a_ids:
            items_api.set_property(id=_id, property_name='Archived', body=PropertyInputV1(value=archive))

    try:
        _do_archive(True)
        search_df = spy.search({'Name': 'Area A_*', 'Datasource ID': 'Example Data'})
        assert len(search_df) == 0
        search_df = spy.search({'Name': 'Area A_*', 'Datasource ID': 'Example Data'}, include_archived=True)
        assert len(search_df) == area_a_count
    finally:
        _do_archive(False)

    with pytest.raises(ValueError):
        spy.search({'Path': 'Example', 'Datasource ID': 'Example Data'}, recursive=False, include_archived=True)

