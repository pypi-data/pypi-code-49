# coding=utf-8
from __future__ import absolute_import, print_function

import os

from suanpan import api
from suanpan.arguments import String
from suanpan.tools import ToolComponent as tc
from suanpan.utils import json


@tc.param(String(key="app", required=True))
@tc.param(String(key="graph", default=os.path.join("tmp", "graph")))
def SPAppGraphUpload(context):
    args = context.args
    filepath = args.graph if args.graph.endswith(".json") else os.path.join(args.graph, f"{args.app}.json")
    api.app.updateAppGraph(args.app, json.load(filepath))


if __name__ == "__main__":
    SPAppGraphUpload()  # pylint: disable=no-value-for-parameter
