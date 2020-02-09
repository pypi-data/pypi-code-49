import requests
import json
import logging
try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs

def main():
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
	payload = {'username': 'alfian@sken.ai', 'password': 'Om@Q*2FPzK*6'}
	try:
		resp = requests.post('https://dev-961749.okta.com/api/v1/authn', data=json.dumps(payload), headers=headers)
		scan_info = resp.json()
		session_token = scan_info['sessionToken']

		payload2 = {
			'response_type': 'token',
			'scope': 'openid',
			'state': 'TEST',
			'nonce': 'TEST',
			'client_id': '0oa1a118shOqGLi4D357',
			'redirect_uri': 'http://localhost:8080/login/oauth2/code/oidc',
			'sessionToken': session_token
		}

		resp2 = requests.get('https://dev-961749.okta.com/oauth2/default/v1/authorize', params=payload2, allow_redirects=False)

		parsed_url = urlparse(resp2.headers['Location'])
		query_string  = parsed_url.query

		if not query_string:
			query_string = parsed_url.fragment

		qs = parse_qs(query_string)

		payload3 = {'projectId': ''}
		headers3 = {'Authorization': qs['token_type'][0] + ' ' + qs['access_token'][0]}
		resp3 = requests.get("http://localhost:8080/api/cli/getScanData", params=payload3, headers=headers3, allow_redirects=False)
		print(resp3.text)

	except Exception as e:
		print('Failed to get scan info from sken server.')
		logging.exception(e)

if __name__ == "__main__":
    main()