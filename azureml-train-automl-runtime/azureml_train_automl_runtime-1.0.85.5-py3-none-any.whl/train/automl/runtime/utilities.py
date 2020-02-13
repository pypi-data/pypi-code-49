# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility methods used by automated machine learning."""
from typing import Union, Optional
from types import ModuleType
import importlib
import importlib.util
import importlib.abc
import json
import logging
import os
import numpy as np

from automl.client.core.common import constants
from automl.client.core.runtime.types import DataSingleColumnInputType
from azureml.train.automl.exceptions import ConfigException, ServiceException, UserErrorException
from azureml.train.automl._azureautomlsettings import AzureAutoMLSettings


def _load_user_script(script_path: str, logger: logging.Logger, calling_in_client_runtime: bool = True) -> ModuleType:
    #  Load user script to get access to GetData function
    logger.info('Loading data using user script.')

    module_name, module_ext = os.path.splitext(os.path.basename(script_path))
    if module_ext != '.py':
        raise ConfigException('The provided user script was not a Python file.')
    spec = importlib.util.spec_from_file_location('get_data', script_path)
    if spec is None:
        if calling_in_client_runtime:
            raise ConfigException('The provided user script path does not exist.')
        else:
            raise ServiceException('The provided user script path does not exist.')

    module_obj = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ConfigException(
            'The provided user script is a namespace package, which is not supported.')

    # exec_module exists on 3.4+, but it's marked optional so we have to assert
    assert isinstance(spec.loader, importlib.abc.Loader)
    assert spec.loader.exec_module is not None
    try:
        spec.loader.exec_module(module_obj)
    except FileNotFoundError:
        if calling_in_client_runtime:
            raise ConfigException('The provided user script path does not exist.')
        else:
            if not os.path.exists(script_path):
                raise ServiceException('The provided user script path does not exist.')
            else:
                raise ConfigException('The provided user script references files that are not in the project folder.')
    except Exception as e:
        raise UserErrorException('Exception while executing user script: {}'.format(e))

    if not hasattr(module_obj, 'get_data'):
        raise ConfigException('The provided user script does not implement get_data().')

    return module_obj


def _check_if_y_label_has_single_frequency_class(automl_settings: AzureAutoMLSettings,
                                                 y: DataSingleColumnInputType,
                                                 logger: Optional[logging.Logger] = None) -> bool:
    """Check for classification tasks, if there is some label with only occurrence."""
    if automl_settings.task_type == constants.Tasks.CLASSIFICATION:
        unique_classes_set, value_frequency_set = np.unique(y, return_counts=True)
        for class_value, frequency in zip(unique_classes_set, value_frequency_set):
            # In classification case if the there is label which has just one instance.
            # then we should auto-blacklist some pipelines
            if frequency == 1:
                if logger is not None:
                    logger.warning('Found class a with single occurrence. Some pipelines maybe blacklisted')
                return True

    return False
