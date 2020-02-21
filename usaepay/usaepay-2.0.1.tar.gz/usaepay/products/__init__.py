import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /products
	Retreive a list of products in database

	If product_key is included:
	Retreive details of a product in database

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional

	Returns:
		Dictionary ProductResponse

	Returns:
		Dictionary ProductList
	"""
	params={}
	path='/products'
	if 'product_key' in data:
		path = path + '/' + data['product_key']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']

	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /products
	Generate a credit card token

	Args:
		data (dict) ProductRequest

	Returns:
		Dictionary ProductResponse
	"""
	params={}
	path='/products'
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /products/{product_key}
	Delete a product from the database

	Args:
		data (dict) contents:
			product_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'product_key' in data:
		raise Exception('product_key required for products.delete()')

	path='/products'+ '/' + data['product_key']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /products/{product_key}
	Update a product within the database

	Args:
		data (dict) contents:
			product_key (str) required
			Also can contain all fields from ProductRequest

	Returns:
		Dictionary ProductResponse
	"""
	params={}
	if not 'product_key' in data:
		raise Exception('product_key required for products.put()')

	path='/products'+ '/' + data['product_key']
	return run_call('put',path,data,params)
