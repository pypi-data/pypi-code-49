
from copy import deepcopy
from collections import deque

# -*- coding: utf-8 -*-
"""
@author: Aurelien
"""


class Node:  # currentnode = [game, player, my_id, parent_id]  # my_children ]
    """
    Class qui caractérise un noeud qui a:
    game, player, my_id, parent_id=0, move=None, leaf_value=None
    leaf_value est à none au début pour les noeuds. On fait remonter
    le leaf_value des feuilles vers le haut de l'arbre dans l'algorithme Minimax.
    """

    def __init__(self, game, player, my_id, parent_id=0, move=None, leaf_value=None):
        self.game = game
        self.player = player
        self.my_id = my_id
        self.parent_id = parent_id
        self.move = move
        self.value = leaf_value
        self.children = []

    def __repr__(self):
        """
        Pour récupérer un noeud, si on fait Node(...) on récupère tout ça:
        """
        if self.children:
            return str((object.__repr__(self), self.game, self.player, self.my_id, self.parent_id, self.move, self.value, self.children))[1:-1]
        return str((object.__repr__(self), self.game, self.player, self.my_id, self.parent_id, self.move, self.value))[1:-1]

    # return str((object.__repr__(self), self.name, self.my_id, self.parent, self.children))[1:-1]
    # return str((object.__repr__(self), self.name, self.my_id, self.parent))[1:-1]


