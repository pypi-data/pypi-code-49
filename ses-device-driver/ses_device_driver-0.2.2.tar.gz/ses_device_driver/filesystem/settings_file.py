#!/usr/bin/env python3

import sys
import yaml
import os
import io
import logging
class settings_file_handler:
	def __init__(self, filename):
		self.settings_filename = os.path.join(sys.path[0],filename)
		with open(self.settings_filename,"r") as yaml_file:
			self.settings = yaml.safe_load(yaml_file)

	def get_setting(self,section,key):
		with open(self.settings_filename,"r") as yaml_file:
			self.settings = yaml.safe_load(yaml_file)
			return self.settings[section][key]
	
	def set_setting(self,section,key,value):

		self.settings[section][key] = value

		with open(self.settings_filename, 'w') as yaml_file:
			yaml.dump(self.settings, yaml_file, default_flow_style=False)

	def get_settings_file_contents(self):
		with open(self.settings_filename,"r") as yaml_file:
			self.settings = yaml.safe_load(yaml_file)
		output = io.StringIO()
		yaml.dump(self.settings, output,default_flow_style=True)
		logging.debug(output.getvalue())
		return output.getvalue()

	def save_settings_file_contents(self, contents):
		self.settings = yaml.safe_load(contents)
		with open(self.settings_filename, 'w') as yaml_file:
			yaml.dump(self.settings, yaml_file, default_flow_style=False)

if __name__=="__main__":
	logging.basicConfig(level=logging.DEBUG, format='%(name)s [%(levelname)s] : %(message)s')
	testClient = settings_file_handler("scenarios.yml")
	filec = testClient.get_settings_file_contents()

	testClient.set_setting("scenario","test",["tes.urp"])
	testClient.save_settings_file_contents(filec)

		

