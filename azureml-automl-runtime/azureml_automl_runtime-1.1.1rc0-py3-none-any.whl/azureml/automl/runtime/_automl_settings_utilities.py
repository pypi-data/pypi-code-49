# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utilities for managing settings for AutoML experiments."""
from typing import Any, cast, Dict, List, Optional, Tuple, Union
import scipy
from sklearn.model_selection import train_test_split
import azureml.automl.core
import azureml.automl.runtime
from automl.client.core.common import constants
from automl.client.core.common.logging_utilities import _get_null_logger
from automl.client.core.runtime.types import DataInputType, DataSingleColumnInputType
from azureml.automl.runtime.faults_verifier import VerifierManager


def rule_based_validation(
        automl_settings,
        X: DataInputType = None,
        y: DataSingleColumnInputType = None,
        sample_weight: DataSingleColumnInputType = None,
        X_valid: DataInputType = None,
        y_valid: DataSingleColumnInputType = None,
        sample_weight_valid: DataSingleColumnInputType = None,
        cv_splits_indices: Any = None,
        logger: Any = None,
        test_size: Optional[float] = constants.RuleBasedValidation.DEFAULT_TRAIN_VALIDATE_TEST_SIZE,
        random_state: Optional[int] = constants.RuleBasedValidation.DEFAULT_TRAIN_VALIDATE_RANDOM_STATE,
        verifier: Optional[VerifierManager] = None
) -> Tuple[DataInputType, DataSingleColumnInputType, DataSingleColumnInputType,
           DataInputType, DataSingleColumnInputType, DataSingleColumnInputType]:
    """
    Choose CV or train validation based on the data size.

    This will choose cv/ train validation based on the input data. And the AutoMLSettings will be changed.
    :param X: Training data.
    :type X: pandas.DataFrame or numpy.ndarray or scipy.sparse
    :param y: Training labels.
    :type y: pandas.DataFrame or numpy.ndarray or scipy.sparse
    :param sample_weight: Training sample weights
    :type sample_weight: pandas.DataFrame or numpy.ndarray
    :param X_valid: validation features.
    :type X_valid: pandas.DataFrame or numpy.ndarray
    :param y_valid: validation labels.
    :type y_valid: pandas.DataFrame or numpy.ndarray
    :param sample_weight_valid: Validation sample weights
    :type sample_weight_valid: pandas.DataFrame or numpy.ndarray
    :param cv_splits_indices: Indices where to split training data for
    cross validation
    :type cv_splits_indices: list(int), or list(Dataflow) in which each Dataflow represent a train-valid set
                                where 1 indicates record for training and 0
                                indicates record for validation
    :param logger: the logger.
    :type logger: logger
    :param test_size: train validation test_size.
    :type test_size: float
    :param random_state: train validation random_state.
    :type random_state: int
    :return:
    """
    if logger is None:
        logger = _get_null_logger()
    if not _is_rule_based_validation_needed(
            X_valid, automl_settings.n_cross_validations,
            cv_splits_indices, automl_settings.validation_size,
            automl_settings.is_timeseries
    ):
        logger.info("User has validation defined, no train rule based validation needed.")
        return X, y, sample_weight, X_valid, y_valid, sample_weight_valid

    number_of_cv = _get_cv_number(X)
    if number_of_cv > 1:  # As CV must be larger than 1, so 1 here means train valid split
        automl_settings.n_cross_validations = number_of_cv
        if verifier:
            verifier.update_data_verifier_for_cv(automl_settings.n_cross_validations)
        logger.info(
            "Rule based validation: Using rule based cv now with cv {}.".format(
                str(automl_settings.n_cross_validations))
        )
    else:
        logger.info("Rule based validation: Using rule based train/test splits.")
        # Using stratified split for classification. If the dataset cannot be split using
        # stratified split or the task type is regression, then using normal train test split.
        is_stratified = True
        if automl_settings.task_type == constants.Tasks.CLASSIFICATION:
            try:
                if sample_weight is None:
                    X, X_valid, y, y_valid = train_test_split(
                        X, y, stratify=y, test_size=test_size, random_state=random_state)
                else:
                    X, X_valid, y, y_valid, sample_weight, sample_weight_valid = train_test_split(
                        X, y, sample_weight, stratify=y, test_size=test_size, random_state=random_state)
                logger.info("Rule based validation: Using stratified sampling.")
            except Exception:
                is_stratified = False
                logger.warning("Straified split meets exception")
                logger.warning("Rule based validation: Stratified split failed. Fall to use random sampling.")
        if automl_settings.task_type == constants.Tasks.REGRESSION or not is_stratified:
            if sample_weight is None:
                X, X_valid, y, y_valid = train_test_split(
                    X, y, test_size=test_size, random_state=random_state)
            else:
                X, X_valid, y, y_valid, sample_weight, sample_weight_valid = train_test_split(
                    X, y, sample_weight, test_size=test_size, random_state=random_state)
            logger.info("Rule based validation: Using random sampling.")

        if verifier:
            verifier.update_data_verifier_for_train_test_validation(X.shape[0], X_valid.shape[0])

    return X, y, sample_weight, X_valid, y_valid, sample_weight_valid


def _is_rule_based_validation_needed(
        X_valid,
        n_cross_validations: Optional[int] = None,
        cv_splits_indices: Optional[Any] = None,
        validation_size: Optional[float] = None,
        is_timeseries: Optional[bool] = None
) -> bool:
    """
    Check whether user input need automated validation settings.

    This function will be true if user has no input validation settings and the training is not timeseries.
    """
    is_needed = not is_timeseries
    is_needed = is_needed and X_valid is None and (validation_size is None or validation_size == 0.0)
    is_needed = is_needed and n_cross_validations is None and cv_splits_indices is None
    return is_needed


def _get_cv_number(X) -> int:
    """Return the number of cross validation is needed. If is 1 using train test splits."""
    if scipy.sparse.issparse(X):
        return constants.RuleBasedValidation.SPARSE_N_CROSS_VALIDATIONS
    for rule in constants.RuleBasedValidation.VALIDATION_LIMITS_NO_SPARSE:
        if X.shape[0] >= rule.LOWER_BOUND and X.shape[0] < rule.UPPER_BOUND:
            return rule.NUMBER_OF_CV
    # by default return constants.RuleBasedValidation.DEFAULT_N_CROSS_VALIDATIONS
    return constants.RuleBasedValidation.DEFAULT_N_CROSS_VALIDATIONS
