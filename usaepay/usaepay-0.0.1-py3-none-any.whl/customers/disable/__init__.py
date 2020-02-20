import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /customers/disable
	Disable a customer.

	Args:
		data (dict) Key

	Returns:
		Dictionary Status
	"""
	params={}
	path='/customers/disable'
	return run_call('post',path,data,params)
