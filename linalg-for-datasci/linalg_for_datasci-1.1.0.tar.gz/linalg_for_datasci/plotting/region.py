import matplotlib.pyplot as plt
import numpy as np

from ..tests import typecheck_basis
from ..tests import typecheck_matrix
from .two_dimensional import plot_vector


def plot_region_with_func_random_pts(linear_function, n=10000, plot_size=5):
    typecheck_matrix(linear_function)
    pts = np.random.rand(2, 10000) * 2 - 1
    fig, axs = plt.subplots(1, 2, subplot_kw={"aspect": "equal"})

    xs = pts[0, :]
    ys = pts[1, :]
    axs[0].set_xlim(-plot_size, plot_size)
    axs[0].set_ylim(-plot_size, plot_size)
    axs[0].scatter(xs, ys)
    axs[0].set_xlabel("$x_1$ value")
    axs[0].set_ylabel("$x_2$ value")
    axs[0].set_title("Before linear function")

    img = linear_function @ pts
    x_img = img[0, :]
    y_img = img[1, :]
    axs[1].set_xlim(-plot_size, plot_size)
    axs[1].set_ylim(-plot_size, plot_size)
    axs[1].scatter(x_img, y_img)
    axs[1].set_xlabel("$x_1$ value")
    axs[1].set_ylabel("$x_2$ value")
    axs[1].set_title("After linear function")

    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
    plt.subplots_adjust(wspace=0.5)


def plot_region_with_func(
    linear_function,
    title="Vectors after being modified by linear function",
    colors=["r", "y", "g", "b"],
    basis_scale=1.5,
    alpha=0.3,
    plot_axis=True,
    fig=None,
    ax=None,
    plot_size=5,
):

    if not fig or not ax:
        fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
    ax.set_title(title)

    typecheck_matrix(linear_function)

    quad1_x = np.array([0, 1, 1, 0])
    quad1_y = np.array([0, 0, 1, 1])
    quad2_x = np.array([0, -1, -1, 0])
    quad2_y = np.array([0, 0, 1, 1])
    quad3_x = np.array([0, -1, -1, 0])
    quad3_y = np.array([0, 0, -1, -1])
    quad4_x = np.array([0, 1, 1, 0])
    quad4_y = np.array([0, 0, -1, -1])

    xs = (quad1_x, quad2_x, quad3_x, quad4_x)
    ys = (quad1_y, quad2_y, quad3_y, quad4_y)

    ax.set_xlabel("$x_1$ value")
    ax.set_ylabel("$x_2$ value")

    X = np.array([np.hstack(xs), np.hstack(ys)])
    X = linear_function @ X
    ax.set_xlim(-plot_size, plot_size)
    ax.set_ylim(-plot_size, plot_size)
    polygons = []
    for i, x_list in enumerate(xs):
        n = len(x_list)
        region = X[:, :n]
        X = X[:, n:]
        x = region[0, :]
        y = region[1, :]
        color = colors[i % len(colors)]
        [polygon] = ax.fill(x, y, color)
        polygons.append(polygon)
    _ = [polygon.set_alpha(alpha) for polygon in polygons]

    if plot_axis:
        plot_vector(ax, linear_function[:, 0], label="e1")
        plot_vector(ax, linear_function[:, 1], label="e2")


def plot_region_with_two_basises(
    linear_function,
    title,
    alternative_basis,
    standard_basis,
    fig=None,
    ax=None,
    plot_size=5,
):
    typecheck_matrix(linear_function)
    typecheck_basis(alternative_basis, dimension=2)
    typecheck_basis(standard_basis, dimension=2)

    if not fig or not ax:
        fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})

    plot_region_with_func(
        linear_function, title, plot_axis=False, fig=fig, ax=ax, plot_size=plot_size
    )

    plot_vector(ax, alternative_basis[0], color="m", label="v1")
    plot_vector(ax, alternative_basis[1], color="m", label="v2")

    plot_vector(ax, standard_basis[0], label="e1")
    plot_vector(ax, standard_basis[1], label="e2")
