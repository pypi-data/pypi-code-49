# Arena.py -- Implements a multiplayer arena style deathmatch between AI agents.
# General operation:
# Arena.py works on a simple 50x50 grid where each player may take up one space.
# On each "turn", an agent may opt to do one of the following:
#  1. Move one space in any direction
#  2. Pick up an object present on the space
#  3. "Fire" on a given space with coordinates (depending on the object/weapon equipped)
# Each space is represented as a tuple with the following attrributes:
# (player, item)
# player is either None or the name of the AI on that space.
# item is either None or an int referring to one of the following item codes:
# 0 - health pickup (+10 health)
# 1 - AoE pickup (increases the radius of attacks by one tile)
# TODO: add more of these
# 
# On each turn, the agent will be passed the following game state information:
# {"health": player health as an integer,
#  "board": game board information,
#  "position": the player's position (tuple; row, column)
#  "inventory": list of items picked up
#  "range": The player's firing range (max euclidean distance to a given tile)
#  "aoe": The radius (in tiles) of splash damage on the player's shots
#  "lastmove": bool representing whether the last move was valid
#  "score": Integer representing the player's current score.
# }
# TODO: Implement items and such. So far they will be stripped just to get the game working quickly.

import random
import math
import copy

ACTIONS=[None, "move", "none", "pickup", "fire"]
BOARDWIDTH=25
BOARDHEIGHT=25

def place(board, player, pos, oldPos=None):
    if board[pos[0]][pos[1]][0] is None:
        # Update the board tuple here with (player, oldcontents)
        board[pos[0]][pos[1]]=(player, board[pos[0]][pos[1]][1])
        
        if oldPos is not None:
            board[oldPos[0]][oldPos[1]]=(None, board[oldPos[0]][oldPos[1]][1])
        return True
    return False

def euDist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def checkMove(oldPos, newPos, maxDist=2):
    # The player 
    #print(euDist(oldPos, newPos), oldPos, newPos)
    if newPos[0]<0 or newPos[1]<0 or newPos[0]>=BOARDHEIGHT or newPos[1]>=BOARDWIDTH:
        return False
    
    # The player may move one tile in any direction per turn:
    else:
        # This calculates the overall movement between the two spots:
        dist=euDist(newPos, oldPos)
        # We allow movement along diagonals:
        return dist<maxDist

def doFire(board, target, aoe, baseDamage=10):
    playerDamage={}
    for i, cols in enumerate(board):
        for j, tile in enumerate(cols):
            bPos=(i, j)
            dist=euDist(bPos, target)
            # This means we're within the AoE to actually hit something:
            if dist<=aoe:
                player=board[i][j][0]
                if player is not None:
                    # uses dist+1 so that we don't break when dist is actually 0
                    playerDamage[player]=int(baseDamage/(dist+1))
    return playerDamage


def genArenaPlayer(name, pos, health, aoe, rng, inventory=[], lastmove=None, score=0, board=None):
    arPlayer={}
    arPlayer["name"]=name
    arPlayer["position"]=pos
    arPlayer["health"]=health
    arPlayer["aoe"]=aoe
    arPlayer["lastmove"]=lastmove
    arPlayer["score"]=score
    arPlayer["inventory"]=inventory
    arPlayer["board"]=board
    arPlayer["range"]=rng
    return arPlayer


