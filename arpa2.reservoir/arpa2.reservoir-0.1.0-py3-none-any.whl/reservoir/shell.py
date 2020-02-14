#!/usr/bin/env python
#
# arpa2.reservoir.shell -- Administration utility for Reservoir
#
# This commandline TODO:uses the Reservoir API to update LDAP.
# It is useful as an administrator's tool which, based on
# the ACL mechanism, could be opened up to the public!
#
# The ARPA2 shell mechanism includes a few facilities:
#  - arpa2shell is a meta-shell that can start this one
#  - arpa2shell adds commands to return to other shells
#  - arpa2amqp.d acccesses this shell for JSON commands
#
# From: Rick van Rein <rick@openfortress.nl>


import os
import sys
import uuid
import re

from arpa2.shell import cmdshell, cmdparser

#TODO# MOVE OUT to api
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
#TODO# MOVE OUT to api
reservoir_uuid = '904dfdb5-6b34-3818-b580-b9a0b4f7e7a9'


# The home directory for ARPA2 Reservoir
#
#TODO# MOVE OUT to api
reservoir_home = '/var/arpa2/reservoir'


#
# Configuration
#

if len (sys.argv) == 2:
	sys.stderr.write ('Usage: ' + sys.argv [0] + ' [thingy add|del|list|get|... [args...]]\n')
	sys.exit (1)

base = 'ou=Reservoir,o=arpa2.net,ou=InternetWide'

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

dn_2_coll_dom = re.compile ('^resins=([^,]+),associatedDomain=([^,]+),' + base + '$')
dn_2_res_coll_dom = re.compile ('^resource=([^,]+),resins=([^,]+),associatedDomain=([^,]+),' + base + '$')

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
for rdn in map (str.strip, whoami.split (',')):
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


# Produce a UUID in the format we like it (lowercase string).
#
def random_uuid ():
	return str (uuid.uuid4 ()).lower ()

# Add a domain to LDAP; Riak KV treats this level as implicitly created
#
def cmd_domain_add (domain, orgname=None):
	dn1 = 'associatedDomain=' + domain + ',' + base
	at1 = [
		('objectClass', ['organization','domainRelatedObject','reservoirIndex', 'aclObject']),
		('o', orgname or domain),
		('associatedDomain', domain),
	]
	try:
		meta = dap.add_s (dn1,at1)
	except ALREADY_EXISTS:
		print ('Domain already exists.')
		return
	os.mkdir (reservoir_home + '/' + domain)

# Delete a domain from LDAP; Riak KV treats this level as implicitly created
#
def cmd_domain_del (*domains):
	for domain in domains:
		dn1 = 'associatedDomain=' + domain + ',' + base
		try:
			#DEBUG# print ('deleting', dn1)
			dap.delete_s (dn1)
		except NOT_ALLOWED_ON_NONLEAF:
			print ('Remove other stuff first')
		except NO_SUCH_OBJECT:
			sys.stderr.write ('No such domain\n')
		os.rmdir (reservoir_home + '/' + domain)

# List domains in LDAP
#
def fetch_domain_list ():
	try:
		dn1 = base
		fl1 = '(objectClass=domainRelatedObject)'
		al1 = ['associatedDomain']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single associatedDomain
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ str (at.get ('associatedDomain', [b'(undefined)']) [0],
		              'utf-8')
		         for (dn,at) in qr1 ]
	except NO_SUCH_OBJECT:
		return []

def cmd_domain_list ():
	for domain in fetch_domain_list ():
		print ('Domain:', domain)


# Add a new Resource Collection.
# This adds a collection RDN to LDAP and a bucket to Riak KV.
# It sets up a default ACL granting no (or "Visitor") rights to anyone.
#
def cmd_collection_add (domain, collname):
	colluuid = random_uuid ()
	dn1 = 'resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	at1 = [
		('objectClass', ['reservoirCollection', 'resourceInstance', 'accessControlledObject','reservoirIndex']),
		('rescls', reservoir_uuid),
		('resins', colluuid),
		('cn', collname),
	]
	print ('adding', dn1)
	dap.add_s (dn1, at1)
	os.mkdir (reservoir_base + '/' + domain + '/' + colluuid)
	print ('Collection:', colluuid)
	return colluuid

