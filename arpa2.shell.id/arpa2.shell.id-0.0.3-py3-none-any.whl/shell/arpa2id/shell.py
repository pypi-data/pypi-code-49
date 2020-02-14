#!/usr/bin/env python
#
# arpa2id -- ARPA2 Shell for IdentityHub
#
# This shell allows a variety of commands to add and remove,
# rename and refine users, aliases, pseudonyms as well as
# group memberships and role occupancy.  In short, it allows
# the great variety of identity configurations that ARPA2
# offers to support both that users control their own online
# identity, and that they may Bring Your Own IDentity (BYOID).
#
# Completion is based on word-by-word actions; in some cases,
# regular expressions are used (such as for new domain names);
# in other cases, already known values can be listed by a
# function.  There are also fixed words, indicating a command
# match; this is also used for sub-commands.
#
# From: Rick van Rein <rick@openfortress.nl>


import os
import sys
import re
import string

import cmd
from arpa2.shell import cmdshell

import ldap
from ldap import MOD_ADD, MOD_DELETE, MOD_REPLACE, MOD_INCREMENT
from ldap import SCOPE_BASE, SCOPE_ONELEVEL, SCOPE_SUBTREE
from ldap import NO_SUCH_OBJECT, ALREADY_EXISTS, NOT_ALLOWED_ON_NONLEAF
from ldap import TYPE_OR_VALUE_EXISTS, NO_SUCH_ATTRIBUTE


#
# Configuration
#

cfgln_re = re.compile ('^([A-Z]+)[ \t]*(.*)$')
ldapcfg = { }
try:
        for cfgln in open ('/etc/ldap/ldap.conf', 'r').readlines ():
                m = cfgln_re.match (cfgln)
                if m is not None:
                        (key,val) = m.groups ()
                        ldapcfg [key] = val
except:
        pass

if 'URI' in ldapcfg:
	ldapuri = ldapcfg ['URI']
else:
	ldapuri = os.environ.get ('ARPA2_LDAPURI', None)
if ldapuri is None:
	sys.stderr.write ('Please set URI in /etc/ldap/ldap.conf or configure ARPA2_LDAPURI\n')
	sys.exit (1)

if 'BINDDN' in ldapcfg:
	ldapuser = ldapcfg ['BINDDN']
	ldappasw = os.environ.get ('ARPA2_BINDPW')

use_gssapi = ldapuser [-18:].lower () == ',cn=gssapi,cn=auth'

if not use_gssapi:
	if ldappasw is None:
		import getpass
		print ('LDAPuser: ', ldapuser)
		ldappasw = getpass.getpass ('Password: ')
		os.environ ['ARPA2_BINDPW'] = ldappasw

#
# Initialisation
#

dap = ldap.initialize (ldapuri)
if use_gssapi:
	sasl_auth = ldap.sasl.gssapi()
	dap.sasl_interactive_bind_s(ldapuser, sasl_auth)
else:
	dap.bind_s (ldapuser, ldappasw)

whoami = dap.whoami_s ()
if whoami [:3] == 'dn:':
	whoami = whoami [3:]
#DEBUG# print ('I seem to be', whoami, '::', type (whoami))

whoami_uid = None
whoami_dom = None
whoami_a2id = None
for rdn in map (string.strip, whoami.split (',')):
	if rdn [:4] == 'uid=' and whoami_uid is None:
		whoami_uid = rdn [4:].strip ().lower ()
	if rdn [:17] == 'associatedDomain=' and whoami_dom is None:
		whoami_dom = rdn [17:].strip ().lower ()
		if whoami_dom [-1:] == '.':
			whoami_dom = whoami_dom [:-1]
if whoami_uid is None or whoami_dom is None:
	sys.stderr.write ('Failed to construct uid@associatedDomain from ' + whoami)
else:
	whoami_nai = whoami_uid + '@' + whoami_dom


base = 'ou=IdentityHub,o=arpa2.net,ou=InternetWide'


