# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains helper methods for dataprep."""

MIN_DATAPREP_VERSION = '1.1.29'
_version_checked = False


def check_min_version():
    global _version_checked
    if _version_checked:
        return
    _version_checked = True
    from pkg_resources import parse_version
    import logging
    import azureml.dataprep as _dprep
    try:
        if parse_version(_dprep.__version__) < parse_version(MIN_DATAPREP_VERSION):
            logging.getLogger().warning(
                _dataprep_incompatible_version_error.format(_dprep.__version__, MIN_DATAPREP_VERSION))
    except AttributeError:
        # this is so that in dev mode when __version__ does not exist this will still work.
        pass


def is_dataprep_installed():
    try:
        from azureml.dataprep import __version__
        return __version__ is not None
    except:
        return False


def dataprep():
    try:
        import azureml.dataprep as _dprep
        check_min_version()
        return _dprep
    except ImportError:
        raise ImportError(_dataprep_missing_error)


def dataprep_fuse():
    try:
        import azureml.dataprep.fuse.dprepfuse as _dprep_fuse
        check_min_version()
        return _dprep_fuse
    except ImportError:
        raise ImportError(_dataprep_missing_error)


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


_dataprep_missing_error = (
    'Could not import package "azureml-dataprep". Please ensure it is installed by running: ' +
    'pip install "azureml-dataprep[fuse,pandas]"'
)

_dataprep_incompatible_version_error = (
    'Found installed version of "azureml-dataprep": {}' +
    '\nMinimum supported version: {}' +
    '\nSome functionality may not work correctly. Please upgrade by running:' +
    '\npip install azureml-dataprep[fuse,pandas] --upgrade'
)
