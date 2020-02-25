# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.api.requests import affinity


def getAppGraph(appId):
    return affinity.get(f"/app/graph/{appId}")["data"]


def updateAppGraph(appId, graph):
    return affinity.post(f"/app/graph/{appId}", json={"graph": graph})


def revertAppGraph(appId):
    return affinity.post(f"/app/graph/{appId}/revert")
