
class Player_Informations:
    """
    Classe liante
    Définit chaque joueur, leur inventaire, le tour à laquelle ils en sont
    """

    def __init__(self, player, currentphase, pawn):

        self.player = player  # le nom du joueur
        self.currentphase = currentphase  # la phase où il en est
        self.pawn = pawn  # le pion
        self.phase = None  # la phase où il en est

    def __repr__(self):
        """
        Pour récupérer l'objet, si on fait Player_Informations(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.player, self.pawn, self.currentphase, self.sub_phase))[1:-1]
