import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /customers
	Gets a list of your customers

	If custkey is included:
	Retrieve a existing customer

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional

	Returns:
		Dictionary Customer

	Returns:
		Dictionary CustomerList
	"""
	params={}
	path='/customers'
	if 'custkey' in data:
		path = path + '/' + data['custkey']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']

	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /customers
	Save a customer to your customer database

	Args:
		data (dict) CustomerRequest

	Returns:
		Dictionary Customer
	"""
	params={}
	path='/customers'
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /customers/{custkey}
	Delete a existing customer

	Args:
		data (dict) contents:
			custkey (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.delete()')

	path='/customers'+ '/' + data['custkey']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /customers/{custkey}
	Updates a existing customer

	Args:
		data (dict) contents:
			custkey (str) required
			Also can contain all fields from CustomerRequest

	Returns:
		Dictionary Customer
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.put()')

	path='/customers'+ '/' + data['custkey']
	return run_call('put',path,data,params)
