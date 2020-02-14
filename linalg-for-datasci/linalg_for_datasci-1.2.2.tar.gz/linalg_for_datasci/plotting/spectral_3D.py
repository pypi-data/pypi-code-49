import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from ..tests import typecheck_matrix
from ..tests import typecheck_vector


def plot_3D_vector(ax, vector, label="", color="k"):
    typecheck_vector(vector)
    assert len(vector) == 3
    origin = np.array([0, 0, 0])
    ax.quiver(*origin, *vector, color=color)
    if label:
        ax.text(*vector, label, color=color)


def plot_parallelepiped(ax, A):
    P = np.array(
        [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1],
        ]
    )
    P = (A @ P.T).T
    verts = [
        [P[0], P[1], P[2], P[3]],
        [P[4], P[5], P[6], P[7]],
        [P[0], P[1], P[5], P[4]],
        [P[2], P[3], P[7], P[6]],
        [P[1], P[2], P[6], P[5]],
        [P[4], P[7], P[3], P[0]],
    ]
    polygon_options = {"alpha": 0.1, "linewidths": 1, "edgecolors": "r"}
    pc = Poly3DCollection(verts, **polygon_options)
    pc.set_facecolor("cyan")
    ax.add_collection3d(pc)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")


def plot_3D_spectral_demo(
    transformation_matrix, eigenbasis_matrix, plot_size=3, eigvec_color="m"
):
    typecheck_matrix(transformation_matrix)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(-plot_size, plot_size)
    ax.set_ylim(-plot_size, plot_size)
    ax.set_zlim(-plot_size, plot_size)

    I = np.eye(3)
    transformed_eigenbasis_matrix = transformation_matrix @ eigenbasis_matrix

    plot_parallelepiped(ax, transformation_matrix)

    # plot unit vectors under transformation
    plot_3D_vector(ax, transformation_matrix[:, 0], "e1")
    plot_3D_vector(ax, transformation_matrix[:, 1], "e2")
    plot_3D_vector(ax, transformation_matrix[:, 2], "e3")

    # plot eigenbasis under transformation
    plot_3D_vector(ax, transformed_eigenbasis_matrix[:, 0], "v1", color=eigvec_color)
    plot_3D_vector(ax, transformed_eigenbasis_matrix[:, 1], "v2", color=eigvec_color)
    plot_3D_vector(ax, transformed_eigenbasis_matrix[:, 2], "v3", color=eigvec_color)
