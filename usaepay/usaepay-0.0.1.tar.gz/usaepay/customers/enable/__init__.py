import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /customers/enable
	Enables a customer.

	Args:
		data (dict) Key

	Returns:
		Dictionary Status
	"""
	params={}
	path='/customers/enable'
	return run_call('post',path,data,params)
