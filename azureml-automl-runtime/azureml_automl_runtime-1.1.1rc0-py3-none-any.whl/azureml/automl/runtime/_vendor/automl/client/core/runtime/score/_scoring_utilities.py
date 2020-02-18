# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utilities for computing model evaluation metrics."""
import logging
import numpy as np
import sklearn.preprocessing

from sklearn.base import TransformerMixin
from typing import Any, Callable, Dict, Optional, Tuple, Type

from automl.client.core.common.exceptions import ClientException
from automl.client.core.runtime.score import _classification, _regression, _forecasting, constants
from automl.client.core.runtime.score._metric_base import Metric


def pad_predictions(y_pred_probs: np.ndarray,
                    trained_labels: Optional[np.ndarray],
                    class_labels: Optional[np.ndarray]) -> np.ndarray:
    """
    Add padding to the predicted probabilities for missing training classes.

    If the model is not trained on every class from the dataset it will not
    predict those missing classes.
    Here we insert columns of all zeros for those classes on which the model was not trained.
    Effectively, the model predicts these classes with zero probability.

    :param y_pred_probs: Predictions from a classification model
    :param trained_labels: The class labels on which the model was trained
    :param class_labels: The class labels from the full dataset
    :return: Padded predicted probabilities
    """
    if trained_labels is None or class_labels is None:
        return y_pred_probs
    if len(trained_labels) == len(class_labels):
        return y_pred_probs
    if np.setdiff1d(trained_labels, class_labels).shape[0] > 0:
        raise ClientException("Trained labels must all exist in class labels")

    new_y_pred_probs_trans = []
    for class_label in class_labels:
        found = False
        for trained_index, trained_label in enumerate(trained_labels):
            if class_label == trained_label:
                new_y_pred_probs_trans.append(y_pred_probs.T[trained_index])
                found = True
                break
        if not found:
            new_y_pred_probs_trans.append(np.zeros((y_pred_probs.shape[0],)))
    return np.array(new_y_pred_probs_trans).T


def total_variance(counts, means, variances):
    """
    Compute total population variance.

    Computes the variance of a population given the counts, means, and
    variances of several sub-populations.
    This uses the law of total variance:
    `https://en.wikipedia.org/wiki/Law_of_total_variance`
    var(y) = E[var(y|x)] + var(E[y|x])
        y: predicted value
        x: cross-validation index

    var(y|x) = variances
    E[y|x] = means
    E[var(y|x)] = np.sum(counts * variances) / total_count
    var(E[y|x]) = np.sum(counts * (means - total_mean) ** 2) / total_count
    """
    total_count = np.sum(counts)
    total_mean = np.sum(counts * means) / total_count
    unweighted_vars = variances + (means - total_mean) ** 2
    total_var = np.sum(counts * unweighted_vars) / total_count
    return total_var


class LabelEncodingBinarizer(TransformerMixin):
    """
    Wrapper for sklearn binarizer.

    This wrapper can transform floats, strings, and ints.
    By default, sklearn does not support binarizing floats because they are not
    standard label types. AutoML supports float class labels, so this binarizer
    should be used in those cases.
    """

    def __init__(self):
        """Construct a LabelEncodingBinarizer."""
        self._encoder = sklearn.preprocessing.LabelEncoder()
        self._binarizer = sklearn.preprocessing.LabelBinarizer()

    def fit(self, fit_values: np.ndarray) -> None:
        """
        Fit the LabelEncodingBinarizer to some labels.

        :param fit_values: Values on which to fit the tranformer.
            These can be of type int, string, or float
        """
        self._binarizer.fit(self._encoder.fit_transform(fit_values))

    def transform(self, transform_values: np.ndarray) -> np.ndarray:
        """
        Transform labels with the encoding binarizer.

        :param transform_values: Values to transform to a one-hot encoding.
        :return: One hot encoding of the values.
        """
        return self._binarizer.transform(self._encoder.transform(transform_values))

    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        """
        Encode and binarize labels.

        :param values: Values to fit_transform.
        :return: The transformed values.
        """
        encoded = self._encoder.fit_transform(values)
        return self._binarizer.fit_transform(encoded)


