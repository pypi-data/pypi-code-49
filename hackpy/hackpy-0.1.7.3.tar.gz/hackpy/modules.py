# Import modules
from os import path, remove, listdir, environ
from shutil import rmtree
from hackpy.settings import *
from hackpy.network  import *

# Get modules path
global modules_path
modules_path = environ['TEMP'] + '\\hackpy\\executable\\'

# Require module
def require_module(module):
	# Get modules location
	location = modules_path + module
	# Error function
	def error():
		raise ImportError('ERROR: HackPy requires module ' + module + ', but it not loaded\n' + location)
	# If module is .zip
	if module.endswith('.zip'):
		if not path.exists(location.split('.')[0]):
			error()
	# If module is .exe
	elif not path.exists(location):
		error()
		

# Load module
def load_module(module):
	# Get modules location
	location = modules_path + module
	# Check if module exists
	if path.exists(location) or path.exists(location.split('.')[0]):
		return True
	else:
		# Try to download module from server
		try:
			download(server_url + module, output = location)
		except:
			raise ConnectionError('Failed connect to server while downloading module ' + module)
		else:
			# If module is .zip archive
			if module.endswith('.zip'):
				from zipfile import ZipFile
				with ZipFile(location, 'r') as archive:
					archive.extractall(location.split('.')[0])
				remove(location)

# Load modules from .zip archive
def load_archive(archive):
	from zipfile import ZipFile
	with ZipFile(archive, 'r') as archive:
		archive.extractall(modules_path)

# Load modules
def load_modules(*modules):
	for module in modules:
		load_module(module)

# Unload module
def unload_module(module):
	# Get modules location
	location = modules_path + module
	# Check if module exists
	if path.exists(location) or path.exists(location.split('.')[0]):
		# Delete folder module
		if module.endswith('.zip'):
			rmtree(location.split('.')[0])
		# Delete file module
		elif path.isfile(location):
			remove(location)

# Unloading modules
def unload_modules(*modules):
	for module in modules:
		unload_module(module)

# Get modules list
def get_modules():
	modules = []
	for module in listdir(modules_path):
		modules.append(module)
	return modules