#!/usr/bin/env python3
#
# Remote Magnetic Tape program, called by mt, tar and so on to dump and
# retrieve backup files and skip the tape forward, backward and so on.
# The 1981 version contains many problems, and is part of GNU tar.  This
# implementation follows the 1989 version, or "version 1", instead.
#
# The purpose of a rmt-reservoir clone is that it allows these existing
# programs to operate directly on the Reservoir, which helps it to be
# useful as a backup stash.
#
# Every tape is represented as a Collection, with backup files presented
# as individual Resource objects.  The simulated tapes are fixed-mounted
# in their own drives, so a backup process can select a Collection by
# accessing a drive.  This allows all backup processes to be setup with
# suitable permissions on the Collection.
#
# The application hint for RMT is the name "Remote magnatic tape", which
# helps to keep the tapes away from the user's Reservoir experience.
# 
# From: Rick van Rein <rick@openfortress.nl>


import sys
import re

import os
import errno



# Excellent hints and references from Joerg Schiller:
# 
# Be careful, the rmt implementation from gtar is outdated since approx. 30 years.
# 
# It implements the old protocol version from 1981 instead of the new protocol 
# version 1 from 1989.
# 
# The old protocol is unable to abstract from binariy incompatibilities in the 
# MTIOCTOP ioctl() implemented e.g. on Linux, compared to a typical UNIX. This 
# typically causes a "tape rewind" command to be mapped to e.g. "erase tape" on 
# the remote side and this usually results in junk values retrieved from the 
# "status" command.
# 
# 
# The implementation from gtar is also slower than the current enhanced version 1 
# implementation.
# 
# See:
# 
# http://schilytools.sourceforge.net/man/man1/rmt.1.html
# 
# For the documentation of the RMT daemon and:
# 
# http://schilytools.sourceforge.net/man/man3/librmt.3.html
# 
# http://schilytools.sourceforge.net/man/man3/rmtgetconn.3.html
# 
# http://schilytools.sourceforge.net/man/man3/rmtopen.3.html
# 
# http://schilytools.sourceforge.net/man/man3/rmtinit.3.html
# 
# http://schilytools.sourceforge.net/man/man3/rmtstatus.3.html
# 
# for a documentation of the application counterpart in librmt.
# 
# The Source code is in schilytools:
# 
# http://sourceforge.net/projects/schilytools/files/

# The client is v1 aware, meaning that it uses the 1989 protocol
#
client_v1 = False


# Reservoir's app hint for RMT
#
rmt_apphint = 'Remote magnetic tape'


# I/O streams for textual and binary interaction
#
stdin  = sys.stdin
stdout = sys.stdout
#
rawin  = sys.stdin .buffer
rawout = sys.stdout.buffer


# The current tape position information in global variables
#   - curtape is the arpa2.reservoir.Index for the current tape
#   - curlist is the list of Resource objects on the curtape
#   - curfidx is the list index of the currently active Resource
#   - curfile is the               the currently active file
#   - curfpos is the position within the current file, -1 for the end
# Values are None when they are undefined.
#
curtape = None
curlist = None
curfidx = None
curfile = None
curfpos = None


# Pattern to recognise all-numeric data
#
int_re = re.compile ('^[0-9]+$')


# Open a remote tape
#  - when "numeric_mode symbolic_mode" is provided, prefer the latter
#  - when only "numeric_mode"
#  - we should not insert files on a simulated tape, but may replace one
#
def rmt_open (device, mode):
	global curtape, curlist, curfidx, curfile, curfpos
	creat = False
	trunc = False
	wr_xs = False
	appnd = False
	# Prefer the two-word symbolic notation
	if ' ' in mode:
		#
		# Map wods to local flags
		mode = mode.split (' ') [1]
		for modeword in mode.split ('|'):
			creat = creat or flagbits in ['CREAT',  'O_CREAT' ]
			trunc = trunc or flagbits in ['TRUNC',  'O_TRUNC' ]
			wr_xs = wr_xs or flagbits in ['RDWR',   'O_RDWR'  ]
			wr_xs = wr_xs or flagbits in ['WRONLY', 'O_WRONLY']
			appnd = appnd or flagbits in ['APPEND', 'O_APPEND']
	else:
		#
		# Minimalism in reliance on numeric modes
		mode = int (mode)
		wr_xs = 0 != (mode & os.O_WRONLY)
		#
		# For Reservoir, the safest writing mode uses O_CREAT
		creat = wr_xs
	raise NotImplementedError ('rmt_open() should return home, hint app, access collection by device name, set curtape')
	#TODO# Setup cur_tape, cur_list
	cur_fidx = 0
	cur_file = None
	cur_fpos = None
	send_ok (0)


