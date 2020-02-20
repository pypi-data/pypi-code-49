from requests.auth import HTTPBasicAuth
import json

from .api_endpoints import *
from .api_requests import *
from .projects import *


class ApiConnection:

	def __init__(self, id_user, key_pass, auth_type_user=False):
		self.key_pass = key_pass
		self.id_user = id_user
		self.auth_type_user = auth_type_user

		# If the authentication is using a user login, include additional request parameters
		if auth_type_user == False:
			dc_auth_params = {} 
		elif auth_type_user == True:
			dc_auth_params = {'root':1} 
		else:
			return('Unrecognised auth type. Use \'api\' or \'user\'')
		
		response = api_request(url=api_endpoint(endpoint='session'), method='post', params = dc_auth_params, auth=HTTPBasicAuth(id_user, key_pass))

		response_json = json.loads(response.text)
		token = response_json["token"]
		self.token = token


	def create_project(self, account_id, project_settings):
		endpoint_url = api_endpoint(endpoint='projects', account_id=account_id)
		new_project_response = api_request(
											url=endpoint_url, 
											method='post', 
											json_body=project_settings, 
											headers=request_headers(self)
											)
		new_project = DeepCrawlProject(connection=self, project_data=json.loads(new_project_response.text), account_id=account_id)
		return new_project

	def get_projects(self, account_id, filters={}, nrows=10000):
		endpoint_url = api_endpoint(endpoint='projects', account_id=account_id)
		projects = get_api_data(
								self, 
								request_url=endpoint_url, 
								method='get', 
								filters=filters, 
								nrows=nrows
								)
		list_of_projects = []

		for project in projects:
				list_of_projects.append(DeepCrawlProject(connection=self, project_data=project, account_id=account_id))

		return list_of_projects


	def get_project(self, account_id, project_id):

		endpoint_url = api_endpoint(endpoint='project', account_id=account_id, project_id=project_id)
		response = api_request(
								url=endpoint_url, 
								method='get', 
								headers=request_headers(self))
		
		response_json = json.loads(response.text)
		project = DeepCrawlProject(connection=self, project_data=response_json, account_id=account_id)
		return project








