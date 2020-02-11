# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Global methods used during an automated machine learning iteration for both remote and local runs."""
import json
import logging
from typing import Optional, Union

import numpy as np
import pandas as pd
import scipy.sparse
from azureml.core import Run

import azureml.automl.core
from automl.client.core.runtime.types import DataInputType, DataSingleColumnInputType
from automl.client.core.runtime.cache_store import CacheStore
from automl.client.core.runtime import logging_utilities as runtime_logging_utilities
from azureml.automl.runtime import data_transformation
from azureml.automl.runtime import feature_skus_utilities
from azureml.automl.runtime.data_context import RawDataContext, TransformedDataContext
from azureml.automl.runtime.streaming_data_context import StreamingTransformedDataContext
from azureml.train.automl import _constants_azureml
from azureml.train.automl._azureautomlsettings import AzureAutoMLSettings
from .utilities import _check_if_y_label_has_single_frequency_class


def _subsampling_recommended(num_samples, num_features):
    """
    Recommend whether subsampling should be on or off based on shape of X.

    :param num_samples: Number of samples after preprocessing.
    :type num_samples: int
    :param num_features: Number of features after preprocessing.
    :type num_features: int
    :return: Flag indicate whether subsampling is recommended for given shape of X.
    :rtype: bool
    """
    # Ideally this number should be on service side.
    # However this number is proportional to the iteration overhead.
    # Which makes this specific number SDK specific.
    # For nativeclient or miroclient, this number will be different due to smaller overhead.
    # We will leave this here for now until we have a way of incorporating
    # hardware and network numbers in our model
    return num_samples * num_features > 300000000


def _set_problem_info(X: DataInputType,
                      y: DataSingleColumnInputType,
                      automl_settings: AzureAutoMLSettings,
                      current_run: Run,
                      transformed_data_context: Optional[Union[TransformedDataContext,
                                                         StreamingTransformedDataContext]] = None,
                      cache_store: Optional[CacheStore] = None,
                      is_adb_run: bool = False,
                      logger: Optional[logging.Logger] = None) -> None:
    """
    Set statistics about user data.

    :param X: The training features to use when fitting pipelines during AutoML experiment.
    :type X: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow
    :param y: Training labels to use when fitting pipelines during AutoML experiment.
    :type y: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow
    :param automl_settings: The AutoML settings to use.
    :type automl_settings: AzureAutoMLSettings
    :param current_run: The AutoMLRun to set the info for.
    :type current_run: azureml.core.run.Run
    :param transformed_data_context: Containing X, y and other transformed data info.
    :type transformed_data_context: TransformedDataContext or StreamingTransformedDataContext
    :param is_adb_run: flag whether this is a Azure Databricks run or not.
    :type is_adb_run: bool
    :param logger: the logger.
    :type logger: logging.logger
    :return: None
    """
    x_raw_column_names = None
    if isinstance(X, pd.DataFrame):
        x_raw_column_names = X.columns.values
    run_id = current_run._run_id
    if logger is not None:
        streaming = automl_settings.enable_streaming
        logger.info("Logging dataset information for {}".format(run_id))
        runtime_logging_utilities.log_data_info(logger=logger, data_name="X", data=X,
                                                run_id=run_id, streaming=streaming)
        runtime_logging_utilities.log_data_info(logger=logger, data_name="y", data=y,
                                                run_id=run_id, streaming=streaming)

    if transformed_data_context is None:
        raw_data_context = RawDataContext(automl_settings_obj=automl_settings,
                                          X=X,
                                          y=y,
                                          x_raw_column_names=x_raw_column_names)

        transformed_data_context = \
            data_transformation.transform_data(raw_data_context=raw_data_context,
                                               cache_store=cache_store,
                                               is_onnx_compatible=automl_settings.enable_onnx_compatible_models,
                                               enable_dnn=automl_settings.enable_dnn,
                                               force_text_dnn=automl_settings.force_text_dnn,
                                               logger=logger,
                                               enable_streaming=automl_settings.enable_streaming,
                                               working_dir=automl_settings.path)
    X = transformed_data_context.X
    y = transformed_data_context.y

    subsampling = automl_settings.enable_subsampling
    if subsampling is None:
        subsampling = _subsampling_recommended(X.shape[0], X.shape[1])

    problem_info_dict = {
        "dataset_num_categorical": 0,
        "is_sparse": scipy.sparse.issparse(X),
        "subsampling": subsampling
    }

    if automl_settings.enable_streaming:
        # Note: when using incremental learning, we are not calculating
        # some problem info properties that Miro may use for recommendation. It's uncertain at
        # this point whether these properties are needed
        problem_info_dict["dataset_features"] = X.head(1).shape[1]

        # If subsampling, set the number of dataset samples.
        # Note: when not subsampling, avoid this, because invoking Dataflow.shape
        # triggers Dataflow profile computation, which is expensive on large data
        if subsampling:
            problem_info_dict["dataset_samples"] = X.shape[0]
    else:
        problem_info_dict["dataset_classes"] = len(np.unique(y))
        problem_info_dict["dataset_features"] = X.shape[1]
        problem_info_dict["dataset_samples"] = X.shape[0]
        problem_info_dict['single_frequency_class_detected'] = \
            _check_if_y_label_has_single_frequency_class(automl_settings=automl_settings,
                                                         y=transformed_data_context.y,
                                                         logger=logger)
    problem_info_str = json.dumps(problem_info_dict)

    # This is required since token may expire
    if is_adb_run:
        current_run = Run.get_context()

    current_run.add_properties({
        _constants_azureml.Properties.PROBLEM_INFO: problem_info_str,
        'feature_skus': feature_skus_utilities.serialize_skus(
            feature_skus_utilities.get_feature_skus_from_settings(automl_settings)
        )
    })
