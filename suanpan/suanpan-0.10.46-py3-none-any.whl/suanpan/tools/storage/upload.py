# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.arguments import String
from suanpan.storage import storage
from suanpan.tools import ToolComponent as tc


@tc.param(String(key="local", required=True))
@tc.param(String(key="remote", required=True))
def SPStorageUpload(context):
    args = context.args
    storage.upload(args.remote, args.local)


if __name__ == "__main__":
    SPStorageUpload()  # pylint: disable=no-value-for-parameter
