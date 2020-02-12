import numpy as np

from .arrays import col_to_vec
from .arrays import vec_to_col
from .tests import typecheck_basis
from .tests import typecheck_symmetric_matrix


def Rx(theta):
    return np.array(
        [
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta), np.cos(theta)],
        ]
    )


def Ry(theta):
    return np.array(
        [
            [np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)],
        ]
    )


def Rz(theta):
    return np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )


def get_2D_rotation_matrix(deg):
    theta = np.radians(deg)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    return R


# 2D spectral demo
import math


def angle_of(v):
    u = v / np.linalg.norm(v)
    return math.atan2(u[1], u[0])


def get_angle_of_rot_mat(U):
    return math.degrees(angle_of(U[:, 0]))


def get_parts_for_diagonalization_demo(A):
    typecheck_symmetric_matrix(A)

    d, V = np.linalg.eigh(A)
    d = np.flip(d, axis=0)
    V = np.flip(V, axis=1)
    V *= np.sign(V[0, 0])
    angle = get_angle_of_rot_mat(V)

    v1 = V[:, 0]
    v2 = V[:, 1]
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    return d, V, v1, v2, e1, e2, angle


def apply_func_to_basis(linear_function, basis):
    typecheck_basis(basis)
    transformed_basis = []
    for vector in basis:
        transformed_vector = linear_function @ vec_to_col(vector)
        transformed_basis.append(col_to_vec(transformed_vector))
    typecheck_basis(transformed_basis)
    return transformed_basis
