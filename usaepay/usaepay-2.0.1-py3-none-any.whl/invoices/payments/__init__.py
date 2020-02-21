import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /invoices/{invoice_key}/payments
	Retreive details of a invoice in database

	Args:
		data (dict) contents:
			invoice_key (str) required

	Returns:
		Dictionary InvoicePaymentList
	"""
	params={}
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']

	if not 'invoice_key' in data:
		raise Exception('invoice_key required for invoices.payments.get()')

	path='/invoices/' + data['invoice_key'] + '/payments'
	return run_call('get',path,data,params)