def class_averaged_score(score_func: Callable[..., float],
                         y_test_bin: np.ndarray,
                         y_pred_proba: np.ndarray,
                         class_labels: np.ndarray,
                         test_class_labels: np.ndarray,
                         average: str,
                         metric_name: str,
                         logger: Optional[logging.Logger] = None,
                         **kwargs: Dict[str, Any]) -> float:
    """
    Calculate class-averaged metrics like AUC_weighted only on classes present in the validation set.

    For the case when a model was trained on more classes than what the validation set contains
    we will only average over those classes present in the validation set.

    Note that this implementation assumes that the y_pred_proba and y_test_bin matrices have padding so that
    there is a column for all classes present in the entire dataset.  Thus, each column should map to
    the class_labels array.

    Example.
    Dataset classes: 0, 1, 2, 3, 4
    Training classes: 0, 1, 2, 3, 4
    Validation classes: 0, 1, 2, 4

    Initial predicted probabilities: (columns ordered by ascending labels)
    [[.25,  .2,  .3,   0, .25],
     [  0, .25,   0, .25,  .5],
     [.33, .33, .34,   0,  .0],
     [  0,  .7,   0,  .3,   0],
     [.25,  .3,   0,  .2, .25]]

    In this example the model was trained on all classes from the dataset, but class 3 was left
    out of the validation set. There is no meaningful interpretation for the score of class 3,
    so the column for label 3 of the predicted probabilities is dropped from the calculation (see below).

    Resulting predicted probabilities:
    [[.25,  .2,  .3, .25],
     [  0, .25,   0,  .5],
     [.33, .33, .34,  .0],
     [  0,  .7,   0,   0],
     [.25,  .3,   0, .25]]

    From this new matrix of predicted probabilities the class-averaged metrics are calculated normally by sklearn.

    :param score_func: sklearn score function that has an api like sklearn.metrics.roc_auc_score
    :param y_test_bin: Test class label indicator matrix of shape (n_test_examples, len(class_labels))
    :param y_pred_proba: Predicted probability matrix from X_test, shape (n_test_examples, len(class_labels))
    :param class_labels: Class labels present the entire dataset.
    :param test_class_labels: Class labels present in the validation set.
    :param average: Averaging strategy (e.g. "micro", "macro", etc.)
    :param metric_name: Name of the metric.
    :param kwargs: Extra keyword arguments to be passed into score_func.
    :return: the output of score_func
    """
    n_classes = len(class_labels)

    # Micro averaging does not perform class level averaging, so handling imbalanced classes is not needed
    if average != "micro" and n_classes > 2:
        # Assert that padding logic worked correctly
        y_test_bin_padded = y_test_bin.shape[1] == n_classes if y_test_bin.ndim == 2 else False
        y_pred_proba_padded = y_pred_proba.shape[1] == n_classes if y_pred_proba.ndim == 2 else False

        msg = "len(class_labels) = {} should correpond to {}'s shape of = {}"
        assert y_test_bin_padded, msg.format(len(class_labels), "y_test_bin", y_test_bin.shape)
        assert y_pred_proba_padded, msg.format(len(class_labels), "y_pred_proba", y_pred_proba.shape)

        # Intersection logic for only scoring on classes present in test set
        intersection_labels = np.intersect1d(test_class_labels, class_labels)
        intersection_indices = np.array([i for i, val in enumerate(class_labels) if val in intersection_labels])
        dropped_classes = [_class for _class in class_labels if _class not in intersection_labels]
        if len(dropped_classes) > 0:
            dropped_msg_fmt = "For {} classes not found in the validation set were ignored."
            dropped_msg = dropped_msg_fmt.format(metric_name)
            if logger is not None:
                logger.info(dropped_msg)

        y_test_bin = y_test_bin[:, intersection_indices]
        y_pred_proba = y_pred_proba[:, intersection_indices]

    if metric_name == constants.NORM_MACRO_RECALL:
        n_classes = y_test_bin.shape[1]
        return score_func(y_test_bin, y_pred_proba, n_classes=n_classes, logger=logger, **kwargs)
    else:
        # Else no intersection is performed we proceed with normal metric computation
        return score_func(y_test_bin, y_pred_proba, average=average, **kwargs)


