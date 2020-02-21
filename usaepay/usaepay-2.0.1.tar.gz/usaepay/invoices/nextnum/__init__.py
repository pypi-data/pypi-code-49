import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /invoices/nextnum
	Next default invoice number

	Returns:
		String
	"""
	params={}
	path='/invoices/nextnum'
	return run_call('get',path,data,params)
