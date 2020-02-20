# Generate request headers with the API connection token and the appropriate content-type
def request_headers(connection, content_type='json'):

	if content_type == 'json':
		content_type_value = 'application/json'
	elif content_type == 'form':
		content_type_value = 'application/x-www-form-urlencoded'

	return {
					'X-Auth-Token' : connection.token,
					'Content-Type': content_type_value,
					'User-Agent' : 'PostmanRuntime/7.17.1',
					'Accept' : '*/*',
					'Cache-Control' : 'no-cache',
					'Accept-Encoding' : 'gzip, deflate'
				 } 



