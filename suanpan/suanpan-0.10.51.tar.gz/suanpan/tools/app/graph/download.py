# coding=utf-8
from __future__ import absolute_import, print_function

import os

from suanpan import api, path
from suanpan.arguments import String
from suanpan.tools import ToolComponent as tc
from suanpan.utils import json


@tc.param(String(key="app", required=True))
@tc.param(String(key="dist", default=os.path.join("tmp", "graph")))
def SPAppGraphDownload(context):
    args = context.args
    filepath = args.dist if args.dist.endswith(".json") else os.path.join(args.dist, f"{args.app}.json")
    path.mkdirs(filepath, parent=True)
    json.dump(api.app.getAppGraph(args.app), filepath)


if __name__ == "__main__":
    SPAppGraphDownload()  # pylint: disable=no-value-for-parameter
