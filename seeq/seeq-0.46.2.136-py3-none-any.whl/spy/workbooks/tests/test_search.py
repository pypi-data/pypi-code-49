import pytest

from seeq.sdk import *
from seeq import spy

from ...tests import test_common
from . import test_load


def setup_module():
    test_common.login()


@pytest.mark.system
def test_non_recursive():
    workbooks = test_load.load_example_export()
    spy.workbooks.push(workbooks, path='Non-Recursive Import', errors='catalog')
    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*'
    })
    assert len(workbooks_df) == 2

    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*',
        'Name': '*Analysis'
    })
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Analysis'

    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*',
        'Workbook Type': 'Topic'
    })
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Topic'


@pytest.mark.system
def test_recursive():
    workbooks = test_load.load_example_export()
    spy.workbooks.push(workbooks, path='Recursive Import >> Another Folder Level', errors='catalog')
    workbooks_df = spy.workbooks.search({
        'Path': 'Recursive I?port'
    })
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Another Folder Level'
    assert workbooks_df.iloc[0]['Type'] == 'Folder'

    # The items will have been moved from the non-recursive location
    workbooks_df = spy.workbooks.search({
        'Path': 'Non-Recursive*'
    })
    assert len(workbooks_df) == 0

    workbooks_df = spy.workbooks.search({
        'Path': r'/Recursive\sImport/',
        'Name': '*Analysis'
    }, recursive=True)
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Analysis'

    workbooks_df = spy.workbooks.search({
        'Path': r'/^Recursive.*/',
        'Workbook Type': 'Topic'
    }, recursive=True)
    assert len(workbooks_df) == 1
    assert workbooks_df.iloc[0]['Name'] == 'Example Topic'


@pytest.mark.system
def test_archived():
    archived_workbook = spy.workbooks.Analysis({'Name': 'An Archived Workbook'})
    archived_workbook.worksheet('Only Worksheet')
    not_archived_workbook = spy.workbooks.Analysis({'Name': 'A Not Archived Workbook'})
    not_archived_workbook.worksheet('Only Worksheet')
    spy.workbooks.push([archived_workbook, not_archived_workbook], path='test_archived')
    items_api = ItemsApi(test_common.get_client())
    items_api.set_property(id=archived_workbook.id, property_name='Archived', body=PropertyInputV1(value=True))
    try:
        search_df = spy.workbooks.search({'Path': 'test_archived'}, include_archived=True)
        assert len(search_df) == 2
        assert 'An Archived Workbook' in search_df['Name'].tolist()
        assert 'A Not Archived Workbook' in search_df['Name'].tolist()
        search_df = spy.workbooks.search({'Path': 'test_archived'}, include_archived=False)
        assert len(search_df) == 1
        assert search_df.iloc[0]['Name'] == 'A Not Archived Workbook'
    finally:
        # Unarchive it so we can run this test over and over
        items_api.set_property(id=archived_workbook.id, property_name='Archived', body=PropertyInputV1(value=False))
