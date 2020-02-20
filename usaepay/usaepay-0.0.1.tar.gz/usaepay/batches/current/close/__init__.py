import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /batches/current/close
	Closes the currently open batch

	Returns:
		Dictionary BatchSummary
	"""
	params={}
	path='/batches/current/close'
	return run_call('post',path,data,params)
