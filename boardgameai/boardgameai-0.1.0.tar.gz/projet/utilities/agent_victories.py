class Agent_Victories:
    """
    Classe liante
    Permet de connaitre le nombre de victoires pour chaque agent
    Classe valable pour un ensemble de parties
    """

    def __init__(self, player, agent):
        self.player = player
        self.agent = agent
        self.victories = 0

    def __repr__(self):
        """
        Pour récupérer l'objet, si on fait Agent_Victories(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.player, self.agent, self.victories))[1:-1]
