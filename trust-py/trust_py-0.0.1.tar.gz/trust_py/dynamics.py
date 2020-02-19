import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import math
import sys
from typing import *

plt.style.use('ggplot')


a, b = 0, 1
n, beta, tmax, t_weight = 3, 2, 500, 1
w = 1 / n


class Functions:
    def sigmoid(self, x: float) -> float:
        return 1 / (1 + np.exp(x))

    def swish(self, x: float, beta: float = 2) -> float:
        return x * self.sigmoid(x * beta)

    def trust(self, x: float) -> float:
        raise NotImplementedError

    def softmax(self, x: float) -> float:
        raise NotImplementedError

    def tanh(self, x: float, alpha: float) -> float:
        return math.tanh(math.sqrt(2 / math.pi) * (x + alpha * x ** 3))

    def arctan(self, x: float) -> float:
        raise NotImplementedError

    def relu(self, x: float) -> float:
        return x * (x > 0)

    def lrelu(self, x: float, alpha: float = 0.01) -> float:
        return (x * (x > 0)) + (alpha * (x <= 0))

    def prelu(self, x: float, alpha: float = 0.01) -> float:
        return (x * (x > 0)) + (alpha * x * (x <= 0))

    def elu(self, x: float, alpha: float = 0.01) -> float:
        return (x * (x > 0)) + (alpha * (np.exp(x) - 1) * (x <= 0))

    def selu(self, x: float, alpha: float = 0.01) -> float:
        return (x * (x > 0)) + (alpha * (np.exp(x) - 1) * (x <= 0))

    def gelu(self, x: float, alpha: float = 0.01) -> float:
        return 0.5 * x * (1 + self.tanh(x * 0.7978845608 * (1 + 0.044715 * x * x)))


def sig(x: float, beta: float = -1) -> float:
    return 1 / (1 + np.exp(beta * x))


class Gradients:
    def __init__(self):
        self.beta = 2

    def softmax(self, x: float) -> float:
        return np.exp(self.beta * x) / (np.exp(self.beta * x) + 1)

    def trust(self, x: float) -> float:
        return (-self.beta * (x / (1 - x)) ** self.beta) / ((x - 1) * x * (1 + (x / (1 - x)) ** self.beta) ** 2)

    def sigmoid(self, x: float) -> float:
        return (sig(x)) * (1 - (sig(x)))

    def swish(self, x: float) -> float:
        return self.beta * Functions().swish(x) + (Functions().sigmoid(x * self.beta) *(1 - self.beta * Functions().swish(x)))

    def tanh(self, x: float) -> float:
        return (4 * np.exp(-2 * x)) / (np.exp(-2 * x) + 1) ** 2

    def arctan(self, x: float) -> float:
        return 1 / (1 + x ** 2)

    def relu(self, x: float) -> float:
        if x > 0:
            x = 1
        else:
            x = 0
        return x

    def lrelu(self, x: float, alpha: float = 0.01) -> float:
        if x < 0:
            x = alpha
        else:
            x = 1
        return x

    def prelu(self, x: float, alpha: float = 0.01) -> float:
        x = 1
        if x < 0:
            x = alpha * x
        return x

    def elu(self, x: float, alpha: float = 0.01) -> float:
        x = 1
        if x < 0:
            x = alpha * np.exp(x)
        return x

    def gelu(self, x: float, alpha: float = 0.01) -> float:
        return 1 / (
            np.exp(-(56146134542243 * x * ((6444110634811895 * x ** 2) / 144115188075855872 + 1)) / 35184372088832) + 1) + \
            (x * np.exp(-(56146134542243 * x * ((6444110634811895 * x ** 2) / 144115188075855872 +1)) / 35184372088832) *
                ((1085435708121742813248709141455 * x ** 2) / 5070602400912917605986812821504 +
                 56146134542243 / 35184372088832)) / (np.exp(-(56146134542243 * x * ((6444110634811895 * x ** 2) / 144115188075855872+ 1)) / 35184372088832) + 1) ** 2


def vector_field(beta: float = 2, xmin: float = 0, xmax: float = 100,
                 tmin: float = 0, tmax: float = 100, partition: int = 10, trust: bool = True,
                 save: bool = False) -> None:
    times = np.linspace(tmin, partition, tmax)
    x = np.linspace(xmin, partition, xmax)
    if trust:
        x = sig(-beta * np.log(x / (1 - x)))
    else:
        x = sig(x)

    # Strogatz
    T, X = np.meshgrid(times, x)
    dxdt = X * (1 - X)
    dt = np.ones(X.shape)
    dx = dxdt * dt
    plt.quiver(T, X, dt, dx, headwidth=0., angles='xy', scale=15.)
    plt.show()
    plt.xlabel('Time')
    if trust:
        plt.ylabel('M(x, b)')
        plt.title('Vector Field: Trust')
        if save:
            plt.savefig(
                os.environ['HOME'] + '/Dropbox (MIT)/optimal_control/figures/VF_Trust.png')
    else:
        plt.ylabel('S(x)')
        plt.title('Vector Field: Sigmoid')
        if save:
            plt.savefig(
                os.environ['HOME'] + '/Dropbox (MIT)/optimal_control/figures/VF_Sigmoid.png')


