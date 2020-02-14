import numpy as np

from ..tests import typecheck_series
from ..tests import typecheck_vector
from .utils import angle_of
from .utils import get_2D_rotation_matrix


def circle_to_double_shell(vector):
    try:
        typecheck_vector(vector)
    except AssertionError:
        typecheck_series(vector)
    angle = angle_of(vector)
    # Scalar multiple needs to be some pi-periodic function of angle
    sawtooth = lambda theta: (theta) % np.pi
    scalar_multiple = sawtooth(angle)
    return scalar_multiple * vector


def circle_to_diamond(vector):
    try:
        typecheck_vector(vector)
    except AssertionError:
        typecheck_series(vector)
    angle = angle_of(vector)
    scalar_multiple = 1 / (np.abs(np.cos(angle)) + np.abs(np.sin(angle)))
    return scalar_multiple * vector


unit_diagonal = np.array([np.sqrt(2) / 2, np.sqrt(2) / 2])
projection_onto_diagonal = lambda vector: np.dot(vector, unit_diagonal) * unit_diagonal

reflection_matrix = np.array([[-1, 0], [0, 1]])
reflect_over_vertical_axis = lambda vector: reflection_matrix @ vector

rotate_45_ccw = lambda vector: get_2D_rotation_matrix(45) @ vector

shear_matrix = np.array([[1, 0], [3, 1]])
shear_vertically = lambda vector: shear_matrix @ vector
