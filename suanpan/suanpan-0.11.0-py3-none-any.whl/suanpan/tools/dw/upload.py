# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.arguments import String
from suanpan.dw import dw
from suanpan.tools import ToolComponent as tc
from suanpan.utils import csv


@tc.param(String(key="file", required=True))
@tc.param(String(key="table", required=True))
def SPDWUpload(context):
    args = context.args
    dw.writeTable(args.table, csv.load(args.file))


if __name__ == "__main__":
    SPDWUpload()  # pylint: disable=no-value-for-parameter