#
# Cleanup a UID object including any references pointing to it
#
def cleanup_uid (domain, uid, objcls):
	donai = uid + '@' + domain
	#
	# Check if the object actually exists, and has the intended class
	dn1 = 'uid=' + uid + ',associatedDomain=' + domain + ',' + base
	fl1 = '(objectClass=' + objcls + ')'
	al1 = []
	try:
		qr1 = dap.search_s (dn1, SCOPE_BASE, filterstr=fl1, attrlist=al1)
		if qr1 == []:
			raise NO_SUCH_OBJECT ()
		#DEBUG# print ('Object exists:', qr1)
	except NO_SUCH_OBJECT:
		sys.stderr.write ('There is no ' + donai + ' of type ' + objcls + '\n')
		return False
	#
	# Ensure that no aliases or pseudonyms rest on the uid about to be deleted
	dn2 = 'associatedDomain=' + domain + ',' + base
	fl2 = '(&(objectClass=identityHubUser)(|(uidAlias=' + uid + ')(uidPseudonym=' + uid + ')))'
	al2 = [ 'uid', 'uidAlias', 'uidPseudonym' ]
	try:
		#DEBUG# print ('Searching for blocking aliases/pseudonyms under', dn2)
		qr2 = dap.search_s (dn2, SCOPE_ONELEVEL, filterstr=fl2, attrlist=al2)
		#DEBUG# print ('Query Result:', qr2)
		if qr2 == []:
			raise NO_SUCH_OBJECT ()
		for (dn2,at2) in qr2:
			sys.stderr.write ('Blocking deletion on ' + str (at2) + '\n')
		return False
	except NO_SUCH_OBJECT:
		# Good, we don't want to find anything now :)
		#DEBUG# print ('Nothing blocking removal')
		pass
	#
	# Actually remove the targeted object
	dn3 = dn1
	try:
		#DEBUG# print ('Deleting', dn3)
		dap.delete_s (dn3)
		#DEBUG# print ('Deleted', dn3)
	except NOT_ALLOWED_ON_NONLEAF:
		sys.stderr.write ('Remove other stuff first\n')
		return False
	except NO_SUCH_OBJECT:
		sys.stderr.write ('No such user\n')
		return False
	#
	# Look for objects that reference this one, and remove such references
	dn4 = dn2
	fl4 = '(|(&(objectClass=identityHubGroup)(|(uidMember=' + uid + ')(uidDecline=' + uid + ')))(&(objectClass=identityHubRole)(|(uidOccupant=' + uid + ')(uidDecline=' + uid + ')))(&(objectClass=identityHubUser)(|(uidRole=' + uid + ')(uidGroup=' + uid + '))))'
	al4 = [ 'uidMember', 'uidOccupant', 'uidDecline', 'uidRole', 'uidGroup' ]
	try:
		qr4 = dap.search_s (dn4, SCOPE_ONELEVEL, filterstr=fl4, attrlist=al4)
		for (dn5,at4) in qr4:
			#DEBUG# print ('Referrals in', dn5)
			at5 = [ ]
			for a5 in al4:
				if uid in at4.get (a5, []):
					#DEBUG# print ('Removing an attribute value for', a5)
					at5.append ( (MOD_DELETE, a5, uid) )
			dap.modify_s (dn5, at5)
	except NO_SUCH_OBJECT:
		# Nice, the user had no social bindings at all
		#DEBUG# print ('Nice, no social bindings at all')
		pass
	return True


#
# Regular expressions for fields
#
re_fqdn = re.compile ('^[a-z0-9-_]{1,}(\.[a-z0-9-_]{1,}){1,}$')
re_user = re.compile ('^[a-z0-9_-]{1,}$')
re_alias = re.compile ('^[a-z0-9_-]{1,}$')
re_role = re_alias
re_group = re_alias

#
# Listing functions for various fields
#

