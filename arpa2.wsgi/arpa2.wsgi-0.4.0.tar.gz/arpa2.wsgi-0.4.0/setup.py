# setup.py for ARPA2 WSGI Middleware
#
# Package name "arpa2wsgi"
#
# From: Rick van Rein <rick@openfortress.nl>

import setuptools
from os import path

#
# Preparation
#
here = path.dirname (path.realpath (__file__))


#
# Packaging Instructions -- arpa2wsgi
#
readme = open (path.join (here, 'README.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.wsgi',
	version = '0.4.0',
	url = 'https://github.com/arpa2/wsgi-middleware',
	description = 'WSGI Middleware to "Bring Your Own IDentity" to a web server',
	long_description = readme,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (ARPA2 developer)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [
		'arpa2',
		'arpa2.wsgi',
	],
	packages = [
		'arpa2',
		'arpa2.wsgi',
		'arpa2.wsgi.byoid',
	],
	package_dir = {
		'arpa2'           : path.join (here,'arpa2'),
		'arpa2.wsgi'      : path.join (here,'arpa2','wsgi'),
		'arpa2.wsgi.byoid': path.join (here,'arpa2','wsgi','byoid'),
	},

	# How?
	# entry_points = ... Not for WSGI, right?

        # Requirements
        # install_requires = [ ... ],

)

