#!/usr/bin/env python
"""
 CLICOL plugin package for IP calculator

 example output:
 ...
"""
from __future__ import print_function
from __future__ import unicode_literals
from builtins import input
from socket import gethostbyaddr, gaierror, herror


class DNSresolve:
    loadonstart = True
    cmap = dict()
    setup = dict()
    regex = ()
    __IPCALC_KEY = 'R'
    keybinds = (__IPCALC_KEY)

    def __init__(self, setup):
        (self.setup, self.cmap) = setup

    @staticmethod
    def resolve(name):
        name = name.strip()
        if not name:
            return ""
        try:
            resolved = gethostbyaddr(name)
            resolved = "Host: %s, aliases: %s, ipaddrlist: %s" % resolved
        except (gaierror, herror):
            resolved = "Host/IP unknown"
        return resolved

    def plugin_command(self, cmd):
        """
        In the event of user command, this method is run. First plugin checks if it needs to run...
        :param cmd: command by user.
        """
        if cmd == self.__IPCALC_KEY:
            inputstr = input("\r" + " " * 100 + "\rIP/NAME: ")
            print(self.resolve(inputstr))

    def plugin_help(self, command):
        """
        For quick help this function is used to return the help text
        :param command: for checking if we need to return the help text
        :return: If the command is ours, return the help text
        """
        if command == self.__IPCALC_KEY:
            return " Start DNS resolver"
        else:
            return ""

    def plugin_test(self):
        """
        Do plugin test
        :return: Test output by this plugin
        """
        ip = '8.8.8.8'
        name = 'github.com'
        return "plugin.ipcalc", "\n command(%s):\r\n%s" % \
            (self.__IPCALC_KEY, " dnsresolve %s: %s\r\n dnsresolve %s: %s" %
             (ip, self.resolve(ip), name, self.resolve(name)))
