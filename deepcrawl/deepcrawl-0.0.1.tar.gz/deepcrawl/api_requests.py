import requests
from requests.exceptions import HTTPError
import json
import time

from .request_headers import *

def api_request(url, method, params="", auth="", headers="", json_body="", data=""):
	try:
		if method == 'get':
			response  = requests.get(url=url, params=params, auth=auth, headers=headers)
		elif method == 'patch':
			response  = requests.patch(url=url, params=params, auth=auth, headers=headers, data=data, json=json_body)
		elif method == 'post':
			response  = requests.post(url=url, params=params, auth=auth, headers=headers, data=data, json=json_body)
		elif method == 'delete':
			response  = requests.delete(url=url, params=params, auth=auth, headers=headers)          
		response.raise_for_status()
		
	except HTTPError as http_err:
		return f'HTTP error occurred: {http_err}' + response.text
	
	except Exception as err:
		return (f'Other error occurred: {err}')
	
	else:
		#return response.text
		return response



# Paginates through API requests until all the data is returned
# Returns all the items in a list
def get_api_data(connection, request_url, method, per_page=200, page_limit=100, nrows=10000, filters={}):
		
	# List to store the results
	response_list= []

	page = 1
	position = 0
	# Used to determine if we get less results than attempted
	results_ended = False
	# The number of rows remaining to try
	remaining_rows = nrows - position
	
	while position < nrows and page <= page_limit and results_ended == False:
		
		#print('page: ' + str(page))
		#print('position: ' + str(position))
		remaining_rows = nrows - position

		#print('remaining rows: ' +str(remaining_rows))

		if remaining_rows >= per_page:
				new_rows = per_page
		else:
				new_rows = remaining_rows


		pagination_params = {'page':page, 'per_page':new_rows}
		
		if filters:
				#print('Request includes filters')
				params = {**pagination_params, **filters}
				#print(pagination_params)
		else:
				params = {**pagination_params, **filters}
		

		response = api_request(url=request_url, method=method, params=params, headers=request_headers(connection))

		try:
			response_json = json.loads(response.text)
		except:
			print(response.text)
		number_of_rows_returned = len(response_json)
		#print('Rows returned: ' + str(number_of_rows_returned))
		if number_of_rows_returned < new_rows:
			results_ended = True

		response_list.extend(response_json)
		
		# Increment the position counter
		position += number_of_rows_returned
		page +=1
		#print('getting ' +str(new_rows) + ' new rows')
		#print('\n')

		# Be nice
		time.sleep(1)


					
	return response_list