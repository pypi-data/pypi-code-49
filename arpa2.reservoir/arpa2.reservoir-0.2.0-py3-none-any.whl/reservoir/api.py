# arpa2.reservoir -- Functions to work on the Reservoir.
#
# Functions to directly address the LDAP tree for Reservoir,
# as well as the file store.
#
# From: Rick van Rein <rick@openfortress.nl>


import os
import sys
import copy
import fcntl

import uuid
import string
import re

import ldap
from ldap import MOD_ADD, MOD_DELETE, MOD_REPLACE, MOD_INCREMENT
from ldap import SCOPE_BASE, SCOPE_ONELEVEL, SCOPE_SUBTREE
from ldap import NO_SUCH_OBJECT, ALREADY_EXISTS, NOT_ALLOWED_ON_NONLEAF


# As assigned a fixed value on http://uuid.arpa2.org
#
# This is used as follows:
#  - in a resourceClass/reservoirIndex objects at
#    associatedDomain=,ou=Reservoir,o=arpa2.net,ou=InternetWide
#  - in resourceInstance/reservoirCollection/reservoirIndex objects
#    with a random UUID representing a Collection UUID located at
#    resins=,associatedDomain=,ou=Reservoir,...
#  - it is _not_ used in reservoirResource objects at
#    resource=,resins=,associatedDomain=,ou=Reservoir,...
#
reservoir_uuid = '904dfdb5-6b34-3818-b580-b9a0b4f7e7a9'



# Utility function to produce UUID strings.
#
def random_uuid ():
	"""Produce a random UUID in the lowercase string format.
	"""
	return str (uuid.uuid4 ()).lower ()


#
# Configuration
#

reservoir_base = 'ou=Reservoir,o=arpa2.net,ou=InternetWide'
reservoir_home = '/var/arpa2/reservoir'


#
# Initialisation of LDAP
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

dap = ldap.initialize (ldapuri)
if use_gssapi:
	sasl_auth = ldap.sasl.gssapi()
	dap.sasl_interactive_bind_s(ldapuser, sasl_auth)
else:
	dap.bind_s (ldapuser, ldappasw)


#
# Utilities to map str() and bytes()
#
def s2b (s):
	t = type (s)
	if t == bytes:
		return s
	elif t == str:
		return bytes(s,'utf-8')
	elif t == list:
		return [ s2b(s0) for s0 in s ]
	elif t == set:
		return set([ s2b(s0) for s0 in s ])
	elif t == tuple:
		# Highly specific for Python-LDAP
		return tuple([s[0]] + [ s2b(s0) for s0 in s[1:] ])
	elif t == dict:
		return { k:s2b(v) for (k,v) in s.items() }
	else:
		raise TypeError ('s2b got %s' % str(t))

def b2s (b):
	t = type (b)
	if t == str:
		return b
	elif t == bytes:
		return str(b,'utf-8')
	elif t == list:
		return [ b2s(b0) for b0 in b ]
	elif t == set:
		return set([ b2s(b0) for b0 in b ])
	elif t == tuple:
		# Highly specific for Python-LDAP
		return tuple([b[0]] + [ b2s(b0) for b0 in b[1:] ])
	elif t == dict:
		return { k:b2s(v) for (k,v) in b.items() }
	else:
		raise TypeError ('b2s got %s' % str(t))



#
# Classes
#


