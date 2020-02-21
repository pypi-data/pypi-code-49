import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /invoices/defaults
	Get invoice defaults

	Returns:
		Dictionary Defaults
	"""
	params={}
	path='/invoices/defaults'
	return run_call('get',path,data,params)
