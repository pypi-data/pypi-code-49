# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan import g


class Interface(object):
    def __init__(self, request):
        super(Interface, self).__init__()
        self.request = request

    def init(self, suanpanUrl):
        return self.request.post(
            "/api/suanpan/init",
            json={
                "suanpanUrl": suanpanUrl,
                "userId": g.userId,
                "accessKey": g.accessKey,
                "accessSecret": g.accessSecret,
            },
        )