# Delete a Resource Collection.
# This removes a recourceInstanceKey RDN from LDAP and the bucket in Riak KV
#
def cmd_collection_del (domain, *colluuids):
	for colluuid in colluuids:
		dn1 = 'resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
		#DEBUG# print ('deleting', dn1)
		dap.delete_s (dn1)
		os.rmdir (reservoir_base + '/' + domain + '/' + colluuid)

# List the Resource Collections under a domain.
#
def fetch_collection_list (domain):
	try:
		dn1 = 'associatedDomain=' + domain + ',' + base
		fl1 = '(&(objectClass=reservoirCollection)(rescls=' + reservoir_uuid + '))'
		al1 = ['resins','resourceInstance']
		#DEBUG# print ('searching', dn1, fl1, al1)
		qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
		#DEBUG# print ('Query response:', qr1)
		# Note that we always set a single resins
		# but domainRelatedObject does not set it as SINGLE-VALUE
		return [ str (at.get ('resins',
		              at.get ('resourceInstance',
		                      [b'(undefined)'])) [0],
		              'utf-8')
		         for (dn,at) in qr1 ]
	except NO_SUCH_OBJECT:
		return []

def cmd_collection_list (domain=None):
	if domain is None:
		domains = fetch_domain_list ()
	else:
		domains = [domain]
	for domain in domains:
		print ('Domain:', domain)
		for colluuid in fetch_collection_list (domain):
			print ('Collection:', colluuid)

def cmd_index_add_by_dn (dn1, refname, refcolluuid):
	at1 = [ (MOD_ADD, 'reservoirRef', refcolluuid + ' ' + refname) ]
	dap.modify_s (dn1, at1)

def cmd_index_add (domain, colluuid, refname, refcolluuid):
	dn1 = 'resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	cmd_index_add_by_dn (dn1, refname, refcolluuid)

def cmd_index_del_by_dn (dn1, refname, refcolluuid):
	at1 = [ (MOD_DELETE, 'reservoirRef', refcolluuid + ' ' + refname) ]
	dap.modify_s (dn1, at1)

def cmd_index_del (domain, colluuid, refname, refcolluuid):
	dn1 = 'resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	cmd_index_del_by_dn (dn1, refname, refcolluuid)

def fetch_index_list (dn1):
	rv1 = { }
	#DEBUG# print ('searching', dn1)
	qr1 = dap.search_s (dn1, SCOPE_BASE, attrlist=['reservoirRef'])
	#DEBUG# print ('Query result:', qr1)
	for (dn,at) in qr1:
		for rr in at.get ('reservoirRef', []):
			rr = str (rr, 'utf-8')
			try:
				[v,k] = rr.split (' ', 1)
				rv1 [k] = v
			except:
				rv1 [rr] = '(undefined)'
	return rv1

def fetch_index_colluid_by_dn_name (dn1, name):
	idx = fetch_index_list (dn1)
	return idx [name]

def cmd_index_list (domain, colluuid):
	print ('Domain:', domain)
	print ('Collection:', colluuid)
	dn1 = 'resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	for (refname,uuid) in fetch_index_list (dn1).items ():
		print ('Reference:', uuid, refname or '')

# Add an object to the given Resource Collection.
# This sets up a descriptive object in LDAP and loads the object into Riak KV.
#
def cmd_resource_add (domain, colluuid, mediatype, objname, blob):
	objkey = random_uuid ()
	dn1 = 'resource=' + objkey + ',resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	at1 = [
		('objectClass', ['document', 'reservoirResource']),
		('resource', objkey),
		('documentIdentifier', objkey),
		('mediaType', mediatype),
		('cn', objname),
	]
	fn1 = '%s/%s/%s/%s' % (reservoir_home, domain, colluuid, objkey)
	with open (fn1, 'w') as f:
		f.write (blob)
	dap.add_s (dn1, at1)
	# print ('Domain:', domain)
	# print ('Collection:', colluuid)
	print ('Resource:', objkey)
	return objkey

