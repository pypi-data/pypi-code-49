import json
from pathlib import Path

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
HERE = Path(__file__).parent

with open((Path(HERE, 'config/keys.json')), 'r') as keys_file:
    data = keys_file.read()
    data = json.loads(data)
    CONSUMER_KEY = data["consumer_token"]
    CONSUMER_SECRET = data["consumer_token_secret"]