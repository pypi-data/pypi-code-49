import setuptools
from os import path


#
# Preparation
#
here = path.dirname (path.realpath (__file__))


#
# Packaging Instructions -- arpa2.shell.cmdshell, .cmdparser, .amqp
#
readme = open (path.join (here, 'README.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.shell',
	version = '0.1.0',
	url = 'https://gitlab.com/arpa2/shell',
	description = 'Generic ARPA2 commandline shell support -- shell switching -- JSON/AMQP backend',
	long_description = readme,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Shell project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [ 'arpa2', 'arpa2.shell', ],
	packages = [
		'arpa2',
		'arpa2.shell',
		'arpa2.shell.cmdshell',
		'arpa2.shell.cmdparser',
		'arpa2.shell.amqp',
	],
	package_dir = {
		'arpa2'                 : path.join (here, 'src'),
		'arpa2.shell'           : path.join (here, 'src', 'shell'),
		'arpa2.shell.cmdshell'  : path.join (here, 'src', 'shell', 'cmdshell'),
		'arpa2.shell.cmdparser' : path.join (here, 'src', 'shell', 'cmdparser'),
		'arpa2.shell.amqp'      : path.join (here, 'src', 'shell', 'amqp'),
	},

	# How?
	entry_points = {
		'arpa2.shell.cmdshell.subclasses' : [
			'arpa2shell=arpa2.shell.cmdshell.meta:Cmd',
		],
		'console_scripts' : [
			'arpa2shell=arpa2.shell.cmdshell.meta:main',
			'arpa2api=arpa2.shell.amqp.client:main [JSON]',
			'arpa2api.d=arpa2.shell.amqp.server:main [JSON]',
		],
	},

	# Requirements
	install_requires = [ 'enum34 ; python_version < "3"', 'six' ],
	extras_require = {
		'JSON' : [ 'gssapi', 'python-qpid-proton' ],
	},

)



#
# Additional setup -- for the arpa2dns shell
#
readme_dns = open (path.join (here, 'src', 'shell', 'arpa2dns', 'README.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.shell.dns',
	version = '0.0.3',
	url = 'https://github.com/arpa2/arpa2shell/tree/master/src/arpa2dns',
	description = 'The ARPA2 Shell for DNS',
	long_description = readme_dns,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Shell project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [ 'arpa2', 'arpa2.shell', ],
	packages = [
		'arpa2.shell',
		'arpa2.shell.arpa2dns',
	],
	package_dir = {
		'arpa2.shell'           : path.join (here, 'src', 'shell'),
		'arpa2.shell.arpa2dns'  : path.join (here, 'src', 'shell', 'arpa2dns'),
	},

	# How?
	entry_points = {
		'arpa2.shell.cmdshell.subclasses' : [
			'arpa2dns=arpa2.shell.arpa2dns.shell:Cmd',
		],
		'console_scripts' : [
			'arpa2dns=arpa2.shell.arpa2dns.shell:main',
		],
	},

	# Requirements
	install_requires = [ 'arpa2.shell', 'libknot' ],

)



#
# Additional setup -- for the arpa2identityhub shell
#
# BIG TODO: Not a cmdparser shell yet, so no integration with arpa2shell
#
readme_id = open (path.join (here, 'src', 'shell', 'arpa2id', 'README.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.shell.id',
	version = '0.0.3',
	url = 'https://github.com/arpa2/arpa2shell/tree/master/src/arpa2id',
	description = 'The ARPA2 Shell for Identity Management',
	long_description = readme_id,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Shell project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [ 'arpa2', 'arpa2.shell', ],
	packages = [
		'arpa2.shell',
		'arpa2.shell.arpa2id',
	],
	package_dir = {
		'arpa2.shell'           : path.join (here, 'src', 'shell'),
		'arpa2.shell.arpa2id'   : path.join (here, 'src', 'shell', 'arpa2id'),
	},

	# How?
	entry_points = {
		#NOTYET# 'arpa2shell.cmdshell.subclasses' : [
		#NOTYET# 	'arpa2id=arpa2shell.arpa2id.shell:Cmd',
		#NOTYET# ],
		'console_scripts' : [
			'arpa2identityhub=arpa2.shell.arpa2id.shell:main',
		],
	},

	# Requirements
	install_requires = [ 'arpa2.shell', 'python-ldap' ],

)



#
# Removed setup -- the arpa2reservoir shell is now arpa2.reservoir.shell
#



#
# Additional setup -- for the arpa2acl shell
#
readme_acl = open (path.join (here, 'src', 'shell', 'arpa2acl', 'README.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.shell.acl',
	version = '0.0.3',
	url = 'https://github.com/arpa2/arpa2shell/tree/master/src/arpa2acl',
	description = 'The ARPA2 Shell for ACL Management',
	long_description = readme_acl,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Shell project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [ 'arpa2', 'arpa2.shell', ],
	packages = [
		'arpa2.shell',
		'arpa2.shell.arpa2acl',
	],
	package_dir = {
		'arpa2.shell'           : path.join (here, 'src', 'shell'),
		'arpa2.shell.arpa2acl'  : path.join (here, 'src', 'shell', 'arpa2acl'),
	},

	# How?
	entry_points = {
		'arpa2.shell.cmdshell.subclasses' : [
			'arpa2acl=arpa2.shell.arpa2acl.shell:Cmd',
		],
		'console_scripts' : [
			'arpa2acl=arpa2.shell.arpa2acl.shell:main',
		],
	},

	# Requirements
	install_requires = [ 'arpa2.shell', 'python-ldap' ],

)

