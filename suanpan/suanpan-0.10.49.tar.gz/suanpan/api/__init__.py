# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.api import app, component, oss
from suanpan.api.requests import affinity, host

get = host.get
post = host.post
put = host.put
delete = host.delete
call = host.call
