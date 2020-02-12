from cro_validate.enum import DataType
import cro_validate.api.configuration_api as ConfigApi
import cro_validate.api.name_resolver_api as NameResolverApi
import cro_validate.api.exception_api as ExceptionApi
import cro_validate.api.example_api as ExampleApi
import cro_validate.classes.parameter_classes as Parameters
import cro_validate.classes.schema_classes as Schemas
import cro_validate.classes.name_strategy_classes as NameStrategies


class DataDefinitionDefaultValue:
	pass


class Meta:
	def initialize(self, definition, **kw):
		raise NotImplementedError()


class DefaultMeta(Meta):
	def __init__(self, component_name_strategy=NameStrategies.DefaultComponentNameStrategy()):
		self.component_name_strategy = component_name_strategy
		self.schema_name = None
		self.component_name = None

	def initialize(self, definition, component_name_suffix='Model'):
		if definition.is_object():
			self.schema_name = definition.data_format.model_name
			self.component_name = self.schema_name
		elif definition.is_array():
			self.component_name = definition.data_format
		else:
			self.component_name = self.component_name_strategy.create_name(definition, component_name_suffix)


class Definition:
	def __init__(
				self,
				definition_index,
				name,
				aliases,
				description,
				data_type,
				data_format,
				default_value,
				examples,
				nullable,
				is_internal,
				rules,
				transforms,
				meta,
				dependency_resolver
			):
		self.name = name
		self.aliases = aliases
		self.definitions = definition_index
		self.description = description
		self.data_type = data_type
		self.data_format = data_format
		self.default_value = default_value
		self.examples = examples
		self.nullable = nullable
		self.is_internal = is_internal
		self.dependencies = set()
		self.rules = rules
		self.transforms = transforms
		self.meta = meta
		self.dependency_resolver = dependency_resolver
		# Name
		######
		self.name = ConfigApi.get_definition_name_strategy().create_name(self, self.name)
		if self.name is None:
			ExceptionApi.create_internal_error(
					'<unset>', 'Definition name cannot be None (description={0})'.format(self.description)
				)
		# Data Format
		#############
		if self.data_type is DataType.OneOf:
			self.data_format = dependency_resolver.list_dependent_definition_names(self.name)
		# Validator
		###########
		if self.is_object():
			self.validator = self._get_obj_validator()
		elif self.is_array():
			self.validator = self._validate_array	
		else:
			self.validator = self._assign_value
		# Dependencies
		##############
		self.dependencies = set(self.dependency_resolver.list_dependency_fields(self.name))

		# Examples
		##########
		if not self.examples:
			self.examples = ExampleApi.get_default_examples(self)
		if not self.is_object() and not self.is_array():
			if not self.examples:
				raise ExceptionApi.create_input_error(self.name, 'Missing examples')
		# Meta
		######
		self.meta.initialize(self)

	def _get_obj_model_validator(self):
		validator = Schemas.ModelValidator(
				self.data_format.model_name,
				self.data_format.allow_unknown_fields
			)
		required = set()
		optional = set()
		ignored = set()
		unvalidated = set()
		definition_names = {}
		output_names = {}
		dependencies = {}
		model = self.data_format.model
		if model is None:
			raise ExceptionApi.create_internal_error(self.data_format.model_name, 'Missing model')
		for name in dir(model):
			if name.startswith('_'):
				continue			
			field_definition = getattr(model, name)
			if field_definition is None:
				field_definition = Schemas.Field()
			if field_definition.required:
				required.add(name)
			else:
				optional.add(name)
			if field_definition.ignored:
				ignored.add(name)
			if field_definition.unvalidated:
				unvalidated.add(name)
			if field_definition.definition_name:
				definition_names[name] = field_definition.definition_name
			if field_definition.output_name:
				output_names[name] = field_definition.output_name
			definition_name = name
			if field_definition.definition_name is not None:
				definition_name = field_definition.definition_name
			if field_definition.unvalidated is not True:
				dependencies[name] = self.definitions.get(definition_name).dependencies
		validator.add_spec(
				required=required,
				optional=optional,
				ignored=ignored,
				unvalidated=unvalidated,
				definition_names=definition_names,
				output_names=output_names,
				dependencies=dependencies)
		return validator

	def _get_obj_validator(self):
		model_validator = self._get_obj_model_validator()
		validator = Schemas.Validator(
				self.name,
				self.data_format.output_target,
				model_validator
			)
		return validator

	def _validate_array(self, results, field_fqn, field_name, definition, values, dependent_values):
		if not isinstance(values, list):
			raise ExceptionApi.create_input_error(field_fqn, 'Expected array, received: {0}'.format(type(values)))
		items = []
		for entry in values:
			item = self.definitions.validate_input(None, field_fqn, field_name, self.data_format, entry, dependent_values)
			items.append(item[field_name])
		results[field_name] = items

	def _assign_value(self, results, field_fqn, field_name, definition, value, dependent_values):
		results[field_name] = value

	def validate(self, results, field_fqn, field_name, definition, value, dependent_values):
		try:
			normalized = Parameters.Index()
			validator = self.validator
			dependent_definition_name = self.dependency_resolver.get_dependent_definition(
					field_fqn,
					dependent_values
				)
			if dependent_definition_name is not None:
				self.definitions.validate_input(
						results,
						field_fqn,
						field_name,
						dependent_definition_name,
						value,
						dependent_values
					)
			else:
				validator(normalized, field_fqn, field_name, self, value, dependent_values)
			for rule in self.rules:
				normalized[field_name] = rule.execute(field_fqn, normalized[field_name])
			for transform in self.transforms:
				transformed = Parameters.Index()
				transform.execute(definition, normalized, transformed)
				normalized = transformed
			results.update(normalized)
		except Exception as ex:
			if self.is_internal:
				raise ExceptionApi.create_internal_error(ex.source, ex.message)
			else:
				raise ex

	def has_default_value(self):
		if isinstance(self.default_value, DataDefinitionDefaultValue):
			return False
		return True

	def get_default_value(self, name):
		if not self.has_default_value():
			raise ExceptionApi.create_internal_error(self.name, 'No default value configured')
		return self.default_value

	def get_name(self):
		return self.name

	def get_aliases(self):
		return self.aliases

	def is_array(self):
		if self.data_type == DataType.Array:
			return True
		return False

	def is_object(self):
		if self.data_type == DataType.Object:
			return True
		return False

	def is_primitive(self):
		if self.is_object() or self.is_array():
			return False
		return True

	def is_internal(self):
		return self.is_internal

	def is_nullable(self):
		return self.is_nullable


