# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility methods for interacting with azureml.dataprep."""
from typing import Any, Dict
import json
import numpy as np
import pandas as pd

from automl.client.core.common.exceptions import DataException, DataprepException
from azureml.automl.core.dataprep_utilities import is_dataflow

DATAPREP_INSTALLED = True
try:
    import azureml.dataprep as dprep
except ImportError:
    DATAPREP_INSTALLED = False


__activities_flag__ = 'activities'


def retrieve_numpy_array(dataflow: Any) -> np.array:
    """Retreieve pandas dataframe from dataflow and return underlying ndarray.

    Param dataflow: the dataflow to retrieve
    type: azureml.dataprep.Dataflow
    return: the retrieved np.ndarray, or the original dataflow value when it is of incorrect type
    """
    if not is_dataflow(dataflow):
        return dataflow
    try:
        df = dataflow.to_pandas_dataframe(on_error='null')
        if df.empty:
            raise DataException.create_without_pii("Dataflow resulted in empty array.")
        if df.shape[1] == 1:
            # if the DF is a single column ensure the resulting output is a 1 dim array by converting
            # to series first.
            return df[df.columns[0]].values
        return df.values
    except DataException:
        raise
    except Exception as e:
        raise DataException.from_exception(e)


def retrieve_pandas_dataframe(dataflow: Any) -> pd.DataFrame:
    """Retreieve pandas dataframe from dataflow.

    Param dataflow: the dataflow to retrieve
    type: azureml.dataprep.Dataflow
    return: the retrieved pandas DataFrame, or the original dataflow value when it is of incorrect type
    """
    if not is_dataflow(dataflow):
        return dataflow
    try:
        df = dataflow.to_pandas_dataframe(on_error='null')
        if df.empty:
            raise DataException.create_without_pii("Dataflow resulted in empty dataframe.")
        return df
    except DataException:
        raise
    except Exception as e:
        raise DataException.from_exception(e)


def resolve_cv_splits_indices(cv_splits_indices):
    """Resolve cv splits indices.

    Param cv_splits_indices: the list of dataflow where each represents a set of split indices
    type: list(azureml.dataprep.Dataflow)
    return: the resolved cv_splits_indices, or the original passed in value when it is of incorrect type
    """
    if cv_splits_indices is None:
        return None
    cv_splits_indices_list = []
    for split in cv_splits_indices:
        if not is_dataflow(split):
            return cv_splits_indices
        else:
            is_train_list = retrieve_numpy_array(split)
            train_indices = []
            valid_indices = []
            for i in range(len(is_train_list)):
                if is_train_list[i] == 1:
                    train_indices.append(i)
                elif is_train_list[i] == 0:
                    valid_indices.append(i)
            cv_splits_indices_list.append(
                [np.array(train_indices), np.array(valid_indices)])
    return cv_splits_indices_list
