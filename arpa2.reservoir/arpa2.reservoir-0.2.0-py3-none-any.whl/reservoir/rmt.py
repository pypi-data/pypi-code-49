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
from os import environ
import errno


from arpa2 import reservoir



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


#
# Reservoir Collection Naming for Remote Magnetic Tape:
#
# 'documentIdentifier': 'active, gen %d, file %d'  [ + ', ...' ]
#
#   -> 'active' means currently being used
#   -> 'gen' is an integer for #prior tape erases
#   -> 'file' is an integer for #preceding files
#
# 'documentIdentifier': 'erased, gen %d, file %d'  [ + ', ...' ]
#
#   -> 'erased' means that it has been wiped
#   -> 'gen' is the generation that was wiped
#   -> 'file' was the file number that was wiped
#
# This structure allows us to communicate erasure but
# still apply some management.  Simple searches will
# allow us to quickly find the active files, and/or the
# last erasure.
#
# Note: Erasure marks are less accurate than a counter.
#       They are idempotent, in that erasing an empty
#       tape will not increment the generation number.
#
rex_active = '^active, *gen *([1-9][0-9]*|0), *file *([1-9][0-9]*|0)(?:,|$)'
rex_erased = '^erased, *gen *([1-9][0-9]*|0), *file *([1-9][0-9]*|0)(?:,|$)'
re_active = re.compile (rex_active)
re_erased = re.compile (rex_erased)


# The current tape position information in global variables
#   - curtape is the arpa2.reservoir.Index for the current tape
#   - curlist is the list of Resource objects on the curtape
#   - curfidx is the list index of the currently active Resource
#   - curfile is the               the currently active file
# Values are None when they are undefined.
#
curtape = None
curtgen = None
curlist = None
curfidx = None
curfile = None


# Pattern to recognise all-numeric data
#
int_re = re.compile ('^[0-9]+$')


# Load a tape.  First try to get only active elements, as that
# already holds the generation.  If this does not work, load all
# data and work out the generation from that.
#
def tape_load (tapename, domain, user=None):
	global curtape, curtgen, curlist, curfidx, curfile
	if user is None:
		idx = reservoir.get_domain (domain)
	else:
		idx = reservoir.get_domain_user (domain, user)
	idx.index_apphint (rmt_apphint)
	idx.index_name (tapename)
	contents = reservoir.search_resources (idx, '(documentIdentifier=active,*)')
	re_ = re_active
	is_erased = curlist == []
	if is_erased:
		contents = reservoir.search_resources (idx, '(documentIdentifier=erased,*)')
		re_ = re_erased
	# Collect map_all : (generation,file) -> Resource
	map_all = { }
	for (rscuuid,rsc) in contents.items ():
		for doi in rsc ['documentIdentifier']:
			m = re_.match (doi)
			if m is None:
				continue
			(gen,fil) = m.groups ()
			if not re_int.match (gen):
				continue
			if not re_int.match (fil):
				continue
			map_all [ (int(gen),int(fil)) ] = rsc
	# Determine the generation
	gen = max ([-1] + [ g
			for (g,f) in map_all.keys () ])
	if is_erased:
		gen += 1
	# Determine the file number
	fil = 1 + max ([-1] + [ f
			for (g,f) in map_all.keys () 
			if g == gen ])
	# Fill out the tape position
	curtape = idx
	curtgen = max (0, gen + 1 if is_erased else gen)
	curlist = [ None ] * (fil + 1)
	curfidx = 0
	for (g,f) in map_all.keys ():
		if g == gen:
			curlist [f] = map_all [ (g,f) ]
			if f > curfidx:
				curfidx = f + 1
	# Do not open the file until the latest (no vain truncations)
	curfile = None


# Open a remote tape
#  - when "numeric_mode symbolic_mode" is provided, prefer the latter
#  - when only "numeric_mode"
#  - we should not insert files on a simulated tape, but may replace one
#
def rmt_open (device, mode):
	global curtape, curlist, curfidx, curfile
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
			creat = creat or modeword in ['CREAT',  'O_CREAT' ]
			trunc = trunc or modeword in ['TRUNC',  'O_TRUNC' ]
			wr_xs = wr_xs or modeword in ['RDWR',   'O_RDWR'  ]
			wr_xs = wr_xs or modeword in ['WRONLY', 'O_WRONLY']
			appnd = appnd or modeword in ['APPEND', 'O_APPEND']
	else:
		#
		# Minimalism in reliance on numeric modes
		mode = int (mode)
		wr_xs = 0 != (mode & os.O_WRONLY)
		#
		# For Reservoir, the safest writing mode uses O_CREAT
		creat = wr_xs
	# Access LDAP and setup curtape and so on
	#TODO# Rather limited approach to finding user@domain information
	(user,domain) = os.environ ['REMOTE_USER'].rsplit ('@', 1)
	tape_load (device, domain=domain, user=user)
	send_ok (0)


