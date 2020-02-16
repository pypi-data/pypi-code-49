import json
import requests

def post(url, data=None, headers=None, **kwargs):
    def testPostRequest(func):
        def wrapper(*args, **kwargs):
            resp = requests.post(url, data=data)
            j = json.loads(resp.text)
            func(resp, j)
        return wrapper
    return testPostRequest