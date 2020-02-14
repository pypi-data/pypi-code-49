#!/usr/bin/env python
#
# arpa2dns -- Manage data published in DNS
#
# From: Rick van Rein <rick@openfortress.nl>


import os
import sys
import uuid
import string
import re

from arpa2.shell import cmdshell, cmdparser

import json


#
# This uses the Python library to control Knot DNS.
# Its document includes a decent example:
#
#     Example:
#         import json
#         from libknot.control import *
#     
#         #load_lib("/usr/lib/libknot.so")
#     
#         ctl = KnotCtl()
#         ctl.connect("/var/run/knot/knot.sock")
#     
#         try:
#             ctl.send_block(cmd="conf-begin")
#             resp = ctl.receive_block()
#     
#             ctl.send_block(cmd="conf-set", section="zone", item="domain", data="test")
#             resp = ctl.receive_block()
#     
#             ctl.send_block(cmd="conf-commit")
#             resp = ctl.receive_block()
#     
#             ctl.send_block(cmd="conf-read", section="zone", item="domain")
#             resp = ctl.receive_block()
#             print(json.dumps(resp, indent=4))
#         finally:
#             ctl.send(KnotCtlType.END)
#             ctl.close()
#


from ..arpa2dns import tightknot

#TESTCODE# #TODO# BE LAZY, BOOT KNOTD FROM HERE
#TESTCODE# os.system ("/etc/init.d/knot start")
#TESTCODE# import time
#TESTCODE# time.sleep (2)
#TESTCODE#
#TESTCODE#
#TESTCODE# #TODO# BE LAZY, START THINGS FROM HERE
#TESTCODE# 
#TESTCODE# knot = tightknot.TightKnot ()
#TESTCODE# 
#TESTCODE# knot.have_conf ()
#TESTCODE# # knot.knot (cmd='conf-set', section='zone', item='domain', data='orvelte.nep')
#TESTCODE# knot.add_zone ('orvelte.nep')
#TESTCODE# knot.try_commit ()
#TESTCODE# 
#TESTCODE# knot.have_zones ('orvelte.nep')
#TESTCODE# knot.add_rr ('orvelte.nep', '@',
#TESTCODE# 		'3600', 'SOA',
#TESTCODE# 		'ns1.orvelte.nep. admin.orvelte.nep. 0 10800 3600 1814400 3600')
#TESTCODE# # knot.knotc_shell ('zone-set orvelte.nep @ 3600 SOA ns1.orvelte.nep. admin.orvelte.nep. 0 10800 3600 1814400 3600', expect_ok=True)
#TESTCODE# knot.add_rr ('orvelte.nep', '_443._tcp.www',
#TESTCODE# 		'3600', 'TLSA',
#TESTCODE# 		('%d %d %d %s' % (0,1,2,'6660')))
#TESTCODE# # knot.knotc_shell ('zone-set orvelte.nep _443._tcp.www.orvelte.nep 3600 TLSA 0 1 2 666', expect_ok=True)
#TESTCODE# knot.try_commit ()
#TESTCODE# 
#TESTCODE# knot.have_zones ('orvelte.nep')
#TESTCODE# knot.del_rr ('orvelte.nep', '_443._tcp.www',
#TESTCODE# 		'3600', 'TLSA',
#TESTCODE# 		('%d %d %d %s' % (0,1,2,'6660')))
#TESTCODE# knot.try_commit ()
#TESTCODE# 
#TESTCODE# knot.have_conf ()
#TESTCODE# # knot.knot (cmd='conf-unset', section='zone', item='domain', data='orvelte.nep')
#TESTCODE# knot.del_zone ('orvelte.nep')
#TESTCODE# knot.force_abort ()
#TESTCODE# 
#TESTCODE# knot.close ()


