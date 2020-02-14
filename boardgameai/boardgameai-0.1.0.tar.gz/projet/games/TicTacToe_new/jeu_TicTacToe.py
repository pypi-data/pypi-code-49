import random

from games.game import Game
from games.TicTacToe_new.player_informations import Player_Informations


class TicTacToe(Game):
    """ The game class. New instance created for each new game. """

    def __init__(self):  # constructeur
        self.players = ['Player1', 'Player2']  # liste des joueurs en string
        self.board = [['-', '-', '-'], ['-', '-', '-'],
                      ['-', '-', '-']]  # le plateau
        self.currentplayer = None  # caractérise le dernier joueur qui a joué

        self.phases = []  # création des différentes phases
        # phase n°1: position du pion
        self.phases.append("Choix position")  # instruction de la phase 1
        self.currentphase = self.phases[0]  # la phase actuelle
        """
        Player1 -> 'X'
        Player2 -> 'O'
        """
        self.players_info = []  # création des joueurs et leurs informations
        self.players_info.append(
            Player_Informations(self.players[0], self.currentphase, "X"))
        self.players_info.append(
            Player_Informations(self.players[1], self.currentphase, "O"))
        return

    def play_move(self, choice, currentplayer):  # utilisé par les agents
        """
        Methode pour jouer au jeu. Les sous fonctions représentent chaque phase
        et donc l'action effectuée en fonction de la phase du jeu
        """
        def phase1(choice, currentplayer_info):
            """ changement d'état pour la phase 1 """
            if choice in self.valid_moves():
                row, col = int(choice[0]), int(choice[1])
                self.board[row][col] = currentplayer_info.pawn  # pose pion

        currentplayer_info = None  # on récupère le joueur par players_info
        self.currentplayer = currentplayer  # ce qui permet de récupérer son inventaire
        for i in self.players_info:  # et aussi lui faire passer à la phase d'après
            if i.player is self.currentplayer:
                currentplayer_info = i
                break

        switch = {  # switch case sur self.currentphase
            self.phases[0]: phase1(choice, currentplayer_info),
            # une autre phase...
        }
        switch.get(self.currentphase)
        # et on fait passer le joueur à la phase suivante
        # phase suivante dynamique selon self.currentphase dans self.phases
        currentplayer_info.currentphase = self.phases[(
            self.phases.index(self.currentphase) + 1) % len(self.phases)]

        """
        On change de phase globale. Si tous les joueurs sont à la phase suivante
        alors la phase globale du jeu passe à la phase d'après.
        """
        dummy_phase = self.players_info[0].currentphase
        for i, element in enumerate(self.players_info):
            if element.currentphase is not dummy_phase:
                break  # alors quelqu'un n'a pas encore terminé
            if i is len(self.players_info):  # dernier element
                self.currentphase = self.players_info[0]

    def valid_moves(self, all_moves=False):  # utilisé par les agents
        """
        Methode qui donne sous forme de liste tous les coups jouables possibles.
        La liste récupérée représente un tour.
        Chaque sous fonction représente les phases dans le jeu et donc donnent 
        chacunes les coups possibles en fonction des différentes phases du jeu.
        """
        def phase1():
            moves_phase1 = [
            ]  # tous les coups jouables sous forme de liste de tuples pour la phase 1

            def check_phase1(choice):
                """ Vérifie si le coup est valide selon le plateau pour la phase 1 """
                if type(choice) is list or tuple:  # si la donnée entrée est un tuple (row, col)
                    row, col = int(choice[0]), int(choice[1])
                    if row not in range(3) or col not in range(3) or not self.board[row][col] == '-':
                        return False
                    else:
                        return True
                else:
                    return False

            # On numérote n'importe quel coup
            for i in range(0, len(self.board)):
                for j in range(0, len(self.board)):
                    if check_phase1((i, j)):  # on vérifie selon le plateau du jeu
                        moves_phase1.append((i, j))

            return moves_phase1  # et on return la liste

        switch = {  # switch case sur self.currentphase
            self.phases[0]: phase1(),
            # une autre phase...
        }

        if not all_moves:  # les moves pour la phase globale actuelle du jeu
            moves = switch.get(self.currentphase)
        else:  # tous moves possibles du jeu, sert à initialiser la matrice Q
            moves = sum(switch.values(), [])  # on applatit la liste
        return moves

    def winner(self):  # utilisé par les agents
        """
        Methode pour récupérer le joueur victorieux
        Si match nul on récupère: "Draw"
        Si le match est toujours en cours on retourne "None"
        """

        for i in self.players_info:
            if self.check_win(i.pawn):
                return i.player

        if self.check_draw():
            return "Draw"

        return None

    def check_win(self, key):
        """
        Check to see whether the player/agent with token 'key' has won.
        Returns a boolean holding truth value.

        Parameters
        ----------
        key : string
            token of most recent player. Either 'O' or 'X'
        """
        # check for player win on diagonals
        a = [self.board[0][0], self.board[1][1], self.board[2][2]]
        b = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if a.count(key) == 3 or b.count(key) == 3:
            return True
        # check for player win on rows/columns
        for i in range(3):
            col = [self.board[0][i], self.board[1][i], self.board[2][i]]
            row = [self.board[i][0], self.board[i][1], self.board[i][2]]
            if col.count(key) == 3 or row.count(key) == 3:
                return True
        return False

    def check_draw(self):
        """
        Check to see whether the game has ended in a draw. Returns a
        boolean holding truth value.
        """
        draw = True
        for row in self.board:
            for elt in row:
                if elt == '-':
                    draw = False
        return draw

    def print_game(self):  # utilisé par l'humain et les algorithmes d'apprentissage
        """
        Return the game board as string.
        Représente l'état du jeu pour le reinforcement learning.
        """
        string = str('    0   1   2')
        string += str('\n\n')
        for i, row in enumerate(self.board):
            string += str('%i   ' % i)
            for elt in row:
                string += str('%s   ' % elt)
            string += str('\n\n')
        return string
