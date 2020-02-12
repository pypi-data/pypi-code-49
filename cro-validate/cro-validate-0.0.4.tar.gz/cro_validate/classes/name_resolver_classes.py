import cro_validate.api.name_resolver_api as NameResolverApi


class DefaultNameResolver:
	def resolve(self, namespace, name):
		if name in namespace:
			return name
		normalized_name = self.get_base_name(namespace, name)
		if normalized_name in namespace:
			return normalized_name
		normalized_name = self.get_nullable_name(namespace, name)
		if normalized_name in namespace:
			return normalized_name
		return None

	def is_nullable(self, namespace, name):
		if name.startswith('nullable_'):
			return True
		return False

	def get_base_name(self, namespace, name):
		normalized_name = name
		if self.is_nullable(namespace, normalized_name):
			normalized_name = name[9:]
		return normalized_name

	def get_nullable_name(self, namespace, name):
		if self.is_nullable(namespace, name):
			return name
		return 'nullable_' + name