class Resource:
	"""Cache the LDAP contents of a Reservoir Resource Object.
	   The various attributes can be inspected as desired.
	   #TODO# support collecting and then saving state to LDAP
	   #TODO# have a form for a new/empty Resource
	"""
	def __init__ (self, indexobj, resuuid, preloaded_attrs=None):
		assert resuuid  is not None, 'Provide a Resource UUID'
		assert indexobj is not None, 'Provide a Collection object'
		self.resuuid  = resuuid
		self.indexobj = indexobj
		self.colluuid = indexobj.get_colluuid ()
		self.domain   = indexobj.get_domain ()
		self.dn = 'resource=%s,resins=%s,associatedDomain=%s,%s' % (resuuid,self.colluuid,self.domain,reservoir_base)
		if preloaded_attrs is None:
			fl1 = '(objectClass=reservoirResource)'
			try:
				#DEBUG# print ('searching', dn1, fl1, al1)
				qr1 = dap.search_s (self.dn, SCOPE_BASE, filterstr=fl1)
				#DEBUG# print ('Query response:', qr1)
			except NO_SUCH_OBJECT:
				return KeyError ('Resource %s not found in collection %s of %s' % (resuuid,self.colluuid,self.domain))
			assert len(qr1) == 1, 'Query lists unexpected elements'
			[(dn,at)] = qr1
		else:
			at = preloaded_attrs
		self.meta = { k:set (b2s (vs)) for (k,vs) in at.items () }
		self.olds = { }

	def __del__ (self):
		"""When the object is cleaned up, we consider it too late
		   to save the state to LDAP.  But we can still moan about
		   being left behind.
		"""
		if self.olds != { }:
			sys.stderr.write ('\n\n### LOOSING CACHED RESOURCE STATE: %s\n\n' % self.dn)

	def __str__ (self):
		return '%r @%s' % (self.meta,self.dn)

	def get_index (self):
		"""Return the index object under which this Resource resides.
		"""
		return self.indexobj

	def get (self, key, default=None):
		return self.meta.get (key, default)

	def rollback (self):
		"""Deliberately forget changes made to this object.
		   This is part of an orderly return to an old state.
		   This is the opposite of commit(), which writes any
		   collected changes to LDAP.
		"""
		for (k,vs) in self.olds.items ():
			self.meta [k] = vs
		self.olds = { }

	def commit (self):
		"""Commit changes by sending them to LDAP.  When the
		   stored values have changed since this object cached
		   changes, it may happen that conflicts arise, which
		   will be reported by this call.
		"""
		if self.olds == { }:
			return
		dn1 = self.dn
		addkv = [ (k, self.meta[k] - self.olds.get(k      ))
		          for k in self.meta
		          if  k in self.olds ]
		delkv = [ (k, self.olds[k] - self.meta.get(k,set()))
		          for k in self.olds ]
		at1 = [
			(MOD_ADD   ,k,[s2b(v) for v in vs]) for (k,vs) in addkv
		] + [
			(MOD_DELETE,k,[s2b(v) for v in vs]) for (k,vs) in delkv
		]
		print ('ABOUT TO MODIFY %r' % at1)
		dap.modify_s (dn1, at1)
		self.olds = { }

	def __getitem__ (self, k):
		return self.meta [k]

	def __setitem__ (self, k, vs):
		if k not in self.olds:
			self.olds [k] = self.meta.get (k, set ())
		self.meta [k] = set (vs)

	def __delitem__ (self, k):
		if k not in self.olds:
			self.olds [k] = self.meta [k]
		del self.meta [k]

	def open (self, reading=True, writing=False, locked=True,
	                truncate=False, endpos=False):
		"""Return the file underneath this resource.  The
		   returned object is file-like and offers at least
		   the functions read, write, seekable/seek/tell
		   and of course, close.
		   
		   The file must be opened for reading and/or writing.
		   Creating and truncating only works when writing.
		   Locking while writing is exclusive, otherwise it
		   is shared; the lock is filesystem-operated and
		   is given up when closing; unrelated to LDAP lockedBy.
		   When endpos is set, the file pointer is at the end.
		"""
		devnull = False
		lockmode = fcntl.LOCK_SH
		if writing:
			flags = 'w' if truncate else 'w+'
			lockmode = fcntl.LOCK_EX
		else:
			assert not truncate, 'You can only truncate a Resource in write mode'
		if reading and not writing:
			flags = 'r'
		fn = '%s/%s/%s' % (reservoir_home,self.colluuid,self.resuuid)
		fh = open (fn, flags, 0o644)
		if locked:
			fd = fh.fileno ()
			try:
				fcntl.lockf (fd, lockmode | fcntl.LOCK_NB)
			except:
				fh.close ()
				raise
		return fh


