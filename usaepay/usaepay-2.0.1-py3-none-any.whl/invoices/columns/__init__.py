import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /invoices/columns
	Get invoice defaults

	Returns:
		List of Columns
	"""
	params={}
	path='/invoices/columns'
	return run_call('get',path,data,params)
