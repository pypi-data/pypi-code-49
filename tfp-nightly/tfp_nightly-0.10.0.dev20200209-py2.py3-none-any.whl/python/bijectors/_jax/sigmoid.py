# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Sigmoid bijector."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.python.internal.backend.jax.compat import v2 as tf
from tensorflow_probability.python.bijectors._jax import bijector
from tensorflow_probability.python.internal._jax import assert_util
from tensorflow_probability.python.internal._jax import tensor_util


__all__ = [
    'Sigmoid',
]


class Sigmoid(bijector.Bijector):
  """Bijector that computes the logistic sigmoid function.

  If the `low` and `high` parameters are not passed, the transformation is
  equivalent to `Y = g(X) = 1 / (1 + exp(-X))`, the same as `tf.sigmoid`.

  If the `low` and `high` parameters are passed, the transformation is
  equivalent to `low + (high - low) * g(X)` (with `g(X)` as defined above),
  a sigmoid that is shifted and scaled along the output axis. This is
  implemented as `high * g(X) + low * g(-X)`, which is more numerically
  stable than direct shifting and scaling.
  """

  def __init__(self, low=None, high=None, validate_args=False, name='sigmoid'):
    """Initialize a `Sigmoid` bijector.

    Args:
      low: Floating point tensor or `None`, lower boundary of the output
        interval. If `None`, the implied default is `0.`. Either both or neither
        of `low` and `high` must be specified. If specified, Must have
        `low < high`.
      high: Floating point tensor or `None`, upper boundary of the output
        interval. if `None`, the implied default is `1.`. Either both or neither
        of `low` and `high` must be specified. If specified, must have
        `low < high`.
      validate_args: Python `bool`, default `False`. When `True` bijector
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      ValueError: If exactly one of `low` and `high` is specified.
    """
    parameters = dict(locals())
    with tf.name_scope(name) as name:
      if low is None and high is None:
        self._is_standard_sigmoid = True
      elif low is not None and high is not None:
        self._is_standard_sigmoid = False
      else:
        raise ValueError(
            'Either both or neither of `low` and `high` must be passed. '
            'Received `low={}`, `high={}`'.format(low, high))

      self._low = tensor_util.convert_nonref_to_tensor(low)
      self._high = tensor_util.convert_nonref_to_tensor(high)
      super(Sigmoid, self).__init__(
          forward_min_event_ndims=0,
          validate_args=validate_args,
          parameters=parameters,
          name=name)

  @classmethod
  def _is_increasing(cls):
    return True

  @property
  def low(self):
    return self._low

  @property
  def high(self):
    return self._high

  def _forward(self, x):
    if self._is_standard_sigmoid:
      return tf.sigmoid(x)
    lo = tf.convert_to_tensor(self.low)  # Concretize only once
    hi = tf.convert_to_tensor(self.high)
    diff = hi - lo
    left = lo + diff * tf.math.sigmoid(x)
    right = hi - diff * tf.math.sigmoid(-x)
    return tf.where(x < 0, left, right)
    # Alternative:
    #   ans = hi * tf.sigmoid(x) + lo * tf.sigmoid(-x)
    #   return tfp_math.clip_by_value_preserve_gradient(ans, lo, hi)
    # Apparent pros of this alternative
    # - 2 fewer subtracts and 1 fewer tf.where, but another add and
    #   tf.clip_by_value
    # - The answer obviously falls into [lo, hi]
    # Apparent cons of this alternative
    # - Messing around with clipping and stopping gradients
    # - Suppresses any potential severe numerical errors

  def _inverse(self, y):
    if self._is_standard_sigmoid:
      return tf.math.log(y) - tf.math.log1p(-y)
    return tf.math.log(y - self.low) - tf.math.log(self.high - y)

  # We implicitly rely on _forward_log_det_jacobian rather than explicitly
  # implement _inverse_log_det_jacobian since directly using
  # `-tf.log(y) - tf.log1p(-y)` (or `tf.log(high - low) - tf.log(y - low) -
  # tf.log(high - y)`) has lower numerical precision.

  def _forward_log_det_jacobian(self, x):
    sigmoid_fldj = -tf.math.softplus(-x) - tf.math.softplus(x)
    if self._is_standard_sigmoid:
      return sigmoid_fldj
    return sigmoid_fldj + tf.math.log(self.high - self.low)

  def _parameter_control_dependencies(self, is_init):
    if not self.validate_args or self._is_standard_sigmoid:
      return []
    assertions = []
    if is_init != (tensor_util.is_ref(self.high) or
                   tensor_util.is_ref(self.low)):
      assertions.append(assert_util.assert_less(
          self.low, self.high,
          message='`Sigmoid` is not defined when `low` >= `high`.'))
    return assertions

