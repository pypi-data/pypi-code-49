import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /products/categories
	Retreive a list of product categories in database

	If category_key is included:
	Retreive details of a product in database

	Args:
		data (dict) contents:
			limit (str) optional
			offset (str) optional

	Returns:
		Dictionary ProductCategoryResponse

	Returns:
		Dictionary ProductCategoryList
	"""
	params={}
	path='/products/categories'
	if 'category_key' in data:
		path = path + '/' + data['category_key']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']

	return run_call('get',path,data,params)

def post(data={}):
	"""Calls /products/categories
	Generate a credit card token

	Args:
		data (dict) ProductCategoryRequest

	Returns:
		Dictionary ProductCategoryResponse
	"""
	params={}
	path='/products/categories'
	return run_call('post',path,data,params)

def delete(data={}):
	"""Calls /products/categories/{category_key}
	Delete a product from the database

	Args:
		data (dict) contents:
			category_key (str) required

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'category_key' in data:
		raise Exception('category_key required for products.categories.delete()')

	path='/products/categories'+ '/' + data['category_key']
	return run_call('delete',path,data,params)

def put(data={}):
	"""Calls /products/categories/{category_key}
	Update a product within the database

	Args:
		data (dict) contents:
			category_key (str) required
			Also can contain all fields from ProductCategoryRequest

	Returns:
		Dictionary ProductCategoryResponse
	"""
	params={}
	if not 'category_key' in data:
		raise Exception('category_key required for products.categories.put()')

	path='/products/categories'+ '/' + data['category_key']
	return run_call('put',path,data,params)
