import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /customers/{custkey}/billing_schedules/{billing_schedule_key}/billing_schedule_rules
	Gets rules for a specific schedule from a customer

	If billing_rule_key is included:
	Gets rules for a specific schedule from a customer

	Args:
		data (dict) contents:
			billing_rule_key (str) optional

	Returns:
		Dictionary CustomerRule

	Returns:
		Dictionary CustomerRuleList
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.billing_schedule_rules.get()')

	if not 'billing_schedule_key' in data:
		raise Exception('billing_schedule_key required for customers.billing_schedules.billing_schedule_rules.get()')

	path='/customers/' + data['custkey'] + '/billing_schedules/' + data['billing_schedule_key'] + '/billing_schedule_rules'
	if 'billing_rule_key' in data:
		path = path + '/' + data['billing_rule_key']
	return run_call('get',path,data,params)

def delete(data={}):
	"""Calls /customers/{custkey}/billing_schedules/{billing_schedule_key}/billing_schedule_rules/{billing_rule_key}
	Delete a existing customer billing rule

	Args:
		data (dict) contents:
			custkey (str) required
			billing_schedule_key (str) required
			billing_rule_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.billing_schedule_rules.delete()')

	if not 'billing_schedule_key' in data:
		raise Exception('billing_schedule_key required for customers.billing_schedules.billing_schedule_rules.delete()')

	if not 'billing_rule_key' in data:
		raise Exception('billing_rule_key required for customers.billing_schedules.billing_schedule_rules.delete()')

	path='/customers/' + data['custkey'] + '/billing_schedules/' + data['billing_schedule_key'] + '/billing_schedule_rules'+ '/' + data['billing_rule_key']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /customers/{custkey}/billing_schedules/{billing_schedule_key}/billing_schedule_rules/{billing_rule_key}
	Gets rules for a specific schedule from a customer

	Args:
		data (dict) contents:
			custkey (str) required
			billing_schedule_key (str) required
			billing_rule_key (str) required
			Also can contain all fields from CustomerRule

	Returns:
		Dictionary CustomerRule
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.billing_schedule_rules.put()')

	if not 'billing_schedule_key' in data:
		raise Exception('billing_schedule_key required for customers.billing_schedules.billing_schedule_rules.put()')

	if not 'billing_rule_key' in data:
		raise Exception('billing_rule_key required for customers.billing_schedules.billing_schedule_rules.put()')

	path='/customers/' + data['custkey'] + '/billing_schedules/' + data['billing_schedule_key'] + '/billing_schedule_rules'+ '/' + data['billing_rule_key']
	return run_call('put',path,data,params)
