import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /paymentengine/payrequests
	Start a new transaction on device

	Args:
		data (dict) PayRequest

	Returns:
		Dictionary PayRequestStatus
	"""
	params={}
	path='/paymentengine/payrequests'
	return run_call('post',path,data,params)

def get(data={}):
	"""Calls /paymentengine/payrequests/{requestkey}
	Retreive status of an existing payment request.

	Args:
		data (dict) contents:
			requestkey (str) required

	Returns:
		Dictionary PayRequestStatus
	"""
	params={}
	if not 'requestkey' in data:
		raise Exception('requestkey required for paymentengine.payrequests.get()')

	path='/paymentengine/payrequests'+ '/' + data['requestkey']
	return run_call('get',path,data,params)

def delete(data={}):
	"""Calls /paymentengine/payrequests/{requestkey}
	Cancel a payment request.

	Args:
		data (dict) contents:
			requestkey (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'requestkey' in data:
		raise Exception('requestkey required for paymentengine.payrequests.delete()')

	path='/paymentengine/payrequests'+ '/' + data['requestkey']
	return run_call('delete',path,data,params)
