from requests.auth import HTTPBasicAuth
import json

from .api_endpoints import *
from .api_requests import *
from .majestic_settings import *
from .project_settings import *
from .extractions import *

class DeepCrawlProject:

	def __init__(self, connection, project_data, account_id):

		# Set the project's attributes
		self.project_data = project_data
		self.id = project_data['id']
		self.account_id = account_id
		self.connection = connection
		self.crawls_count = project_data['crawls_count']
		self.issues_count = project_data['issues_count']
		self.next_run_time = project_data['next_run_time']

		# Set conditional attributes
		if 'crawls_finished_last_finished_at' in project_data.keys():
			self.crawls_finished_last_finished_at = project_data['crawls_finished_last_finished_at']
		if 'crawls_finished_last_progress_crawled' in project_data.keys():		
			self.crawls_finished_last_progress_crawled = project_data['crawls_finished_last_progress_crawled']

		# Create a project settings object
		self.project_settings = ProjectSettings(project_data)

		# Create a list of custom extractions objects
		extraction_data = project_data['custom_extractions']
		self.custom_extractions = []
		for extraction in extraction_data:
		    self.custom_extractions.append(DeepCrawlExtraction(extraction_data=extraction))
    

	def update_settings(self, settings):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='project', account_id=self.account_id, project_id=self.id)
		headers = request_headers(self.connection)

		response = api_request(url=endpoint_url, method='patch', json_body=settings, headers=headers)
		try:
			response_json = json.loads(response.text)
		except:
			print(response)
		self.__init__(self.connection, project_data=response_json, account_id=self.account_id)
		return

	def start_crawl(self):
		# settings required to start a crawl
		crawl_start_data = {"status": "crawling"}

		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='crawls', account_id=self.account_id, project_id=self.id)
		headers = request_headers(self.connection, content_type='form')

		response = api_request(url=endpoint_url, method='post', data=crawl_start_data, headers=headers)

		return
		

	def get_issues(self, nrows=1000):
		return get_issues(connection=self.connection, account_id=self.account_id, project_id=self.id, nrows=nrows)

	def create_issue(self, issue):
		new_issue = { "actions": False,
							"assigned_to": issue.assigned_to,
							"deadline_at": issue.deadline_at,
							"description": issue.description,
							"dismissed": issue.dismissed,
							"filters": issue.filters,
							"priority": issue.priority,
							"report_template": issue.report_template,
							"report_type": issue.report_type,
							"title": issue.title
							}

		new_issue_json = json.dumps(new_issue)

		return create_issue(connection=self.connection, account_id=self.account_id, project_id=self.id, issue_json=new_issue_json)

	def add_extractions(self, extractions):
		
		self.custom_extractions.append(extractions)

		#! Build dict from extraction objects
		custom_extractions_list = []
		for custom_extraction in self.custom_extractions:
			custom_extractions_list.append({'label': custom_extraction.label,
											'regex': custom_extraction.regex,
											'match_number_from': custom_extraction.match_number_from,
											'match_number_to': custom_extraction.match_number_to,
											'filter': custom_extraction.filter,
											'clean_html_tags': custom_extraction.clean_html_tags})

		new_settings = {'custom_extractions': custom_extractions_list}

		self.update_settings(new_settings)

	def update_majestic_settings(self, majestic_settings):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='majestic', 
									account_id=self.account_id, 
									project_id=self.id)

		headers = request_headers(self.connection, content_type='json')

		response = api_request(url=endpoint_url,
								method='patch',
								json_body=majestic_settings,
								headers=headers)
		
		try:
			response_json = json.loads(response.text)
			self.majestic_settings.__init__(majestic_settings=response_json)
		except:
			print(response)
		
		return

	def get_majestic_settings(self):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='majestic', account_id=self.account_id, project_id=self.id)
		headers = request_headers(self.connection, content_type='json')

		majestic_settings_response = api_request(url=endpoint_url, method='get', headers=headers)
		self.majestic_settings = MajesticSettings(majestic_settings=json.loads(majestic_settings_response.text))
		return self.majestic_settings


