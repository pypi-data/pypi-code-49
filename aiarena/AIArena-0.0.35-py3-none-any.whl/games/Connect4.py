import copy

class Connect4:
    """This implements a game of Connect4"""
    def __init__(self, state=None, players=None, replayStates=None, moves=None):
        #Game Constants
        self.dims = (7 , 6)

        if state:
            self.state = state
        else:
            self.state = {
                "turn": 0,
                "board": [[0]*self.dims[1] for _ in range(self.dims[0])],
                "players":[]#an array of player ids
            }
            self.players = players
            for p in self.players:
                self.state["players"].append(p.id)
        if replayStates:
            self.replayStates = replayStates
        else:
            self.replayStates = []
        if moves:
            self.moves = moves
        else:
            self.moves = []

    def runGame(self, display=False):
        result = {
            "error":"none",
            "replayStates":self.replayStates,
            "moves":self.moves
        }


        self.replayStates.append(copy.deepcopy(self.state))
        while "Winner" not in self.state:
            # print("turn", self.game.state["turn"])
            player = self.players[self.state["turn"]]
            move = player.makeMove(self.state)
            self.moves.append(move)
            if not self.validateMove(move):
                result['rewards'] = self.genErrRewards(self.state["turn"])
                result['error'] = "AI : " + player.name + " made an illegal move"
                return result
            self.makeMove(move)
            self.replayStates.append(copy.deepcopy(self.state))
            self.postMove()
            if display:
                self.game.print()

        result['rewards'] = self.genRewards(self.state["Winner"])
        return result

    def genRewards(self, winner):
        rewards = []
        for i, player in enumerate(self.players):
            if i == winner:
                r = 1
            else:
                r = -1
            rewards.append((player.id, r))
        return rewards

    def genErrRewards(self, screwUp):
        rewards = []
        for i, player in enumerate(self.players):
            if i == screwUp:
                r = -1
            else:
                r = 0
            rewards.append((player.id, r))
        return rewards

    def print(self):
        print("---------------")
        for j in range(self.dims[1]):
            pStr = "|"
            for i in range(self.dims[0]):
                pStr += str(self.state["board"][i][self.dims[1] - 1 - j]) + "|"
            print(pStr)
        print("---------------")

    def validateMove(self, move):
        if move < 0 or move >= self.dims[0]:
            return False

        if self.state["board"][move][-1] == 0:
            return True

        return False

    def makeMove(self, move):#assumes move has been validated
        y = self.dims[1] - 1
        while self.state["board"][move][y] == 0:
            y += -1
            if y < 0:
                break

        marker = self.state["turn"] + 1
        self.state["board"][move][y+1] = marker




    def postMove(self):
        dirs = [(0,1),(1,0),(1,1),(-1,1)]
        #check for winner
        for i in range(self.dims[0]):
            j = 0
            while self.state["board"][i][j] != 0:
                match = self.state["board"][i][j]
                for dir in dirs:
                    streak = 1
                    dx = i + dir[0]
                    dy = j + dir[1]
                    if dx >= self.dims[0] or dy >= self.dims[1]:
                        continue
                    while self.state["board"][dx][dy] == match:
                        streak += 1
                        if streak == 4:
                            self.endGame(match - 1)
                        dx += dir[0]
                        dy += dir[1]

                        if dx >= self.dims[0] or dy >= self.dims[1]:
                            break

                j += 1
                if j == self.dims[1]:
                    break

        #if no winner incement move
        self.state["turn"] = (self.state["turn"] + 1) % 2

    def endGame(self, winner):
        #print("Winner", winner)
        #print(self.state["players"][winner])
        self.state["Winner"] = winner