class Arena:
    def __init__(self, state=None, players=None, replayStates=None, moves=None):
        #Game Constants
        #Moves are spec'd in row, col
        self.dims = (BOARDHEIGHT, BOARDWIDTH)
        
        self.board=[[(None, None) for i in range(self.dims[1])] for j in range(self.dims[0])]

        self.models = {}
        for ai in players:
            self.models[ai.id] = ai
        players = [x.name for x in players]
        self.players=players
        self.originalPlayers=players.copy()
        
        # randomly seed the board with items:
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                pass
        
        # randomly add players to the board:
        self.playerPos={}
        for p in players:
            pos=(random.randint(0, self.dims[0]-1), random.randint(0, self.dims[1]-1))
            while not place(self.board, p, pos):
                pos=(random.randint(0, self.dims[0]-1), random.randint(0, self.dims[1]-1))
            
            # pos should now be the player's position:
            self.playerPos[p]=pos
        
        # Let's do some dictionary comprehension, lads:
        self.playerArr={p: genArenaPlayer(p, self.playerPos[p], 100, 2, 10, board=self.board) for p in players}
        self.lastMove=None
        
        self.shortMoveList=[]
        
        if state:
            self.state = state
        else:
            self.state = {
                "turn": 0,
                "players": players,
                "board": self.board,
                "playerpos": self.playerPos,
                "players": self.playerArr
            }
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
            "error": "none",
            "replayStates": self.replayStates,
            "moves": self.moves
        }

        print("Running Arena")
        # print(self.game.state)
        while "Winner" not in self.state:
            print("Turn: %d" % self.state["turn"])
            for p in self.players:
                # playerArr has the player-accessible player state:
                print(p, self.playerArr)
                if p in self.playerArr:
                    move = self.models[p].makeMove(self.playerArr[p])
                    self.moves.append(move)
                    if not self.makeMove(move, self.models[p]):
                        pass
                        """print("player %s made invalid move" % p)
                        print("Move: ", move)
                        result['rewards'] = self.genErrRewards(p)
                        result['error'] = "AI : " + p + " made an illegal move"
                        return result"""
                        # return -1
                    else:
                        print("player %s made move" % p)
                        print("Move: ", move)
                        self.replayStates.append(copy.deepcopy(self.state))
                elif display:
                    # print("Skipping player "+p.name)
                    pass
            self.postMove()
            if display:
                self.print()

        result['rewards'] = self.genRewards(self.state["Winner"])
        return result

    def genRewards(self, winner):
        rewards = []
        for i, player in enumerate(self.players):
            if i == winner:
                r = 1
            else:
                r = -1
            rewards.append((player, r))
        return rewards

    def genErrRewards(self, screwUp):
        rewards = []
        for i, player in enumerate(self.players):
            if i == screwUp:
                r = -1
            else:
                r = 0
            rewards.append((player, r))
        return rewards

    def colorFormat(self, plrName, text):
        color=41+self.originalPlayers.index(plrName)
        return "\033[1;%dm%s\033[0m" % (color, text)
        
    def print(self):
        print("Round %d---------------" % self.state["turn"])
        for i, cols in enumerate(self.board):
            if i==0:
                trStr="*"
                for j in range(len(cols)):
                    trStr+=str(j%10)
                print(trStr)
            rStr=""
            for j, tile in enumerate(cols):
                if j==0:
                    rStr+=str(i%10)
                if tile[0] is None:
                    rStr+=" "
                else:
                    #plrColor=self.originalPlayers.index(tile[0])
                    rStr+=self.colorFormat(tile[0], "P")#"P"
            print(rStr)
        print()
        print("Moves this turn: ")#+str(self.lastMove))
        for m in self.shortMoveList:
            print(self.colorFormat(m[0], m[0]), m[1])
        print("--------------------")
        print()

    def validateMove(self, move, player):
        player = player.name
        #print("Attempting to validate move ", move, " from player ", player)
        try:
            pl=None
            if player in self.playerArr:
                pl=self.playerArr[player]
            
            # Determine if the player is dead:
            if pl is None:
                #print("pl was none")
                return False
            
            # Determine if the move is actually valid (these will throw an exception if the move
            # is improperly formatted)
            action=move["action"]
            params=move["params"]
            maxDist=pl["range"]
            
            # Now validate the action type:
            if action in ACTIONS:
                if action is None or action=="none":
                    return True
                elif action=="move":
                    return checkMove(pl["position"], params)
                elif action=="fire":
                    #print("player is attempting to fire")
                    # once again, if this fails, then we automatically return false.
                    return checkMove(pl["position"], params, maxDist)
                # Go ahead and specify whatever you want, player. "pickup" doesn't take an argument, and
                # invalid commands won't even be executed.
                else:
                    return True
            else:
                pass
                #print("action not valid")
            return False
            
        except:
            return False

    def makeMove(self, move, player):#assumes move has been validated
        player = player.name
        # Step 1: determine what the player actually wants:
        action=move["action"]
        params=move["params"]
        
        if player not in self.playerArr:
            return
        
        if action=="move":
            newPos=params
            oldPos=self.playerPos[player]
            # Hoo boy...
            self.playerPos[player]=newPos
            self.playerArr[player]["position"]=newPos
            # Now we need to actually update the board:
            place(self.board, player, newPos, oldPos)
        
        elif action=="fire":
            # TODO: add player base damage (rather than the default 10:
            playerDmg=doFire(self.board, params, self.playerArr[player]["aoe"])
            # Update all players who got hit:
            for p in playerDmg:
                pl=self.playerArr[p]
                pl["health"]-=playerDmg[p]
                if pl["health"]<=0:
                    print("Player %s died!" % self.colorFormat(p, p))
                    # Remove them from the game:
                    plPos=self.playerPos[p]
                    self.board[plPos[0]][plPos[1]]=(None, self.board[plPos[0]][plPos[1]][1])
                    del self.playerPos[p]
                    del self.playerArr[p]
        
        elif action=="pickup":
            # We don't actually do anything here (yet!)
            pass
        self.lastMove=(player, move)
        if len(self.shortMoveList)>0 and len(list(self.playerArr.keys()))>0:
            if self.shortMoveList[-1][0]==list(self.playerArr.keys())[-1]:
                self.shortMoveList=[]
        self.shortMoveList.append(self.lastMove)
        return True

    # perform cleanup and determine if the game is over:
    def postMove(self):
        if len(self.playerArr)==1:
            self.endGame(list(self.playerArr)[0])
        elif len(self.playerArr)==0:
            self.endGame(None)
        else:
            # This just indicates that there has been another timestep.
            # The ref keeps track of move history so we don't have to (which is very convenient!)
            self.state["turn"]=self.state["turn"]+1

    def endGame(self, winner):
        #print("Winner", winner)
        #print(self.state["players"][winner])
        winnerInd = self.originalPlayers.index(winner)
        self.state["Winner"] = winnerInd
        self.shortMoveList=[(winner, 'won!')]
