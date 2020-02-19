import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import config
from dynamics import Gradients, sim, sim_beta
import os

cur_dir = os.getcwd() 
figure_dir = os.path.join(cur_dir,'figures')
plt.style.use('ggplot')

a, b = 0, 1
SIGMAS, WINDOW = 2, 50


def simulate_af(tmax: int, n: int, save: bool=False) -> None:
    vec = []
    functions = [ele for ele in list(Gradients.__dict__.keys()) if '_' not in ele]
    for func in functions:
        np.random.seed(1)
        Theta = np.zeros([tmax, n])
        Theta[0] = (a + ((b - a) * (np.random.rand(n, 1)))).T
        df = sim(func=eval('Gradients().{}'.format(func)), Theta=Theta, tmax=tmax, n=n)
        vec.append(df)
    df = 1 - pd.concat(vec, axis=1, keys=functions)
    colors = cm.rainbow(np.linspace(a, b, len(functions)))
    color_dict = dict(zip(functions, colors))
    smooth_path = df.stack().mean(level=0).rolling(WINDOW).mean()
    path_deviation = SIGMAS * df.stack().std(level=0).rolling(WINDOW).std()
    for j in functions:
        plt.plot(smooth_path[j], linewidth=2, label=str(j))
        plt.fill_between(path_deviation.index, (smooth_path - SIGMAS * path_deviation)[j],
                         (smooth_path + SIGMAS * path_deviation)[j],
                         color=color_dict[j], alpha=.1)
    plt.legend()
    plt.ylabel('$\Theta(t)$')
    plt.xlabel('t')
    plt.title('Performance of Activation Functions')
    if save:
        plt.savefig(figure_dir + 'AF_comparison.png')
    plt.show()


def simulate_beta(min_beta: int, max_beta: int, tmax: int, n: int, save: bool=False) -> None:
    betas = list(range(min_beta, max_beta))
    vec = []
    for beta in betas:
        np.random.seed(1)
        Theta = np.zeros([tmax, n])
        Theta[0] = (a + ((b - a) * (np.random.rand(n, 1)))).T
        df = sim_beta(func=Gradients().trust, Theta=Theta, tmax=tmax, n=n, beta=beta)
        vec.append(df)
    df = pd.concat(vec, axis=1, keys=betas)
    colors = cm.rainbow(np.linspace(a, b, len(betas)))
    color_dict = dict(zip(betas, colors))
    smooth_path = df.stack().mean(level=0).rolling(WINDOW).mean()
    path_deviation = SIGMAS * df.stack().std(level=0).rolling(WINDOW).std()
    for j in betas:
        plt.plot(smooth_path[j], linewidth=2, label=str(j))
        plt.fill_between(path_deviation.index, (smooth_path - SIGMAS * path_deviation)[j],
                         (smooth_path + SIGMAS * path_deviation)[j], color=color_dict[j], alpha=.1)
    plt.legend()
    plt.ylabel('$\Theta(t)$')
    plt.xlabel('t')
    plt.title('Performance Across $\beta$')
    if save:
        plt.savefig(figure_dir + 'beta_comparison.png')
    plt.show()


def main():
    simulate_af(tmax=1000, n=100, save=True)
    simulate_beta(min_beta=2, max_beta=10, tmax=1000, n=100, save=True)


if __name__ == 'main':
    main()
