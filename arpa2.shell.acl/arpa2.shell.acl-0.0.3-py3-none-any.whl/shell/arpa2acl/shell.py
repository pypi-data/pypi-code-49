#!/usr/bin/env python
#
# arpa2acl -- The shell to add and remove ACL items
#
# This program edits accessControlledObjects as setup in LDAP.
#
# From: Rick van Rein <rick@openfortress.nl>


import os
import sys
import re
import string

from arpa2.shell import cmdshell


try:
	import readline
	readline.set_completer_delims (' \t\n')
except:
	pass


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

#CHOOSE# base = 'ou=IdentityHub,o=arpa2.net,ou=InternetWide'
base = 'ou=InternetWide'




class ACL ():

	"""ACL objects relate rights to ARPA2 Identity Selectors.  Rights are treated
	   as strings, without interpreting their contents.  This object maintains a
	   selector2rights mapping from selector to rights, and rights2selectors from
	   rights to a list of selectors to which it applies.  One object can have
	   multiple meaningful ACL attributes, and those will be treated as one ACL
	   in the code below, and also written out as one.
	"""

	uniquenr = 0

	def __init__ (self, dap, dn):
		self.dap = dap
		self.dn  = dn
		self.attr = []
		self.orig = None
		self.load_from_dn ()

	def load_from_dn (self):
		self.orig = [ ]
		self.selector2rights = { }
		self.rights2selectors = { }
		dn1 = self.dn
		fl1 = '(objectClass=accessControlledObject)'
		al1 = ['acl', 'rescls', 'resins', 'cn']
		try:
			#DEBUG# print ('Query for', dn1)
			qr1 = self.dap.search_s (dn1, SCOPE_BASE, filterstr=fl1, attrlist=al1)
			#DEBUG# print ('Query response', qr1)
			if qr1 == []:
				raise NO_SUCH_OBJECT ()
			[(dn1,at1)] = qr1
			self.attr = { }
			for (k,vs) in at1.items ():
				if type (k) == bytes:
					k = str(k,'utf-8')
				k = {
					'acl': 'accessControlList',
					'resins': 'resourceInstance',
					'rescls': 'resourceClass',
				}.get (k, k)
				self.attr [k] = [ str(v,'utf-8') for v in vs ]
			self.orig = self.attr.get ('accessControlList', [])
			for acl1 in self.orig:
				rgt = None
				for wrd1 in acl1.strip ().split ():
					#DEBUG# print ('Considering word', wrd1, 'while right is', rgt)
					if wrd1 [:1] == '%' and wrd1 [:2] != '%%':
						# Set rights for following Selectors
						rgt = wrd1
					else:
						# Process the Selector or %%elector
						if rgt is None:
							# Silently skip
							continue
						if wrd1 [:2] == '%%':
							# Remove escape
							wrd1 = wrd1 [1:]
						self.selector_add (wrd1, rgt)
		except Exception as e:
			print ('Unlucky at', dn1)
			raise

	def dn ():
		return self.dn

	def keys (self):
		return self.attr.keys ()

	def get (self, attrtype):
		return self.attr.get (attrtype, None)

	def selector_del (self, selector):
		if not selector in self.selector2rights:
			print ('Selector', selector, 'unknown.  Got', self.selector2rights.keys ())
			return
		rights = self.selector2rights [selector]
		print ('Removing rights', rights, 'from selector', selector)
		del self.selector2rights [selector]
		if self.rights2selectors [rights] == [selector]:
			del self.rights2selectors [rights]
		else:
			self.rights2selectors [rights].remove (selector)

	def selector_add (self, selector, rights):
		if selector in self.selector2rights:
			raise Exception ('Selector is already set')
		#DEBUG# print ('Adding rights', rights, 'to selector', selector)
		self.selector2rights [selector] = rights
		if rights in self.rights2selectors:
			self.rights2selectors [rights].append (selector)
		else:
			self.rights2selectors [rights] = [selector]

	def save (self):
		#DEBUG# print ('OLD =', self.orig)
		new = [ ]
		for (rgt,sels) in self.rights2selectors.items ():
			new.append (rgt)
			for sel in sels:
				if sel [:1] == '%':
					new.append ('%' + sel)
				else:
					new.append (sel)
		#DEBUG# print ('NEW =', new)
		#TODO# Maybe stupid: deleting everything and pushing it back is leads to more work downstream
		mod = [ ]
		for acl in self.orig:
			mod.append ( (MOD_DELETE, 'acl', bytes(acl,'utf-8')) )
		#TODO# Maybe stupid: one line would always change as a whole, leading to more work downstream
		new = ' '.join (new)
		mod.append ( (MOD_ADD,    'acl', bytes(new,'utf-8')) )
		try:
			#DEBUG# print ('MOD =', mod)
			dap.modify_s (self.dn, mod)
			self.orig = [new]
		except:
			print ('Error saving ACL changes; resetting')
			self.load_from_dn ()
			raise