class GameTree:

    def __init__(self, game, win_value=10, loss_value=-10, players=['Human', 'Bot']):
        # X = Human
        # O = Bot
        """
        Constructeur pour les jeux à tirages de nombres.
        On doit avoir: l'état du jeu, la méthode pour jouer, la méthode pour copier le plateau, et la méthode pour vérifier l'état du jeu
        """
        self.game = game

        self.win_value = win_value
        self.loss_value = loss_value
        self.players = players

        # self.root = None
        return

    # TODO from_board
    @classmethod
    def from_board(cls, game, win_value=10, loss_value=-10, players=['Human', 'Bot']):
        """
        Constructeur pour les jeux de plateau.
        """
        g = GameTree(game, win_value, loss_value, players)

        boardSample = g.current_state
        self.boardSizeX = len(boardSample)
        self.boardSizeY = map(len, boardSample)

        return g

    def create_tree(self, currentgame, currentplayer='Bot'):
        """
        Pour les jeux à tirages de nombres.
        Méthode pour créer un arbre de jeu en fonction de l'état du jeu.
        On fait plein de parties dans cette méthode.
        Return une liste
        """
        # pour ne pas mélanger les variables current : c'est le jeu réel
        game = currentgame
        player = currentplayer

        # La liste à return
        game_tree = []

        my_id = 0

        # chaque noeud contient l'objet jeu, le joueur, sa clef primaire, la clef primaire du parent et s'il y en a une la valeur de feuille
        # si c'est un parent alors le parent sera suivi par ses enfants

        currentnode = Node(game, player, my_id, my_id)

        # la queue, on ititialise la file avec l'état du jeu et le joueur qui joue
        queue = deque()  # <Node>

        queue.append(currentnode)
        game_tree.append(currentnode)

        while len(queue) != 0:  # while is not empty

            currentnode = queue.pop()

            print("current node : " + str(currentnode))

            game = currentnode.game
            parent_move = currentnode.move
            player = currentnode.player
            parent_id = currentnode.my_id

            constructingnode = []  # the next node

            # Si c'est une feuille: on return la valeur de victoire ou défaite
            winner_loser, done = game.check_current_state()
            if done == True or done == "Draw":

                my_id += 1

                constructingnode = Node(game, player,
                                        my_id, parent_id,
                                        parent_move, self.create_leaf(game))

                print("leaf : " + str(constructingnode))
                game_tree.append(constructingnode)
                continue  # skip over the part of the loop

            empty_cells = []

            # On numérote les coups où l'on peut jouer (pas vides)
            for i in range(game.minimal_move(), game.current_state() + 1):  # l'état actuel du jeu
                if game.check_valid_move(i) == True:
                    empty_cells.append(i)
            print("empty_cells " + str(empty_cells))

            # Jeux imaginaires
            for empty_cell in [x for x in empty_cells if x not in game.invalid_moves()]:

                print("empty_cell " + str(empty_cell))

                my_id += 1

                copy_game = deepcopy(game)  # on copie le jeu
                # on fait le coup sur cette copie de jeu
                copy_game.play_move(empty_cell, player)

                # Si c'est à l'IA de jouer.    players = ['Human', 'Bot']
                if player == self.players[1]:  # == O
                    # make more depth tree for human
                    constructingnode = Node(copy_game, self.players[0],
                                            my_id, parent_id, empty_cell)  # au tours de human à jouer
                    print("constructed node : " + str(constructingnode))

                # Si c'est à l'humain de jouer.
                if player == self.players[0]:  # == X
                    # make more depth tree for AI
                    constructingnode = Node(copy_game, self.players[1],
                                            my_id, parent_id, empty_cell)  # au tours de bot à jouer
                    print("constructed node : " + str(constructingnode))

                queue.append(constructingnode)
                game_tree.append(constructingnode)

        # while not queue.empty():
         #   game_tree.append(queue.pop())

        # try:
        # self.create_node_game_board(self.state, self.players[0])
        # except NameError:
        # self.create_node(state, currentplayer)

        print("___ FINAL TREE ___", game_tree)
        print(" ")

        # v transformation v

        parent = None
        for node in game_tree:
            if node.my_id == node.parent_id:
                parent = node
                break

        print('___Parent:___', parent)
        print(" ")
        # self.root = parent

        indexed_objects = {node.my_id: node for node in game_tree}
        for node in game_tree:
            if node.my_id != node.parent_id:
                my_parent = indexed_objects[node.parent_id]
                my_parent.children.append(node)

        print('___Parent:___', parent)
        print(" ")
        return parent

    def create_leaf(self, game):
        """
        Return the value of a leaf
        """

        # Si c'est des feuilles: on return la valeur de victoires ou défaite
        winner_loser, done = game.check_current_state()

        """
        players = ['X', 'O']
        # X = Human
        # O = Bot

        # Si le jeu est fini et que l'IA a gagné.
        if done == "Done" and winner_loser == 'O':
            return 1
        # Si le jeu est fini et que l'IA a perdu.
        elif done == "Done" and winner_loser == 'X':
            return -1
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0
        """

        # Si le jeu est fini et que l'IA a gagné.
        if done == True and winner_loser == self.players[1]:  # IA O
            return self.win_value
        # Si le jeu est fini et que l'IA a perdu.
        elif done == True and winner_loser == self.players[0]:  # Humain X
            return self.loss_value
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0

    # TODO  create_node_game_board
    def create_node_game_board(self, state, player):
        """
        Pour les jeux de plateau.
        Méthode pour faire un noeud de l'arbre.
        On joue une partie dans cette méthode.
        Return un noeud
        """

        winner_loser, done = self.check_current_state.upper(state)

        # Si c'est des feuilles: on return la valeur de victoires ou défaite

        # Si le jeu est fini et que l'IA a gagné.
        if done == "Done" and winner_loser == players[0]:  # Humain X
            return win_value
        # Si le jeu est fini et que l'IA a perdu.
        elif done == "Done" and winner_loser == players[1]:  # IA O
            return loss_value
        # Si le jeu est fini et que personne n'a gagné.
        elif done == "Draw":
            return 0

        moves = []
        empty_cells = []

    # On numérote les cases où l'on peut jouer (pas vides)
        for i in range(self.boardSizeX):
            for j in range(self.boardSizeY):
                if state[i][j] is self.check_playable:  # empty / playable
                    empty_cells.append(i*self.boardSizeX + (j+1))

    # Jeux imaginaires
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell
            new_state = self.copy_game_state.upper(state)
            self.play_move.upper(new_state, player, empty_cell)

            # Si c'est à l'IA de jouer.
            if player == players[1]:  # == O
                # make more depth tree for human
                result = create_node_game_board(new_state, players[0])
                move['score'] = result
            # Si c'est à l'humain de jouer.
            else:  # == X
                # make more depth tree for AI
                result = create_node_game_board(new_state, players[1])
                move['score'] = result
