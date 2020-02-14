# Lint as: python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Confusion matrix metrics."""

from __future__ import absolute_import
from __future__ import division
# Standard __future__ imports
from __future__ import print_function

from tensorflow_model_analysis.types_compat import Any, Callable, Dict, List, Optional, Text, Union

import numpy as np
from tensorflow_model_analysis import config
from tensorflow_model_analysis.metrics import binary_confusion_matrices
from tensorflow_model_analysis.metrics import metric_types
from tensorflow_model_analysis.metrics import metric_util
from tensorflow_model_analysis.proto import metrics_for_slice_pb2

SPECIFICITY_NAME = 'specificity'
FALL_OUT_NAME = 'fall_out'
MISS_RATE_NAME = 'miss_rate'
CONFUSION_MATRIX_AT_THRESHOLDS_NAME = 'confusion_matrix_at_thresholds'


class Specificity(metric_types.Metric):
  """Specificity (TNR) or selectivity."""

  def __init__(self,
               thresholds = None,
               name = SPECIFICITY_NAME):
    """Initializes specificity metric.

    Args:
      thresholds: Thresholds to use for specificity. Defaults to [0.5].
      name: Metric name.
    """
    super(Specificity, self).__init__(
        metric_util.merge_per_key_computations(_specificity),
        thresholds=thresholds,
        name=name)


metric_types.register_metric(Specificity)


def _specificity(
    thresholds = None,
    name = SPECIFICITY_NAME,
    eval_config = None,
    model_name = '',
    output_name = '',
    sub_key = None,
    class_weights = None
):
  """Returns metric computations for specificity."""

  def rate_fn(tp, tn, fp, fn):
    del tp, fn
    if tn + fp > 0.0:
      return tn / (tn + fp)
    else:
      return float('nan')

  return _rate(rate_fn, thresholds, name, eval_config, model_name, output_name,
               sub_key, class_weights)


class FallOut(metric_types.Metric):
  """Fall-out (FPR)."""

  def __init__(self,
               thresholds = None,
               name = FALL_OUT_NAME):
    """Initializes fall-out metric.

    Args:
      thresholds: Thresholds to use for fall-out. Defaults to [0.5].
      name: Metric name.
    """
    super(FallOut, self).__init__(
        metric_util.merge_per_key_computations(_fall_out),
        thresholds=thresholds,
        name=name)


metric_types.register_metric(FallOut)


def _fall_out(
    thresholds = None,
    name = FALL_OUT_NAME,
    eval_config = None,
    model_name = '',
    output_name = '',
    sub_key = None,
    class_weights = None
):
  """Returns metric computations for fall-out."""

  def rate_fn(tp, tn, fp, fn):
    del tp, fn
    if fp + tn > 0.0:
      return fp / (fp + tn)
    else:
      return float('nan')

  return _rate(rate_fn, thresholds, name, eval_config, model_name, output_name,
               sub_key, class_weights)


class MissRate(metric_types.Metric):
  """Miss rate (FNR)."""

  def __init__(self,
               thresholds = None,
               name = MISS_RATE_NAME):
    """Initializes miss rate metric.

    Args:
      thresholds: Thresholds to use for miss rate. Defaults to [0.5].
      name: Metric name.
    """
    super(MissRate, self).__init__(
        metric_util.merge_per_key_computations(_miss_rate),
        thresholds=thresholds,
        name=name)


metric_types.register_metric(MissRate)


def _miss_rate(
    thresholds = None,
    name = MISS_RATE_NAME,
    eval_config = None,
    model_name = '',
    output_name = '',
    sub_key = None,
    class_weights = None
):
  """Returns metric computations for miss rate."""

  def rate_fn(tp, tn, fp, fn):
    del tn, fp
    if fn + tp > 0.0:
      return fn / (fn + tp)
    else:
      return float('nan')

  return _rate(rate_fn, thresholds, name, eval_config, model_name, output_name,
               sub_key, class_weights)


