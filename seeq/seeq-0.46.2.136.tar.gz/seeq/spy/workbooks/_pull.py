import pandas as pd

from seeq.sdk.rest import ApiException

from ._workbook import Workbook

from .. import _common
from .. import _login
from ... import spy
from .._common import Status


def pull(workbooks_df, *, include_referenced_workbooks=True, include_inventory=True,
         errors='raise', quiet=False, status=None):
    """
    Pulls the definitions for each workbook specified by workbooks_df into
    memory as a list of Workbook items.

    Parameters
    ----------
    workbooks_df : pandas.DataFrame
        A DataFrame containing 'ID', 'Type' and 'Workbook Type' columns that
        can be used to identify the workbooks to pull. This is usually created
        via a call to spy.workbooks.search().

    include_referenced_workbooks : bool, default True
        If True, Analyses that are depended upon by Topics will be
        automatically included in the resulting list even if they were not part
        of the workbooks_df DataFrame.

    include_inventory : bool, default False
        If True, all items that are referenced in worksheets, journals, topics
        etc are included in the Workbook object's "inventory", along with
        anything that is scoped to the workbook.

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

    """
    if errors == 'catalog' and status is None:
        raise ValueError("status argument must be a valid Status object when errors='catalog'")

    _common.validate_argument_types([
        (workbooks_df, 'workbooks_df', pd.DataFrame),
        (include_referenced_workbooks, 'include_referenced_workbooks', bool),
        (include_inventory, 'include_inventory', bool),
        (errors, 'errors', str),
        (quiet, 'quiet', bool),
        (status, 'status', _common.Status)
    ])

    _login.validate_login()

    status = Status.validate(status, quiet)
    _common.validate_errors_arg(errors)

    if len(workbooks_df) == 0:
        status.update('workbooks_df is empty', Status.SUCCESS)
        return list()

    for required_column in ['ID', 'Type', 'Workbook Type']:
        if required_column not in workbooks_df.columns:
            raise ValueError('"%s" column must be included in workbooks_df' % required_column)

    status_columns = list()

    for col in ['ID', 'Name', 'Workbook Type']:
        if col in workbooks_df:
            status_columns.append(col)

    workbooks_df = workbooks_df[workbooks_df['Type'] != 'Folder']

    status.df = workbooks_df[status_columns].copy().reset_index(drop=True)
    status.df['Count'] = 0
    status.df['Time'] = 0
    status.df['Result'] = 'Queued'
    status_columns.extend(['Count', 'Time', 'Result'])

    status.update('Pulling workbooks', Status.RUNNING)

    workbooks_to_pull = {_common.get(row, 'ID'): {
        'Index': index,
        'Workbook Type': _common.get(row, 'Workbook Type'),
        'Search Folder ID': _common.get(row, 'Search Folder ID'),
        'Worksteps': set()
    } for index, row in workbooks_df.iterrows()}

    # Process Topics first so that we can discover Analyses and Worksteps (of embedded content) to add to our list (
    # assuming include_referenced_workbooks is True). Note that it is possible for Analyses to reference Topics (via
    # a link in a Journal) and they will not be properly included in the output. We have accepted this hole because
    # otherwise if we add a Topic to our list and that Topic refers to a workstep in an already-processed Analysis,
    # we would have to go back and re-pull the Analysis. (Maybe someday we'll do that, but not now. :-) )
    for phase in ['Topic', 'Analysis']:
        while True:
            at_least_one_item_pulled = False
            for item_id, pull_info in workbooks_to_pull.copy().items():
                try:
                    if not isinstance(pull_info, dict):
                        # Already pulled
                        continue

                    if pull_info['Workbook Type'] != phase:
                        continue

                    status.reset_timer()
                    status.current_df_index = pull_info['Index']
                    status.put('Result', 'Pulling')

                    workbook = Workbook.pull(item_id,
                                             extra_workstep_tuples=pull_info['Worksteps'],
                                             include_inventory=include_inventory,
                                             status=status)  # type: Workbook

                    if pull_info['Search Folder ID']:
                        workbook['Search Folder ID'] = pull_info['Search Folder ID']

                    if include_referenced_workbooks:
                        def _add_if_necessary(_workbook_id, _workstep_tuples):
                            if _workbook_id not in workbooks_to_pull:
                                to_add_df = spy.workbooks.search({'ID': _workbook_id},
                                                                 status=status.create_inner(quiet=True))
                                if len(to_add_df) == 0:
                                    # Workbook with this ID not found, probably as a result of a tool making an
                                    # invalid link in a Journal or Topic Document.
                                    return

                                workbook_type_to_add = _common.get(to_add_df.iloc[0], 'Workbook Type')
                                if phase == 'Analysis' and workbook_type_to_add == 'Topic':
                                    # We can't process more Topics once we're in the Analysis phase. (See comment
                                    # above the "for phase" loop.)
                                    return

                                workbooks_to_pull[_workbook_id] = {
                                    'Index': len(status.df),
                                    'Workbook Type': workbook_type_to_add,
                                    'Search Folder ID': pull_info['Search Folder ID'],
                                    'Worksteps': set()
                                }

                                to_add_df['Count'] = 0
                                to_add_df['Time'] = 0
                                to_add_df['Result'] = 'Queued'
                                status.df.loc[len(status.df)] = to_add_df.iloc[0][status_columns]

                            if not isinstance(workbooks_to_pull[_workbook_id], dict):
                                # We've already pulled it, that ship has sailed. This can happen when there are a
                                # web of links between Topics / Journals. We only do a "best effort" to make the
                                # links work.
                                return

                            workbooks_to_pull[_workbook_id]['Worksteps'].update(_workstep_tuples)

                        for workbook_id, workstep_tuples in workbook.referenced_workbooks.items():
                            _add_if_necessary(workbook_id, workstep_tuples)

                        for workbook_id, workstep_tuples in workbook.find_workbook_links().items():
                            _add_if_necessary(workbook_id, workstep_tuples)

                    workbooks_to_pull[item_id] = workbook
                    at_least_one_item_pulled = True

                    status.put('Result', 'Success')

                except BaseException as e:
                    if isinstance(e, KeyboardInterrupt):
                        status.df['Result'] = 'Canceled'
                        status.update('Pull canceled', Status.CANCELED)
                        return None

                    if errors == 'raise':
                        status.exception(e)
                        raise

                    status.put('Result', _common.format_exception(e))

            if not at_least_one_item_pulled:
                break

    status.update('Pull successful', Status.SUCCESS)

    return list(workbooks_to_pull.values())
