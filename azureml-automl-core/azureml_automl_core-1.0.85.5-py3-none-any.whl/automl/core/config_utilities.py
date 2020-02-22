# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility methods for interacting with AutoMLConfig."""
from typing import Any, cast, Callable, Dict, List, Optional, Set, Tuple, Union

import azureml.automl.core
from automl.client.core.common.exceptions import DataException, ConfigException


def _check_validation_config(
    X_valid: Any,
    y_valid: Any,
    sample_weight: Any,
    sample_weight_valid: Any,
    cv_splits_indices: Any,
    n_cross_validations: Optional[int] = None,
    validation_size: Optional[float] = None
) -> None:
    """
    Validate that validation parameters have been correctly provided.

    :param X_valid:
    :param y_valid:
    :param sample_weight:
    :param sample_weight_valid:
    :param cv_splits_indices:
    :param n_cross_validations:
    :param validation_size:
    """

    if X_valid is not None and y_valid is None:
        raise DataException(
            "X validation provided but y validation data is missing.")

    if y_valid is not None and X_valid is None:
        raise DataException(
            "y validation provided but X validation data is missing.")

    if X_valid is not None and sample_weight is not None and \
            sample_weight_valid is None:
        raise DataException("sample_weight_valid should be set to a valid value")

    if sample_weight_valid is not None and X_valid is None:
        raise DataException(
            "sample_weight_valid should only be set if X_valid is set")

    if X_valid is not None:
        if n_cross_validations is not None and n_cross_validations > 0:
            raise ConfigException("Both custom validation data and "
                                  "n_cross_validations specified. "
                                  "If you are providing the training "
                                  "data, do not pass any n_cross_validations.")
        if validation_size is not None and validation_size > 0.0:
            raise ConfigException("Both custom validation data and "
                                  "validation_size specified. If you are "
                                  "providing the training data, do not pass "
                                  "any validation_size.")

    if cv_splits_indices is not None:
        if n_cross_validations is not None and n_cross_validations > 0:
            raise ConfigException("Both cv_splits_indices and n_cross_validations "
                                  "specified. If you are providing the indices to "
                                  "use to split your data. Do not pass any "
                                  "n_cross_validations.")
        if validation_size is not None and validation_size > 0.0:
            raise ConfigException("Both cv_splits_indices and validation_size "
                                  "specified. If you are providing the indices to "
                                  "use to split your data. Do not pass any "
                                  "validation_size.")
        if X_valid is not None:
            raise ConfigException("Both cv_splits_indices and custom split "
                                  "validation data specified. If you are providing "
                                  "the training data, do not pass any indices to "
                                  "split your data.")
