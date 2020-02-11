from flask import Flask, request

import suanpan
from suanpan import asyncio, g
from suanpan.app import app
from suanpan.app.arguments import String
from suanpan.log import logger
from suanpan.utils import json

if g.debug:
    web = Flask(__name__)

    @web.route("/", methods=["POST"])
    def testWeb():
        with asyncio.lock(thread=True):
            app.args.update(request.json)
        logger.debug(f"App args updated: {app.args}")
        return json.dumps(app.args)

    @app.afterInit
    def startWeb(_):
        asyncio.run(web.run, kwds={"host": "0.0.0.0", "port": 8000}, thread=True)


@app.trigger(interval=10)
@app.trigger.output(String(key="outputData1"))
@app.trigger.param(String(key="param1"))
def test(context):
    args = context.args
    with asyncio.lock(thread=True):
        logger.debug(f"Trigger: {args}")


if __name__ == "__main__":
    suanpan.run(app)
