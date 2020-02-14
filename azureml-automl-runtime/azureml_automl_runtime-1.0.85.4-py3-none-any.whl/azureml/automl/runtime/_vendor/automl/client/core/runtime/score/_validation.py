# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Validation for AutoML metrics."""
import logging
import numpy as np
import sklearn.utils

from sklearn.base import TransformerMixin
from typing import Dict, List, Optional

from automl.client.core.runtime.score import constants, utilities
from automl.client.core.runtime.score._metric_base import NonScalarMetric
from automl.client.core.common.exceptions import ClientException


def validate_classification(y_test: np.ndarray,
                            y_pred_probs: np.ndarray,
                            metrics: List[str],
                            class_labels: np.ndarray,
                            train_labels: np.ndarray,
                            sample_weight: Optional[np.ndarray],
                            y_transformer: Optional[TransformerMixin]) -> None:
    """
    Validate the inputs for scoring classification.

    :param y_test: Target values.
    :param y_pred_probs: The predicted probabilities for all classes.
    :param metrics: Metrics to compute.
    :param class_labels: All classes found in the full dataset.
    :param train_labels: Classes as seen (trained on) by the trained model.
    :param sample_weight: Weights for the samples.
    :param y_transformer: Used to inverse transform labels.
    """
    for metric in metrics:
        if metric not in constants.CLASSIFICATION_SET:
            message = "Metric {} not a valid classification metric".format(metric)
            safe_message = "Invalid metric while scoring classification results"
            raise ClientException(message).with_generic_msg(safe_message)

    if class_labels is None:
        raise ClientException.create_without_pii("class_labels must not be None")

    if train_labels is None:
        raise ClientException.create_without_pii("train_labels must not be None")

    _check_y_test_y_pred(y_test, y_pred_probs, y_pred_name='y_pred_probs')

    array_dict = {
        'class_labels': class_labels,
        'train_labels': train_labels,
        'y_test': y_test,
    }
    _check_arrays_same_type(array_dict)

    _check_dim(y_test, 'y_test', 1)
    _check_dim(y_pred_probs, 'y_pred_probs', 2)

    _check_array(class_labels, 'class_labels', ensure_2d=False)
    _check_array(train_labels, 'train_labels', ensure_2d=False)
    _check_array(y_test, 'y_test', ensure_2d=False)
    _check_array(y_pred_probs, 'y_pred_probs')

    if sample_weight is not None and y_test.shape[0] != sample_weight.shape[0]:
        message = "Number of samples does not match in y_test ({}) and sample_weight ({})".format(
            y_test.shape[0], sample_weight.shape[0])
        raise ClientException.create_without_pii(message)

    if train_labels.shape[0] != y_pred_probs.shape[1]:
        message = "train_labels.shape[0] ({}) does not match y_pred_probs.shape[1] ({}).".format(
            train_labels.shape[0], y_pred_probs.shape[1])
        raise ClientException.create_without_pii(message)

    set_diff = np.setdiff1d(train_labels, class_labels)
    if set_diff.shape[0] != 0:
        message = "Labels {} found in train_labels are missing from class_labels.".format(set_diff)
        safe_message = "train_labels contains values not present in class_labels"
        raise ClientException(message).with_generic_msg(safe_message)

    set_diff = np.setdiff1d(np.unique(y_test), class_labels)
    if set_diff.shape[0] != 0:
        message = "Labels {} found in y_test are missing from class_labels.".format(set_diff)
        safe_message = "y_test contains values not present in class_labels"
        raise ClientException(message).with_generic_msg(safe_message)


