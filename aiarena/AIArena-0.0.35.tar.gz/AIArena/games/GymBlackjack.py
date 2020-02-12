import gym

# Implements a simple blackjack game based on the gym library
# This is intended to be a *very* simple example to demonstrate how gym can be used
# to implement games.

class GymBlackjack:
    def __init__(self, state=None, players=None, playerClass=None):
        # Set up a gym environment for this game:
        self.env=gym.make('Blackjack-v0')
        self.env.reset()
        # This will be an array of tuples consisting of (move, cardsum)
        self.done=False
        self.reward=0
        # This tuple is formatted (playerhand, dealerhand, bool for whether player has a usable ace)
        self.board=self.env._get_obs()
        self.moveHist=[(None, (self.board[0], self.board[1]))]
        self.playerClass=None

        if state:
            self.state = state
        else:
            self.state = {
                "turn": 0,
                "players": players,
                "board": self.board
            }

    def print(self):
        print("---------------")
        print("Move history:")
        for elem in self.moveHist:
            if elem[0] is None:
                print("Initial. %s" % str(elem[1]))
            else:
                if elem[0]:
                    print("Hit. %s" % str(elem[1]))
                else:
                    print("Stick. %s" % str(elem[1]))
        print("---------------")

    def validateMove(self, move):
        # Move should be a boolean (True or False depending on whether the player would like to continue)
        return self.env.action_space.contains(move)

    def makeMove(self, move):#assumes move has been validated
        observation, reward, done, info=self.env.step(move)
        self.state['board']=observation
        self.done=done
        self.reward=reward
        self.moveHist.append((move, (observation[0], observation[1])))
        print(self.reward)

    def postMove(self):
        # check for a winner:
        if self.done:
            if self.state['players'] is not None and self.reward>0:
                self.endGame(self.state['players'][0])
            else:
                self.endGame("Dealer")
        else:
            self.state["turn"] = (self.state["turn"] + 1) % len(self.state["players"])

    def endGame(self, winner):
        self.state["Winner"] = winner
 
