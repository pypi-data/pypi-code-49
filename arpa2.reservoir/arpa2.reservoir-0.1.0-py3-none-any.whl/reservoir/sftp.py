#!/usr/bin/env python3
#
# SFTP subsystem for OpenSSH2
#
# This implementation adheres to draft-ietf-secsh-filexfer-13
# which, as I understood it, was never formalised into an RFC because
# there were conflicting implementations that did not reach agreement.
#
# Usage Option #1: Configure it in /etc/ssh/sshd_config as
#
#     Subsystem sftp /path/to/sftp-reservoir
#
# Usage Option #2: Invoke SFTP with an extra option
#
#     sftp -s /path/to/sftp-reservoir ...
#
# Note: SFTP will reproduce stderr output from this program on its stderr.
#
#
# From: Rick van Rein <rick@openfortress.nl>


import sys
import struct

import syslog


syslog.openlog ('sftp-reservoir', syslog.LOG_NDELAY | syslog.LOG_PERROR, syslog.LOG_AUTH)
syslog.syslog (syslog.LOG_INFO, 'Server started for (whoami)')

sshin  = sys.stdin .buffer
sshout = sys.stdout.buffer


# Packet codes
#
SSH_FXP_INIT            =   1
SSH_FXP_VERSION         =   2
SSH_FXP_OPEN            =   3
SSH_FXP_CLOSE           =   4
SSH_FXP_READ            =   5
SSH_FXP_WRITE           =   6
SSH_FXP_LSTAT           =   7
SSH_FXP_FSTAT           =   8
SSH_FXP_SETSTAT         =   9
SSH_FXP_FSETSTAT        =  10
SSH_FXP_OPENDIR         =  11
SSH_FXP_READDIR         =  12
SSH_FXP_REMOVE          =  13
SSH_FXP_MKDIR           =  14
SSH_FXP_RMDIR           =  15
SSH_FXP_REALPATH        =  16
SSH_FXP_STAT            =  17
SSH_FXP_RENAME          =  18
SSH_FXP_READLINK        =  19
SSH_FXP_LINK            =  21
SSH_FXP_BLOCK           =  22
SSH_FXP_UNBLOCK         =  23
SSH_FXP_STATUS          = 101
SSH_FXP_HANDLE          = 102
SSH_FXP_DATA            = 103
SSH_FXP_NAME            = 104
SSH_FXP_ATTRS           = 105
SSH_FXP_EXTENDED        = 200
SSH_FXP_EXTENDED_REPLY  = 201


# The init function treats reqid as the version, and sends its own
# function and any extensions.
#
def ssh_fxp_init (version, msg):
	assert version in [3,6], 'Client version number must be 3 or 6, got %d' % version
	sshout.write (struct.pack ('>IBI', 5, SSH_FXP_VERSION, 6))
	syslog.syslog (syslog.LOG_INFO, 'Protocol initialisation complete')

# Handler function map, from SSH_FXP_ type to handler function
#
handlermap = {
	SSH_FXP_INIT: ssh_fxp_init,
}


# Take a given number of string from a message and return (string,...,msgtail)
#
def getstrings (msg, count):
	retval = []
	pos = 0
	for i in range (count):
		assert len(msg) > pos+4, 'Insufficient message size to carry string length'
		strlen = struct.unpack ('>I', msg [pos:pos+4])
		assert len(msg) > pos+4+strlen, 'Insufficient message size to carry string'
		retval.append (msg [pos+4:pos+4+strlen])
		pos += 4 + strlen
	retval.append (msg [pos:])
	return retval


# Construct a sequence of strings into a message part
#
def mkstrings (*bytestrings):
	retval = b''
	for bs in bytestrings:
		retval += struct.pack ('>I', len (bs)) + bs
	return retval


# Load a message and return its SSH_FXP_ type, reqid, message
#
def getmsg ():
	#
	# Read uint32 length, byte type, uint32 reqid
	# Same-format exception SSH_FXP_INIT: uint32 reqid --> uint32 version
	len_type_reqid = b''
	while len(len_type_reqid) < 9:
		len_type_reqid += sshin.read (9-len(len_type_reqid))
	(ssh_len,ssh_type,ssh_reqid) = struct.unpack ('!IBI', len_type_reqid)
	syslog.syslog (syslog.LOG_INFO, 'Packet length %d, type 0x%02x' % (ssh_len,ssh_type))
	#
	# Check packet validity
	assert ssh_type in handlermap, 'Unsupported package type'
	assert ssh_len >= 5, 'Impossible packet length'
	#
	# Read the message
	ssh_msg = b''
	while len(ssh_msg) + 5 < ssh_len:
		ssh_msg += sshin.read (ssh_len - len(ssh_msg))
	#
	# Return values
	return (ssh_type,ssh_reqid,ssh_msg)


def main ():
	(ssh_type,ssh_reqid,ssh_msg) = getmsg ()
	assert ssh_type == SSH_FXP_INIT, 'Initial packet must be SSH_FXP_INIT'
	assert len(ssh_msg) == 0, 'Initial packet must not have a message'
	handlermap [ssh_type] (ssh_reqid, ssh_msg)
	# print ('SSH Length:', ssh_len  )
	# print ('SSH Type:  ', ssh_type )
	# print ('SSH ReqId: ', ssh_reqid)


if __name__ == '__main__':
	main ()
else:
	main ()

raise NotImplementedError ('The SFTP subsystem for OpenSSH2 is not implemented yet')
