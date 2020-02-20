import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /paymentengine/devices/{devicekey}/settings
	Get a devices settings

	Args:
		data (dict) contents:
			devicekey (str) required

	Returns:
		Dictionary DeviceSettings
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.settings.get()')

	path='/paymentengine/devices/' + data['devicekey'] + '/settings'
	return run_call('get',path,data,params)

def put(data={}):
	"""Calls /paymentengine/devices/{devicekey}/settings
	Register a device

	Args:
		data (dict) contents:
			devicekey (str) required
			Also can contain all fields from DeviceSettings

	Returns:
		Dictionary DeviceResponse
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.settings.put()')

	path='/paymentengine/devices/' + data['devicekey'] + '/settings'
	return run_call('put',path,data,params)
