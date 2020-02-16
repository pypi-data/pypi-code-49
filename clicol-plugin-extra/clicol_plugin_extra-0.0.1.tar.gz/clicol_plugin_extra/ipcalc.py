#!/usr/bin/env python
"""
 CLICOL plugin package for IP calculator

 example output:
 ...
"""
from __future__ import print_function
from __future__ import unicode_literals
from builtins import input
from netaddr import IPNetwork, IPAddress, AddrFormatError


class IPCalc:
    loadonstart = True
    cmap = dict()
    setup = dict()
    regex = ()
    __IPCALC_KEY = 'I'
    keybinds = (__IPCALC_KEY)

    def __init__(self, setup):
        (self.setup, self.cmap) = setup

    @staticmethod
    def showip(ip):
        """
        Display IP data
        :param ip: input IP network object (netaddr.IPNetwork)
        :return: filled table of IP data
        """
        output = ""
        output += "ipaddress:\t%s\r\n" % ip.ip
        output += "network/nm:\t%s\r\n" % ip.cidr
        output += "prefixlen:\t%s\r\n" % ip.prefixlen
        output += "netmask:\t%s\r\n" % ip.netmask
        if ip.version == 4:
            output += "wildcard:\t%s\r\n" % IPAddress(IPNetwork('255.255.255.255').value - ip.netmask.value)
        output += "network:\t%s\r\n" % ip.network
        output += "broadcast:\t%s\r\n" % ip.broadcast
        if len(ip) <= 2:
            output += "number of ips:\t%s\r\n" % len(ip)
        else:
            output += "number of ips:\t%s - 2 = %s\r\n" % (len(ip), len(ip) - 2)
        output += "first host:\t%s\r\n" % (ip[1] if len(ip) > 2 else ip[0])
        output += "last host:\t%s\r\n" % (ip[-2] if len(ip) > 2 else ip[len(ip)-1])

        return output

    def plugin_command(self, cmd):
        """
        In the event of user command, this method is run. First plugin checks if it needs to run...
        :param cmd: command by user.
        """
        if cmd == self.__IPCALC_KEY:
            inputstr = input("\r" + " " * 100 + "\rIP: ")
            #  Support 10.0.0.0 255.255.0.0 format
            inputstr = inputstr.replace(" ", "/")
            try:
                print(self.showip(IPNetwork(inputstr)))
            except AddrFormatError:
                print("Invalid input!")

    def plugin_help(self, command):
        """
        For quick help this function is used to return the help text
        :param command: for checking if we need to return the help text
        :return: If the command is ours, return the help text
        """
        if command == self.__IPCALC_KEY:
            return " Start IP calculator"
        else:
            return ""

    def plugin_test(self):
        """
        Do plugin test
        :return: Test output by this plugin
        """
        ip = IPNetwork('192.168.0.2/27')
        return "plugin.ipcalc", "\n command(%s):%s" % \
               (self.__IPCALC_KEY, " ipcalc 192.168.0.2/27:\r\n" + self.showip(ip))
