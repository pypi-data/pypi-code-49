import dill as pickle
import requests

def upload(Ai, game=None, aid=None):
    if aid is None:
        print("Please paste in the AI Id as the third parameter")
        return
    if game is None:
        print("Please enter the game as the second parameter")
        return

    payload = {
        "Ai":Ai,
        "aid":aid,
        "game":game
    }
    sPayload = pickle.dumps(payload,recurse=True)
    r = requests.post("https://us-central1-ai-olympics.cloudfunctions.net/saveAI",sPayload)
    print("status code:",r.status_code)
    print("response:",r.content.decode())


