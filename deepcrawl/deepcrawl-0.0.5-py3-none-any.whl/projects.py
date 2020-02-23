from requests.auth import HTTPBasicAuth
import json

from .api_endpoints import *
from .api_requests import *
from .majestic_settings import *
from .project_settings import *
from .extractions import *
from .issues import *
from .schedules import *

class DeepCrawlProject:

	def __init__(self, connection, project_data, account_id):

		# Set the project's required attributes
		self.project_data = project_data
		self.id = project_data['id']
		self.account_id = account_id
		self.connection = connection
		self.crawls_count = project_data.get('crawls_count')
		self.issues_count = project_data.get('issues_count')
		self.next_run_time = project_data.get('next_run_time')

		# Set conditional attributes
		self.crawls_finished_last_finished_at = project_data.get('_crawls_finished_last_finished_at')
		self.crawls_finished_last_progress_crawled = project_data.get('_crawls_finished_last_progress_crawled')

		# Create a project settings object
		self.project_settings = ProjectSettings(self.project_data)

		# Create a list of custom extractions objects
		extraction_data = project_data['custom_extractions']
		self.extractions = []
		for extraction in extraction_data:
		    self.extractions.append(Extraction(extraction_data=extraction))
    
	def start_crawl(self):
		# settings required to start a crawl
		crawl_start_data = {"status": "crawling"}

		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='crawls', account_id=self.account_id, project_id=self.id)
		headers = request_headers(self.connection, content_type='form')

		response = api_request(url=endpoint_url, method='post', data=crawl_start_data, headers=headers)

		return response
		

	def update_settings(self, settings):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='project', account_id=self.account_id, project_id=self.id)
		headers = request_headers(self.connection)

		response = api_request(url=endpoint_url, method='patch', json_body=vars(settings), headers=headers)
		try:
			response_json = json.loads(response.text)
		except:
			print(response)

		# Recreate the project instance with the API response
		self.__init__(self.connection, project_data=response_json, account_id=self.account_id)
		
		return

	def add_extractions(self, new_extractions):

		if isinstance(new_extractions, list):
			self.extractions.extend(new_extractions)
		else:
			self.extractions.append(new_extractions)

		new_extractions_list = []
		for extraction in self.extractions:
			new_extractions_list.append(vars(extraction))

		new_settings = ProjectSettings({'custom_extractions': new_extractions_list})
		
		self.update_settings(new_settings)

	def replace_extractions(self, new_extractions):

		new_extractions_list = []
		for extraction in new_extractions:
			new_extractions_list.append(vars(extraction))

		new_settings = ProjectSettings({'custom_extractions': new_extractions_list})
		
		self.update_settings(new_settings)


	def update_majestic_settings(self, majestic_settings):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='majestic', 
									account_id=self.account_id, 
									project_id=self.id)

		headers = request_headers(self.connection, content_type='json')

		majestic_settings_fields = vars(majestic_settings)

		majestic_settings_response = api_request(url=endpoint_url,
								method='patch',
								json_body=majestic_settings_fields,
								headers=headers)

		self.majestic_settings = MajesticSettings(majestic_settings=json.loads(majestic_settings_response.text))
		
		return

	def get_majestic_settings(self):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='majestic',
									account_id=self.account_id,
									project_id=self.id)

		headers = request_headers(self.connection, content_type='json')

		majestic_settings_response = api_request(url=endpoint_url, method='get', headers=headers)

		self.majestic_settings = MajesticSettings(majestic_settings=json.loads(majestic_settings_response.text))

		return

	def get_schedule(self):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='crawl_schedules',
									account_id=self.account_id,
									project_id=self.id)

		headers = request_headers(self.connection, content_type='json')

		schedule_response = api_request(url=endpoint_url, method='get', headers=headers)


		try:
			self.crawl_schedule = Schedule(json.loads(schedule_response.text)[0])
			return self.crawl_schedule
		except:
			return

	def delete_schedule(self):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='crawl_schedule',
									account_id=self.account_id,
									project_id=self.id,
									schedule_id=self.crawl_schedule.id)

		headers = request_headers(self.connection, content_type='json')

		api_request(url=endpoint_url, method='delete', headers=headers)

		return

	def update_schedule(self, schedule):
		# Generate API endpoint URL and request headers
		endpoint_url = api_endpoint(endpoint='crawl_schedules', 
									account_id=self.account_id, 
									project_id=self.id)

		headers = request_headers(self.connection, content_type='json')

		schedule_settings = vars(schedule)

		schedule_response = api_request(url=endpoint_url,
								method='post',
								json_body=schedule_settings,
								headers=headers)
		
		self.crawl_schedule = Schedule(json.loads(schedule_response.text))
		
		return



	def get_issues(self, nrows=1000):
		self.issues = get_issues(connection=self.connection, account_id=self.account_id, project_id=self.id, nrows=nrows)

	def delete_issue(self, issue):
		delete_issue(self.connection, self.account_id, self.id, issue.id)
		return

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
