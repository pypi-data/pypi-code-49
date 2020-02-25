import os
import sys
import json
import flask
import getopt
import logging
import socketio
import eventlet
import threading
import webbrowser
import eventlet.wsgi
import forbiddenfruit
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

from spheres.magic import *
from spheres.view import *
from spheres.expressions import *
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

def __init__(app, sockets, port=8080):
    show_prelude()
    app.run(threaded=True, port=port)

PORT = 8080
try:
    arguments, values = getopt.getopt(sys.argv[1:], "p:", ["port="])
    for arg, val in arguments:
        if arg in ("-p", "--port"):
            PORT = val
except getopt.error as err:
    print(str(err))
    sys.exit(2)

thread = threading.Thread(target=__init__, args=(app, sockets, PORT))
thread.start()

webbrowser.open_new_tab("http://localhost:8080")

########################################################################################

while not connected:
    pass