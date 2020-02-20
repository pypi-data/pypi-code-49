import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /batches/{batch_key}/transactions
	Retrieves transactin detail for a specific batch.

	Args:
		data (dict) contents:
			batch_key (str) required

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

	if not 'batch_key' in data:
		raise Exception('batch_key required for batches.transactions.get()')

	path='/batches/' + data['batch_key'] + '/transactions'
	return run_call('get',path,data,params)