#
# Map ENUM aliases to their unfriendly DNS form.
#
# This is a user convenience.  Whenever the form
# +ddddddd
# is entered in the position of a zone, it is mapped to
# d.d.d.d.d.d.d.e164.arpa
# which is the naming scheme of ENUM in DNS.
#
# Dashes and dots in the interior of the number are
# silently removed.  This means that zones must not
# have labels that begin with + which is indeed not
# permitted by the <label> grammar in RFC 1035.  We
# would stop matching when a letter occurred in the
# zone name though, and that is also required.
#
# Other forms pass through this function without change,
# so normal zones shall not be modified.
#
enum_short_form = re.compile ('^[+][0-9-.]{3,}$')
def map_enum (tel_or_zone):
	if not enum_short_form.match (tel_or_zone):
		return tel_or_zone
	dns_form = 'e164.arpa'
	for d in tel_or_zone:
		if d in string.digits:
			dns_form = d + '.' + dns_form
	return dns_form

#
# Test if a zone is in ENUM form.
#
enum_zone = re.compile ('^([0-9][.]){3,}e164[.]arpa$')
def is_enum (zone):
	return enum_zone.match (zone) is not None


#
# Map an ENUM zone form or short form to a number,
# digits only.
#
def enum_digits (tel_or_zone):
	zone = map_enum (tel_or_zone)
	if not is_enum (zone):
		return None
	retval = ''
	for digidx in range (len (zone) - 11, -1, -2):
		retval += zone [digidx]
	return retval

#
# Map an ENUM service-field to the services it provides.
#
enum_service_field_re = re.compile ('^E2U(?:[+][A-Za-z0-9-]{1,32}(?:[:][A-Za-z0-9-]{1,32})*)+$')
def enum_service_field (service_field):
	if enum_service_field_re.match (service_field) is None:
		return None
	retval = { }
	for svc_sub in service_field [4:].split ('+'):
		svc_type_subs = svc_sub.split (':')
		svc_type = svc_type_subs [0]
		svc_subs = svc_type_subs [1:]
		if svc_type in retval:
			return None
		retval [svc_type] = svc_subs
	return retval

#
# Produce lists of new values (or indicate anything is accepted)
#
#TODO# Map to arpa2dns values
#
def token_factory (token):
	# For now, allow anything
	return None



