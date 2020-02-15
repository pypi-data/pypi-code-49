import json
import os

home = os.path.expanduser("~")
fpath = os.path.join(home, ".recvani")

with open(fpath) as f:
    jdata  = json.load(f)

MODEL = jdata.get("MODEL")
API_KEY = jdata.get("API_KEY")
SECRET_KEY = jdata.get("SECRET_KEY")