# Remove an object.
# This removes the data from Riak KV and the metadata from LDAP.
#
def cmd_resource_del (domain, colluuid, *objkeys):
	for objkey in objkeys:
		dn1 = 'resource=' + objkey + ',resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
		fn1 = '%s/%s/%s/%s' % (reservoir_home, domain, colluuid, objkey)
		#DEBUG# print ('searching', dn1)
		dap.search_s (dn1, SCOPE_BASE)
		#DEBUG# print ('deleting', dn1)
		try:
			dap.delete_s (dn1)
			os.remove (fn1)
		except NOT_ALLOWED_ON_NONLEAF:
			print ('Remove other stuff first')

# List the objects in a Resource Collection.
#
def fetch_resource_list_by_dn (dn1):
	fl1 = '(objectClass=document)'
	al1 = ['resource']
	#DEBUG# print ('searching', dn1, fl1, al1)
	qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
	#DEBUG# print ('Query response:', qr1)
	# Treat the resource as SINGLE-VALUE
	# as this is how we use it
	return [ str (at.get ('resource', [b'(undefined)']) [0],
	              'utf-8')
	         for (dn,at) in qr1 ]
def fetch_resource_list (domain, colluuid):
	dn1 = 'resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	return fetch_resource_list_by_dn (dn1)
def cmd_resource_list (domain=None, colluuid=None):
	if domain is None:
		domains = fetch_domain_list ()
	else:
		domains = [domain]
	for domain in domains:
		print ('Domain:', domain)
		if colluuid is None:
			colluuids = fetch_collection_list (domain)
		else:
			colluuids = [colluuid]
		for colluuid in colluuids:
			print ('Collection:', colluuid)
			for objkey in fetch_resource_list (domain, colluuid):
				print ('Resource:', objkey)

# Get an object.
# This finds the object in LDAP and subsequently downloads in from Riak KV.
# Or... does it not even need to look into LDAP?
#
resource_attribute_map = {
	'resource': 'Resource',
	'mediaType': 'Content-Type',
	'cn': 'Name',
}
def cmd_resource_get (domain, colluuid, objkey):
	print ('Constructing dn1: resource=', objkey, ',resins=', colluuid, ',associatedDomain=', domain, ',', base)
	dn1 = 'resource=' + objkey + ',resins=' + colluuid + ',associatedDomain=' + domain + ',' + base
	fl1 = '(&(objectClass=reservoirResource)(resource=%s))' % objkey
	al1 = resource_attribute_map.keys ()
	#DEBUG# print ('searching', dn1, fl1, al1)
	qr1 = dap.search_s (dn1, SCOPE_ONELEVEL, filterstr=fl1, attrlist=al1)
	#DEBUG# print ('Query response:', qr1)
	fn1 = '%s/%s/%s/%s' % (reservoir_home, domain, colluuid, objkey)
	blob = open (fn1, 'rb').read ()
	for (dn,at) in qr1:
		for atnm in al1:
			for atvals in at.get (atnm, []):
				for atval in atvals:
					if type (atval) == bytes:
						atval = str (atval, 'utf-8')
					print ('%s: %s' % (resource_attribute_map [atnm], atval))
	print ('Content-Length', len (blob))
	#TEST# print ('Data:', blob [:100])
	print ('Data:', blob)



class ListOfDomains (cmdparser.Token):
	def get_values (self, *context):
		#DEBUG# print ('Fetching domain list under context', context, '::', type (context))
		retval = fetch_domain_list ()
		#DEBUG# print ('Returning domain list', retval)
		return retval
	def __str__ (self):
		return 'domain'


