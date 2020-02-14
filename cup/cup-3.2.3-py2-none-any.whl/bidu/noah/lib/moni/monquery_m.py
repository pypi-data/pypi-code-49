################################################################################
#
# Copyright (c) 2014 Baidu.com,  Inc. All Rights Reserved
#
################################################################################
"""
This module provide method to get the argus monitoring item and values
Actually, This moduel is a encapsulation of the tool monquery.

Authors: pankai01(pankai01)
Date:    2014/12/04 19:08:00
"""
from __future__ import print_function
import os
import sys
import commands
import json

class MonQueryCrashException(Exception):
    """class MonQueryCrashException self defined"""
    def __init__(self, msg):
        """init"""
        Exception.__init__(self)
        self.msg = msg


class MonQuery(object):
    """encapsulation of a monquery.
    such as the get all the monitor items of a namespace and the item values between some time
    attention:here,  the timestamp is not the unix timestamp its format is human readable yyyymmddhhmmss
    Attributes:None
    """
    def __init__(self):
        if os.path.exists("/usr/bin/monquery"):
            self._cmdpath = "/usr/bin/monquery"
        else:
            self._cmdpath = "%s/../utils/monquery" % (os.path.dirname(os.path.abspath(__file__)))

    def get_namespace_items(self, name):
        """get items of a namespace"""
        if name == "":
            raise MonQueryCrashException("name empty error")
        entity = name
        if name.find(".baidu.com") != -1:
            entity = name[:name.find(".baidu.com")]
        cmd = "%s -n %s -o json" % (self._cmdpath, entity)
        (stat, output) = commands.getstatusoutput(cmd)
        if stat != 0:
            raise MonQueryCrashException(output)
        ret = []
        try:
            for ln in output.split("\n"):
                if ln == "":continue
                js = json.loads(ln.strip())
                if len(js["item"])!=1:continue
                ret.append({"item_name":js["item"][0]["item_name"], "cycle":js["item"][0]["cycle"]})
        except Exception as e:
            raise MonQueryCrashException(e)
        return ret

    def get_item_value(self, namespace, item_name, start=None, end=None):
        """get montor value of a specified item of the namespace.if start or end is none, we return the latest value"""
        if namespace == "":
            raise MonQueryCrashException("namespace empty error")
        if item_name == "":
            raise MonQueryCrashException("item_name empty error")
        if namespace.find(".baidu.com") != -1:
            namespace = namespace[:namespace.find(".baidu.com")]
        if((start is None) or (end is None)):
            cmd = "%s -n %s -i %s -o json" % (self._cmdpath, namespace, item_name)
        else:
            if len(start) != 14:
                raise MonQueryCrashException("start time format error")
            if len(end) != 14:
                raise MonQueryCrashException("end time format error")
            cmd = "%s -n %s -i %s -s %s -e %s -o json" % (self._cmdpath,\
            namespace, item_name, start, end)
        (stat, output) = commands.getstatusoutput(cmd)
        if stat != 0:
            raise MonQueryCrashException(output)
        ret = []
        try:
            for ln in output.split("\n"):
                if ln.strip()=="":continue
                js = json.loads(ln.strip())
                if len(js["item"])!=1:continue
                if ((start is None) or (end is None)):
                    ret.append({"timestamp":js["item"][0]["timestamp"],\
                    "value":js["item"][0]["value"]})
                else:
                    ret.append({"timestamp":js["timestamp"], "value":js["item"][0]["value"]})
        except Exception as e:
            raise MonQueryCrashException(e)
        if len(ret) == 0:
            msg = "exe failed %s" % (cmd)
            raise MonQueryCrashException(msg)
        return ret

    def get_item_value_avg(self, namespace, item_name, sample_span, start, end):
        """get average value of a item in a period between start and end time"""
        if namespace == "":
            raise MonQueryCrashException("namespace empty error")
        if item_name == "":
            raise MonQueryCrashException("item_name empty error")
        if namespace.find(".baidu.com") != -1:
            namespace = namespace[:namespace.find(".baidu.com")]
        if((start is None) or (end is None)):
            raise MonQueryCrashException("start time or end time empty error")
        if len(start) != 14:
            raise MonQueryCrashException("start time format error")
        if len(end) != 14:
            raise MonQueryCrashException("end time format error")
        cmd = "%s -n %s -i %s -s %s -e %s -o json -d %d" % (self._cmdpath,\
              namespace, item_name, start, end, sample_span)
        (stat, output) = commands.getstatusoutput(cmd)
        if stat != 0:
            raise MonQueryCrashException(output)
        ret = []
        try:
            for ln in output.split("\n"):
                if ln.strip()=="":continue
                js = json.loads(ln.strip())
                if len(js["item"])!=1:continue
                if ((start is None) or (end is None)):
                    ret.append({"timestamp":js["item"][0]["timestamp"],\
                              "value":js["item"][0]["value"]})
                else:
                    ret.append({"timestamp":js["timestamp"], "value":js["item"][0]["value"]})
        except Exception as e:
            raise MonQueryCrashException(e)
        if len(ret) == 0:
            msg = "exe failed %s" % (cmd)
            raise MonQueryCrashException(msg)
        return ret

if __name__ == "__main__":
    mq = MonQuery()
    items = mq.get_namespace_items("cp01-yxtocp021.vm.baidu.com")
    for item in items:
        print(item)
    print(mq.get_item_value("cp01-yxtocp021.vm.baidu.com", "CPU_IDLE",\
                            start=None, end=None))
    print(mq.get_item_value("cp01-yxtocp021.vm.baidu.com", "CPU_IDLE",\
                            start="20141204000000", end="20141204030000"))
    print(mq.get_item_value_avg("cp01-yxtocp021.vm.baidu.com", "CPU_IDLE", \
                                86400, "20141201000000", "20141209000000"))
