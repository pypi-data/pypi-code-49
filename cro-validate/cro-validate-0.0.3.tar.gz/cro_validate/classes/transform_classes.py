import json

import cro_validate.api.exception_api as ExceptionApi


########################################################################################################################
#                                                      Transform                                                       #
########################################################################################################################
class TransformInput:
	def __init__(self, callback, required_inputs=set()):
		self.callback = callback
		self.required_inputs = required_inputs
		self._class = '<unset>'
		self._kw = {}

	def _validate(self, input_values):
		for name in self.required_inputs:
			if name not in input_values:
				raise ExceptionApi.create_input_error(name, 'Required (missing)')

	def execute(self, definition, input_values, output_values):
		self._validate(input_values)
		self.callback(definition, input_values, output_values)


########################################################################################################################
#                                                        DictToJson                                                    #
########################################################################################################################
class DictToJson(TransformInput):
	def __init__(self, dict_name):
		super().__init__(self.dict_to_json, {dict_name})
		self.dict_name = dict_name
		self._class = 'DictToJson'
		self._kw = {'dict_name':dict_name}

	def dict_to_json(self, definition, input_values, output_values):
		try:
			value = input_values[self.dict_name]
			result = json.loads(value)
			return result
		except Exception as ex:
			raise ExceptionApi.create_input_error(definition.name, 'Invalid JSON', None, ex)


########################################################################################################################
#                                                      PassValue                                                       #
########################################################################################################################
class PassValue(TransformInput):
	def __init__(self, source_name=None, target_name=None):
		required_inputs = set()
		if not source_name is None:
			required_inputs.add(source_name)
		super().__init__(self.pass_value, required_inputs)
		self.source_name = source_name
		self.target_name = target_name
		self._class = 'PassValue'
		self._kw = {'source_name':source_name, 'target_name':target_name}

	def pass_value(self, definition, input_values, output_values):
		normalized_target_name = self.target_name
		if normalized_target_name is None:
			normalized_target_name = definition.name
		normalized_source_name = self.source_name
		if normalized_source_name is None:
			normalized_source_name = definition.name
		output_values[normalized_target_name] = input_values[normalized_source_name]


########################################################################################################################
#                                                  NormalizePageIndex                                                  #
########################################################################################################################
class NormalizedPageIndex(TransformInput):
	def __init__(self):
		super().__init__(self.normalize_page_index, {'page_index'})
		self._class = 'NormalizedPageIndex'
		self._kw = {}

	def normalize_page_index(self, definition, input_values, output_values):
		output_values.page_index = input_values.page_index - 1


########################################################################################################################
#                                                      TenantCode                                                      #
########################################################################################################################
class TenantCode(TransformInput):
	def __init__(self):
		super().__init__(self.parse_tenant_code, {'tenant_code'})
		self._class = 'TenantCode'
		self._kw = {}

	def _parse_tenant_code(self, value):
		split = value.split('+')
		if len(split) != 2:
			raise ExceptionApi.create_input_error('tenant_code', 'Invalid format')
		yard_code = split[0]
		try:
			location_id = int(split[1])
		except:
			raise ExceptionApi.create_input_error('tenant_code', 'Invalid format')
		return (yard_code, location_id)


	def parse_tenant_code(self, definition, input_values, output_values):
		yard_code, location_id = self._parse_tenant_code(input_values.tenant_code)
		output_values.yard_code = yard_code
		output_values.location_id = location_id


########################################################################################################################
#                                                     Str Replace                                                      #
########################################################################################################################
class StrReplace(TransformInput):
	def __init__(self, target, replacement):
		super().__init__(self.replace, {})
		self.target = target
		self.replacement = replacement
		self._class = 'StrReplace'
		self._kw = {'target':target, 'replacement':replacement}

	def replace(self, definition, input_values, output_values):
		for input_name in input_values:
			output_values[input_name] = input_values[input_name].replace(self.target, self.replacement)


########################################################################################################################
#                                                      To Str                                                          #
########################################################################################################################
class ToStr(TransformInput):
	def __init__(self, input_name):
		super().__init__(self.to_str, {input_name})
		self._class = 'ToStr'
		self._kw = {'input_name':input_name}

	def to_str(self, definition, input_values, output_values):
		for name in input_values:
			output_values[name] = str(input_values[name])