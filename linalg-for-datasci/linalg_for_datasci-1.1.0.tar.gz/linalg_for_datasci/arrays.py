import numpy as np

from .tests import typecheck_column_vector
from .tests import typecheck_row_vector
from .tests import typecheck_vector


def vec_to_col(vector):
    typecheck_vector(vector)
    return vector.reshape((-1, 1))


def vec_to_row(vector):
    typecheck_vector(vector)
    return vector.reshape((1, -1))


def col_to_vec(column):
    typecheck_column_vector(column)
    return column.reshape((-1))


def row_to_vec(row):
    typecheck_row_vector(row)
    return row.reshape((-1))


from .tests import typecheck_matrix
from .tests import typecheck_array


def ignore_floating_point_error(array):
    typecheck_array(array)
    epsilon = 10 * np.finfo(np.float).eps
    # This line might be in-place and have unintended side effects
    array[np.abs(array) < epsilon] = 0
    return array


def permute_rows(matrix, permutation):
    """
    Given a permutation of the index set corresponding to the number of rows of a given matrix,
    permute the rows of the matrix using that permutation.
    """
    typecheck_matrix(matrix)
    try:
        typecheck_vector(permutation)
    except AssertionError:
        assert (
            type(permutation) == list
        ), "Permutation must be represented by a one-modal NumPy array or a list"
    # Permutation is of the same index set as number of rows of matrix
    height = matrix.shape[0]
    assert len(permutation) == height and np.allclose(
        np.sort(permutation), np.arange(height)
    ), "Permutation must be of the indices of the rows."
    return matrix[np.argsort(permutation), :]


def permute_columns(matrix, permutation):
    """
    Given a permutation of the index set corresponding to the number of columns of a given matrix,
    permute the columns of the matrix using that permutation.
    """
    typecheck_matrix(matrix)
    try:
        typecheck_vector(permutation)
    except AssertionError:
        assert (
            type(permutation) == list
        ), "Permutation must be represented by a one-modal NumPy array or a list"
    # Permutation is of the same index set as number of columns of matrix
    width = matrix.shape[1]
    assert len(permutation) == width and np.allclose(
        np.sort(permutation), np.arange(width)
    ), "Permutation must be of the indices of the columns."
    return matrix[:, np.argsort(permutation)]


# Helper function to stringify matrices in a prettier way
def stringify_matrix(A):
    typecheck_matrix(A)
    return "\n".join(
        [
            " ".join(["{:7.4f}".format(A[i, j]) for j in range(A.shape[1])])
            for i in range(A.shape[0])
        ]
    )