def get_metric_class(metric_name):
    """
    Return the metric class based on the constant name of the metric.

    :param metric: the constant name of the metric
    :return: the class of the metric
    """
    classification_classes = {
        constants.ACCURACY: _classification.Accuracy,
        constants.WEIGHTED_ACCURACY: _classification.WeightedAccuracy,
        constants.BALANCED_ACCURACY: _classification.BalancedAccuracy,
        constants.NORM_MACRO_RECALL: _classification.NormMacroRecall,
        constants.LOG_LOSS: _classification.LogLoss,
        constants.AUC_MACRO: _classification.AUCMacro,
        constants.AUC_MICRO: _classification.AUCMicro,
        constants.AUC_WEIGHTED: _classification.AUCWeighted,
        constants.AVERAGE_PRECISION_MACRO: _classification.AveragePrecisionMacro,
        constants.AVERAGE_PRECISION_MICRO: _classification.AveragePrecisionMicro,
        constants.AVERAGE_PRECISION_WEIGHTED: _classification.AveragePrecisionWeighted,
        constants.MATTHEWS_CORRELATION: _classification.MatthewsCorrelation,
        constants.F1_MACRO: _classification.F1Macro,
        constants.F1_MICRO: _classification.F1Micro,
        constants.F1_WEIGHTED: _classification.F1Weighted,
        constants.PRECISION_MACRO: _classification.PrecisionMacro,
        constants.PRECISION_MICRO: _classification.PrecisionMicro,
        constants.PRECISION_WEIGHTED: _classification.PrecisionWeighted,
        constants.RECALL_MACRO: _classification.RecallMacro,
        constants.RECALL_MICRO: _classification.RecallMicro,
        constants.RECALL_WEIGHTED: _classification.RecallWeighted,
        constants.ACCURACY_TABLE: _classification.AccuracyTable,
        constants.CONFUSION_MATRIX: _classification.ConfusionMatrix
    }      # type: Dict[str, Type[Metric]]
    regression_classes = {
        constants.EXPLAINED_VARIANCE: _regression.ExplainedVariance,
        constants.R2_SCORE: _regression.R2,
        constants.SPEARMAN: _regression.Spearman,
        constants.RMSLE: _regression.RMSLE,
        constants.NORM_RMSLE: _regression.NormRMSLE,
        constants.RMSE: _regression.RMSE,
        constants.NORM_RMSE: _regression.NormRMSE,
        constants.MEAN_ABS_ERROR: _regression.MeanAbsoluteError,
        constants.NORM_MEAN_ABS_ERROR: _regression.NormMeanAbsoluteError,
        constants.MEDIAN_ABS_ERROR: _regression.MedianAbsoluteError,
        constants.NORM_MEDIAN_ABS_ERROR: _regression.NormMedianAbsoluteError,
        constants.MAPE: _regression.MAPE,
        constants.RESIDUALS: _regression.Residuals,
        constants.PREDICTED_TRUE: _regression.PredictedTrue
    }      # type: Dict[str, Type[Metric]]
    forecasting_classes = {
        constants.FORECASTING_RESIDUALS: _forecasting.ForecastResiduals,
        constants.FORECASTING_MAPE: _forecasting.ForecastMAPE
    }      # type: Dict[str, Type[Metric]]
    class_map = dict()      # type: Dict[str, Type[Metric]]
    class_map.update(classification_classes)
    class_map.update(regression_classes)
    class_map.update(forecasting_classes)

    if metric_name not in class_map:
        raise ValueError("Metric class {} was not found in \
                            Metric.get_metric_class".format(metric_name))
    return class_map[metric_name]


def make_json_safe(o: Any) -> Any:
    """
    Convert a value into something that is safe to parse into JSON.

    :param o: Object to make JSON safe.
    :return: New object
    """
    scalar_types = [int, float, str, type(None)]
    if type(o) in scalar_types:
        return o
    elif isinstance(o, dict):
        return {k: make_json_safe(v) for k, v in o.items()}
    elif isinstance(o, list):
        return [make_json_safe(v) for v in o]
    elif isinstance(o, tuple):
        return tuple(make_json_safe(v) for v in o)
    elif isinstance(o, np.ndarray):
        return make_json_safe(o.tolist())
    else:
        # If item is a numpy scalar type try to convert it to python builtin
        try:
            return o.item()
        except Exception as e:
            raise ValueError("Cannot encode type {}".format(type(o))) from e


def classification_label_decode(y_transformer: Optional[TransformerMixin],
                                y_test: np.ndarray,
                                y_pred: np.ndarray,
                                class_labels: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Decode classification labels if a y_transformer is passed.

    This is important for non-scalar metrics, which require the actual labels so that charts
    can be displayed with the correct user-provided labels.

    :param y_transformer: sklearn LabelEncoder transformer
    :param y_test: Actual targets.
    :param y_pred: Predicted targets.
    :param class_labels: All classes found in the full dataset.
    :return: The labels that have been decoded as a tuple.
    """
    if y_transformer is None:
        return y_test, y_pred, class_labels

    y_test_original = y_transformer.inverse_transform(y_test)
    y_pred_original = y_transformer.inverse_transform(y_pred)
    class_labels_original = y_transformer.inverse_transform(class_labels)
    return y_test_original, y_pred_original, class_labels_original


def classification_label_encode(y_test: np.ndarray,
                                y_pred: np.ndarray,
                                class_labels: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Encode classification labels that are strings, floats, or negative integers.

    This allows sklearn to operate on integer labels which is the most common format.
    :param y_test: Actual targets.
    :param y_pred: Predicted targets.
    :param class_labels: All classes found in the full dataset.
    :return: The labels that have been encoded as a tuple.
    """
    metrics_transformer = sklearn.preprocessing.LabelEncoder()
    metrics_transformer.fit(class_labels)
    y_test_encoded = metrics_transformer.transform(y_test)
    y_pred_encoded = metrics_transformer.transform(y_pred)
    class_labels_encoded = metrics_transformer.transform(class_labels)
    return y_test_encoded, y_pred_encoded, class_labels_encoded
