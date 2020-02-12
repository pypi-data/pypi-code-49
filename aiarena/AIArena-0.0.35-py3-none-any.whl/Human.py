from AIArena.AI import Player as Player

class Human_Connect4(Player):
    """This class is an example human interface for the Connect4 game. It allows
    for play over a terminal. 
    """
    def __init__(self):
        super().__init__("Human", "Connect4")

    def makeMove(self, state):
        """In order to support human play, this method reads a response from stdin and
        returns it.
        
        :return: Human move
        :rtype: int
        """
        move = "-1"
        while not move.isdigit() or int(move) >=7:
            move = input("Enter column number (0-6) to place piece: ")
        return int(move)
