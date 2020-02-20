import usaepay
from usaepay import run_call


def delete(data={}):
	"""Calls /customers/{custkey}/billing_schedules/{billing_schedule_key}/billing_schedule_rules/bulk
	Delete a existing customer billing rule

	Args:
		data (dict) contents:
			Keys (list) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.billing_schedule_rules.bulk.delete()')

	if not 'billing_schedule_key' in data:
		raise Exception('billing_schedule_key required for customers.billing_schedules.billing_schedule_rules.bulk.delete()')

	path='/customers/' + data['custkey'] + '/billing_schedules/' + data['billing_schedule_key'] + '/billing_schedule_rules/bulk'
	data_list = data['Keys']
	return run_call('delete',path,data,params)