# List the available domains found in LDAP:
# (associatedDomain=d_*) under ou=IdentityHub,o=arpa2.net,ou=InternetWide
#
def list_domain (self, words, d_):
	try:
		dn1 = base
		fl1 = '(&(objectClass=domainRelatedObject)(associatedDomain=' + d_ + '*))'
		al1 = ['associatedDomain']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single associatedDomain
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ at.get ('associatedDomain', ['undefined']) [0]
			for (dn,at) in qr1 ]
	except NO_SUCH_OBJECT:
		return []

# List the users for the given domain in LDAP:
# (&(objectClass=identityHubUser)(uid=u_*)) under
# associatedDomain=d,ou=IdentityHub,o=arpa2.net,ou=InternetWide
#
def list_user (self, words, u_):
	try:
		dn1 = 'associatedDomain=' + words [1] + ',' + base
		fl1 = '(&(objectClass=identityHubUser)(uid=' + u_ + '*))'
		al1 = ['uid']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single collection
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ atn
			for (dn,at) in qr1
			for atn in at.get ('uid', [])
			if '%2b' not in atn ]
	except NO_SUCH_OBJECT:
		return []
#
def list_alias (self, a_):
	try:
		dn1 = 'associatedDomain=' + words [1] + ',' + base
		fl1 = '(&(objectClass=identityHubUser)(uidAlias=' + words [2] + '%2b' + a_ + '*))'
		al1 = ['uidAlias']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single collection
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ atn.split ('%2b') [1]
			for (dn,at) in qr1
			for atn in at.get ('uidAlias', [])
			if '%2b' in atn ]
	except NO_SUCH_OBJECT:
		return []
#
def list_group (self, g_):
	try:
		dn1 = 'associatedDomain=' + words [1] + ',' + base
		fl1 = '(&(objectClass=identityHubGroup)(uid=' + g_ + '*))'
		al1 = ['uid']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single collection
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ atn
			for (dn,at) in qr1
			for atn in at.get ('uid', [])
			if '%2b' not in atn ]
	except NO_SUCH_OBJECT:
		return []
#
def list_roles (self, r_):
	try:
		dn1 = 'associatedDomain=' + words [1] + ',' + base
		fl1 = '(&(objectClass=identityHubRole)(uid=' + r_ + '*))'
		al1 = ['uid']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single collection
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ atn
			for (dn,at) in qr1
			for atn in at.get ('uid', [])
			if '%2b' not in atn ]
	except NO_SUCH_OBJECT:
		return []
#
def list_member (self, words, m_):
	try:
		dn1 = 'associatedDomain=' + words [1] + ',' + base
		fl1 = '(&(objectClass=identityHubUser)(uidMember=' + words [2] + '%2b' + m_ + '*))'
		al1 = ['uidMember']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single collection
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ atn.split ('%2b') [1]
			for (dn,at) in qr1
			for atn in at.get ('uidMember', [])
			if '%2b' in atn ]
	except NO_SUCH_OBJECT:
		return []
#
def list_occupant (self, words, o_):
	try:
		dn1 = 'associatedDomain=' + words [1] + ',' + base
		fl1 = '(&(objectClass=identityHubUser)(uidOccupant=' + o_ + '*))'
		al1 = ['uidOccupant']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single collection
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ atn.split ('%2b') [1]
			for (dn,at) in qr1
			for atn in at.get ('uidOccupant', [])
			if '%2b' in atn ]
	except NO_SUCH_OBJECT:
		return []

# Overview of possible (sub)command structures
#
matchables = {
	"domain_add":		[ re_fqdn ],
	"domain_del":		[ list_domain ],
	"domain_xfer_away":	[ list_domain ],
	"user_add":		[ list_domain, re_user ],
	"user_del":		[ list_domain, list_user ],
	"user_mov":		[ list_domain, list_user, re_user ],
	"alias_add":		[ list_domain, list_user, re_alias ],
	"alias_del":		[ list_domain, list_user, list_alias ],
	"role_add":		[ list_domain, list_user, re_role ],
	"role_del":		[ list_domain, list_user, list_roles ],
	"role_mov":		[ list_domain, list_user, list_roles, re_role ],
	"group_add":		[ list_domain, re_group ],
	"group_del":		[ list_domain, list_group ],
	"member_add":		[ list_domain, list_group, re_alias, list_user, re_alias ],
	"member_del":		[ list_domain, list_group, re_alias, list_user, re_alias ],
	"member_join":		[ list_domain, list_user, re_alias, list_group, re_alias ],
	"member_leave":		[ list_domain, list_user, list_alias ],
	# "group_mov":		[ list_domain, list_group, re_group ],
	# "member_mov":		[ list_domain, list_member, re_user ],
}


