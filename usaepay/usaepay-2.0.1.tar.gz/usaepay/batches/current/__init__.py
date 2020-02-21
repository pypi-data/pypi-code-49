import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /batches/current
	Retrieves the currently open batch.

	Returns:
		Dictionary BatchDetails
	"""
	params={}
	path='/batches/current'
	return run_call('get',path,data,params)