def log_classification_debug(logger: logging.Logger,
                             y_test: np.ndarray,
                             y_pred_probs: np.ndarray,
                             class_labels: np.ndarray,
                             train_labels: np.ndarray,
                             sample_weight: Optional[np.ndarray] = None) -> None:
    """
    Log shapes of classification inputs for debugging.

    :param logger: A logger to log errors and warnings
    :param y_test: Target values
    :param y_pred_probs: The predicted probabilities for all classes
    :param class_labels: All classes found in the full dataset
    :param train_labels: Classes as seen (trained on) by the trained model
    :param sample_weight: Weights for the samples
    """
    unique_y_test = np.unique(y_test)
    debug_data = {
        'y_test': y_test.shape,
        'y_pred_probs': y_pred_probs.shape,
        'unique_y_test': unique_y_test.shape,
        'class_labels': class_labels.shape,
        'train_labels': train_labels.shape,
        'n_missing_train': np.setdiff1d(class_labels, train_labels).shape[0],
        'n_missing_valid': np.setdiff1d(class_labels, unique_y_test).shape[0],
        'sample_weight': None if sample_weight is None else sample_weight.shape
    }

    logger.info("Classification metrics debug: {}".format(debug_data))


def validate_regression(y_test: np.ndarray,
                        y_pred: np.ndarray,
                        metrics: List[str]) -> None:
    """
    Validate the inputs for scoring regression.

    :param y_test: Target values.
    :param y_pred: Target predictions.
    :param metrics: Metrics to compute.
    """
    for metric in metrics:
        if metric not in constants.REGRESSION_SET:
            message = "Metric {} not a valid regression metric".format(metric)
            safe_message = "Invalid metric while scoring regression results"
            raise ClientException(message).with_generic_msg(safe_message)

    _check_y_test_y_pred(y_test, y_pred)
    _check_array(y_test, 'y_test', ensure_2d=False)
    _check_array(y_pred, 'y_pred', ensure_2d=False)


def log_regression_debug(logger: logging.Logger,
                         y_test: np.ndarray,
                         y_pred: np.ndarray,
                         sample_weight: Optional[np.ndarray] = None) -> None:
    """
    Log shapes of regression inputs for debugging.

    :param logger: A logger to log errors and warnings
    :param y_test: Target values
    :param y_pred: Predicted values
    :param sample_weight: Weights for the samples
    """
    debug_data = {
        'y_test': y_test.shape,
        'y_pred': y_pred.shape,
        'sample_weight': None if sample_weight is None else sample_weight.shape
    }

    logger.info("Regression metrics debug: {}".format(debug_data))


def validate_forecasting(y_test: np.ndarray,
                         y_pred: np.ndarray,
                         metrics: List[str]) -> None:
    """
    Validate the inputs for scoring forecasting.

    :param y_test: Target values.
    :param y_pred: Target predictions.
    :param metrics: Metrics to compute.
    """
    for metric in metrics:
        if metric not in constants.FORECASTING_SET:
            message = "Metric {} not a valid forecasting metric".format(metric)
            safe_message = "Invalid metric while scoring forecasting results"
            raise ClientException(message).with_generic_msg(safe_message)

    _check_y_test_y_pred(y_test, y_pred)
    _check_array(y_test, 'y_test', ensure_2d=False)
    _check_array(y_pred, 'y_pred', ensure_2d=False)


def log_forecasting_debug(logger: logging.Logger,
                          y_test: np.ndarray,
                          y_pred: np.ndarray,
                          sample_weight: Optional[np.ndarray] = None) -> None:
    """
    Log shapes of forecasting inputs for debugging.

    :param logger: A logger to log errors and warnings
    :param y_test: Target values
    :param y_pred: Predicted values
    :param sample_weight: Weights for the samples
    """
    debug_data = {
        'y_test': y_test.shape,
        'y_pred': y_pred.shape,
        'sample_weight': None if sample_weight is None else sample_weight.shape
    }

    logger.info("Forecasting metrics debug: {}".format(debug_data))


