from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt

"""
fonctions matplotlib
"""

# asserts:
from agents.agent import Agent
from agents.apprentissage_RL.agent import Learner


def plot_winrate(results, names, number_games):
    """
    les résultats en % des parties gagnées sur le nombre total de parties
    """
    for i, element in enumerate(results):
        results[i] = (element/number_games)*100
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # print(results, names)

    fig1, ax1 = plt.subplots()
    ax1.pie(results, labels=names, autopct='%1.1f%%', startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title("Win Rate Of Each Agents")
    plt.show()


def plot_learners_reward(*leaners):
    """
    Comparer un ou plusieurs learners avec des courbes.
    """
    for i in leaners:
        try:
            isinstance(i, Agent)
        except AttributeError:
            raise Exception("AttributeError")

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']

    j = 0
    for i in leaners:
        plt.plot(np.cumsum(i.rewards),
                 color=colors[j], label=str(i.__class__.__name__) + ", Q matrix's size: " + str(len(i.rewards)))
        j += 1
        if j is len(leaners):  # retour à la couleur n°1
            j = 0

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper right', borderaxespad=0.)
    plt.title('Cumulative Reward vs. Iteration')
    plt.ylabel('Reward')
    plt.xlabel('Episode')
    plt.show()
