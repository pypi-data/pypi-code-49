# -*- coding: utf-8 -*-

class Variable(object):
	"""
	Variable item in a vault.
	"""

	def __init__(self, variable_name, variable_json):
		self.variable_name = variable_name;
		self.variable_json = variable_json;


	"""
	Unique variable ID.
	"""
	variable_id = None;

	"""
	Owner. Delegates of this user can manage his variables as well. When null,
	defaults to the API authenticated user.
	"""
	user_id_owner = None;

	"""
	The user which last updated the variable.
	"""
	user_id_authenticated = None;

	"""
	Must start with a letter and end with a letter or digit. May contain
	underscores, latin characters and digits. When copied into the generated
	variables JSON of an AnsibleBundle execution context, the variable name is
	used as-is.
	"""
	variable_name = None;

	"""
	If null, any kind of usage is enabled. Otherwise, a comma separated list of
	allowed usage types.
	"""
	variable_usage = None;

	"""
	Variable value in JSON format.
	"""
	variable_json = None;

	"""
	Date and time of the variable's creation.
	"""
	variable_created_timestamp = None;

	"""
	Date and time of the variable's update (replace).
	"""
	variable_updated_timestamp = None;

	"""
	The schema type
	"""
	type = None;
