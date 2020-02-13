from .enviroment import CONSUMER_KEY, CONSUMER_SECRET, HERE
from pathlib import Path
import tweepy
import webbrowser
import json

def run() -> tweepy.API:
    
    success, token = fetch_token()

    if success:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(token["access_token"], token["access_token_secret"])
        return tweepy.API(auth)
    else:
        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            redirect_url = auth.get_authorization_url()
            webbrowser.open_new_tab(redirect_url)
            
            print("Check your browser for an authorization form :D")
            code = input("Insert the code Twitter provided:")

            auth.get_access_token(verifier=code)
            store_token(auth)
            return tweepy.API(auth)
        except tweepy.TweepError:
            print('Error! Maybe you\'ve passed the wrong code :/.')
    
    return tweepy.API(auth)

def store_token(token):
    with open(Path(HERE, 'config/user_keys.json'), 'w') as token_file:
        token_file.write(
            json.dumps(
                {
                    "access_token": token.access_token, 
                    "access_token_secret": token.access_token_secret
                }
            )
        )

def fetch_token() -> (bool, None): 
    try:
        with open(Path(HERE, 'config/user_keys.json'), 'r') as token_file:
            tokens = json.loads(token_file.read())
            if tokens["access_token"] is not None and tokens["access_token_secret"] is not None:
                return True, tokens
            else:
                return False, None
    except:
        return False, None