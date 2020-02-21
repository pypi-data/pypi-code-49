import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /paymentengine/devices/{devicekey}/terminal-config
	Get a devices details

	Args:
		data (dict) contents:
			devicekey (str) required

	Returns:
		Dictionary DeviceTerminalConfig
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.terminal-config.get()')

	path='/paymentengine/devices/' + data['devicekey'] + '/terminal-config'
	return run_call('get',path,data,params)

def put(data={}):
	"""Calls /paymentengine/devices/{devicekey}/terminal-config
	Register a device

	Args:
		data (dict) contents:
			devicekey (str) required
			Also can contain all fields from DeviceTerminalConfig

	Returns:
		Dictionary DeviceResponse
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.terminal-config.put()')

	path='/paymentengine/devices/' + data['devicekey'] + '/terminal-config'
	return run_call('put',path,data,params)
