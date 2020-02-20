import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /transactions
	Gets a list of transactions

	If trankey is included:
	Retrieve a specific transaction.

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional
			fuzzy (str) optional

	Returns:
		Dictionary Transaction

	Returns:
		Dictionary TransactionList
	"""
	params={}
	path='/transactions'
	if 'trankey' in data:
		path = path + '/' + data['trankey']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']
	if 'fuzzy' in data:
		params['fuzzy']=data['fuzzy']

	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /transactions
	Run a transaction

	Args:
		data (dict) TransactionRequest

	Returns:
		Dictionary TransactionResponse
	"""
	params={}
	path='/transactions'
	return run_call('post',path,data,params)
