import AIArena.games
from AIArena.upload import upload
from AIArena.AI import AI as AI
from AIArena.Human import Human_Connect4 as Human_Connect4

name = "AIArena"

def runGame(Ais,gameName):
    result = {
        "error":"None"
    }
    #Game setup
    try:
        if gameName == "Connect4":
            game = AIArena.games.Connect4(players=Ais)
        elif gameName == "Arena":
            game = AIArena.games.Arena(players=Ais)
        else:
            result["error"] = "Game Creation: Bad Name"
            return result
    except:
        result["error"] = "Game Creation"
        return result

    #Game run
    try:
        gameResult = game.runGame(False)
        result.update(gameResult)
    except:
        result["error"] = "Game Run"
        result["replayStates"] = game.replayStates
        return result
    #gameResult = game.runGame(False)
    #result["replayStates"] = game.replayStates
    result.update(gameResult)

    return result

def runMove(AI, state):
    try:
        move = AI.makeMove(state)
        results = {
            "error": "None"
        }
        if move == None:
            results['error'] = 'Bad move response'
        else:
            results['move'] = move
        return results
    except Exception as e:
        print("EXCEPTION:", e)
        return {'exception': e}


