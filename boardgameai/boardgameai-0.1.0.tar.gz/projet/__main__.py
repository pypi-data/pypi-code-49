# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import multiprocessing
import sys
import argparse

# fonctions utilitaires: sont toutes dans utilities.py
from utilities.utilities import TurnBased_episodes
from utilities.utilities import save_learner
from utilities.utilities import load_learner

# plotting: pour créer des graphiques mathplotlib sont toutes dans plot.py
from utilities.plot import plot_learners_reward

# ───────────────────────────────── imports agents

# algorithme d'optimisation:
from agents.optimisation_MinMax.minimax import Minimax
# algorithmes d'apprentissage:
from agents.apprentissage_RL.agent import Qlearner
from agents.apprentissage_RL.agent import SARSAlearner

# pour jouer en tant qu'utilisateur ou random:
from agents.human import Human
from agents.random import Random

# ───────────────────────────────── imports jeux

# les jeux à importer:
from games.jeu_Nim import Nim
from games.TicTacToe_old.jeu_TicTacToe import TicTacToe as TicTacToe_old
from games.TicTacToe_new.jeu_TicTacToe import TicTacToe as TicTacToe_new


# ──────────────────────────────────────────────────────────────────────────────── main
# lancement des jeux avec les algorithmes


if __name__ == "__main__":

    # ───────────────────────────────── arguments

    parser = argparse.ArgumentParser(
        description="Reinforcement learning options.")
    parser.add_argument("-t", "--teacher_episodes", default=10000, type=int,
                        help="employ teacher agent who knows the optimal "
                        "strategy and will play for TEACHER_EPISODES games")
    parser.add_argument("-s", "--save", action='store_true',
                        help="whether to save all trained agents")
    parser.add_argument("-l", "--load", nargs="+",
                        help="whether to load one or multiple trained agents"
                        "enter your files *.pkl after -l each separated by"
                        "one space")
    parser.add_argument("-p", "--plot", action='store_true',
                        help="whether to plot reward vs. episode of stored agent")

    args = parser.parse_args()

    if args.plot:
        assert args.load, "Must load an agent to plot reward."

    # ───────────────────────────────── main

    # v changer ci-dessous le jeu (game) souhaité v
    # game = Nim(6)
    # game = TicTacToe_old()
    game = TicTacToe_new()

    # algorithmes/agents ou teachers
    # on peut rajouter autant qu'on veut d'agents ou teachers ici:
    human = Human()
    random = Random()
    minimax = Minimax()

    # the game learners:
    learners = []  # <-- tous contenus ici

    # ───────────────────────────────── partie load
    # ne pas toucher la partie load
    if args.load:
        for i in args.load:
            loaded_agent = load_learner(i)
            if args.plot:  # If plotting, show plot
                plot_learners_reward(loaded_agent)
            learners.append(loaded_agent)

    # sinon on peut rajouter autant qu'on veut de learners ici:
    glQ = Qlearner(game.valid_moves(True))
    learners.append(glQ)
    glS = SARSAlearner(game.valid_moves(True))
    learners.append(glS)

    manual_games = 3  # nombre de jeux tests à la main après l'entrainement

    # ───────────────────────────────── apprentissage

    if args.teacher_episodes is not None:  # on apprend puis on teste à la main
        TurnBased_episodes(game, args.teacher_episodes,
                           False, learners[0], random)
        # plot_learners_reward peut plot plusieurs learners en même temps
        plot_learners_reward(learners[0])
        TurnBased_episodes(game, manual_games, True, learners[0], human)

        # ─────────────────────────────  partie save

        if args.save:
            for i in learners:
                save_learner(game, i)

    # TODO raise Exception()
    # TODO save/load dans un dossier à part
    # TODO save dans un dossier et numéroter
    # TODO faire plus d'asserts / exceptions
    # TODO faire fonctionner MinMax + nettoyer
    # TODO documenter
    # TODO nettoyer le code
