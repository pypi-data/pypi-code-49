# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains helper methods for dataprep."""

import sys


MIN_DATAPREP_VERSION = '1.1.29'
_version_checked = False


def check_min_version():
    global _version_checked
    if _version_checked:
        return
    _version_checked = True
    from pkg_resources import parse_version, get_distribution
    import logging
    installed_version = get_distribution('azureml-dataprep').version
    if parse_version(installed_version) < parse_version(MIN_DATAPREP_VERSION):
        logging.getLogger().warning(
            _dataprep_incompatible_version_error.format(MIN_DATAPREP_VERSION, installed_version))


def is_dataprep_installed():
    try:
        from azureml.dataprep import api
        return api is not None
    except:
        return False


def dataprep():
    if not is_dataprep_installed:
        raise ImportError(get_dataprep_missing_message())
    import azureml.dataprep as _dprep
    check_min_version()
    return _dprep


def dataprep_fuse():
    try:
        import azureml.dataprep.fuse.dprepfuse as _dprep_fuse
        check_min_version()
        return _dprep_fuse
    except ImportError:
        raise ImportError(get_dataprep_missing_message(extra='[fuse]'))


def ensure_dataflow(dataflow):
    if not isinstance(dataflow, dataprep().Dataflow):
        raise RuntimeError('dataflow must be instance of azureml.dataprep.Dataflow')


def get_dataflow_for_execution(dataflow, action, source, **kwargs):
    from copy import deepcopy
    meta = deepcopy(dataflow._meta)
    if 'activityApp' not in meta:
        meta['activityApp'] = source
    if 'activity' not in meta:
        meta['activity'] = action
    if len(kwargs) > 0:
        kwargs.update(meta)
        meta = kwargs
    return dataprep().Dataflow(dataflow._engine_api, dataflow._steps, meta)


def get_dataflow_with_meta_flags(dataflow, **kwargs):
    from copy import deepcopy
    if len(kwargs) > 0:
        meta = deepcopy(dataflow._meta)
        kwargs.update(meta)
        meta = kwargs
        return dataprep().Dataflow(dataflow._engine_api, dataflow._steps, meta)
    return dataflow


def get_dataprep_missing_message(issue=None, extra=None, how_to_fix=None):
    dataprep_available = sys.maxsize > 2**32  # no azureml-dataprep available on 32 bit
    extra = extra or ''
    if how_to_fix:
        suggested_fix = ' This can {}be resolved by {}.'.format('also ' if dataprep_available else '', how_to_fix)
    else:
        suggested_fix = ''

    message = (issue + ' due to missing') if issue else 'Missing'
    message += ' required package "azureml-dataprep{}", which '.format(extra)

    if not dataprep_available:
        message += 'is unavailable for 32bit Python.'
    else:
        message += 'can be installed by running: {}.'.format(_get_install_cmd(extra))

    return message + suggested_fix


def _get_install_cmd(extra):
    return '"{}" -m pip install azureml-dataprep{} --upgrade'.format(sys.executable, extra or '')


_dataprep_incompatible_version_error = (
    'Warning: The minimum required version of "azureml-dataprep" is {}, but {} is installed.' +
    '\nSome functionality may not work correctly. Please upgrade it by running:' +
    '\n' + _get_install_cmd('[fuse,pandas]')
)
