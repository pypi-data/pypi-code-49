import numpy as np
import pandas as pd


def typecheck_array(array, name="array"):
    assert isinstance(
        array, np.ndarray
    ), "{} must be represented as a NumPy array".format(name)


def typecheck_vector(vector, name="vector"):
    typecheck_array(vector, name=name)
    assert (
        len(vector.shape) == 1
    ), "{} must be represented as a one-modal NumPy array".format(name)


def typecheck_unit_vector(vector, name="vector"):
    typecheck_vector(vector, name=name)
    assert np.isclose(np.linalg.norm(vector), 1), "{} must have unit norm".format(name)


def typecheck_vector_pair(
    vector1, vector2, name1="first vector", name2="second vector"
):
    typecheck_vector(vector1)
    typecheck_vector(vector2)
    assert len(vector1) == len(vector2), "{} and {} must have the same length".format(
        name1, name2
    )


def typecheck_matrix(matrix, name="matrix"):
    typecheck_array(matrix, name=name)
    assert (
        len(matrix.shape) == 2
    ), "{} must be represented as a two-modal NumPy array".format(name)


def typecheck_column_vector(column, name="column"):
    typecheck_matrix(column, name=name)
    assert (column.shape)[
        1
    ] == 1, "{} must be represented as a column vector, i.e. a matrix with a single column".format(
        name
    )


def typecheck_row_vector(row, name="row"):
    typecheck_matrix(row, name=name)
    assert (row.shape)[
        0
    ] == 1, "{} must be represented as a row vector, i.e. a matrix with a single row".format(
        name
    )


def typecheck_square_matrix(matrix, name="matrix"):
    typecheck_matrix(matrix, name=name)
    assert (matrix.shape)[0] == (matrix.shape)[
        1
    ], "In order for {} to be square, its height and width must be the same".format(
        name
    )


def typecheck_symmetric_matrix(matrix, name="matrix"):
    typecheck_square_matrix(matrix, name=name)
    assert np.allclose(
        matrix, matrix.T
    ), "In order for {} to be symmetric, it must equal its own transpose".format(name)


def typecheck_basis(basis, dimension=None):
    """
    `basis` should be list or NumPy array of vectors, i.e. one-dimensional NumPy arrays
    No check for linear independence because of laziness and not wanting to waste compute.
    """
    if dimension:
        assert len(basis) == dimension
    else:
        dimension = len(basis)
    assert isinstance(basis, (list, np.ndarray))
    for vector in basis:
        typecheck_vector(vector)
        assert len(vector) == dimension


def typecheck_dataframe(dataset, name="dataset"):
    assert isinstance(
        dataset, pd.DataFrame
    ), "{} must be represented as a Pandas DataFrame".format(name)


def typecheck_dataframe_row(dataset_row, name="dataset row"):
    typecheck_dataframe(dataset_row, name=name)
    assert (
        len(row.index) == 1
    ), "{} must be represented by a Pandas DataFrame with a single row".format(name)


def typecheck_series(dataset, name="dataset"):
    assert isinstance(
        dataset, pd.Series
    ), "{} must be represented by a Pandas Series".format(name)
