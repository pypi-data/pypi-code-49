import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /paymentengine/devices
	Gets a list of registered devices

	If devicekey is included:
	Get a devices details

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional

	Returns:
		Dictionary DeviceResponse

	Returns:
		Dictionary DeviceList
	"""
	params={}
	path='/paymentengine/devices'
	if 'devicekey' in data:
		path = path + '/' + data['devicekey']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']

	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /paymentengine/devices
	Register a device

	Args:
		data (dict) DeviceRequest

	Returns:
		Dictionary DeviceResponse
	"""
	params={}
	path='/paymentengine/devices'
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /paymentengine/devices/{devicekey}
	Unregisters a device

	Args:
		data (dict) contents:
			devicekey (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.delete()')

	path='/paymentengine/devices'+ '/' + data['devicekey']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /paymentengine/devices/{devicekey}
	Register a device

	Args:
		data (dict) contents:
			devicekey (str) required
			Also can contain all fields from DeviceRequest

	Returns:
		Dictionary DeviceResponse
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.put()')

	path='/paymentengine/devices'+ '/' + data['devicekey']
	return run_call('put',path,data,params)