def sim(func, init: np.ndarray, tmax: int, n: int, stubborn: bool = False) -> pd.DataFrame:
    Theta = init
    for t in range(1, tmax):
        theta_old = Theta[t - 1, :]
        theta_new = theta_old.copy()
        p = int(np.ceil(np.random.rand(1) * (n - 1))[0])
        for i in range(n):
            if ((i != p) & ((theta_old[i] - theta_old[p]) != 0) & (np.abs(theta_old[i] - theta_old[p]) != 1) & (
                    theta_old[i] != 1) & (theta_old[i] != 0)):
                if theta_old[p] > theta_old[i]:
                    theta_new[i] = theta_old[i] + (w * t_weight * (func(theta_old[i] - theta_old[p])) * (func(theta_old[i])))
                else:
                    theta_new[i] = theta_old[i] - (w * t_weight * (func(theta_old[i] - theta_old[p])) * (func(theta_old[i])))
            else:
                theta_new[i] = theta_old[i]
        if stubborn:
            theta_new[n - 1] = max(0, theta_new[n - 2] - 0.5)  # Stubborn agent
        for j in range(n):
            if theta_new[j] > 1:
                theta_new[j] = 1
            elif theta_new[j] < 0:
                theta_new[j] = 0
        Theta[t] = theta_new
    return pd.DataFrame(Theta, columns=['agent_' + str(j) for j in range(n)])


def sim_beta(func, Theta: np.ndarray, tmax: int, beta: int, n: int, stubborn: bool = False) -> pd.DataFrame:
    for t in range(1, tmax):
        theta_old = Theta[t - 1, :]
        theta_new = theta_old.copy()
        p = int(np.ceil(np.random.rand(1) * (n - 1))[0])
        for i in range(n):
            if ((i != p) & ((theta_old[i] - theta_old[p]) != 0) & (np.abs(theta_old[i] - theta_old[p]) != 1) & (
                    theta_old[i] != 1) & (theta_old[i] != 0)):
                if theta_old[p] > theta_old[i]:
                    theta_new[i] = theta_old[i] + (w * t_weight * (func(theta_old[i] - theta_old[p], b=beta)) * (func(theta_old[i], b=beta)))
                else:
                    theta_new[i] = theta_old[i] - (w * t_weight * (func(theta_old[i] - theta_old[p], b=beta)) * (func(theta_old[i], b=beta)))
            else:
                theta_new[i] = theta_old[i]
        if stubborn:
            theta_new[n - 1] = max(0, theta_new[n - 2] - 0.5)  # Stubborn agent
        for j in range(n):
            if theta_new[j] > 1:
                theta_new[j] = 1
            elif theta_new[j] < 0:
                theta_new[j] = 0
        Theta[t] = theta_new
    return pd.DataFrame(Theta, columns=['agent_' + str(n) for n in range(n)])


def plot(data: pd.DataFrame, function: str, n: int, beta: float, time: int) -> None:
    pd.DataFrame(data, columns=['agent_' + str(j) for j in range(n)]).plot()
    plt.ylabel('$\Theta_i(t)$')
    plt.xlabel('$t$')
    plt.savefig(os.environ['HOME'] + '/Dropbox (MIT)/optimal_control/figures/{}_{}n_{}b_{}t.png'.format(function, str(n), str(beta), str(time)))


class DoubleGradient:
    def __init__(self):
        beta = 2

    def trust(self, x: float):
        return (self.beta * (x / (1 - x)) ** self.beta * ((x / (1 - x)) ** self.beta * (2 * x - self.beta - 1) + 2 * x + self.beta - 1)) / (
            (x - 1) ** 2 * x ** 2 * (1 + (x / (1 - x)) ** self.beta) ** 3)


def main(function: str = 'trust') -> None:
    theta = np.zeros([tmax, n])
    theta[0] = (a + ((b - a) * (np.random.rand(n, 1)))).T
    plot(data=sim(func=Gradients().softmax, init=theta),function=function, n=n, beta=beta, time=tmax)
