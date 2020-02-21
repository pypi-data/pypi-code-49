import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /invoices
	Get a list of invoices

	If invoice_key is included:
	Retreive details of a invoice in database

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional

	Returns:
		Dictionary InvoiceResponse

	Returns:
		Dictionary InvoiceList
	"""
	params={}
	path='/invoices'
	if 'invoice_key' in data:
		path = path + '/' + data['invoice_key']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']

	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /invoices
	Generate a credit card token

	Args:
		data (dict) InvoiceRequest

	Returns:
		Dictionary InvoiceResponse
	"""
	params={}
	path='/invoices'
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /invoices/{invoice_key}
	Delete a invoice from the database

	Args:
		data (dict) contents:
			invoice_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'invoice_key' in data:
		raise Exception('invoice_key required for invoices.delete()')

	path='/invoices'+ '/' + data['invoice_key']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /invoices/{invoice_key}
	Update a invoice within the database

	Args:
		data (dict) contents:
			invoice_key (str) required
			Also can contain all fields from InvoiceRequest

	Returns:
		Dictionary InvoiceResponse
	"""
	params={}
	if not 'invoice_key' in data:
		raise Exception('invoice_key required for invoices.put()')

	path='/invoices'+ '/' + data['invoice_key']
	return run_call('put',path,data,params)
