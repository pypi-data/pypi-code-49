__version__ = '0.1.0'

import requests
import json
import pandas as pd

baseUrl = "https://infeedapi.azurewebsites.net"

def getSettings(connectionId, pluginToken):
    url = f"{baseUrl}/connections/{connectionId}/settings-fromplugin?token={pluginToken}"
    resp = requests.get(url)
    return resp.json()

def configure(connectionId, pluginToken, settings):
    url = f"{baseUrl}/connections/{connectionId}/settings-fromplugin?token={pluginToken}"
    data = json.dumps(settings)
    resp = requests.patch(url, data=data, headers={"Content-Type": "application/json"})
    return resp.json()

def stream(connectionId, stream):
    url = f"{baseUrl}/streams/{stream}?cid={connectionId}"
    resp = requests.get(url)
    data = resp.json()
    if "type" in data.keys() and data["type"] == "TimeSeriePeriod":
        return pd.DataFrame(data["values"])
    else:
        return data
