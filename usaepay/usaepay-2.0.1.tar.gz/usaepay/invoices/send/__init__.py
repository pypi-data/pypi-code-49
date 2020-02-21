import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /invoices/{invoice_key}/send
	Update a invoice within the database

	Args:
		data (dict) contents:
			invoice_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'invoice_key' in data:
		raise Exception('invoice_key required for invoices.send.post()')

	path='/invoices/' + data['invoice_key'] + '/send'
	return run_call('post',path,data,params)