# Close the current remote tape
#
def rmt_close (device):
	global curtape, curlist, curfidx, curfile
	if curfile is not None:
		curfile.close ()
	curfile = None
	curlist = None
	curtape = None
	send_ok (0)


# Seek to an offset, relative to whence
#
def rmt_whence (whence, offset):
	global curtape, curlist, curfidx, curfile
	assert curfile is not None, 'There is no current open file'
	offset = int (offset)
	whencemap = {
		'0':0, 'SET':0, 'SEEK_SET':0,
		'1':1, 'CUR':1, 'SEEK_CUR':1,
		'2':2, 'END':2, 'SEEK_END':2,
	}
	if whence not in whencemap:
		raise OSError (errno.EINVAL, 'Invalid Whence Argument')
	curfpos = curfile.seek (offset, whencemap [whence])
	send_ok (curfpos)


# Be sure to have an open file, open one if needed
#
def have_open_file ():
	global curtape, curtgen, curlist, curfidx, curfile
	if curfile is None:
		# Fillup with None if needed
		while curfidx >= len (curlist):
			curlist.append (None)
		# Append a new Resource at the end if needed
		if curlist [curfidx] is None:
			cn  = 'backup, gen %d, file %d' % (curtgen,curfidx)
			doi = 'active, gen %d, file %d' % (curtgen,curfidx)
			meta = {
				'objectClass': ['reservoirResource'],
				'cn': cn,
				'mediaType': ['application/octet-stream'],
				'documentIdentifier': doi,
			}
			newres = reservoir.add_resource (curtape, **meta)
			curlist [curfidx] = newres
		# Open the file at position 0 (not truncated)
		curfile = curlist [curfidx].open (reading=True, writing=True)


# Be sure to have no open file, but sync if needed
#
def have_sync_file ():
	global curtape, curlist, curfidx, curfile
	if curfile is not None:
		curfile.sync ()
	curfile = None


# Read bytes from the current tape
#
def rmt_read (count):
	global curtape, curlist, curfidx, curfile
	count = int (count)
	have_open_file ()
	rdbytes = curfile.read (count)
	rdcount = len (rdbytes)
	if count > rdcount:
		#TODO# Terrible crash, as documented?
		sys.exit (1)
	send_ok (rdcount)
	#TODO#MAYNOTWORK# rawout.write (rdbytes)
	stdout.write (rdbytes)


# Write bytes to the current tape
#
def rmt_write (count):
	global curtape, curlist, curfidx, curfile
	count = int (count)
	#TODO#WONTWORK# wrbytes = rawin.read (count)
	wrbytes = stdin.read (count)
	have_open_file ()
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


# Truncate the current file at the current position (write EOF markers).
#
def rmt_weof (count):
	global curtape, curlist, curfidx, curfile
	if not client_v1:
		raise NotImplementedError ('Upgrade required: EOF marker writing is unsafe for clients predating version 1 of 1989')
	for c in range (int (count)):
		have_open_file ()
		curfile.truncate ()
		have_sync_file ()
		curfidx += 1


# Next file (repeated count times).  Position tape on the
# first block.
#
def rmt_fsf (count):
	global curtape, curlist, curfidx, curfile
	have_sync_file ()
	curfidx += int (count)


# Move back by count files.  Position is at the end of the file.
#
def rmt_bsf (count):
	rmt_nbsf (count)
	have_open_file ()
	curfile.seek (0, whence=2)


# Find the first file (rewind the tape).
#
def rmt_rew (count):
	global curtape, curlist, curfidx, curfile
	have_sync_file ()
	curfidx = 0


# Rewind and put the tape offline.  No current implementation.
#
def rmt_offl (count):
	have_sync_file ()
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
# Note that this might be useful in the future, to repair trouble.
#
def rmt_reten (count):
	rmt_rew (count)


# Erase the entire tape.  This empties the current Collection.
#
# Implementation does not erase files, but increment generation.
# However, when no file was opened, there will be no new generation.
#
def rmt_erase (count):
	if not client_v1:
		raise NotImplementedError ('Upgrade required: Tape erase is unsafe for clients predating version 1 of 1989')
	if curlist != []:
		have_sync_file ()
		curtgen += 1
		curlist = [ ]
		curfidx = 0


# Position to end of media.  Newly written files appear after the last.
#
def rmt_eom (count):
	have_sync_file ()
	curfidx = len (curlist)


# Move back by count files.  Position is at the beginning of the file.
#
def rmt_nbsf (count):
	global curtape, curlist, curfidx, curfile
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
	'' : (rmt_nop,False),
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


# Read and process commands; read from stdin and write to stdout
# This program does not fork, it is started for one session only.
#
def main ():
	while True:
		cmd = stdin.readline ()
		if cmd == '':
			break
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
		stdout.flush ()

if __name__ == '__main__':
	main ()