class DependentDefinitionResolver:
	def list_dependent_definition_names(self, fqn):
		raise NotImplementedError()

	def get_dependent_definition(self, fqn, dependent_values):
		raise NotImplementedError()

	def list_dependency_fields(self, fqn):
		raise NotImplementedError()


class DefaultResolver(DependentDefinitionResolver):
	def list_dependent_definition_names(self, fqn):
		return []

	def get_dependent_definition(self, fqn, dependent_values):
		return None

	def list_dependency_fields(self, fqn):
		return []


class OneOfResolver(DependentDefinitionResolver):
	def __init__(self):
		self._dependencies = set()
		self._dependency_idx = {}
		self._dependency_order = []
		self._permutations = []

	def _update_dependency_idx_order(self, fqn, keys):
		diff = self._dependencies.difference(keys)
		if len(diff) > 0:
			raise ExceptionApi.create_internal_error(fqn, 'Permutation keys must match dependencies.')
		self._dependencies.update([k for k in keys])
		for k in keys:
			if k in self._dependency_order:
				continue
			self._dependency_order.append(k)
		self._dependency_order.sort()

	def _index_permutation(self, fqn, permutation, value):
		self._permutations.append(permutation)
		idx = self._dependency_idx
		for k in self._dependency_order[:-1]:
			state = permutation[k]
			if state not in idx:
				idx[state] = {}
			idx = idx[state]
		state = permutation[self._dependency_order[-1]]
		if state in idx:
			raise ExceptionApi.create_internal_error(fqn, 'Cannot re-index a permutation.')
		idx[state] = value

	def _get_permutation_value(self, fqn, permutation):
		idx = self._dependency_idx
		last_index = len(self._dependency_order) - 1
		for i in range(len(self._dependency_order)):
			k = self._dependency_order[i]
			if k not in permutation:
				raise ExceptionApi.create_internal_error(
						fqn,
						'k not in permutation ({0})'.fromat(permutation)
					)
			state = permutation[k]
			if state not in idx:
				raise ExceptionApi.create_internal_error(
						fqn,
						'Unknown permutation value (k={0} p={2}).'.format(k, state, permutation)
					)
			if i == last_index:
				return idx[state]
			idx = idx[state]
		return None

	def list_dependent_definition_names(self, fqn):
		result = set()
		for p in self._permutations:
			name = self._get_permutation_value(fqn, p)
			result.add(name)
		return result

	def index_dependent_definition(self, fqn, dependency_state, dependent_definition_name):
		self._update_dependency_idx_order(fqn, dependency_state.keys())
		self._index_permutation(fqn, dependency_state, dependent_definition_name)

	def get_dependent_definition(self, fqn, dependent_values):
		name = self._get_permutation_value(fqn, dependent_values)
		return name

	def list_dependency_fields(self, fqn):
		return self._dependencies



