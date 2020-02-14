################################################################################
#
# Copyright (c) 2014 Baidu.com,  Inc. All Rights Reserved
#
################################################################################
"""
This module provide method to get the argus alert information.
If you want to get all of the raw alerts you can use the "raw" version of method.
Of else you can use the merge verision method which is processed by me.

Authors: pankai01(pankai01)
Date:    2014/12/05 99:23:00
"""
from __future__ import print_function
import os
import sys
import urllib
import json
import commands


class AlertException(Exception):
    """self define class AlertException"""
    def __init__(self, msg):
        """init"""
        Exception.__init__(self)
        self.msg = msg

class Alerts(object):
    """This class provide alert information read method"""
    def __init__(self):
        if os.path.exists("/usr/bin/montool"):
            self._montool_cmdpath = "/usr/bin/montool"
        else:
            self._montool_cmdpath = "%s/../utils/montool.py" \
                                     % (os.path.dirname(os.path.abspath(__file__)))

    def _get_url_content(self, url):
        rp = None
        try:
            rp = urllib.urlopen(url)
            if rp is None:
                raise AlertException("urlopen failed")
            if 200 != rp.getcode():
                raise AlertException("http code not 200")
        except HTTPError as e:
            raise AlertException("http exception")
        return rp.read()

    def get_all_rules(self, namespace):
        """get rule list of a namespace.type=instance, service, host"""
        if namespace == "":
            raise AlertException("namespace empty error")
        if type == "":
            raise AlertException("type empty error")
        if namespace.find(".baidu.com") != -1:
            namespace = namespace[:namespace.find(".baidu.com")]
        rules = []
        cmd = "%s -r %s" % (self._montool_cmdpath, namespace)
        (stat, output) = commands.getstatusoutput(cmd)
        if stat != 0:
            raise AlertException("access montool error ret code not 0")
        for ln in output.split("\n"):
            rule_name = ln.strip().split()[0]
            blocked = ln.strip().split()[1]
            rules.append({"rule_name":rule_name, "blocked":blocked})
        return rules

    def get_raw_alerts(self, namespace, start_time, end_time):
        """get the raw alerts infomation"""
        if namespace == "":
            raise AlertException("namespace empty error")
        if namespace.find(".baidu.com") != -1:
            namespace = namespace[:namespace.find(".baidu.com")]
        url_1 = "http://mt.noah.baidu.com/api/?\
                r=API/AlertList&namespace=%s&start_time=%s&end_time=%s&per_page=1" \
                 % (namespace, start_time, end_time)
        content = self._get_url_content(url_1)
        alerts = []
        try:
            js = json.loads(content)
            if js["success"] != True:
                AlertException, js["message"]
            total = int(js["data"]["total"])
            per_page = 20
            times = total / per_page + 1
            for i in range(0, times):
                url_2 = "http://mt.noah.baidu.com/api/?\
                r=API/AlertList&namespace=%s&start_time=%s&\
                end_time=%s&per_page=%d&cur_page=%d" % (namespace,\
                start_time, end_time, per_page, i + 1)
                onepass = json.loads(self._get_url_content(url_2))
                for item in onepass["data"]["datas"]:
                    alerts.append(item)
        except Exception as e:
            raise AlertException(e)
        return alerts


if __name__ == "__main__":
    alt = Alerts()
    try:
        print(alt.get_all_rules("cp01-yxtocp021.vm.baidu.com"))
        # alerts = alt.get_raw_alerts("lcdc.spide", "20141205000000", "20141205010000")
        # for alert  in alerts:
        #     print alert["mail_title"]
    except Exception as e:
        print(e)
