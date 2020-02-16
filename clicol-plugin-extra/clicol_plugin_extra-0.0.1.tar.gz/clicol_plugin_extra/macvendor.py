#!/usr/bin/env python
"""
 CLICOL plugin package for MAC vendor lookup

 example output:
 ...
"""
from __future__ import print_function
from __future__ import unicode_literals
import re

from netaddr import *


class MACVendor:
    loadonstart = True
    cmap = dict()
    setup = dict()
    regex = ()
    outtype = "append"
    column = 85

    def __init__(self, setup):
        (self.setup, self.cmap) = setup
        self.regex = (
            re.compile(self.cmap['BOS'] + r"(?<![:-])\b((?:[a-fA-F0-9]{2}[:-]){5}[a-fA-F0-9]{2})\b(?![:-])", re.M),
            re.compile(self.cmap['BOS'] + r"(?<!\.)\b((?:[a-fA-F0-9]{4}\.){2}[a-fA-F0-9]{4})\b(?!\.)", re.M))

        if 'outtype' in self.setup.keys():  # Set output type (inline|append)
            if self.setup['outtype'] in ("inline", "append"):
                self.outtype = self.setup['outtype']
        if 'column' in self.setup.keys():  # Set column for append
            self.column = int(self.setup['column'])

    @staticmethod
    def org(mac=""):
        """
        Finds OUI for MAC address
        :param mac: input MAC address
        :return: Organization name for the MAC
        """
        try:
            return EUI(mac).oui.registration()['org']
        except:
            return None

    def plugin_preprocess(self, inputtext, effects=None):
        """
        Search and add MAC vendor data to input text
        :param inputtext: Text to process
        :param effects: not used here
        :return: processed text
        """
        # if effects is None:
        #    effects = []
        output = inputtext
        macdb = dict()
        macs = self.regex[0].findall(inputtext)
        macs.extend(self.regex[1].findall(inputtext))
        for mac in macs:
            org = self.org(mac)
            if org:
                macdb[mac] = org

        if len(macdb) == 0:
            return output

        if self.outtype == 'inline':
            for mac in macdb.keys():
                output = output.replace(mac, "%s(%s)" % (mac, macdb[mac]))
        else:
            out = ""
            #  clean regex for backspaced output on devices
            r = re.compile(r"[\b]+ +[\b]+(.*)", re.UNICODE)
            for line in output.splitlines(True):
                strippedline = line
                match = r.match(line)
                if match:
                    strippedline = match.group(1)
                for mac in macdb.keys():
                    if mac in line:
                        line = line.replace("\r", " %s%sMAC: %s%s\r" % (
                            " " * (self.column - len(strippedline)), self.cmap['description'], macdb[mac],
                            self.cmap['default']))
                out += line
            output = out.encode().decode('unicode_escape')

        return output

    def plugin_test(self):
        """
        Do plugin test
        :return: Test output by this plugin
        """
        return ("plugin.macvendor", "\n preprocess:%s" % self.plugin_preprocess("""
Internet  10.253.226.154         14   3c61.04c6.12fc  ARPA   GigabitEthernet0/0/2.2\r
      320 9cf4.8ee4.f398  dynamic  Yes      300     Po1\r
*     101 f8ca.b819.2dfc  dynamic  Yes        0     Po2\r
"""))
