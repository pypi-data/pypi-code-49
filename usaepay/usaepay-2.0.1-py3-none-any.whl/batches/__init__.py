import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /batches
	Retrieves a list of batches associated with the account

	If batch_key is included:
	Retrieves a specific batch.

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional
			openedlt (str) optional
			openedgt (str) optional
			closedlt (str) optional
			closedgt (str) optional
			openedle (str) optional
			openedge (str) optional
			closedle (str) optional
			closedge (str) optional

	Returns:
		Dictionary BatchDetails

	Returns:
		Dictionary BatchList
	"""
	params={}
	path='/batches'
	if 'batch_key' in data:
		path = path + '/' + data['batch_key']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']
	if 'openedlt' in data:
		params['openedlt']=data['openedlt']
	if 'openedgt' in data:
		params['openedgt']=data['openedgt']
	if 'closedlt' in data:
		params['closedlt']=data['closedlt']
	if 'closedgt' in data:
		params['closedgt']=data['closedgt']
	if 'openedle' in data:
		params['openedle']=data['openedle']
	if 'openedge' in data:
		params['openedge']=data['openedge']
	if 'closedle' in data:
		params['closedle']=data['closedle']
	if 'closedge' in data:
		params['closedge']=data['closedge']

	return run_call('get',path,data,params)
