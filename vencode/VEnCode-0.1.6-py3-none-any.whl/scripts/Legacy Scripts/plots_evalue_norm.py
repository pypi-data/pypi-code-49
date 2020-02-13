"""
Plotting module
"""
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Plots3D():
    @staticmethod
    def helper(x, y):
        coefs = {"a": -164054.1, "b": 0.9998811, "c": 0.000006088948, "d": 1.00051, "m": 0.9527, "e": -0.1131}
        return (coefs["m"] * y + coefs["e"]) * x ** (
            coefs["d"] + ((coefs["a"] - coefs["d"]) / (1 + (y / coefs["c"]) ** coefs["b"])))

    @staticmethod
    def plot_scatter():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_prep = [20, 80, 100, 154, 200, 250, 350, 450, 550, 650, 800, 1000]
        xs = [i for i in x_prep for _ in range(12)]
        ys = list(range(1, 13))*12
        zs = [Plots3D.helper(x, y) for x, y in zip(xs, ys)]

        ax.scatter(xs, ys, zs)

        ax.set_xlabel('Number of cell types')
        ax.set_ylabel('k number')
        ax.set_zlabel('E Value')

        plt.show()

    @staticmethod
    def plot_surface():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_prep = np.array([20, 80, 100, 154, 200, 250, 350, 450, 550, 650, 800, 1000])
        x_prep_2 = np.arange(10, 1000, 10)
        y_prep = np.arange(1, 13, 0.12)
        xs,ys = np.meshgrid(x_prep_2, y_prep)
        z_prep = np.array([Plots3D.helper(x,y) for x,y in zip(np.ravel(xs), np.ravel(ys))])
        zs = z_prep.reshape(xs.shape)

        ax.plot_surface(xs, ys, zs, cmap="viridis")

        ax.set_xlabel('Number of cell types')
        ax.set_ylabel('k number')
        ax.set_zlabel('E Value')

        plt.show()
