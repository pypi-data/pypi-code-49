# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan import api


def getAppGraph(appId):
    return api.affinity.get(f"/app/graph/{appId}")["data"]


def updateAppGraph(appId, graph):
    return api.affinity.post(f"/app/graph/{appId}", json={"graph": graph})


def revertAppGraph(appId):
    return api.affinity.post(f"/app/graph/{appId}/revert")
