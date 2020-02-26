

import requests
import os

from flask import Flask, request
app = Flask(__name__)
from .dicplus import DicPlus

SECRETS = DicPlus.from_json('secrets.json').secrets

from .secure import *

mykeyset = KeySet(jsonfile = "keySet.json")

mysecurity = Secure(
    service = "https://notif.pnbx.cc",
    private_key=SECRETS.private_key,
    authenticator = {
        "client_id":SECRETS.auth0.client_id,
        "client_secret":SECRETS.auth0.client_secret,
        "domain":SECRETS.auth0.domain
    },
    keySet = mykeyset
)

app.secure = mysecurity


@app.route('/test_signer')
def signer():
    url = "https://webhook.site/8dda8c52-84c2-45fa-a8c3-228bfe972b6e"
    body = {
        "test": "123",
        "test2": "3345"
    }
    headers = app.secure.signed_headers(body, "https://notif.pnbx.cc")
    res = requests.post(url, headers=headers, json=body)
    print(res.status_code)
    return headers


@app.route('/test_signature')
@app.secure.verify(issuers = ["https://notif.pnbx.cc", "https://penbox.eu.auth0.com/"])
def test_signature():
    print("it worked !!")
    return "Yup worked"


@app.route('/test_authorize')
@app.secure.authorize("sms:send email:send")
def test_authorize():
    return "Ok"

@app.route('/test_authenticate')
def test_authenticate():
    app.secure.auth_headers
    return app.secure.auth_headers()
