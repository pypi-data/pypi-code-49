import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /customers/{custkey}/payment_methods
	Delete a existing customer billing rule

	If paymethod_key is included:
	Delete a existing customer billing rule

	Args:
		data (dict) contents:
			paymethod_key (str) optional

	Returns:
		Dictionary CustomerPaymentMethod

	Returns:
		Dictionary CustomerPaymentMethodList
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.payment_methods.get()')

	path='/customers/' + data['custkey'] + '/payment_methods'
	if 'paymethod_key' in data:
		path = path + '/' + data['paymethod_key']
	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /customers/{custkey}/payment_methods
	Add an array of new payment methods to an existing customer

	Args:
		data (dict) contents:
			CustomerPaymentMethodRequests (list) required

	Returns:
		List of CustomerPaymentMethods
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.payment_methods.post()')

	path='/customers/' + data['custkey'] + '/payment_methods'
	data_list = data['CustomerPaymentMethodRequests']
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /customers/{custkey}/payment_methods/{paymethod_key}
	Delete a existing customer billing rule

	Args:
		data (dict) contents:
			custkey (str) required
			paymethod_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.payment_methods.delete()')

	if not 'paymethod_key' in data:
		raise Exception('paymethod_key required for customers.payment_methods.delete()')

	path='/customers/' + data['custkey'] + '/payment_methods'+ '/' + data['paymethod_key']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /customers/{custkey}/payment_methods/{paymethod_key}
	Update an existing customer payment method

	Args:
		data (dict) contents:
			custkey (str) required
			paymethod_key (str) required
			Also can contain all fields from CustomerPaymentMethodRequest

	Returns:
		Dictionary CustomerPaymentMethod
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.payment_methods.put()')

	if not 'paymethod_key' in data:
		raise Exception('paymethod_key required for customers.payment_methods.put()')

	path='/customers/' + data['custkey'] + '/payment_methods'+ '/' + data['paymethod_key']
	return run_call('put',path,data,params)
