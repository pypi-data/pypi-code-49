import AIArena.games as games
import copy

class Ref:
    """ This class coordinates, executes, and determines which AI or player won a given (locally run) game. It is reasonable to assume that AIOlympics uses a similar process to perform game execution for the purposes of AI development.
    """
    
    #def __init__(self, state=None):
    def createGame(self,game,players):
        """ Initializes a given game with a given set of players (human and/or AI). This takes the place of a constructor.
        
        :param game: Name of a game to set up (currently, only "Connect4" is implemented)
        :type game: string
        :param players: List of :class:`aiolympics.AI.Player` objects to have play the game.
        :type players: list
        """
        self.pids = [x.name for x in players]
        self.players = players
        self.moves = []
        self.states = []
        self.gameName = game

        if game == "Connect4":
            self.game = games.Connect4(None, self.pids)
        
        elif game=="GymBlackjack":
            self.game=games.GymBlackjack(None, self.pids)
        
        elif game=="GymFrozenLake":
            self.game=games.GymFrozenLake(None, self.pids)

        elif game=="Arena":
            self.game=games.Arena(None, self.pids)
        else:
            print("Invalid game name, please check for typos")
            exit(-1)



    def runGame(self, display=False):
        """ Steps through player moves (in order) until the game specified by createGame() is finished.
        
        :param display: Whether or not to print every move and game state as they occur. Default value is False
        :type display: bool
        :return: The final game state. 
        :rtype: dict
        """
        
        # Treat Arena with kid gloves (sorry! We still need to sort this!)
        self.states.append(copy.deepcopy(self.game.state))
        if self.gameName=="Arena":
            print("Running Arena")
            #print(self.game.state)
            while "Winner" not in self.game.state:
                #print("Turn: %d" % self.game.state["turn"])
                for p in self.players:
                    # playerArr has the player-accessible player state:
                    if p.name in self.game.playerArr:
                        move=p.makeMove(self.game.playerArr[p.name])
                        self.moves.append(move)
                        if not self.move(move, p):
                            print("player %s made invalid move" % p.name)
                            print("Move: ", move)
                            pass
                            #return -1
                        else:
                            #print("player %s made move" % p.name)
                            #print("Move: ", move)
                            self.states.append(copy.deepcopy(self.game.state))
                    elif display:
                        #print("Skipping player "+p.name)
                        pass
                if display:
                    self.game.print()
        else:
            while "Winner" not in self.game.state:
                #print("turn", self.game.state["turn"])
                player = self.players[self.game.state["turn"]]
                move = player.makeMove(self.game.state)
                self.moves.append(move)
                if not self.move(move, player):
                    return -1
                self.states.append(copy.deepcopy(self.game.state))
                if display:
                    self.game.print()
            print("The winner is:",self.game.state["Winner"])
        return self.game.state["Winner"]


    def move(self, move, player):
        """ Runs the move passed.
        
        :param move: The move to directly run in-game.
        :return: Whether or not the move was successful.
        :rtype: bool
        """

        if self.game.validateMove(move, player):
            try:
                self.game.makeMove(move, player)
            except Exception:
                return False
            self.game.postMove()
            return True
        return False

    def endGame(self):
        pass