# Close the current remote tape
#
def rmt_close (device):
	global curtape, curlist, curfidx, curfile, curfpos
	#TODO# Close the current file, if any, and store the results in LDAP?
	cur_fpos = None
	cur_file = None
	cur_list = None
	cur_tape = None
	send_ok (0)


# Seek to an offset, relative to whence
#
def rmt_whence (whence, offset):
	global curtape, curlist, curfidx, curfile, curfpos
	assert curfile is not None, 'There is no current open file'
	assert curfpos is not None, 'There is no current file position'
	setfpos = 0
	endfpos = curfile.size ()
	whencemap = {
		'0':setfpos, 'SET':setfpos, 'SEEK_SET':setfpos,
		'1':curfpos, 'CUR':curfpos, 'SEEK_CUR':curfpos,
		'2':endfpos, 'END':endfpos, 'SEEK_END':endfpos,
	}
	if whence not in whencemap:
		raise OSError (errno.EINVAL, 'Invalid Whence Argument')
	newfpos = whencemap [whence] + int (offset)
	if newfpos < 0:
		raise RangeError ('Sought before the file start')
	elif newfpos > curfile.size ():
		raise RangeError ('Sought beyond the file end')
	#TODO# Indicate offset to Reservoir
	raise NotImplementedError ('rmt_whence() should seek in the current file')
	curfpos = newfpos
	send_ok (curfpos)


# Be sure to have an open file, open one if needed
#
def have_open_file ():
	global curtape, curlist, curfidx, curfile, curfpos
	if curfile is None:
		if curfidx >= len (curlist):
			raise RangeError ('Crashed the head into the end of the tape')
			curfile = TODO_NEW_RESOURCE
			curfpos = 0
			curlist.append (curfile)


# Be sure to have no open file, but sync if needed
#
def have_sync_file ():
	global curtape, curlist, curfidx, curfile, cuffpos
	if curfile is not None:
		curfile.sync ()
	curfile = None
	curfpos = None


# Read bytes from the current tape
#
def rmt_read (count):
	global curtape, curlist, curfidx, curfile, curfpos
	have_open_file ()
	count = int (count)
	rdbytes = curfile.read (count)
	if count > rdbytes:
		#TODO# Terrible crash, as documented?
		sys.exit (1)
	rdcount = len (rdbytes)
	send_ok (rdcount)
	rawout.send (rdbytes)


# Write bytes to the current tape
#
def rmt_write (count):
	global curtape, curlist, curfidx, curfile, curfpos
	have_open_file ()
	count = int (count)
	wrbytes = rawin.read (count)
	wrcount = curfile.write (wrbytes)
	send_ok (wrcount)


# This is a modern client, running protocol version 1 from 1989.
# The older 1981 protocol has compatibility issues across platforms.
# We proudly acknowledge being just as modern!
#
def rmt_v1probe (count):
	global client_v1
	assert count == 0, 'Client sent v1probe as -1,%d not -1,0' % count
	client_v1 = True
	send_ok (1)


# Close the current file (write EOF markers).
#
def rmt_weof (count):
	global curtape, curlist, curfidx, curfile, curfpos
	have_sync_file ()
	curfidx += 1


# Next file (repeated count times).
#
def rmt_fsf (count):
	global curtape, curlist, curfidx, curfile, curfpos
	have_sync_file ()
	curfidx += 1


# Move back by count files.  Position is at the end of the file.
#
# TODO: Check this with "mt" source code to match "bsf" command.
#
def rmt_bsf (count):
	# raise NotImplementedError ('rmt_bsf() moves back %d files' % count)
	# global curtape, curlist, curfidx, curfile, curfpos
	# have_sync_file ()
	# if curfidx == 0:
	# 	raise RangeError ('Crashed the head into the beginning of the tape')
	# curfidx -= 1
	rmt_nbsf (count)
	have_open_file ()
	curfpos = curfile.size ()


# Find the first file (rewind the tape).
#
def rmt_rew (count):
	global curtape, curlist, curfidx, curfile, curfpos
	have_sync_file ()
	curfidx = 0


# Rewind and put the tape offline.  No current implementation.
#
def rmt_offl (count):
	send_ok (0)


# Perform no operation.  Just report status.
#
def rmt_nop (count):
	send_ok (0)


# Switch the cache on.  Currently meaningless for Reservoir.
#
def rmt_cache (count):
	send_ok (0)


# Switch the cache off.  Currently meaningless for Reservoir.
#
def rmt_nocache (count):
	send_ok (0)


