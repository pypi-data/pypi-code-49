from game_tree import Node
from turtle import *
import types

s = 70
startpos = (0, 250)
"""
@author: Aurelien
"""


def drawing(node, pos):
    successors = getSuccessors(node)
    # print(successors)
    i = 0
    for elem in successors:
        goto(pos)
        if not isinstance(elem, list):
            newpos = (pos[0] + s * len(successors) / 4 - s * i, pos[1] - s)
            down()
            goto((newpos[0], newpos[1] + 15))
            up()
            goto(newpos)

            if len(getSuccessors(elem)) != 0:
                write(elem.move, 1)
            else:
                write(elem.value, 1)
            # ^-- on peut changer ici ce qu'on veut afficher ici c'est les move pour les noeuds
            # et les values pour les feuilles

        if (elem.move):
            drawing(elem, newpos)

        i += 1


# successor states in a game tree are the child nodes...
def getSuccessors(node):
    """
    avoir les successeurs/enfants
    """
    assert node is not None
    return node.children


def draw_tree(list):
    """
    Fonction à lancer pour dessinner un arbre de jeu
    À donner en argument une liste comportant des objets de type Node
    """
    up()
    drawing(list, startpos)
    exitonclick()


# myTree = [1, [2, [3, [4, 5], 6], 7, 8]]
# start_drawing(myTree)