class DefinitionIndex:
	def __init__(self):
		self._index = {}

	def get(self, name):
		resolved = NameResolverApi.resolve_definition_name(self._index, name)
		if resolved is None:
			raise ExceptionApi.create_internal_error(name, 'Definition name resolution failed (Unknown definition name).')
		return self._index[resolved]

	def exists(self, name):
		resolved = NameResolverApi.resolve_definition_name(self._index, name)
		if resolved is None:
			return False
		return True

	def as_dict(self):
		return self._index

	def register_definition(
				self,
				definition_index,
				name,
				aliases,
				description,
				data_type,
				data_format,
				default_value,
				examples,
				nullable,
				is_internal,
				rules,
				transforms,
				meta,
				dependency_resolver
			):
		definition = Definition(
				definition_index=definition_index,
				name=name,
				aliases=aliases,
				description=description,
				data_type=data_type,
				data_format=data_format,
				default_value=default_value,
				examples=examples,
				nullable=nullable,
				is_internal=is_internal,
				rules=rules,
				transforms=transforms,
				meta=meta,
				dependency_resolver=dependency_resolver
			)
		definition_name = definition.get_name()
		names = set()
		names.add(definition_name)
		if isinstance(aliases, str):
			names.add(aliases)
		else:
			names.update(aliases)
		for entry in names:
			if definition_name in self._index:
				raise ExceptionApi.create_internal_error(definition_name, 'Input definiton already exists.')
		for entry in names:
			self._index[entry] = definition
		return definition

	def validate_inputs(self, validated, **kw):
		results = Parameters.Index.ensure(validated)
		for name in kw:
			self.validate_input(results, name, name, name, kw[name])
		return results

	def validate_input(self, validated, field_fqn, field_name, definition_name, value, dependent_values={}):
		results = Parameters.Index.ensure(validated)
		nullable = False
		definition = self.get(definition_name)
		nullable = self.is_nullable(definition_name)
		if value is None:
			if nullable is True or NameResolverApi.is_definition_name_nullable(self._index, definition_name):
				results[field_name] = None
			else:
				raise ExceptionApi.create_input_error(field_name, 'Not nullable.')
		else:
			if not definition.validator:
				raise ExceptionApi.create_internal_error(definition_name, "Missing validator.")
			definition.validate(results, field_fqn, field_name, definition, value, dependent_values)
		return results

	def is_nullable(self, name):
		nullable = False
		if NameResolverApi.is_definition_name_nullable(self.as_dict(), name):
			nullable = True
		else:
			definition = self.get(name)
			nullable = definition.nullable
		return nullable

	def get_description(self, name, delim):
		definition = self.get(name)
		result = definition.description
		if definition.rules is not None and len(definition.rules) > 0:
			result = result + delim + delim.join([rule.get_description() for rule in definition.rules])
		return result

	def ensure_alias(self, name, alias):
		definition = self.get(name)
		if alias not in self._index:
			self._index[alias] = definition

	def list_definitions(self):
		result = [k for k in self._index]
		result.sort()
		return result

	def list_dependent_definitions(self, definition_name):
		results = set()
		definition = self.get(definition_name)
		if definition.data_type == DataType.Object:
			result = definition.validator.list_definition_names()
		elif definition.data_type == DataType.Array:
			results = DefinitionIndex.list_dependent_definitions(definition.data_format)
		return results

	def list_fields(self, name):
		definition = self.get(name)
		if definition.data_type == DataType.Object:
			return definition.validator.list_field_names()
		return [name]