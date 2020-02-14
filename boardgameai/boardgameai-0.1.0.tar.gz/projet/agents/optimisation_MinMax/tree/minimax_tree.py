##########################
######   MINI-MAX   ######
##########################

# https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/
"""
@author: Aurelien
"""


class Minimax:
    """
    Minimax ayant besoin de game tree sous forme de liste à fournir (moins optimisé)
    """

    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search

    def __init__(self, game_tree):
        """
        Constructeur où on donne l'arbre de jeu entier.
        Un arbre est constitué de noeuds, il a une racine et des feuilles.
        Cet arbre est le jeu entier: ce sont toutes les possibilités de jeu.
        Les feuilles au bout de l'arbre contiennent des valeurs 
        (qui peuvent être arbitraires selon le jeu).
        Par exemple: -10 pour une défaite et 10 pour une victoire.

        L'arbre est donc sous from de liste cf: https://www.programiz.com/python-programming/list
        Exemple de data: [‘A’, [‘B’, (‘D’, 3), (‘E’, 5)], [‘C’, [‘F’, [‘I’,(‘K’,0), (‘L’, 7)],(‘J’,5)], [‘G’, (‘M’,7), (‘N’,8)], (‘H’,4)]]
        """
        self.game_tree = game_tree  # GameTree
        # self.root = game_tree.root  # GameRoot
        self.currentNode = None  # GameNode
        self.successors = []  # List of GameNodes
        return

    # ────────────────────────────────────────────────────────────────────────────────

    def choose_move(self, node):
        """
        Méthode principale à appeler, on demande un noeud de l'arbre.
        """
        # first, find the max value
        best_val = self.max_value(node)  # should be root node of tree

        # second, find the node which HAS that max value
        #  --> means we need to propagate the values back up the
        #      tree as part of our minimax algorithm
        successors = self.getSuccessors(node)
        print("MiniMax:  Utility Value of Root Node: = " + str(best_val))
        # find the node with our best move
        best_move = None
        for elem in successors:  # ---> propagate values up tree
            """
            On cherche parmis nos élements lequel est celui avec la valeur max de max_value et on fait un break puis on la return
            """
            if elem.value == best_val:
                best_move = elem
                break

        # return that best value that we've found
        print(" -- > MiniMax: Choosen move " + str(best_move))
        return best_move.move

    def max_value(self, node):
        print("MiniMax --> MAX: Visited Node :: " + str(node.my_id))
        if self.isTerminal(node):  # si c'est une feuille
            # alors on retourne sa valeur (return node.value)
            return self.getUtility(node)

        infinity = float('inf')
        # on part de - l'infini pour trouver quelque chose de meilleur à chaque fois
        max_value = -infinity

        successors_states = self.getSuccessors(node)  # successeurs en dessous
        """
          p     : 0 (max) (current)
         / \          v
        s   s   : 1 (min)
            on prend donc le max
        """
        for state in successors_states:
            """
            On fait donc une succession de max, min, max, min... Car dans min_value() on demandera max_value().
            Il n'y a pas de récursivité car on part de max_value() puis on demande min_value() puis max_value() et ainsi de suite.
            On fait remonter les valeurs avec isTerminal(), getUtility(). Les noeuds ne return pas de valeur.
            Le programme fonctionne de façon naturelle : voir Plminmax.gif, MinMax.png.
            """
            max_value = max(max_value, self.min_value(state))

        node.value = max_value
        return max_value

    def min_value(self, node):
        print("MiniMax --> MIN: Visited Node :: " + str(node.my_id))
        if self.isTerminal(node):
            return self.getUtility(node)

        infinity = float('inf')
        # on part de + l'infini pour trouver quelque chose de pire à chaque fois
        min_value = infinity

        successor_states = self.getSuccessors(node)  # successeurs en dessous
        """
          p     : 0 (min) (current)
         / \          v
        s   s   : 1 (max)
            on prend donc le min
        """
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))

        node.value = min_value
        return min_value

    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes...
    def getSuccessors(self, node):
        """
        avoir les successeurs
        """
        assert node is not None
        return node.children

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        """
        si c'est une feuille
        """
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        """
        lorsqu'on veut return la valeur pour une feuille
        """
        assert node is not None
        return node.value
