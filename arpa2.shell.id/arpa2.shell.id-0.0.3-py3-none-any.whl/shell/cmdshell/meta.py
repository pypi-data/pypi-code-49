#!/usr/bin/env python2.7
#
# arpa2.shell.meta -- an ARPA2 Shell to access other shells.
#
# This meta-shell is used to gain access to other shells.
# Since access control is practiced on a per-command basis,
# there is usually no restrictions on showing a prompt for
# each installed shell to any user.  The meta-shell is
# mostly useful to have an access point for remote access,
# such as from an OpenSSH daemon.
#
# This command assumes that setuptools has been used to
# declare entry_points for the group arpa2.shell.cmdshell.subclasses
# with a class name in each.  This allows the separate
# installation of arpa2.shell packages that can then be
# called from this meta-shell.
#
# The JSON infrastructure would not call the meta-shell
# command, but it may use the same group to find the
# locally installed classes to send JSON messages to.
#
# From: Rick van Rein <rick@openfortress.nl>


import os
import sys

import pkg_resources

from .base import Cmd
# from arpa2.shell.cmdshell import base #as a2cmd

entrypoint_group = 'arpa2.shell.cmdshell.subclasses'


# Return a map of shells that can be reached.  The return
# value is a dictionary, mapping a shell class name to a class
# that is loaded from the shell's module.
def named_shell_classes ():
	shells = { }
	for cmd in pkg_resources.iter_entry_points (group=entrypoint_group):
		#DEBUG# print ('Command name is', cmd.name, 'in', cmd.module_name)
		#DEBUG# print ('Entry point offers', dir (cmd))
		cmd_cls = cmd.load ()
		#DEBUG# print ('Command class is', type (cmd_cls))
		if not issubclass (cmd_cls, Cmd):
			raise Exception ('%s is not an ARPA2 Shell' % (cmd.name,))
			continue
		shells [cmd.name] = cmd_cls
	return shells


# The arpa2.shell is invoked with packages to load and
# whose Cmd to start, followed by mutual introductions.
# Each of these Cmd instances are assumed to derive
# from arpa2.shell.Cmd.
#
def main ():
	arpa2base = Cmd ()
	# arpa2base = sys.modules [__name__]
	#DEBUG# print ('My shell module is', arpa2base, '::', type (arpa2base))
	shells = named_shell_classes ()
	#DEBUG# print ('All shell modules are', shells)
	for (shnm,shcls) in shells.items ():
		#DEBUG# print ('Shell class for', shnm, 'has', dir (shcls), '::', shcls)
		cmd = shcls ()
		if not isinstance (cmd, Cmd):
			raise Exception ('%s is not an ARPA2 shell' % (shnm,))
		arpa2base.know_about (shnm, cmd)
		cmd.know_about ('arpa2.shell', arpa2base)
	current_shell = arpa2base
	while current_shell is not None:
		current_shell.next_shell = None
		current_shell.cmdloop ()
		current_shell.reset ()
		current_shell = current_shell.next_shell


# When this script is called directly, run the main function
#
if __name__ == '__main__':
	main ()