class Cmd (cmdshell.Cmd):

	version = (0,0)
	prompt = 'arpa2dns> '
	intro = 'Edit zone data.  Be reported on expected times of publication, based on prior\nrecord timings.  Throughout this shell, you can enter phone numbers in +dddddd\nformat where a zone is expected; this will be mapped to its ENUM counterpart.'


	def __init__ (self):
		cmdshell.Cmd.__init__ (self)
		global tightknot
		if tightknot:
			try:
				self.knot = tightknot.TightKnot ()
			except:
				tightknot = None
		if not tightknot:
			self.knot = None
			self.intro = self.intro + '\n###\n### DYSFUNCT KNOT DNS SETUP, ARPA2DNS WILL CRASH.  BAIL OUT NOW!\n###'
			self.prompt = 'DYSFUNCT*' + self.prompt
		self.tlsa_config = (0,0,0)

	def reset (self):
		self.tlsa_config = (0,0,0)

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_zone (self, args, fields):
		"""
		zone ( add <zone> <ns1> <rp> | del <zone> )

		Add a zone with its first public master and responsible
		person email address; remove a zone.
		"""
		subcmd = args [1]
		zone = map_enum (args [2])
		print ('Got: zone', subcmd, zone)
		self.knot.have_conf ()
		zone_cmd = 'zone-set' if subcmd == 'add' else 'zone-unset'
		self.knot.have_conf ()
		if subcmd == 'add':
			self.knot.add_zone (zone)
		else:
			self.knot.del_zone (zone)
		if not self.knot.try_commit ():
			sys.stderr.write ('Failed to %s zone %s\n' % (subcmd,zone))
			return False
		if subcmd == 'del':
			return False
		self.knot.have_zones (zone)
		ns1 = args [3]
		if not '@' in args [4]:
			sys.stderr.write ('Missing \'@\' in email address for responsible person')
			return False
		(rp0,rp1) = args [4].rsplit ('@', 1)
		if '@' in rp0:
			sys.stderr.write ('Multiple \'@\' in email address for responsible person')
			return False
		rp = rp0.replace ('.', '\\.') + '.' + rp1
		self.knot.add_rr (zone, '@', '3600', 'SOA',
			'%s %s 0 10800 3600 1814400 3600' % (ns1,rp))
		if not self.knot.try_commit ():
			sys.stderr.write ('Failed to setup zone %s\n' % (zone,))
		return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_dane (self, args, fields):
		"""
		dane ( ( add | del ) <zone> <_proto> <port> <fqdn> <to-be-matched> |
		       config (ca-root|pkix-end|trust-root|any-end) (cert|pubkey) (full|sha256|sha512) )

		Adds or removes TLSA records for DANE to match certificates against
		the <to-be-matched> parameter.  The location and matched value are
		determined by the "dane add" command.  The method of comparison used
		is determined by the "dane config" command.

		The parameters setup with "dane config" are in symbolic forms to
		make the result more readable.  Knowledge of these labels is known
		at the side of the DNS shell.

		The setup is not fool-proof; one must provide the suitable kind of
		data in <to-be-matched> for it to work.  All crypto computations
		are assumed to be dealt with by the caller, as this is most likely
		the certificate-generating party, with knowledge about how to do
		this.
		"""
		subcmd = args [1]
		if subcmd == 'config':
			certusage = { 'ca-root':0, 'pkix-end':1, 'trust-root':2, 'any-end':3 } [args [2]]
			selector  = { 'cert':0, 'pubkey':1                                   } [args [3]]
			matchtype = { 'full':0, 'sha256':1, 'sha512':2                       } [args [4]]
			self.tlsa_config = (certusage, selector, matchtype)
		if subcmd in ['add', 'del']:
			zone = map_enum (args [2])
			prefix = '_' + args [4] + '.' + args [3] + '.'
			owner = prefix + args [5]
			tomatch = args [6]
			(tag0,tag1,tag2) = self.tlsa_config
			self.knot.have_zones (zone)
			work_rr = self.knot.add_rr if subcmd == 'add' else self.knot.del_rr
			work_rr (zone, owner, '3600', 'TLSA',
				'%d %d %d %s' % (tag0,tag1,tag2,tomatch))
			if not self.knot.try_commit ():
				sys.stderr.write ('Failed to %s TLSA record for %s under %s\n' % (subcmd, owner, zone))
			return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_acme (self, args, fields):
		"""
		acme ( add | del ) <zone> <fqdn> <txtfield>

		Publish a response to an ACME challenge in DNS.  These entries
		are sometimes required while obtaining certificates to use under
		a domain name.  When protected by DNSSEC, the mechanism can
		indeed be quite strong, though one wonders why the publication
		of a TLSA record is not used.

		This command is a purpose-specific wrapper around general DNS
		editing actions, intended to simplify interfacing to ACME and
		to provide a separate access point in terms of privileges.  If
		your intention is to use ACME, use this command instead of
		direct intervention with resource records.
		"""
		subcmd = args [1]
		zone = map_enum (args [2])
		fqdn = args [3]
		txtfield = args [4].replace ('"', '\\"')
		if fqdn [-2:] != '.@':
			sys.stderr.write ('The <fqdn> parameter should end in ".@" for this use')
			return False
		if fqdn [-3:] in ['..@', '.@']:
			sys.stderr.write ('The <fqdn> parameter is not properly formatted')
			return False
		name = '_acme-challenge.' + fqdn [:-2]
		self.knot.have_zones (zone)
		zone_cmd = self.knot.add_rr if subcmd == 'add' else self.knot.del_rr
		zone_cmd (zone, name, '3600', 'TXT', '"' + txtfield + '"')
		if not self.knot.try_commit ():
			sys.stderr.write ('Publication failed')
		return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_enum (self, args, fields):
		"""
		enum ( add | del ) <zone> [wildcard] <skip> <service-field> <uri>

		Add or remove an NAPTR record for the ENUM <zone> (which may be in +ddddd form).
		The wildcard flag indicates that sub-numbers are added instead of the actual number.
		The <skip> is a number of leading digits to not return from the regexp.
		The <service-field> must follow RFC 6116 grammar, for instance E2U+voice:tel+sms:tel

		The URI is used to indicate the service to forward to; this can use \\1 for the
		matched number excluding the skipped prefix; plus, for a wildcard, \\2 for the
		part following after the number.
		"""

		print ('args =', args)
		print ('fields =', fields)
		subcmd = args [1]
		zone = map_enum (args [2])
		self.knot.have_zones (zone)
		digits = enum_digits (zone)
		if digits is None:
			sys.stderr.write ('Please provide an ENUM zone or the +ddddd form\n')
			return False
		wildcard = 'wildcard' in fields
		try:
			skip = int (fields ['<skip>'][0])
		except:
			sys.stderr.write ('Please specify a number of digits to <skip>\n')
			return False
		if skip < 0 or skip > len (digits):
			sys.stderr.write ('The number of digits to <skip> is out of range\n')
			return False
		svcfld = fields ['<service-field>'][0]
		svcfld_parsed = enum_service_field (svcfld)
		if svcfld is None:
			sys.stderr.write ('Please consult RFC 6116 for <service-field> syntax\n')
			return False
		uri = fields ['<uri>'][0]
		if '!' in uri:
			sys.stderr.write ('Please use no ! in your uri')
			return False
		uri = uri.replace ('\\', '\\\\')
		if '\\\\2' in uri and not wildcard:
			sys.stdout.write ('You might use \\\\2 to capture the wildcarded trailer\n')
			return False
		if '\\\\2' not in uri and wildcard:
			sys.stderr.write ('Suggested wildcard URIs use \\\\1+\\\\2\n')
		pri = 10
		wgt = 10
		rdata = '%d %d "u" "%s" "!^\\+' % (pri,wgt,svcfld)
		rdata += digits [:skip]
		rdata += '(' + digits [skip:] + ')'	# \\1
		if wildcard:
			rdata += '(.*)'			# \\2
		rdata += '$!' + uri + '!" .'
		owner = '*' if wildcard else '@'
		#TODO# Rather confused about backslash quotes
		sys.stderr.write (owner + ' 3600 IN NAPTR ' + rdata + '\n')
		zone_cmd = self.knot.add_rr if subcmd == 'add' else self.knot.del_rr
		zone_cmd (zone, owner, '3600', 'NAPTR', rdata)
		self.knot.try_commit ()
		sys.stderr.write ('Done.\n')
		return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_record (self, args, fields):
		"""
		record ( add | del ) <zone> <fqdn> [in] [<ttl>] <rtype> <rdata> [...]
		"""
		subcmd = args [1]
		zone = map_enum (args [2])
		fqdn = args [3]
		rtype = fields ['<rtype>'] [0]
		rdata = fields ['<rdata>'] [0]
		ttl = fields ['<ttl>'] [0] or '3600'
		rec_cmd = 'zone-set' if subcmd == 'add' else 'zone-unset'
		self.knot.have_zones (zone)
		#OLD#BAD# done_after = self.knot.patience (zone=zone, owner=fqdn, rtype=rtype)
		#OLD#BAD# self.knot.knot (cmd=rec_cmd, section=zone, item=fqdn, data=('%s %s %s' % (ttl,rtype,rdata)))
		self.knot.add_rr (zone, fqdn, ttl, rtype, rdata)
		if not self.knot.try_commit ():
			sys.stderr.write ('Failed to %s %s in zone %s' % (subcmd,rtype,zone))
		#OLD#BAD# if done_after is not None:
		#OLD#BAD# 	print ('Cache-Update-Delay:', done_after)
		#OLD#BAD# else:
		#OLD#BAD# 	print ('DEBUG: No done_after available')
		return False






def main ():
	shell = Cmd ()
	shell.cmdloop ()

if __name__ == '__main__':
	main ()

