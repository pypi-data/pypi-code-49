import gym

# Implements the Frozen Lake game based on the gym library
# The goal of the game is to make it to the 'G' tile while avoiding 'H' tiles.
# Moves are defined as follows:
# LEFT = 0
# DOWN = 1
# RIGHT = 2
# RIGHT = 3

moves=["left", "down", "right", "up"]

class GymFrozenLake:
    def __init__(self, state=None, players=None):
        # Set up a gym environment for this game:
        self.env=gym.make('FrozenLake-v0', is_slippery=False)
        obs=self.env.reset()
        # This will be an array of tuples consisting of (move, cardsum)
        self.done=False
        self.reward=0
        # This is an array of strings:
        self.board=self.env.desc
        self.moveHist=["Start"]

        if state:
            self.state = state
        else:
            self.state = {
                "turn": 0,
                "players": players,
                "board": self.board
            }

    def print(self):
        print(self.moveHist)
        self.env.render()

    def validateMove(self, move):
        # Move should be a boolean (True or False depending on whether the player would like to continue)
        return self.env.action_space.contains(move)

    def makeMove(self, move):#assumes move has been validated
        print("makeMove %d" % move)
        observation, reward, done, info=self.env.step(move)
        # The board doesn't change
        self.done=done
        self.reward=reward
        self.moveHist.append(moves[move])
        print(self.reward)

    def postMove(self):
        # check for a winner:
        if self.done:
            if self.state['players'] is not None and self.reward>0:
                self.endGame(self.state['players'][0])
            else:
                self.endGame("Player lost.")
        else:
            self.state["turn"] = (self.state["turn"] + 1) % len(self.state["players"])

    def endGame(self, winner):
        self.state["Winner"] = winner
 
