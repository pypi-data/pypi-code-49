# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
from azureml.automl.core import dataprep_utilities
from automl.client.core.common import logging_utilities
from azureml.automl.runtime import training_utilities
from azureml.train.automl.runtime._remote_script import _prepare_data


class _input_data_model(object):
    def __init__(self, data_dictionary):
        if data_dictionary is None:
            data_dictionary = {}
        self.X = data_dictionary.get('X', None)
        self.y = data_dictionary.get('y', None)
        self.X_valid = data_dictionary.get('X_valid', None)
        self.y_valid = data_dictionary.get('y_valid', None)
        self.sample_weight = data_dictionary.get('sample_weight', None)
        self.sample_weight_valid = data_dictionary.get('sample_weight_valid', None)
        self.cv_splits_indices = data_dictionary.get('cv_splits_indices', None)
        self.x_raw_column_names = data_dictionary.get('x_raw_column_names', None)
        self.training_data = data_dictionary.get('training_data', None)
        self.validation_data = data_dictionary.get('validation_data', None)


def _none_log_message(message, logging_level=logging.DEBUG):
    pass


def get_input_datamodel_from_dataprep_json(dataprep_json,
                                           automl_settings,
                                           log_message=_none_log_message,
                                           logger=None,
                                           verifier=None):
    """
    Convert dataprep data from json to datamodel.

    :param dataprep_json: The dataprep object in json format.
    :return: The dataprep object in datamodel format.
    """
    try:
        log_message("getting input data from dataprep json...")
        if dataprep_json is None:
            raise ValueError("dataprep_json is None")
        if automl_settings is None:
            raise ValueError("automl_settings is None")
        if logger is None:
            logger = logging_utilities._get_null_logger()

        new_dictionary = _prepare_data(
            dataprep_json=dataprep_json, automl_settings_obj=automl_settings,
            script_directory=None, entry_point=None, logger=logger)
        new_dictionary['is_adb_run'] = True
        new_dictionary['automl_settings'] = automl_settings
        new_dictionary['logger'] = logger
        if verifier:
            new_dictionary['verifier'] = verifier
        return _input_data_model(new_dictionary)
    except Exception as e:
        log_message(message="Error from getting input data from dataprep json: {0}".format(e.__class__),
                    logging_level=logging.ERROR)
        raise
