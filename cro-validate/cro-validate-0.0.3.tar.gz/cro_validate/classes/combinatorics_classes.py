

########################################################################################################################
#                                         Single Variant Vector Generator                                              #
########################################################################################################################
class _SingleVariantStepResult:
	def __init__(self, complete, value=None):
		self.complete = complete
		self.value = value
		

class SingleVariantValueList:
	def __init__(self, name, values):
		self.name = name
		self.values = values
		self.cur_index = 0

	def next(self):
		assert self.values is not None, 'No values for SingleVariantValueList {0}'.format(self.name)
		if self.cur_index >= len(self.values):
			return _SingleVariantStepResult(True)
		result = _SingleVariantStepResult(False, self.values[self.cur_index])
		self.cur_index = self.cur_index + 1
		return result

	def reset(self):
		self.cur_index = 0

	def __str__(self):
		values_len = 0
		if self.values:
			values_len = len(self.values)
		return "{0} (cur_index={1}, len={2}: {3}".format(self.name, self.cur_index, values_len, self.values)

	def __repr__(self):
		return self.__str__()


class SingleVariantVectorGenerator:
	def __init__(self, params, ignore_first_vector=False):
		self.params = params
		self.values = None
		self.cur_tail = 0
		self.cur_variant_id = 0
		self.cur_variant_name = None
		self.ignore_first_vector = ignore_first_vector

	def _get_initial_param_value(self, param):
		step_result = param.next()
		if step_result.complete:
			raise ValueError("No values configured for param ({0})".format(param.name))
		return step_result.value

	def get_cur_tail_name(self):
		return self.params[self.cur_tail].name

	def __iter__(self):
		return self

	def __next__(self):
		# Initial values
		################
		if self.values is None:
			self.cur_tail = 0
			self.values = {}
			for param in self.params:
				param.reset()
				self.values[param.name] = self._get_initial_param_value(param)
			if len(self.values) < 1:
				raise StopIteration
			if not self.ignore_first_vector:
				self.cur_variant_name = self.params[0].name + '_0'
				self.cur_variant_id = 1
				return self.values

		# Next
		######
		while self.cur_tail < len(self.params):
			tail_name = self.params[self.cur_tail].name
			step_result = self.params[self.cur_tail].next()
			if not step_result.complete:
				self.values[tail_name] = step_result.value
				self.cur_variant_name = tail_name + '_' + str(self.cur_variant_id)
				self.cur_variant_id = self.cur_variant_id + 1
				return self.values
			self.params[self.cur_tail].reset()
			self.values[tail_name] = self._get_initial_param_value(self.params[self.cur_tail])
			self.cur_tail = self.cur_tail + 1
			self.cur_variant_id = 0

		# Complete
		##########
		raise StopIteration