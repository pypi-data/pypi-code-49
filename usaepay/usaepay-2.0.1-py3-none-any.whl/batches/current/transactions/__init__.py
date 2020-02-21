import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /batches/current/transactions
	Retrieves transactin detail for the currently open batch.

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional
			return_bin (str) optional

	Returns:
		Dictionary BatchTransactions
	"""
	params={}
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']
	if 'return_bin' in data:
		params['return_bin']=data['return_bin']

	path='/batches/current/transactions'
	return run_call('get',path,data,params)
