class Agent_Informations:
    """
    Classe liante
    Définit chaque joueur et sauvegarde leurs informations
    Permet de faire le parallèle entre les players et les agents
    Classe valable que pour une partie
    """

    def __init__(self, player, agent, prev_state=None, prev_action=None):
        self.player = player  # le nom du joueur
        self.agent = agent
        self.prev_state = prev_state
        self.prev_action = prev_action

    def __repr__(self):
        """
        Pour récupérer l'objet, si on fait Agent_Informations(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.player, self.agent, self.prev_state, self.prev_action))[1:-1]
