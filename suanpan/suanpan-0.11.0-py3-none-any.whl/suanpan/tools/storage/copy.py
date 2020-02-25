# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.arguments import String
from suanpan.storage import storage
from suanpan.tools import ToolComponent as tc


@tc.param(String(key="src", required=True))
@tc.param(String(key="dist", required=True))
def SPStorageCopy(context):
    args = context.args
    storage.copy(args.src, args.dist)


if __name__ == "__main__":
    SPStorageCopy()  # pylint: disable=no-value-for-parameter