#
# Produce lists of new values (or indicate anything is accepted)
#
def token_factory (token):
	#DEBUG# print ('token_factory ("' + token + '")')
	if token [:3] == 'new':
		# Accept any token (as a newxxx value)
		return cmdparser.AnyToken (token)
	elif token == 'domain':
		# Find a list of domains
		#TODO# return ListOfDomains ()
		retval = ListOfDomains ('domain')
		#DEBUG# print (retval, '::', type (retval))
		return retval
	elif token == 'colluuid':
		# Find a list of collection UUIDs, possibly crossing over to another domain
		"TODO"
		return None
	elif token == 'name':
		# Find a name in the current index (the current one -- confusing "index path")
		"TODO"
		return None
	elif token == 'var=val':
		"TODO"
		return None
	elif token == 'key':
		# Find a name in the current collection
		"TODO"
		return None
	elif token == 'descr':
		return cmdparser.AnyTokenString ('descr')
	else:
		# Cry out loud -- this isn't supposed to happen
		raise NotImplementedError ('Unknown kind of token in syntax: ' + token)


#
# The shell for arpa2reservoir (based on cmdparser)
#
#TODO# @cmdparser.CmdClassDecorator()
class Cmd (cmdshell.Cmd):

	version = (0,0)
	prompt = "arpa2reservoir> "
	intro = "Edit Reservoir: Resource Collections and Resources.\nAnd Resource Indexes per Domain and per Resource Collection."

	def __init__ (self):
		cmdshell.Cmd.__init__ (self)
		self.cur_domain = None
		self.cur_dn = None
		#UNUSED# self.cur_colluuid = None

	def reset (self):
		self.cur_domain = None
		self.cur_dn = None

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_domain (self, args, fields):
		"""
		domain ( list | add <newdomain> | del <domain> [...] )

		domain list -- Lists domains managed under the Reservoir.
		domain add -- Creates a new domain under the Reservoir.
		domain del -- Removes an empty domain from the Reservoir
		"""

		if args [1] == 'list':
			for domain in fetch_domain_list ():
				print (domain)
		elif args [1] == 'add':
			cmd_domain_add (args [2])
			self.cur_domain = args [2]
		elif args [1] == 'del':
			print ('Invoking domain deletion on', args [2:])
			cmd_domain_del (*args [2:])
			if args [2] == self.cur_domain:
				self.cur_domain = None
		else:
			raise NotImplementedError ('Unexpected command ' + ' '.join (args))
		return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_index (self, args, fields):
		"""
		index ( dn | list | add <colluuid> <newname> | del <name> |
		        domain <domain> | collection <colluuid> | path <name> [...] )

		index dn -- Shows the LDAP node with the current index.
		index list -- Lists the (<colluid> and) <name> for index entries.
		index add -- Adds a <newcolluid> to the index with a new <newname>.
		index del -- Removes a <name> from the index.
		index domain -- Changes the current index to that of the <domain>.
		index collection -- Changes the current index to a given <colluuid>.
		index path -- Steps from index to index following the <name> in each.
		"""

		if args [1] == 'dn':
			if self.cur_dn is not None:
				print (self.cur_dn)
			else:
				print ('(undefined)')
		elif args [1] == 'list':
			if self.cur_dn is None:
				print ('First use: index domain <domain> | collection <colluuid>')
				return False
			idx = fetch_index_list (self.cur_dn)
			for (k,v) in idx.items ():
				print (k + '\t-> ' + v)
		elif args [1] == 'add':
			if self.cur_dn is None:
				print ('First use: index domain <domain> | collection <colluuid>')
				return False
			cmd_index_add_by_dn (self.cur_dn, args [3], args [2])
		elif args [1] == 'del':
			if self.cur_dn is None:
				print ('First use: index domain <domain> | collection <colluuid>')
				return False
			colluuid = fetch_index_colluid_by_dn_name (self.cur_dn, args [2])
			cmd_index_del_by_dn (self.cur_dn, args [2], colluuid)
			#UNUSED# if colluuid == self.cur_colluuid:
			#UNUSED# 	self.cur_colluuid = None
		elif args [1] == 'domain':
			self.cur_dn = 'associatedDomain=' + args [2] + ',' + base
			self.cur_domain = args [2]
			#UNUSED# self.cur_colluuid = None
		elif args [1] == 'collection':
			#UNUSED# self.cur_colluuid = args [2]
			#TODO# infer cur_domain and construct cur_dn
			print ('NOT IMPLEMENTED YET')
		elif args [1] == 'path':
			if self.cur_dn is None:
				print ('First use: index domain <domain> | collection <colluuid>')
				return False
			domain_and_up = ',associatedDomain=' + self.cur_domain + ',' + base
			for leg in args [2:]:
				idx = fetch_index_list (self.cur_dn)
				if leg not in idx:
					print ('Failed on', leg)
					break
				print (leg + '\t-> ' + idx [leg])
				self.cur_dn = 'resins=' + idx [leg] + domain_and_up
			print ('Current DN is now', self.cur_dn)
		else:
			raise NotImplementedError ('Unexpected command ' + ' '.join (args))
		return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_collection (self, args, fields):
		"""
		collection ( list [<domain>] | add <domain> <descr> | del <domain> <colluuid> [...] )

		collection list -- Shows the indexed collection, possibly for a <domain>.
		collection add -- Adds a collection described as <descr> to domain <domain>.
		collection del -- The indicated <colluid>s under <domain> are removed.
		"""

		if args [1] == 'list':
			#TODO# Currently lists everything, that could get a bit much!
			#TODO# What does this add to "index list" and "resource list"?
			cmd_collection_list (args [3] if len (args)>3 else None)
		elif args [1] == 'add':
			cmd_collection_add (args [2], args [3])
		elif args [1] == 'del':
			cmd_collection_del (args [3], *args [4:])
			#UNUSED# if self.cur_colluuid in args [4:]:
			#USUSED# 	TODO
		else:
			raise NotImplementedError ('Unexpected command ' + ' '.join (args))
		return False

	@cmdparser.CmdMethodDecorator(token_factory=token_factory)
	def do_resource (self, args, fields):
		"""
		resource ( list
		         | add <var=val> [...]
		         | del <key> [...]
		         | get <key> )

		To be added:
		         | set <key> <var=val> [...]

		resource list -- Shows the resources in the current collection.
		resource add -- Adds a resource to the current collection.
		resource del -- Removes a resource from the current collection.
		resource get -- Retrieves the resource and its metadata

		Resource adding requires metadata in var=val parameters,
		at least type=... name=... file=... are required.  (TODO)
		"""

		if args [1] == 'list':
			if self.cur_dn is None:
				print ('First use: index collection <colluuid>')
				return False
			for objkey in fetch_resource_list_by_dn (self.cur_dn):
				print ('Resource:', objkey)
		elif args [1] == 'add':
			m = dn_2_coll_dom.match (self.cur_dn or '')
			if m is None:
				print ('First use: index collection <colluuid>')
				return False
			(colluuid,domain) = m.groups ()
			vars = { }
			for var_val in args [2:]:
				(var,val) = var_val.split ('=', 1)
				vars [var] = val
			print ('VARS =', vars)
			mediatype = vars.get ('type')
			objname = vars.get ('name')
			filename = vars.get ('file')
			print ('TYPE/NAME/FILE =', (mediatype,objname,filename))
			if not (mediatype and objname and filename):
				print ('Please specify at least type= name= file=')
				return False
			blob = open (filename).read ()
			#TODO# Future extension possible with more attributes
			cmd_resource_add (domain, colluuid, mediatype, objname, blob)
		elif args [1] == 'del':
			m = dn_2_coll_dom.match (self.cur_dn or '')
			if m is None:
				print ('First use: index collection <colluuid>')
				return False
			(colluuid,domain) = m.groups ()
			cmd_resource_del (domain, colluuid, args [2:])
		elif args [1] == 'get':
			m = dn_2_coll_dom.match (self.cur_dn or '')
			if m is None:
				print ('First use: index collection <colluuid>')
				return False
			(colluuid,domain) = m.groups ()
			cmd_resource_get (domain, colluuid, args [2])
		else:
			raise NotImplementedError ('Unexpected command ' + ' '.join (args))
		return False

def main ():
	shell = Cmd ()
	shell.cmdloop ()

if __name__ == '__main__':
	main ()

