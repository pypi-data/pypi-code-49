class Player:
    """This forms an interface for a generic game "player." It is extended by the AI class and can be used to represent any kind of entity that makes moves in a given game.
    
    :param name: The human-readable reported name for the player (ex. LilBuddy for our Connect 4 playing AI)
    :param game: The specific game instance for this AI to play.
    """
    def __init__(self, name, game):
        """Constructor
        """
        self.name = name
        self.game = game
        if not hasattr(self, "id"):
            self.id = self.name

    def makeMove(self, state):
        """Returns an appropriate move given a game state. Must be overridden in implementations of the Player class.
        :param state: The game state given which to make a move.
        :return: An appropriate move representation depending on the game played.
        """
        print("This player is missing the method 'makeMove(self, state)'")
        return None

class AI(Player):
    """This is the core interface for AI development. Extending the makeMove() method allows for a hook into an AI so that it can respond to game states and inputs.
    
    :param name: The human-readable reported name for this AI (ex. LilBuddy for our Connect 4 playing AI)
    :param game: The specific game instance for this AI to play.
    """
    def __init__(self, name, game):
        """Constructor. Calls superclass (Player) constructor and nothing else
        """
        super().__init__(name, game)
        #add AI specific code here

    def makeMove(self, state):
        """Returns an appropriate move given a game state. Must be overridden in implementations of the Player class.
        :param state: The game state in which to make a move.
        :return: An appropriate move representation depending on the game played.
        """
        print("Your AI is missing the method 'makeMove(self, state)'")
        return None

class AI_Connect4(AI):
    def __init__(self, name):
        super().__init__(name, "Connect4")



