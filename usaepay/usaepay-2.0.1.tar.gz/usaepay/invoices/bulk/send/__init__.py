import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /invoices/bulk/send
	Get invoice defaults

	Args:
		data (dict) contents:
			Keys (list) required

	Returns:
		Dictionary Status
	"""
	params={}
	path='/invoices/bulk/send'
	data_list = data['Keys']
	return run_call('post',path,data,params)
