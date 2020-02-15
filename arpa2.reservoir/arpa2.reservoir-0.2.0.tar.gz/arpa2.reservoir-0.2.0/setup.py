import setuptools
from os import path


#
# Preparation
#
here = path.dirname (path.realpath (__file__))


#
# Packaging Instructions -- arpa2shell.cmd, .cmdparser, .amqp
#
readme = open (path.join (here, 'README.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.reservoir',
	version = '0.2.0',
	url = 'https://github.com/arpa2/reservoir',
	description = 'ARPA2 Reservoir -- object store with metadata in LDAP',
	long_description = readme,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Reservoir project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [ 'arpa2', ],
	packages = [
		'arpa2',
		'arpa2.reservoir',
	],
	package_dir = {
		'arpa2'            : path.join (here, 'src'),
		'arpa2.reservoir'  : path.join (here, 'src', 'reservoir'),
	},

	# How?
	entry_points = {
		'console_scripts' : [
			'arpa2reservoir=arpa2.reservoir.shell:main',
			'sftp-reservoir=arpa2.reservoir.sftp:main',
			'rmt-reservoir=arpa2.reservoir.rmt:main',
		],
		'arpa2.shell.cmdshell.subclasses' : [
			'arpa2reservoir=arpa2shell.arpa2reservoir.shell:Cmd',
		],
	},

	# Requirements
	install_requires = [ 'arpa2.shell', 'python-ldap', 'gssapi', 'enum34 ; python_version < "3"', 'six' ],
	# extras_require = {
	# 	'JSON' : [ 'gssapi', 'python-qpid-proton' ],
	# },

)