# The UUID for the resource class 'uid.domain.identityhub'
# or uid@domain administrative access control
uuid_uid_domain_idhub = '53281a7c-2c69-3d49-b12f-590e0a2f54bc'



class Cmd (cmdshell.Cmd):

	version = (0,0)
	prompt = 'arpa2id> '
	intro = 'Shell to the ARPA2 IdentityHub.\nYou can add, del, mov identities for users, groups, roles and so on.'

	def do_EOF (self, line):
		return True

	do_exit = do_EOF

	do_quit = do_EOF

	def reset (self):
		"""There is no state to clear for arpa2identityhub.
		"""
		pass

	def completenames (self, text, *ignored):
		return [ w + ' '
			for w in cmd.Cmd.completenames (self, text, *ignored) ]

	def completedefault (self, text, line, begidx, endidx):
		words = string.split (line.lstrip () + 'x')
		last_word = words [-1] [:-1]
		try:
			to_match = matchables.get (words [0], []) [len (words)-2]
			if type (to_match) == type (re_user):
				mtch = to_match.match (last_word)
				if mtch is not None:
					# Confirm
					return [ last_word + ' ' ]
				else:
					# Beep
					return [ ]
			else:
				# Assume a function to be called, usually list_xxx
				cmpl = to_match (self, words [:-1], last_word)
				return [ c + ' ' for c in cmpl if c.startswith (last_word) ]
		except Exception as e:
			# Beep
			return [ ]

	def do_domain_add (self, line):
		"""domain_add DOMAIN.TLD ORGNAME...
		   Add DOMAIN.TLD named ORGNAME... to the managed portfolio of domain names.
		"""
		sys.stdout.write ("do_domain_add: " + line + "\n")
		if whoami_nai is None:
			sys.stderr.write ('Error: No uid@associatedDomain from whoami to assign rights\n')
			return
		else:
			sys.stdout.write ('User identity management will be granted to ' + whoami_nai + '\n')
		(domain,orgname) = string.split (line.strip (), maxsplit=1)
		domain = domain.lower ()
		if domain [-1:] == '.':
			domain = domain [:-1]
		dn1 = 'associatedDomain=' + domain + ',' + base
		at1 = [
			('objectClass', ['organization','domainRelatedObject', 'resourceInstance', 'accessControlledObject']),
			('o', orgname or domain),
			('associatedDomain', domain),
			('resourceClassUUID', uuid_uid_domain_idhub),
			('resourceInstanceKey', bytes (domain)),
			('accessControlList', bytes ('%rwcd ' + whoami_nai + ' %o @' + whoami_dom)),
		]
		try:
			meta = dap.add_s (dn1,at1)
		except ALREADY_EXISTS:
			print ('Domain already exists.')
			return

	def do_domain_del (self, line):
		"""domain_del DOMAIN.TLD
		   Remove DOMAIN.TLD from the managed portfolio of domain names.
		"""
		sys.stdout.write ("do_domain_del: " + line + "\n")
		(domain,) = line.strip ().split ()
		dn1 = 'associatedDomain=' + domain + ',' + base
		try:
			#DEBUG# print ('deleting', dn1)
			dap.delete_s (dn1)
		except NOT_ALLOWED_ON_NONLEAF:
			print ('Remove other stuff first')
		except NO_SUCH_OBJECT:
			sys.stderr.write ('No such domain\n')

	def do_domain_xfer_away (self, line):
		"""domain_xfer_away DOMAIN.TLD [XFER-KEY]
		   Transfer ownership of DOMAIN.TLD to another party.
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_domain_xfer_away: " + line + "\n")
		pass

	def do_user_add (self, line):
		"""user_add DOMAIN.TLD USERID NAME...
		   Add a new user USERID@DOMAIN.TLD with NAME... to a managed domain.
		"""
		sys.stdout.write ("do_user_add: " + line + "\n")
		(domain,uid,name) = string.split (line.strip (), maxsplit=2)
		dn1 = 'uid=' + uid + ',associatedDomain=' + domain + ',' + base
		at1 = [
			('objectClass', ['identityHubUser']),
			('cn', name),
			('uid', uid),
		]
		try:
			meta = dap.add_s (dn1,at1)
		except ALREADY_EXISTS:
			print ('User already exists.')
			return

	def do_user_del (self, line):
		"""user_del DOMAIN.TLD USERID
		   Remove a user USERID@DOMAIN.TLD from a managed domain.
		"""
		sys.stdout.write ("do_user_del: " + line + "\n")
		(domain,user) = line.strip ().split ()
		cleanup_uid (domain, user, 'identityHubUser')
		return False

	def dont_user_mov (self, line):
		"""user_mov DOMAIN.TLD USERID NEWUID
		   Rename a user USERID@DOMAIN.TLD to NEWUID@DOMAIN.TLD.
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_user_mov: " + line + "\n")
		pass

	def do_alias_add (self, line):
		"""alias_add DOMAIN.TLD USERID NEWALIAS
		   Introduce USERID+NEWALIAS@DOMAIN.TLD as an alias for USERID@DOMAIN.TLD.
		"""
		sys.stdout.write ("do_alias_add: " + line + "\n")
		(domain,uid,alias) = string.split (line.strip (), maxsplit=2)
		dn1 = 'uid=' + uid + '%2b' + alias + ',associatedDomain=' + domain + ',' + base
		at1 = [
			('objectClass', ['identityHubUser']),
			# ('cn', name),
			('uid', uid + '%2b' + alias),
			('uidAlias', uid),
		]
		try:
			meta = dap.add_s (dn1,at1)
		except ALREADY_EXISTS:
			print ('Alias already exists.')
			return

	def do_alias_del (self, line):
		"""alias_del DOMAIN.TLD USERID ALIAS
		   Remove an alias USERID+ALIAS@DOMAIN.TLD as from a managed domain.
		"""
		sys.stdout.write ("do_alias_del: " + line + "\n")
		(domain,user,alias) = line.strip ().split ()
		cleanup_uid (domain, user + '%2b' + alias, 'identityHubUser')
		return False

	def do_role_add (self, line):
		"""role_add DOMAIN.TLD USERID NEWROLE
		   Add a role NEWROLE@DOMAIN.TLD to USERID@DOMAIN.TLD
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_role_add: " + line + "\n")
		pass

	def do_role_del (self, line):
		"""role_del DOMAIN.TLD USERID ROLENAME
		   Remove a role ROLENAME@DOMAIN.TLD from USERID@DOMAIN.TLD.
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_role_del: " + line + "\n")
		pass

	def dont_role_mov (self, line):
		"""role_mov DOMAIN.TLD ROLENAME NEWROLENAME
		   Rename ROLENAME@DOMAIN.TLD to NEWROLENAME@DOMAIN.TLD.
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_role_mov: " + line + "\n")
		pass

	def do_group_add (self, line):
		"""group_add DOMAIN.TLD GROUPID NAME...
		   Add GROUPID@DOMAIN.TLD as a group with the given NAME...
		"""
		sys.stdout.write ("do_group_add: " + line + "\n")
		(domain,gid,name) = string.split (line.strip (), maxsplit=2)
		dn1 = 'uid=' + gid + ',associatedDomain=' + domain + ',' + base
		at1 = [
			('objectClass', ['identityHubGroup']),
			('cn', name),
			('uid', gid),
		]
		try:
			meta = dap.add_s (dn1,at1)
		except ALREADY_EXISTS:
			print ('Group already exists.')
		return False

	def do_group_del (self, line):
		"""group_del DOMAIN.TLD GROUPID
		   Remove GROUPID@DOMAIN.TLD as a group.
		"""
		sys.stdout.write ("do_group_del: " + line + "\n")
		(domain,gid) = line.strip ().split ()
		cleanup_uid (domain, gid, 'identityHubGroup')
		return False

	def dont_group_mov (self, line):
		"""group_mov DOMAIN.TLD GROUPID NEWGROUPID
		   Rename GROUPID@DOMAIN.TLD into NEWGROUPID@DOMAIN.TLD.
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_group_mov: " + line + "\n")
		pass

	def do_member_add (self, line):
		"""member_add DOMAIN.TLD GROUPID MEMBER USERID ALIAS
		   Add USERID+ALIAS@DOMAIN.TLD as a member GROUPID+MEMBER@DOMAIN.TLD.
		   TODO: We may have to create a separate object for this to work.
		"""
		sys.stdout.write ("do_member_add: " + line + "\n")
		(domain,gid,member,uid,alias) = string.split (line.strip (), maxsplit=4)
		dn1 = 'uid=' + gid + '%2b' + member + ',associatedDomain=' + domain + ',' + base
		at1 = [ (MOD_ADD, 'uidMember', uid + '%2b' + alias) ]
		try:
			meta = dap.modify_s (dn1,at1)
		except TYPE_OR_VALUE_EXISTS:
			print ('Group member already registered.')
		return False

	def do_member_del (self, line):
		"""member_del DOMAIN.TLD GROUPID MEMBER USERID ALIAS
		   Remove USERID+ALIAS@DOMAIN.TLD as a member GROUPID+MEMBER@DOMAIN.TLD.
		   TODO: We may have to destroy the separate object for this to work.
		"""
		sys.stdout.write ("do_member_del: " + line + "\n")
		(domain,gid,member,uid,alias) = string.split (line.strip (), maxsplit=4)
		dn1 = 'uid=' + gid + '%2b' + member + ',associatedDomain=' + domain + ',' + base
		at1 = [ (MOD_DELETE, 'uidMember', uid + '%2b' + alias) ]
		try:
			meta = dap.modify_s (dn1,at1)
		except NO_SUCH_ATTRIBUTE:
			print ('Group member was not registered.')
		return False

	def do_member_join (self, line):
		"""member_join DOMAIN.TLD USER ALIAS GROUP MEMBER
		   Let USER+ALIAS@DOMAIN.TLD join GROUP@DOMAIN.TLD as GROUP+MEMBER@DOMAIN.TLD.
		"""
		sys.stdout.write ("NOT IMPLEMENTED: do_member_signup: " + line + "\n")
		(domain,uid,alias,gid,member) = string.split (line.strip (), maxsplit=4)
		dn1 = 'uid=' + uid + '%2b' + alias + ',associatedDomain=' + domain + ',' + base
		at1 = [
			('objectClass', ['identityHubUser']),
			# ('cn', name),
			('uid', uid + '%2b' + alias),
			('uidGroup', gid + '%2b' + member),
		]
		try:
			meta = dap.add_s (dn1,at1)
		except ALREADY_EXISTS:
			print ('Membership alias already exists.')
		return False

	def do_member_leave (self, line):
		"""member_leave DOMAIN.TLD USER ALIAS
		   Let USER@DOMAIN.TLD leave GROUP@DOMAIN.TLD as GROUP+MEMBER@DOMAIN.TLD.
		"""
		sys.stdout.write ("do_member_leave: " + line + "\n")
		(domain,uid,alias) = string.split (line.strip (), maxsplit=2)
		cleanup_uid (domain, uid + '%2b' + alias, 'identityHubUser')
		return False


def main ():
	a2shell = Cmd ()
	a2shell.cmdloop ()

if __name__ == '__main__':
	main ()
