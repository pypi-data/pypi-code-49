import inspect

import cro_validate.api.normalize_api as NormalizeApi
import cro_validate.api.exception_api as ExceptionApi
import cro_validate.api.definition_api as DefinitionApi


class Rule:
	def __init__(
				self,
				description,
				callback=None,
				config={}
			):
		self._description = description
		self._callback = callback
		self._config = config

	def get_config(self):
		return self._config

	def get_description(self):
		return self._description

	def execute(self, fqn, value):
		if self._callback is None:
			return None
		return self._callback(fqn, value, **self.get_config())


########################################################################################################################
#                                                         Noop                                                         #
########################################################################################################################

class Noop(Rule):
	def _noop(self, input_name, value):
		return value

	def __init__(self, description):
		super().__init__(
				description=description,
				callback=self._noop
			)


########################################################################################################################
#                                                    DefinitionExists                                                  #
########################################################################################################################

class DefinitionExists(Rule):
	def _def_exists(self, input_name, value):
		if DefinitionApi.exists(value):
			return value
		raise ExceptionApi.create_input_error(input_name, 'Definition does not exist: {0}.'.format(value))

	def __init__(self):
		super().__init__(
				description='Definition must exist.',
				callback=self._def_exists
			)


########################################################################################################################
#                                                       Numbers                                                        #
########################################################################################################################
class AsInt(Rule):
	def __init__(self):
		super().__init__(
				description='Must be an integer.',
				callback=NormalizeApi.as_int
			)


class IntGte(Rule):
	def __init__(self, min_value):
		super().__init__(
				description='Must be integer greater than or equal to {0}.'.format(min_value),
				callback=NormalizeApi.as_int_greater_than_or_equal_to,
				config={'minimum':min_value}
			)


class IntLte(Rule):
	def __init__(self, max_value):
		super().__init__(
				description='Must be integer less than or equal to {0}.'.format(max_value),
				callback=NormalizeApi.as_int_less_than_or_equal_to,
				config={'maximum':max_value}
			)


class FloatGte(Rule):
	def __init__(self, min_value):
		super().__init__(
				description='Must be float greater than or equal to {0}.'.format(min_value),
				callback=NormalizeApi.as_float_greater_than_or_equal_to,
				config={'minimum':min_value}
			)


class FloatLte(Rule):
	def __init__(self, max_value):
		super().__init__(
				description='Must be float less than or equal to {0}.'.format(max_value),
				callback=NormalizeApi.as_float_less_than_or_equal_to,
				config={'maximum':max_value}
			)


class FloatLt(Rule):
	def __init__(self, max_value):
		super().__init__(
				description='Must be float less than {0}.'.format(max_value),
				callback=NormalizeApi.as_float_less_than,
				config={'maximum':max_value}
			)


########################################################################################################################
#                                                       Strings                                                        #
########################################################################################################################

class MatchRegex(Rule):
	def __init__(self, regex, regex_flags=0): # re.IGNORECASE
		super().__init__(				
				description='Must match expression {0}'.format(regex),
				callback=NormalizeApi.as_str_matching_regex,
				config={'rex':regex, 'flags':regex_flags}
			)


class StrWithMinLen(Rule):
	def __init__(self, min_len):
		super().__init__(
				description='Must be at least {0} characters long.'.format(min_len),
				callback=NormalizeApi.as_str_with_min_len,
				config={'min_len':min_len}
			)


class StrWithMaxLen(Rule):
	def __init__(self, max_len):
		super().__init__(
				description='Must be no longer than {0} characters.'.format(max_len),
				callback=NormalizeApi.as_str_with_max_len,
				config={'max_len':max_len}
			)


class StrWithinInclusiveLenRange(Rule):
	def __init__(self, min_len, max_len):
		super().__init__(
				description='Must be at least {0} and no more than {1} characters.'.format(min_len, max_len),
				callback=NormalizeApi.as_str_within_inclusive_len_range,
				config={'max_len':max_len, 'min_len':min_len}
			)

class ValueInSet(Rule):
	def __init__(self, values):
		desc = 'Must be one of: ' + ', '.join(["'{0}'".format(str(entry)) for entry in values])
		if isinstance(values, dict):
			desc = desc + ' (where {0})'.format(', '.join(["'{0}'='{1}'".format(str(entry), values[entry]) for entry in values]))
		desc = desc + '.'
		super().__init__(
				description=desc,
				callback=NormalizeApi.as_value_in_set,
				config={'values':values}
			)