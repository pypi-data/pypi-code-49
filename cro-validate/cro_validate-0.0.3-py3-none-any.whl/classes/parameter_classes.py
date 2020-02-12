import cro_validate.api.name_resolver_api as NameResolverApi
import cro_validate.api.exception_api as ExceptionApi


class Index(dict):
	def __getattr__(self, name):
		resolved = NameResolverApi.resolve_parameter(self, name)
		if resolved is None:
			if not NameResolverApi.is_parameter_name_nullable(self, name):
				raise ExceptionApi.create_input_error(name, 'Unresolved name.')
			return None
		result = self[resolved]
		return result

	def __setattr__(self, name, value):
		self[name] = value

	def ensure(index):
		if index is None:
			return Index()
		return index