def _rate(
    rate_fn,
    thresholds = None,
    name = '',
    eval_config = None,
    model_name = '',
    output_name = '',
    sub_key = None,
    class_weights = None
):
  """Returns rate based confusion matrix metric given rate_fn."""
  key = metric_types.MetricKey(
      name=name,
      model_name=model_name,
      output_name=output_name,
      sub_key=sub_key)

  if not thresholds:
    thresholds = [0.5]

  # Make sure matrices are calculated.
  matrices_computations = binary_confusion_matrices.binary_confusion_matrices(
      eval_config=eval_config,
      model_name=model_name,
      output_name=output_name,
      sub_key=sub_key,
      class_weights=class_weights,
      thresholds=thresholds)
  matrices_key = matrices_computations[-1].keys[-1]

  def result(
      metrics
  ):
    matrices = metrics[matrices_key]
    values = []
    for i in range(len(thresholds)):
      values.append(
          rate_fn(matrices.tp[i], matrices.tn[i], matrices.fp[i],
                  matrices.fn[i]))
    return {key: values[0] if len(thresholds) == 1 else np.array(values)}

  derived_computation = metric_types.DerivedMetricComputation(
      keys=[key], result=result)
  computations = matrices_computations
  computations.append(derived_computation)
  return computations


class ConfusionMatrixAtThresholds(metric_types.Metric):
  """Confusion matrix at thresholds."""

  def __init__(self,
               thresholds,
               name = CONFUSION_MATRIX_AT_THRESHOLDS_NAME):
    """Initializes confusion matrix at thresholds.

    Args:
      thresholds: Thresholds to use for confusion matrix.
      name: Metric name.
    """
    super(ConfusionMatrixAtThresholds, self).__init__(
        metric_util.merge_per_key_computations(_confusion_matrix_at_thresholds),
        thresholds=thresholds,
        name=name)


metric_types.register_metric(ConfusionMatrixAtThresholds)


def _confusion_matrix_at_thresholds(
    thresholds,
    name = CONFUSION_MATRIX_AT_THRESHOLDS_NAME,
    eval_config = None,
    model_name = '',
    output_name = '',
    sub_key = None,
    class_weights = None
):
  """Returns metric computations for confusion matrix at thresholds."""
  key = metric_types.MetricKey(
      name=name,
      model_name=model_name,
      output_name=output_name,
      sub_key=sub_key)

  # Make sure matrices are calculated.
  matrices_computations = binary_confusion_matrices.binary_confusion_matrices(
      eval_config=eval_config,
      model_name=model_name,
      output_name=output_name,
      sub_key=sub_key,
      class_weights=class_weights,
      thresholds=thresholds)
  matrices_key = matrices_computations[-1].keys[-1]

  def result(
      metrics
  ):
    return {key: to_proto(thresholds, metrics[matrices_key])}

  derived_computation = metric_types.DerivedMetricComputation(
      keys=[key], result=result)
  computations = matrices_computations
  computations.append(derived_computation)
  return computations


def to_proto(
    thresholds, matrices
):
  """Converts matrices into ConfusionMatrixAtThresholds proto.

  If precision or recall are undefined then 1.0 and 0.0 will be used.

  Args:
    thresholds: Thresholds.
    matrices: Confusion matrices.

  Returns:
    Matrices in ConfusionMatrixAtThresholds proto format.
  """
  pb = metrics_for_slice_pb2.ConfusionMatrixAtThresholds()
  for i, threshold in enumerate(thresholds):
    precision = 1.0
    if matrices.tp[i] + matrices.fp[i] > 0:
      precision = matrices.tp[i] / (matrices.tp[i] + matrices.fp[i])
    recall = 0.0
    if matrices.tp[i] + matrices.fn[i] > 0:
      recall = matrices.tp[i] / (matrices.tp[i] + matrices.fn[i])
    pb.matrices.add(
        threshold=round(threshold, 6),
        true_positives=matrices.tp[i],
        false_positives=matrices.fp[i],
        true_negatives=matrices.tn[i],
        false_negatives=matrices.fn[i],
        precision=precision,
        recall=recall)
  return pb
