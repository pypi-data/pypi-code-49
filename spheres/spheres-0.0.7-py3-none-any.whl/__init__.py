import os
import json
import flask
import logging
import socketio
import eventlet
import threading
import eventlet.wsgi
from termcolor import colored

########################################################################################

sockets = socketio.Server(async_mode='threading')
app = flask.Flask(__name__)
app.wsgi_app = socketio.Middleware(sockets, app.wsgi_app)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

########################################################################################

def show(s):
    print(colored("\n> ", "yellow")+colored(s, "magenta"))

def show_prelude():
    os.system("clear")
    print(colored("WELCOME", "green", "on_blue", attrs=['blink', 'bold'])+\
          colored(" TO ", "green", "on_blue", attrs=['blink', 'bold'])+\
          colored("SPHERES!", "green", "on_blue", attrs=['blink', 'bold']))

########################################################################################

from spheres.view import *
from spheres.magic import *
from spheres.sphere import *

########################################################################################

@app.route("/")
def root():
    return flask.render_template("index.html")

########################################################################################

connected = False
@sockets.on("connect")
def connect(sid, data):
    global connected
    connected = True
    show("%s connected" % sid)

@sockets.on("disconnect")
def disconnect(sid):
    show("%s disconnected" % sid)

@sockets.on("call")
def call(sid, data):
    if data["uuid"] in View.views:
        obj = View.views[data["uuid"]]
        if hasattr(obj, data["func"]):
            return getattr(obj, data["func"])(*data["args"])
        else:
            return {"error": "server attribute %s not found!" % data["func"]}
    else:
        return {"error": "server object %s not found!" % data["uuid"]}

########################################################################################

def __init__(app, sockets):
    show_prelude()
    app.run(threaded=True, port=8080)

thread = threading.Thread(target=__init__, args=(app, sockets))
thread.start()

########################################################################################

while not connected:
    pass