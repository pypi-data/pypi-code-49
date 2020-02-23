from requests.auth import HTTPBasicAuth
import json

from .api_endpoints import *
from .api_requests import *

schedule_settings_fields = ['schedule_frequency', 'next_run_time', 'id']

class Schedule:
	def __init__(self, schedule_settings=''):

		# Use slots to save memory and prevent invalid values
		__slots__ = schedule_settings_fields
		
		if schedule_settings:
			schedule_data = schedule_settings.get('_href', None)

			if schedule_data:

				self.id = schedule_data.split('/')[-1]

				# create attributes for every valid name
				for key, value in schedule_settings.items():
					if key in schedule_settings_fields:
						setattr(self, key, value)

				# Create a dictable version of attributes to allow use of slots and vars()
				@property
				def __dict__(self):
					return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}