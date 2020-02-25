from .sign import *
import requests

from flask import Flask, request
app = Flask(__name__)

KEYSET = DicPlus.from_json('keys.json')

myverif = Verifyer(
    issuer="http://localhost:2000",
    audience="http://127.0.0.1:5000/test",
    keySet=KEYSET.public_key
)
mysigner = Signer(
    issuer="http://localhost:2000",
    audience="http://127.0.0.1:5000/test",
    private_key=KEYSET.private_key
)


@app.route('/')
def signer():
    url = "https://webhook.site/8dda8c52-84c2-45fa-a8c3-228bfe972b6e"
    body = {
        "test": "123",
        "test2": "3345"
    }
    headers = {
        "Authorization": "Signature {}".format(mysigner.sign(body))
    }
    res = requests.post(url, headers=headers, json=body)
    print(res.status_code)
    return 'Hello, World!'


@app.route('/test')
@myverif.verify
def veryfier():
    print("it worked !!")
    return "Yup worked"