class Index:
	"""Operations to proceed from index to index while traversing
	   the Reservoir.  Calls update the object, but copies may be
	   taken at any time.
	"""

	def __init__ (self, domain, user=None):
		"""Create an initial index object for a domain and
		   possible a user under that domain.
		"""
		#TODO#ACL#
		assert domain is not None, 'You need a domain, and optionally a user, to find a Reservoir home node'
		self.domain   = domain
		self.user     = user
		self.colluuid = None
		self.curidx   = None

	def __str__ (self):
		dn = 'associatedDomain=%s,%s' % (self.domain,reservoir_base)
		if self.colluuid is not None:
			dn = 'resins=%s,%s' % (self.colluuid,dn)
		elif self.user is not None:
			dn = 'uid=%s,%s' % (self.user,dn)
		return dn

	def check_acl (self, colluuid):
		# raise NotImplementedError ('No ACL support yet')
		sys.stderr.write ('\nNOT IMPLEMENTED: ACL SUPPORT FOR RESERVOIR INDEXES\n\n')

	def set_colluuid (self, colluuid):
		"""For the current domain, switch to a fixed collection
		   by setting its UUID.  Drop a cached object, if any;
		   if the caller cared, he should have copied us first.
		"""
		assert colluuid is not None, 'Collection UUID cannot be None'
		self.check_acl (colluuid)
		self.colluuid = colluuid
		self.curidx = None

	def dn_base (self):
		"""Return the baseDN for the Reservoir tree.
		"""
		return reservoir_base

	def dn_domain (self):
		"""Return the DN of the domain home object.
		"""
		dn = 'associatedDomain=%s,%s' % (self.domain, reservoir_base)
		return dn

	def dn_domain_user (self):
		"""Return the DN of the user home object under the domain.
		"""
		assert self.user is not None, 'Not an index for a user'
		dn = self.dn_domain ()
		dn = 'uid=%s,%s' % (self.user, dn)
		return dn

	def dn_home (self):
		"""Return the DN of the home object, either the domain or
		   user under the domain.
		"""
		if self.user is not None:
			return self.dn_domain_user ()
		else:
			return self.dn_domain ()
		return dn

	def dn_cursor (self):
		"""Return the current DN of this object.
		"""
		return str (self)

	def get_domain (self):
		"""Return the domain set for this LDAP object.
		"""
		return self.domain

	def get_user (self):
		"""Return the user set for this LDAP object, or None.
		   Note that the user may not actually be part of the
		   current path at all.
		"""
		return self.user

	def get_colluuid (self):
		"""Return the collection UUID that this cursor currently
		   points at.
		"""
		return self.colluuid

	def reset_home (self):
		"""Return to the home object, basically the domain or
		   its user object.
		"""
		self.check_acl (None)
		self.colluuid = None
		self.curidx = None

	def _index_load (self):
		"""Load the current index and cache it.
		"""
		self.curidx = [ ]
		try:
			dn1 = str (self)
			fl1 = '(objectClass=reservoirIndex)'
			al1 = ['reservoirRef']
			#DEBUG# print ('searching', dn1, fl1, al1)
			qr1 = dap.search_s (dn1, SCOPE_BASE, filterstr=fl1, attrlist=al1)
			#DEBUG# print ('Query response:', qr1)
			for (dn,at) in qr1:
				if 'reservoirRef' in at:
					self.curidx += b2s (at ['reservoirRef'])
		except NO_SUCH_OBJECT:
			pass

	def _index_lookup (self, _name, current_colluuid=None):
		"""Lookup the space-prefixed name or empty string and
		   return the resulting colluuid.  When provided, the
		   search starts from the given colluuid.
		"""
		if self.curidx is None:
			self._index_load ()
		print ('DEBUG: Type of _name is %r' % type (_name))
		_name = _name
		print ('DEBUG: Looking for "%s" in current index %r' % (_name,self.curidx))
		for idx in self.curidx:
			print ('Debug: Comparing against "%s"' % idx [36:])
			if idx [36:] == _name:
				current_colluuid = idx [:36]
				self.check_acl (current_colluuid)
				self.colluuid = current_colluuid
				self.curidx = None
				print ('DEBUG: Found %s' % current_colluuid)
				return current_colluuid
		return None

	def index_default (self):
		"""Lookup the default entry in the current index.
		"""
		colluuid = self._index_lookup ('')
		if colluuid is None:
			raise KeyError ('No unnamed/default entry in %s' % str(self))
		self.check_acl (colluuid)
		self.colluuid = colluuid
		self.curidx = None

	def index_apphint (self, apphint):
		"""The first step taken from a home object is a
		   switch to a collection UUID for an application.
		   This can be done with a name that serves as an
		   apphint in the home object.  When this name is
		   not found in the index, it is silently replaced
		   with the default/unnamed index entry.
		"""
		assert self.colluuid is None, 'Application hints are only available in a home index'
		colluuid = self._index_lookup (' ' + apphint)
		if colluuid is None:
			colluuid = self._index_lookup ('')
		assert colluuid is not None, 'Application hint failed and non default/unnamed node found either'
		self.check_acl (colluuid)
		self.colluuid = colluuid
		self.curidx = None

	def list_index (self):
		"""List the names of the current Index.  Also cache
		   the translation to Collection UUID, but do not
		   return it; index_name() can be used to access each
		   name instead.
		"""
		if self.curidx is None:
			self._index_load ()
		retval = [ entry [37:]
		           for entry in self.curidx
		           if len (entry) >= 37 ]

	def index_name (self, name, defaultOK=False):
		"""Find the given name in the index.  If it is absent
		   and defaultOK is set, the default/unnamed index
		   entry is used instead.  When name is None, this is
		   in fact the only option (but not assumed by the flag).
		   #TODO# defaultOK is standard for a home index (no colluuid)
		"""
		assert defaultOK or name is not None, 'Index lookups require either a name or welcoming the default/unnamed entry'
		assert self.colluuid is not None, 'This is a home node, and needs an apphint before naming entries'
		if name is not None:
			colluuid = self._index_lookup (' ' + name)
		if colluuid is None and defaultOK:
			colluuid = self._index_lookup ('')
		if colluuid is None:
			if defaultOK:
				name = name +' or default/unnamed entry'
			raise KeyError ('Name "%s" not found in %s' % (name,str(self)))
		self.check_acl (colluuid)
		self.colluuid = colluuid
		self.curidx = None

	def index_path (self, *path):
		"""Traverse a sequence of path names, none of which may be
		   None and none of which can use the default/unnamed entry.
		   Note that paths break through the ACL of intermediate
		   steps.  It is only the last index whose ACL matters.
		"""
		assert not name in path, 'Index paths cannot contain None'
		assert self.colluuid is not None, 'This is a home node, and needs an apphint before traversing a path'
		cur_colluuid = self.colluuid
		for step in path:
			cur_colluuid = self._index_lookup (' ' + step, cur_colluuid)
			if cur_colluuid is None:
				raise KeyError ('Path step %s not found' % step)
		self.check_acl (cur_colluuid)
		self.colluuid = cur_colluuid
		self.curidx = None

	def resource_dn (self, resuuid):
		"""Given a resource UUID, return the DN of its object.
		"""
		assert self.colluuid is not None, 'Home nodes need an apphint before resources can be loaded'
		return 'resource=%s,resins=%s,associatedDomain=%s,%s' % (resuuid,self.colluuid,self.domain,reservoir_base)

	def load_resource (self, resuuid):
		"""Load a single resource from LDAP and return it as a
		   Resource object.  Use this when you know its UUID, but
		   for lists the load_all_resources() method may be more
		   efficient.
		"""
		assert self.colluuid is not None, 'Home nodes need an apphint before resources can be loaded'
		me = copy.copy (self)
		return Resource (me, resuuid)

	def list_resources (self):
		"""Return a possibly-empty list of resource UUIDs under the
		   current index.  This is not possible in a home node of a
		   domain or user, because an apphint must first be given.
		   The ACL will be checked live, to avoid lingering objects
		   that are used after their valid lives have expired.
		"""
		assert self.colluuid is not None, 'Home nodes need an apphint before resources can be listed or loaded'
		self.check_acl (self.colluuid)
		try:
			dn1 = str (self)
			fl1 = '(objectClass=reservoirResource)'
			al1 = ['resource']
			#DEBUG# print ('searching', dn1, fl1, al1)
			qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
			#DEBUG# print ('Query response:', qr1)
			retval = [ ]
			for (dn,at) in qr1:
				if 'resource' in at:
					retval += at ['resource']
			return retval
		except NO_SUCH_OBJECT:
			return []

	def load_all_resources (self):
		"""Return a possibly-empty list of resources in the current
		   index.  This is not possible in a home node of a domain or
		   user, because from there an apphint must first be given.
		   The ACL will be checked live, to avoid lingering objects
		   that are used after their valid lives have expired.
		   TODO: Can we skip the ACL completely before?
		"""
		me = copy.copy (self)
		return [ Resource (me, resuuid)
		         for resuuid in self.list_resources () ]



