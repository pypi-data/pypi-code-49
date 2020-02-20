import usaepay
from usaepay import run_call


def delete(data={}):
	"""Calls /invoices/bulk
	Get invoice defaults

	Args:
		data (dict) contents:
			Keys (list) required

	Returns:
		Dictionary Status
	"""
	params={}
	path='/invoices/bulk'
	data_list = data['Keys']
	return run_call('delete',path,data,params)
