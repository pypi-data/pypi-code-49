import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /customers/{custkey}/billing_schedules
	Gets customers billing schedules

	If billing_schedule_key is included:
	Gets specific schedule from a customer

	Args:
		data (dict) contents:
			billing_schedule_key (str) optional

	Returns:
		Dictionary CustomerSchedule

	Returns:
		Dictionary CustomerScheduleList
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.get()')

	path='/customers/' + data['custkey'] + '/billing_schedules'
	if 'billing_schedule_key' in data:
		path = path + '/' + data['billing_schedule_key']
	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /customers/{custkey}/billing_schedules
	Add billing schedules to customer

	Args:
		data (dict) contents:
			CustomerSchedules (list) required

	Returns:
		List of CustomerSchedules
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.post()')

	path='/customers/' + data['custkey'] + '/billing_schedules'
	data_list = data['CustomerSchedules']
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /customers/{custkey}/billing_schedules/{billing_schedule_key}
	Delete a existing customer

	Args:
		data (dict) contents:
			custkey (str) required
			billing_schedule_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.delete()')

	if not 'billing_schedule_key' in data:
		raise Exception('billing_schedule_key required for customers.billing_schedules.delete()')

	path='/customers/' + data['custkey'] + '/billing_schedules'+ '/' + data['billing_schedule_key']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /customers/{custkey}/billing_schedules/{billing_schedule_key}
	Update a customers billing schedule

	Args:
		data (dict) contents:
			custkey (str) required
			billing_schedule_key (str) required
			Also can contain all fields from CustomerSchedule

	Returns:
		Dictionary CustomerSchedule
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.billing_schedules.put()')

	if not 'billing_schedule_key' in data:
		raise Exception('billing_schedule_key required for customers.billing_schedules.put()')

	path='/customers/' + data['custkey'] + '/billing_schedules'+ '/' + data['billing_schedule_key']
	return run_call('put',path,data,params)