def add_domain (domain, orgname=None):
	"""Introduce a domain to Reservoir and possibly an organisation name
	   along with it.  Create a default/unnamed index referencing a new
	   Collection object.  Return a new Index set to the domain's home.
	   #TODO# Treat current user as admin, and set the ACL accordingly.
	"""
	home_colluuid = random_uuid ()
	dn1 = 'associatedDomain=%s,%s' % (domain,reservoir_base)
	at1 = s2b ([
		('objectClass', [b'organization',b'domainRelatedObject',b'reservoirIndex',b'aclObject']),
		('o', orgname or domain),
		('associatedDomain', domain),
		('reservoirRef', [home_colluuid]),
		('acl', '%%w @%s' % domain),
	])
	try:
		meta = dap.add_s (dn1,at1)
	except ALREADY_EXISTS:
		raise FileExistsError ('Domain %s was already introduced to the Reservoir' % domain)
	dn2 = 'resins=%s,%s' % (home_colluuid,dn1)
	at2 = s2b([
		('objectClass', [b'reservoirCollection',b'resourceInstanceObject',b'aclObject',b'reservoirIndex']),
		('rescls', reservoir_uuid),
		('resins', home_colluuid),
		('cn', 'Home Collection of %s' % domain),
		('acl', '555 %%r @%s %%w admin@%s' % (domain,domain)),
	])
	print ('adding', dn2)
	dap.add_s (dn2, at2)
	return Index (domain)


