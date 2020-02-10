# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""`LinearOperator` that wraps a [batch] matrix."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.python.internal.backend.numpy import dtype as dtypes
from tensorflow_probability.python.internal.backend.numpy import ops
from tensorflow_probability.python.internal.backend.numpy import numpy_array as array_ops
from tensorflow_probability.python.internal.backend.numpy import numpy_math as math_ops
from tensorflow_probability.python.internal.backend.numpy import linear_operator
from tensorflow_probability.python.internal.backend.numpy import linear_operator_util
# from tensorflow.python.util.tf_export import tf_export

__all__ = ["LinearOperatorFullMatrix"]


# @tf_export("linalg.LinearOperatorFullMatrix")
class LinearOperatorFullMatrix(linear_operator.LinearOperator):
  """`LinearOperator` that wraps a [batch] matrix.

  This operator wraps a [batch] matrix `A` (which is a `Tensor`) with shape
  `[B1,...,Bb, M, N]` for some `b >= 0`.  The first `b` indices index a
  batch member.  For every batch index `(i1,...,ib)`, `A[i1,...,ib, : :]` is
  an `M x N` matrix.

  ```python
  # Create a 2 x 2 linear operator.
  matrix = [[1., 2.], [3., 4.]]
  operator = LinearOperatorFullMatrix(matrix)

  operator.to_dense()
  ==> [[1., 2.]
       [3., 4.]]

  _ops.TensorShape(operator.shape)
  ==> [2, 2]

  operator.log_abs_determinant()
  ==> scalar Tensor

  x = ... Shape [2, 4] Tensor
  operator.matmul(x)
  ==> Shape [2, 4] Tensor

  # Create a [2, 3] batch of 4 x 4 linear operators.
  matrix = tf.random.normal(shape=[2, 3, 4, 4])
  operator = LinearOperatorFullMatrix(matrix)
  ```

  #### Shape compatibility

  This operator acts on [batch] matrix with compatible shape.
  `x` is a batch matrix with compatible shape for `matmul` and `solve` if

  ```
  _ops.TensorShape(operator.shape) = [B1,...,Bb] + [M, N],  with b >= 0
  _ops.TensorShape(x.shape) =        [B1,...,Bb] + [N, R],  with R >= 0.
  ```

  #### Performance

  `LinearOperatorFullMatrix` has exactly the same performance as would be
  achieved by using standard `TensorFlow` matrix ops.  Intelligent choices are
  made based on the following initialization hints.

  * If `dtype` is real, and `is_self_adjoint` and `is_positive_definite`, a
    Cholesky factorization is used for the determinant and solve.

  In all cases, suppose `operator` is a `LinearOperatorFullMatrix` of shape
  `[M, N]`, and `_ops.TensorShape(x.shape) = [N, R]`.  Then

  * `operator.matmul(x)` is `O(M * N * R)`.
  * If `M=N`, `operator.solve(x)` is `O(N^3 * R)`.
  * If `M=N`, `operator.determinant()` is `O(N^3)`.

  If instead `operator` and `x` have shape `[B1,...,Bb, M, N]` and
  `[B1,...,Bb, N, R]`, every operation increases in complexity by `B1*...*Bb`.

  #### Matrix property hints

  This `LinearOperator` is initialized with boolean flags of the form `is_X`,
  for `X = non_singular, self_adjoint, positive_definite, square`.
  These have the following meaning:

  * If `is_X == True`, callers should expect the operator to have the
    property `X`.  This is a promise that should be fulfilled, but is *not* a
    runtime assert.  For example, finite floating point precision may result
    in these promises being violated.
  * If `is_X == False`, callers should expect the operator to not have `X`.
  * If `is_X == None` (the default), callers should have no expectation either
    way.
  """

  def __init__(self,
               matrix,
               is_non_singular=None,
               is_self_adjoint=None,
               is_positive_definite=None,
               is_square=None,
               name="LinearOperatorFullMatrix"):
    r"""Initialize a `LinearOperatorFullMatrix`.

    Args:
      matrix:  Shape `[B1,...,Bb, M, N]` with `b >= 0`, `M, N >= 0`.
        Allowed dtypes: `float16`, `float32`, `float64`, `complex64`,
        `complex128`.
      is_non_singular:  Expect that this operator is non-singular.
      is_self_adjoint:  Expect that this operator is equal to its hermitian
        transpose.
      is_positive_definite:  Expect that this operator is positive definite,
        meaning the quadratic form `x^H A x` has positive real part for all
        nonzero `x`.  Note that we do not require the operator to be
        self-adjoint to be positive-definite.  See:
        https://en.wikipedia.org/wiki/Positive-definite_matrix#Extension_for_non-symmetric_matrices
      is_square:  Expect that this operator acts like square [batch] matrices.
      name: A name for this `LinearOperator`.

    Raises:
      TypeError:  If `diag.dtype` is not an allowed type.
    """

    with ops.name_scope(name, values=[matrix]):
      self._matrix = linear_operator_util.convert_nonref_to_tensor(
          matrix, name="matrix")
      self._check_matrix(self._matrix)

      super(LinearOperatorFullMatrix, self).__init__(
          dtype=self._matrix.dtype,
          graph_parents=None,
          is_non_singular=is_non_singular,
          is_self_adjoint=is_self_adjoint,
          is_positive_definite=is_positive_definite,
          is_square=is_square,
          name=name)
      # TODO(b/143910018) Remove graph_parents in V3.
      self._set_graph_parents([self._matrix])

  def _check_matrix(self, matrix):
    """Static check of the `matrix` argument."""
    allowed_dtypes = [
        dtypes.float16,
        dtypes.float32,
        dtypes.float64,
        dtypes.complex64,
        dtypes.complex128,
    ]

    matrix = ops.convert_to_tensor(matrix, name="matrix")

    dtype = matrix.dtype
    if dtype not in allowed_dtypes:
      raise TypeError(
          "Argument matrix must have dtype in %s.  Found: %s"
          % (allowed_dtypes, dtype))

    if _ops.TensorShape(matrix.shape).ndims is not None and _ops.TensorShape(matrix.shape).ndims < 2:
      raise ValueError(
          "Argument matrix must have at least 2 dimensions.  Found: %s"
          % matrix)

  def _shape(self):
    return _ops.TensorShape(self._matrix.shape)

  def _shape_tensor(self):
    return array_ops.shape(self._matrix)

  def _matmul(self, x, adjoint=False, adjoint_arg=False):
    return _linalg.matmul(
        self._matrix, x, adjoint_a=adjoint, adjoint_b=adjoint_arg)

  def _to_dense(self):
    return self._matrix

import numpy as np
from tensorflow_probability.python.internal.backend.numpy import linalg_impl as _linalg
from tensorflow_probability.python.internal.backend.numpy import ops as _ops

from tensorflow.python.util import lazy_loader
distribution_util = lazy_loader.LazyLoader(
    "distribution_util", globals(),
    "tensorflow_probability.python.internal._numpy.distribution_util")

