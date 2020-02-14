import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

##### TODO: Implement something like this in plotly and compare whether it looks better?


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


def plot_3D_with_arrows(data, arrows=None, size=5, title="Scatter Plot of Data"):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.set_zlim(-size, size)
    plt.rcParams["legend.fontsize"] = 10
    plot_options = {
        "markersize": 7,
        "color": "blue",
        "alpha": 0.2,
        "label": "observation",
    }
    ax.plot(data[0, :], data[1, :], data[2, :], "o", **plot_options)
    ax.set_title(title)
    ax.legend(loc="upper right")

    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")

    if arrows is not None:
        mu_x = np.mean(data[0, :])
        mu_y = np.mean(data[1, :])
        mu_z = np.mean(data[2, :])

        arrow_options = {
            "mutation_scale": 25,
            "lw": 3,
            "arrowstyle": "->",
            "color": "r",
        }
        for arrow in arrows:
            ax.add_artist(
                Arrow3D(
                    [mu_x, arrow[0]],
                    [mu_y, arrow[1]],
                    [mu_z, arrow[2]],
                    **arrow_options
                )
            )

    plt.show()