def get_domain (domain):
	"""Retrieve an Index object that is home to the given domain name,
	   which already exist in the Reservoir.
	"""
	return Index (domain)


def list_domains ():
	"""Retrieve a list of domain names that are registered with
	   the Reservoir.
	"""
	retval = [ ]
	try:
		dn1 = reservoir_base
		fl1 = '(objectClass=domainRelatedObject)'
		al1 = ['associatedDomain']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single associatedDomain
		# but domainRelatedObject does not set it as SINGLE-VALUE
		for (dn,at) in qr1:
			if 'associatedDomain' in at:
				retval += at ['associatedDomain']
	except NO_SUCH_OBJECT:
		pass
	return retval


def add_domain_user (domain, user):
	"""Add a user node under an already created domain name.  Create a
	   default/unnamed index referencing a new Collection object.
	   Return a new Index set to the user's home.
	"""
	home_colluuid = random_uuid ()
	dn1 = 'uid=%s,associatedDomain=%s,%s' % (user,domain,reservoir_base)
	at1 = s2b ([
		('objectClass', [b'account',b'uidObject',b'domainRelatedObject',b'reservoirIndex',b'aclObject']),
		('uid', user),
		('associatedDomain', domain),
		('reservoirRef', [home_colluuid]),
		('acl', '%%w %s@%s' % (user,domain)),
	])
	try:
		meta = dap.add_s (dn1,at1)
	except ALREADY_EXISTS:
		raise FileExistsError ('User %s of domain %s was already introduced to the Reservoir' % (user,domain))
	dn2 = 'resins=%s,%s' % (home_colluuid,dn1)
	at2 = s2b ([
		('objectClass', [b'reservoirCollection',b'reservoirIndex',b'resourceInstanceObject',b'accessControlledObject']),
		('rescls', reservoir_uuid),
		('resins', home_colluuid),
		('cn', 'Home Collection of %s@%s' % (user,domain)),
		('acl', '%%w %s@%s' % (user,domain)),
	])
	print ('adding', dn2)
	dap.add_s (dn2, at2)
	return Index (domain, user)


def get_domain_user (domain, user):
	"""Return an Index object that is home to the given user@domain,
	   which must already exist in the Reservoir.
	"""
	return Index (domain, user)


