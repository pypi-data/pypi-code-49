#!/usr/bin/env python3

import argparse
import sys

import bottle
from bottle import request, response
import numpy as np
import simplejson as json

from pysisyphus.server.optimizer import OptState


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--nodebug", action="store_false")

    return parser.parse_args(args)


def run_server(host="localhost", port=8080, debug=True):
    cur_module = __import__(__name__)
    app = bottle.default_app()

    @app.post("/init")
    def init():
        data = request.json
        cur_module.opt_state = OptState(**data)

    @app.post("/step")
    def step():
        default_data = {
            "coords": None,
            "energy": None,
            "gradient": None,
            "hessian": None,
        }

        data = request.json
        coords = np.array(data["coords"], dtype=float)
        gradient = np.array(data["gradient"], dtype=float)
        energy = float(data["energy"])

        step, status = cur_module.opt_state.step(coords, energy, gradient)

        resp = {
            "step": step.tolist(),
            "status": status,
        }

        response.content_type = 'application/json'
        return json.dumps(resp)

    bottle.run(host=host, port=port, debug=debug)
    #curl -X POST -H "Content-Type: application/json" -d @h2o.json http://localhost:8080/json


def run():
    args = parse_args(sys.argv[1:])
    print(args)

    host = args.host
    port = args.port
    debug = args.nodebug

    run_server(host=host, port=port, debug=debug)


if __name__ == "__main__":
    # run_server()
    run()
