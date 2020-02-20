import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /customers/{custkey}/transactions
	Retrieve a existing customer

	Args:
		data (dict) contents:
			custkey (str) required

	Returns:
		Dictionary TransactionList
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.transactions.get()')

	path='/customers/' + data['custkey'] + '/transactions'
	return run_call('get',path,data,params)
