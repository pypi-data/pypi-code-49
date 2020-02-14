from abc import ABC, abstractmethod
import os
import pickle
import collections
import numpy as np
import random

from agents.agent import Agent
# les noeuds:
from agents.node import Node


class Learner(ABC, Agent):
    """
    Parent class for Q-learning and SARSA agents.

    Parameters
    ----------
    actions : List
        the list of all the valid_moves() at the beginning of the game
    alpha : float 
        learning rate
    gamma : float
        temporal discounting rate
    eps : float 
        probability of random action vs. greedy action
    eps_decay : float
        epsilon decay rate. Larger value = more decay
    """

    def __init__(self, actions, alpha=0.5, gamma=0.9, eps=0.1, eps_decay=0.):
        # Agent parameters
        self.alpha = alpha
        self.gamma = gamma
        self.eps = eps
        self.eps_decay = eps_decay
        # Possible actions correspond to the set of all possible moves
        self.actions = actions
        # Initialize Q values to 0 for all state-action pairs.
        # Access value for action a, state s via Q[a][s]
        self.Q = {}
        for action in self.actions:
            self.Q[action] = collections.defaultdict(int)
        # Keep a list of reward received at each episode
        self.rewards = []

    def choose_move(self, node, s):
        """
        Select an action given the current game state.

        Parameters
        ----------
        s : string
            state
        node : Node
            contain the game where you can have the valid_moves()
        """

        try:
            isinstance(node, Node)
        except AttributeError:
            raise Exception("AttributeError")

        game = node.game  # current game

        # Only consider the allowed actions (empty board spaces)

        # L'ensemble des coups possibles pour cette node
        possible_actions = game.valid_moves()
        print("Les actions possibles :\n", possible_actions)

        if random.random() < self.eps:
            # Random choose.
            action = possible_actions[random.randint(
                0, len(possible_actions)-1)]
        else:
            # Greedy choose. Pour chaque action de cet état --v
            values = np.array([self.Q[a][s] for a in possible_actions])
            print("Les valeurs de la matrice Q :\n", values)
            # Find location of max
            ix_max = np.where(values == np.max(values))[0]
            if len(ix_max) > 1:
                # If multiple actions were max, then sample from them
                ix_select = np.random.choice(ix_max, 1)[0]
            else:
                # If unique max action, select that one
                ix_select = ix_max[0]
            action = possible_actions[ix_select]

        # update epsilon; geometric decay
        self.eps *= (1.-self.eps_decay)

        return action

    def save_agent(self, path):
        """ Pickle the agent object instance to save the agent's state. """
        if os.path.isfile(path):
            os.remove(path)
        f = open(path, 'wb')
        pickle.dump(self, f)
        f.close()

    @abstractmethod
    def update(self, node, s, s_, a, a_, r):
        pass


class Qlearner(Learner):
    """
    A class to implement the Q-learning agent.
    """

    def __init__(self, actions, alpha=0.5, gamma=0.9, eps=0.1, eps_decay=0.):
        super().__init__(actions, alpha, gamma, eps, eps_decay)

    def update(self, node, s, s_, a, a_, r):
        """
        Perform the Q-Learning update of Q values.

        Parameters
        ----------
        s : string
            previous state
        s_ : string
            new state
        a : (i,j) tuple
            previous action
        a_ : (i,j) tuple
            new action. NOT used by Q-learner!
        r : int
            reward received after executing action "a" in state "s"
        """

        try:
            isinstance(node, Node)
        except AttributeError:
            raise Exception("AttributeError")

        game = node.game  # current game

        # Update Q(s,a)
        if s_ is not None:
            # hold list of Q values for all a_,s_ pairs. We will access the max later
            # possible_actions = [action for action in self.actions if s_[
            #    action[0]*3 + action[1]] == '-']

            possible_actions = game.valid_moves()
            print("Les actions possibles après update :\n", possible_actions)

            Q_options = [self.Q[action][s_] for action in possible_actions]
            # update
            self.Q[a][s] += self.alpha * \
                (r + self.gamma*max(Q_options) - self.Q[a][s])
        else:
            # terminal state update
            self.Q[a][s] += self.alpha*(r - self.Q[a][s])

        # add r to rewards list
        self.rewards.append(r)


class SARSAlearner(Learner):
    """
    A class to implement the SARSA agent.
    """

    def __init__(self, actions,  alpha=0.5, gamma=0.9, eps=0.1, eps_decay=0.):
        super().__init__(actions, alpha, gamma, eps, eps_decay)

    def update(self, node, s, s_, a, a_, r):
        """
        Perform the SARSA update of Q values.

        Parameters
        ----------
        s : string
            previous state
        s_ : string
            new state
        a : (i,j) tuple
            previous action
        a_ : (i,j) tuple
            new action
        r : int
            reward received after executing action "a" in state "s"
        """
        # Update Q(s,a)
        if s_ is not None:
            self.Q[a][s] += self.alpha * \
                (r + self.gamma*self.Q[a_][s_] - self.Q[a][s])
        else:
            # terminal state update
            self.Q[a][s] += self.alpha*(r - self.Q[a][s])

        # add r to rewards list
        self.rewards.append(r)