# Retension the tape.  The net effect is to have rewound the tape.
#
def rmt_reten (count):
	rmt_rew (count)


# Erase the entire tape.  This empties the current Collection.
#
def rmt_erase (count):
	raise NotImplementedError ('rmt_erase() does not yet clear out the current Collection')


# Position to end of media.  Newly written files appear after the last.
#
def rmt_eom (count):
	raise NotImplementedError ('rmt_eom() should position at the end of the Reservoir')


# Move back by count files.  Position is at the beginning of the file.
#
def rmt_nbsf (count):
	global curtape, curlist, curfidx, curfile, curfpos
	have_sync_file ()
	assert count <= curfidx, 'The tape was rewound beyond its beginning and may be broken'
	curfidx -= count


# Simulate an ioctl(MTIOCTOP,...) operation
#  - v1 clients send I-1\n0\n to indicate awareness of fixed opcodes 0..7
#
def rmt_ioctl (opcode, count):
	opcode = int (opcode)
	count  = int (count )
	ioctlmap = {
		-1: rmt_v1probe,
		0: rmt_weof,
		1: rmt_fsf,
		2: rmt_bsf,
		#NOTIMPL#TOOTAPY# 3: rmt_fsr,
		#NOTIMPL#TOOTAPY# 4: rmt_bsr,
		5: rmt_rew,
		6: rmt_offl,
		7: rmt_nop,
	}
	if not opcode in ioctlmap:
		raise NotImplementedError ('rmt_ioctl() does not implement %d' % opcode)
	ioctlmap [opcode] (count)


# Simulate an ioctl(MTIOCOP,...) extended operation
def rmt_ioctl_v1 (opcode, count):
	opcode = int (opcode)
	count  = int (count )
	ioctlmap_v1 = {
		0: rmt_cache,
		1: rmt_nocache,
		2: rmt_reten,
		3: rmt_erase,
		4: rmt_eom,
		5: rmt_nbsf,
	}
	if not opcode in ioctlmap:
		raise NotImplementedError ('rmt_ioctl_v1() does not implement %d' % opcode)
	ioctlmap_v1 [opcode] (count)


# Simulate status from an ioctl(MTIOCGET,...) operation
#
# This should probably dump "struct mtget" from st(4).
# Sending a binary structure across systems, so incompatible!
#
def rmt_status (nothing):
	raise NotImplementedError ('rmt_status() is device-dependent and should no longer be used')


# New portable status in version 1.
# NOTE: This command is not terminated with a newline?!?
# On not-so-tapy devices, this may report an error.
#
def rmt_status_v1 (subcmd):
	raise NotImplementederror ('rmt_status_v1() is only necessary for actual tape devices')


# Send the version number, which we proudly announce to be 1.
#
def rmt_version (nothing):
	assert nothing=='', 'Unexpected argument to version command'
	send_ok (1)


# Map command codes to handler functions and whether an extra line is needed
#
handlermap = {
	'O': (rmt_open,True),
	'C': (rmt_close,False),
	'L': (rmt_whence,True),
	'R': (rmt_read,False),
	'W': (rmt_write,False),
	'I': (rmt_ioctl,True),
	'i': (rmt_ioctl_v1,True),
	'S': (rmt_status,False),
	's': (rmt_status_v1,False),
	'v': (rmt_version),
}


# Produce a positive, numerical response
#
def send_ok (number):
	stdout.write ('A%d\n' % number)


# Produce an error message, both as a code and string
# Note well: Remote sending of errno codes that are not standardised!
#
def send_error (code, message):
	assert not '\n' in message, 'Error messages must not hold line breaks'
	stdout.write ('E%d\n%s\n' % (code,message))


def main ():
	while True:
		cmd = stdin.readline ()
		assert cmd [:1] in handlermap, 'Unrecognised command %s' % cmd
		assert cmd [-1:] == '\n', 'Command is incomplete'
		(hdlfun,extra) = handlermap [cmd [:1]]
		arg0 = cmd [1:-1]
		if extra:
			arg1 = stdin.readline ()
			assert arg1 [-1:] == '\n', 'Argument line is incomplete'
		try:
			if extra:
				hdlfun (arg0, arg1)
			else:
				hdlfun (arg0)
		except OSError as ose:
			send_error (ose.errno, ose.strerror)
		except AssertionError as ae:
			send_error (errno.EINVAL, str(ae))
		except ValueError:
			send_error (errno.EINVAL, 'Invalid Argument')
		except NotImplementedError as nie:
			send_error (errno.ENOSYS, str(nie))

if __name__ == '__main__':
	main ()
else:
	main ()

raise NotImplementedError ('The rmt-reservoir program is not complete')
