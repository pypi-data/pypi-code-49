# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.arguments import String
from suanpan.storage import storage
from suanpan.tools import ToolComponent as tc


@tc.param(String(key="remote", required=True))
def SPStorageRemove(context):
    args = context.args
    storage.remove(args.remote)


if __name__ == "__main__":
    SPStorageRemove()  # pylint: disable=no-value-for-parameter