def list_domain_users (domain):
	"""Retrieve a list of users that are registered under a domain with
	   the Reservoir.  The domain is either an Index object or a string.
	"""
	retval = [ ]
	try:
		if isinstance (domain,Index):
			dn1 = domain.dn_domain ()
		else:
			dn1 = 'associatedDomain=%s,%s' % (domain,reservoir_base)
		fl1 = '(objectClass=domainRelatedObject)'
		al1 = ['uid']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single associatedDomain
		# but domainRelatedObject does not set it as SINGLE-VALUE
		for (dn,at) in qr1:
			if 'uid' in at:
				retval += at ['uid']
	except NO_SUCH_OBJECT:
		pass
	return retval


def add_collection (index, collname):
	"""Add a new Resource Collection under the domain for the given
	   Index.  Move this Index object to the new Collection.
	"""
	domain = index.get_domain ()
	colluuid = random_uuid ()
	newdir = '%s/%s' % (reservoir_home,colluuid)
	os.mkdir (newdir)
	dn1 = 'resins=%s,associatedDomain=%s,%s' % (colluuid,domain,reservoir_base)
	at1 = s2b ([
		('objectClass', [b'reservoirCollection',b'reservoirIndex',b'resourceInstanceObject',b'aclObject']),
		('rescls', reservoir_uuid),
		('resins', colluuid),
		('cn', collname or 'Anonymous Resource Collection'),
		('acl', '%%w @%s' % domain),
	])
	print ('adding', dn1)
	dap.add_s (dn1, at1)
	dn2 = str (index)
	ref = [ s2b ('%s %s' % (colluuid,collname)) ]
	at2 = [ (MOD_ADD,'reservoirRef',ref) ]
	dap.modify_s (dn2, at2)
	index.set_colluuid (colluuid)


def get_collection (index, colluuid):
	"""Find the Resource Collection with the given UUID.  Move the
	   given Index object to that Collection.
	"""
	index.set_colluuid (colluuid)


def add_resource (index, **meta):
	"""Add a new Resource under the given Index (which must not be
	   a home index, so give an apphint before doing this).  Store the
	   metadata as attributes.  Add auxiliary object classes if needed,
	   but at least include the 'reservoirResource' objectClass.  Also
	   provide at least a mediaType and a cn attribute.
	   The underlying file will be created empty.  The created Resource
	   is returned as an object, and it may be used to open() the file.
	"""
	coll_dn = index.dn_cursor ()
	colluuid = index.get_colluuid ()
	resuuid = random_uuid ()
	newfile = '%s/%s/%s' % (reservoir_home,colluuid,resuuid)
	os.close (os.open (newfile, os.O_CREAT | os.O_WRONLY))
	dn1 = 'resource=%s,%s' % (resuuid,coll_dn)
	assert 'reservoirResource' in meta.get ('objectClass',[]), 'Added resources must declare objectClass:reservoirResource (and may add auxiliary classes)'
	assert 'mediaType' in meta, 'Media type must be provided'
	assert 'documentIdentifier' in meta, 'documentIdentifier must be provided'
	assert 'cn' in meta, 'Common name must be provided'
	at1 = [ (k,s2b(v)) for (k,v) in meta.items () ]
	at1.append ( ('resource',s2b(resuuid)) )
	print ('adding', dn1)
	dap.add_s (dn1, at1)
	return index.load_resource (resuuid)

def get_resource (index, resuuid):
	"""Load a resource as identified by UUID under the given Index.
	"""
	return index.load_resource (resuuid)

def search_resources (index, ldap_filter):
	"""Search for resources under the given Index (which must not be
	   a home index, so use the apphint first).  Use the given LDAP
	   filter expression to select objects.  The return value is a
	   (possibly empty) dict with Resource instances indexed by their
	   UUID.  The Resource instances have a cache of attributes, but
	   there is no guarantee that nobody else has another cache.
	"""
	dn1 = str (index)
	assert dn1 [:7] == 'resins=', 'No resources under a home Index, so searching is unsupported'
	fl1 = '(&(objectClass=reservoirResource)%s)' % ldap_filter
	#DEBUG# print ('searching', dn1, fl1, al1)
	qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1)
	retval = { }
	for (dn,at) in qr1:
		if 'resource' in at:
			atres = at ['resource']
			if len (atres) != 1:
				continue
			resuuid = b2s (atres [0])
			retval [resuuid] = Resource (index, resuuid, at)
	return retval