class Cmd (cmdshell.Cmd):

	version = (0,0)
	prompt = "arpa2acl> "
	intro = "Edit Access Control Lists as saved in LDAP."

	"""The current ACL object."""
	cur_acl = None

	"""All DNs of accessControlledObjects."""
	acl_dns = None

	def reset (self):
		self.cur_acl = None
		self.acl_dns = None

	"""Add a space after a complete name."""
	def completenames (self, text, *ignored):
		return [ w + ' '
			for w in cmd.Cmd.completenames (self, text, *ignored) ]

	"""Save the currently edited ACL to LDAP."""
	def do_acl_save (self, *ignored):
		if self.cur_acl is not None:
			self.cur_acl.save ()

	"""The shell for ACL editing in LDAP."""
	def do_acl_dn (self, line):
		try:
			self.do_acl_save ()
		except Exception as e:
			print ('Exception:', e)
		self.cur_acl = ACL (dap, line)
		for k in self.cur_acl.keys ():
			for v in self.cur_acl.get (k):
				print (k + ': ' + v)

	"""Add a %rights selector... combination to the ACL."""
	def do_acl_add (self, line):
		if self.cur_acl is None:
			raise Exception ('First use acl_dn to select an object in LDAP')
		words = line.strip ().split ()
		if len (words) < 2:
			raise Exception ('Format: acl_add %rights selector...')
		rgt = words [0]
		for sel in words [1:]:
			self.cur_acl.selector_add (sel, rgt)

	"""Remove selector.... regardless of its current rights from the ACL in LDAP."""
	def do_acl_del (self, line):
		if self.cur_acl is None:
			raise Exception ('First use acl_dn to select an object in LDAP')
		words = line.strip ().split ()
		if words == [] or words == ['']:
			raise Exception ('Format: acl_del selector...')
		for sel in words:
			self.cur_acl.selector_del (sel)

	"""Command line completion for accessControlledObjects in LDAP."""
	def complete_acl_dn (self, text, line, begidx, lastidx):
		#DEBUG# print ('Completing line "' + line + '"')
		if self.acl_dns is None:
			#DEBUG# print ('Need to query LDAP')
			try:
				dn1 = base
				fl1 = '(objectClass=accessControlledObject)'
				at1 = ['dn']
				#DEBUG# print ('Querying', dn1)
				qr1 = dap.search_s (dn1, SCOPE_SUBTREE, fl1, at1)
				#DEBUG# print ('Query result', qr1)
				self.acl_dns = [ dn for (dn,_) in qr1 ]
				#DEBUG# print ('ACLs found', self.acl_dns)
			except Exception as e:
				print ('Exception:', e)
				return [ ]
		word = (line + 'x').split () [-1] [:-1]
		#DEBUG# print ('Word is "' + word + '"')
		#DEBUG# print ('Selecting from', self.acl_dns, 'starting with', text, 'taken from', line, 'so', word)
		#TODO# What precisely to return?  Cut off first len(word) chars or not?!?
		return [ dn
			for dn in self.acl_dns
			if dn.startswith (word) ]

def main ():
	a2shell = Cmd ()
	a2shell.cmdloop ()

if __name__ == '__main__':
	main ()
