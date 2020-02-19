import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from typing import Union
import os

cur_dir = os.getcwd() 
figure_dir = os.path.join(cur_dir,'figures')

beta = 2
MIN, MAX = 0, 1
PARTS = 100
LABELS = ['$x_i$', '$x_j$', '$J$']
PROJECTION, CMAP, LW = '3d', 'terrain', 0.2

class Functions:
    def sigmoid(self, x: float) -> float:
        raise NotImplementedError

    def trust(self, x: float) -> float:
        raise NotImplementedError

    def softmax(self, x: float) -> float:
        raise NotImplementedError

    def tanh(self, x: float) -> float:
        raise NotImplementedError

    def arctan(self, x: float) -> float:
        raise NotImplementedError


def sig(x: float, beta: float = -1) -> float:
    return 1 / (1 + np.exp(beta * x))


class Gradients:
    def __init__(self):
        self.beta = 2

    def softmax(self, x: float) -> float:
        return np.exp(self.beta * x) / (np.exp(self.beta * x) + 1)

    def trust(self, x: float, beta: Union[None, float]=None) -> float:
        beta = self.beta if not beta else beta
        return (-beta * (x / (1 - x)) ** beta) / ((x - 1) * x * (1 + (x / (1 - x)) ** beta) ** 2)

    def sigmoid(self, x: float) -> float:
        return (sig(x, self.beta)) * (1 - (sig(x, self.beta)))

    def tanh(self, x: float) -> float:
        return (4 * np.exp(-2 * x)) / (np.exp(-2 * x) + 1) ** 2

    def arctan(self, x: float) -> float:
        return 1 / (1 + x ** 2)


class Surface:
    def trust(self, x: float, beta: float = 2.0) -> float:
        return Gradients().trust(x, beta)

    def evaluate(self, x: float, j: float, beta: float = 2.0) -> float:
        if x != j:
            y = abs(x - j)
            return self.trust(y, beta) * self.trust(x, beta)

    def generate(self, beta: float = 2) -> None:
        data = {}
        for x, j in list(itertools.permutations(np.linspace(MIN, MAX, PARTS), 2)):
            try:
                data[x, j] = self.evaluate(x, j, beta).astype(float)
            except AttributeError:
                pass
        df = pd.DataFrame(data).T.reset_index().dropna()
        df.columns = LABELS
        fig = plt.figure()
        ax = fig.gca(projection=PROJECTION)
        c1, c2, c3 = list(df.columns)
        ax.plot_trisurf(df[c1], df[c2], df[c3], cmap=CMAP, linewidth=LW)
        ax.set_xlabel(c1)
        ax.set_ylabel(c2)
        ax.set_zlabel(c3 + '({}, {})'.format(c1, c2))
        plt.savefig('{}surface.png'.format(config.figure_dir))
        plt.show()
