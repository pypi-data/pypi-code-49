################################################################################
#
# Copyright (c) Baidu.com,  Inc. All Rights Reserved
#
################################################################################
"""
This module provide basic read operation of baidu meta information.e.g.service,
instance, host.etc.Actually, This moduel is a encapsulation of the tool meta-query.

Authors: pankai01
"""

import os
import sys
import commands
import json

class MetaQueryCrashException(Exception):
    """MetaQueryCrashException class self define"""
    def __init__(self, msg):
        self._msg = "\n%s\n" % (msg)


class MetaQuery(object):
    """encapsulation of a meta-query.or we only include part of meta-qeury function
    such as the relationship of host\service\instance

    Attributes:None
    """
    def __init__(self):
        if os.path.exists("/usr/bin/meta-query"):
            self._cmdpath = "/usr/bin/meta-query"
        else:
            self._cmdpath = "%s/../utils/meta-query" % (os.path.dirname(os.path.abspath(__file__)))

    def do_get_relation_by_name(self, name, type):
        """give a host name , then we return what type of entity is running on it"""
        entity = name
        if name.find(".baidu.com") != -1:
            entity = name[:name.find(".baidu.com")]
        cmd = "%s relation %s %s -j" % (self._cmdpath, type, entity)
        (stat, output) = commands.getstatusoutput(cmd)
        if stat != 0:
            raise MetaQueryCrashException(output)
        obj = None
        try:
            obj = json.loads(output)
        except Exception as e:
            raise MetaQueryCrashException(e)
        ret = []
        for service in obj[entity]:
            ret.append(service["Name"])
        return ret

