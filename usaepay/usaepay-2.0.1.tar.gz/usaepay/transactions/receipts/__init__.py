import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /transactions/{trankey}/receipts/{receipt_key}
	Retrieve receipt for specific transaction.

	Args:
		data (dict) contents:
			trankey (str) required
			receipt_key (str) required

	Returns:
		String
	"""
	params={}
	if not 'trankey' in data:
		raise Exception('trankey required for transactions.receipts.get()')

	if not 'receipt_key' in data:
		raise Exception('receipt_key required for transactions.receipts.get()')

	path='/transactions/' + data['trankey'] + '/receipts'+ '/' + data['receipt_key']
	return run_call('get',path,data,params)
