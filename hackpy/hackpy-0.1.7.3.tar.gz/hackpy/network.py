import socket
import urllib.request
from os              import remove, devnull
from json            import loads as json_loads
from hackpy.settings import *
from hackpy.commands import *


# Load file from URL
def download(url, output = None):
	if not output:
		output = url.split('/')[-1]
	request = urllib.request.urlopen(url)
	content = request.read()
	with open(output, 'wb') as f:
		f.write(content)
	return output


# Check if port is open
# return True  if port is open
# return False if target not found or port is closed
def portIsOpen(ip, port, timeout = 0.5):
	try:
		sock = socket.socket()
		sock.settimeout(timeout)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		result = sock.connect_ex((ip, int(port)))
		sock.close()
	except:
		return False
	else:
		if result == 0:
			return True
		else:
			return False

# Ping ip address
# return True  if target is online
# return False if target not found
def ping(ip):
	status = command.system('@ping -n 3 ' + ip + ' > NUL', return_code = True)[1]
	if status == 0:
		return True
	else:
		return False

# Get host ip by url
def getHostByName(ip):
	return socket.gethostbyname(ip)

# Get info by ip address
# WARNING! Usage limits:
# This endpoint is limited to 150 requests per minute from an IP address. If you go over this limit your IP address will be blackholed.
# You can unban here: http://ip-api.com/docs/unban
def whois(ip = ''):
	r = urllib.request.urlopen('http://ip-api.com/json/' + ip)
	r = json_loads(r.read())
	return r

# Get geodata by ip
def geoplugin(ip = ''):
	r = urllib.request.urlopen('http://www.geoplugin.net/json.gp?ip=' + ip)
	r = json_loads(r.read())
	return r


	
# Get LATITUDE, LONGITUDE, RANGE with bssid
def bssid_locate(bssid):
	r = urllib.request.urlopen('http://api.mylnikov.org/geolocation/wifi?bssid=' + bssid)
	r = json_loads(r.read())['data']
	return r

# Get router BSSID
def router():
	commandGetRouter = '\"Get-WmiObject -Class Win32_IP4RouteTable | where { $_.destination -eq \'0.0.0.0\' -and $_.mask -eq \'0.0.0.0\'} | Sort-Object metric1 | select nexthop\"'
	ROUTER_IP    = command.powershell(commandGetRouter).split()[2]
	_            = command.powershell('arp -a ' + ROUTER_IP).split()

	for _ in _:
		if '-' in _:
			i = 0
			for j in _:
				if j == '-':
					i+=1
			if i == 5:
				return _.replace('-', ':')