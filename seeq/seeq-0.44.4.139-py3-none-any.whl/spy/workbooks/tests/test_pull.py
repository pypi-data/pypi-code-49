import pytest

from seeq import spy

from . import test_load
from .. import Workbook
from ...tests import test_common


def setup_module():
    test_common.login()


# The tests for pulling workbooks are light because so much of the functionality is tested in the push code. I.e.,
# the push code wouldn't work if the pull code had a problem, since the pull code is what produced the saved workbooks.
# (Same goes for the spy.workbooks.save() functionality.)

@pytest.mark.system
def test_pull():
    push_workbooks = test_load.load_example_export()

    push_df = spy.workbooks.push(push_workbooks, refresh=False, path='test_pull', label='test_pull')

    push_df.drop(columns=['ID'], inplace=True)
    push_df.rename(columns={'Pushed Workbook ID': 'ID'}, inplace=True)
    push_df['Type'] = 'Workbook'

    pull_workbooks = spy.workbooks.pull(push_df)

    pull_workbooks = sorted(pull_workbooks, key=lambda w: w['Workbook Type'])

    analysis = pull_workbooks[0]  # type: Workbook
    assert analysis.id == (push_df[push_df['Workbook Type'] == 'Analysis'].iloc[0]['ID'])
    assert analysis.name == (push_df[push_df['Workbook Type'] == 'Analysis'].iloc[0]['Name'])
    assert len(analysis.datasource_maps) >= 3
    assert len(analysis.item_inventory) >= 25

    assert analysis['URL'] == push_df[push_df['Workbook Type'] == 'Analysis'].iloc[0]['URL']

    worksheet_names = [w.name for w in analysis.worksheets]
    assert worksheet_names == [
        'Details Pane',
        'Calculated Items',
        'Histogram',
        'Metrics',
        'Journal',
        'Global',
        'Boundaries'
    ]

    topic = pull_workbooks[1]
    worksheet_names = [w.name for w in topic.worksheets]
    assert len(topic.datasource_maps) == 1
    assert worksheet_names == [
        'Static Doc',
        'Live Doc'
    ]