def _check_y_test_y_pred(y_test: np.ndarray,
                         y_pred: np.ndarray,
                         y_pred_name: str = 'y_pred') -> None:
    """
    Validate that y_test and y_pred are the same shape.

    :y_test: Actual targets.
    :y_pred: Predicted targets (or probabilities).
    """
    if y_test is None:
        raise ClientException.create_without_pii("y_test must not be None")
    if y_pred is None:
        raise ClientException.create_without_pii("{} must not be None".format(y_pred_name))
    if y_test.shape[0] != y_pred.shape[0]:
        message = "Number of samples does not match in y_test ({}) and {} ({})".format(
            y_test.shape[0], y_pred_name, y_pred.shape[0])
        raise ClientException.create_without_pii(message)


def _check_array(arr: np.ndarray,
                 name: str,
                 ensure_2d: bool = True) -> None:
    """
    Check the array for reasonable values.

    :param arr: Array to check.
    :param name: Array name.
    :param ensure_2d: Extra check to ensure 2 dimensional.
    """
    if arr.dtype.kind in set('bcfiu'):
        if np.isnan(arr).any():
            message = "Elements of {} cannot be NaN".format(name)
            raise ClientException.create_without_pii(message)

        if ~np.isfinite(arr).all():
            message = "Elements of {} cannot be infinite".format(name)
            raise ClientException.create_without_pii(message)

    if not np.issubdtype(arr.dtype, np.str_):
        try:
            sklearn.utils.check_array(arr, ensure_2d=ensure_2d)
        except ValueError:
            raise ClientException.create_without_pii("{} failed sklearn.utils.check_array().".format(name))


def _check_arrays_same_type(array_dict: Dict[str, np.ndarray]) -> None:
    """
    Check that multiple arrays have the same types.

    :param array_dict: Dictionary from array name to array.
    """
    items = list(array_dict.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            i_type, j_type = items[i][1].dtype, items[j][1].dtype
            i_name, j_name = items[i][0], items[j][0]

            # Handle equivalent types like int32/int64 integers, U1/U2 strings
            if np.issubdtype(i_type, np.integer) and np.issubdtype(j_type, np.integer):
                continue
            if np.issubdtype(i_type, np.floating) and np.issubdtype(j_type, np.floating):
                continue
            if np.issubdtype(i_type, np.str_) and np.issubdtype(j_type, np.str_):
                continue

            # Handle all other types
            if i_type != j_type:
                message = "{} ({}) does not have the same type as {} ({})".format(i_name, i_type, j_name, j_type)
                raise ClientException.create_without_pii(message)


def _check_dim(arr: np.array,
               name: str,
               n_dim: int) -> None:
    """
    Check the number of dimensions for the given array.

    :param arr: Array to check.
    :param name: Array name.
    :param n_dim: Expected number of dimensions.
    """
    if arr.ndim != n_dim:
        message = "{} must be an ndarray with {} dimensions, found {}".format(name, n_dim, arr.ndim)
        raise ClientException.create_without_pii(message)


def format_1d(arr: np.ndarray) -> np.ndarray:
    """
    Format an array as 1d if possible.

    :param arr: The array to reshape.
    :return: Array of shape (x,).
    """
    if arr is None:
        return arr
    if arr.ndim == 2 and (arr.shape[0] == 1 or arr.shape[1] == 1):
        arr = np.ravel(arr)
    return arr


def log_failed_splits(scores, metric, logger):
    """
    Log if a metric could not be computed for some splits.

    :scores: The scores over all splits for one metric.
    :metric: Name of the metric.
    :logger: Warning and error logger.
    """
    n_splits = len(scores)

    failed_splits = []
    for score_index, score in enumerate(scores):
        if utilities.is_scalar(metric):
            if np.isnan(score):
                failed_splits.append(score_index)
        else:
            if NonScalarMetric.is_error_metric(score):
                failed_splits.append(score_index)
    n_failures = len(failed_splits)
    failed_splits_str = ', '.join([str(idx) for idx in failed_splits])

    if n_failures > 0:
        warn_args = metric, n_failures, n_splits, failed_splits_str
        warn_msg = "Could not compute {} for {}/{} validation splits: {}"
        logger.warning(warn_msg.format(*warn_args))
