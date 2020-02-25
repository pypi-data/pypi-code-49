# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.api.requests import affinity


def listComponents(limit=9999):
    return affinity.post("/component/list", json={"limit": limit})["list"]


def shareComponent(componentId, userId, name):
    return affinity.post(
        "/component/share",
        json={"id": componentId, "targetUserId": userId, "name": name},
    )
