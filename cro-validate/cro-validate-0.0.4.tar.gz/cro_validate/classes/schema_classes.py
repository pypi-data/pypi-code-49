from cro_validate.enum import DataType, SchemaOutputTarget
import cro_validate.api.definition_api as DefinitionApi
import cro_validate.api.name_api as NameApi
import cro_validate.api.exception_api as ExceptionApi
import cro_validate.classes.parameter_classes as Parameters


class Schema:
	def __init__(
				self,
				model,
				output_target=SchemaOutputTarget.Self,
				allow_unknown_fields=False
			):
		self.model = model
		if isinstance(self.model, type):
			self.model = model()
		self.model_name = self.model.__class__.__name__
		self.output_target = output_target
		self.allow_unknown_fields = allow_unknown_fields


class Field:
	def __init__(
				self,
				output_name=None,
				definition_name=None,
				required=True,
				ignored=False,
				unvalidated=False,
				dependencies=set()):
		self.output_name = output_name
		self.definition_name = definition_name
		self.required = required
		self.ignored = ignored
		self.unvalidated = unvalidated
		self.dependencies = dependencies


class Validator:
	def _validate(self, validated, fqn, field_name, definition, value, dependent_values):
		results = Parameters.Index.ensure(validated)
		normalized = value
		if isinstance(value, dict):
			normalized = Parameters.Index(value)
		if self.output_target is SchemaOutputTarget.Self:
			'''
			HACK: model_target shouldn't exist here.
			Some objs are mangled by an underlying lib (dangling __dict__ entries). Must target objs for overlay instead
			of filtering attrs. This disables SchemaOutputTarget.Parent for objs, but we don't have use cases for that
			now so deferring.
			'''
			model_target = None
			if not isinstance(value, dict):
				model_target = value
			model_result = self.model_validator(model_target, fqn, field_name, definition, normalized)
			results[field_name] = model_result
		elif self.output_target is SchemaOutputTarget.Parent:
			model_result = self.model_validator(None, fqn, field_name, definition, normalized)
			results.update(model_result)

		else:
			raise ExceptionApi.create_internal_error(self.name, 'Invalid schema output configured: {0}'.format(self.output_target))

	def __init__(self, name, output_target, model_validator):
		self.name = name
		self.output_target = output_target
		self.model_validator = model_validator

	def __call__(self, results, fqn, field_name, definition, value, dependent_values):
		return self._validate(results, fqn, field_name, definition, value, dependent_values)

	def is_field_required(self, field_name):
		if field_name in self.model_validator.required:
			return True
		return False

	def get_definition_name(self, field_name):
		return self.model_validator.get_definition_name(field_name)

	def get_dependency_order(self):
		return self.model_validator.get_dependency_order()

	def list_field_dependencies(self, field_name):
		return self.model_validator.dependencies[field_name]

	def list_field_names(self):
		return self.get_dependency_order()

	def list_definition_names(self):
		field_names = set()
		field_names.update(self.model_validator.required)
		field_names.update(self.model_validator.optional)
		definition_names = set()
		for field_name in field_names:
			if field_name in self.model_validator.definition_names:
				definition_names.add(self.model_validator.definition_names[field_name])
			else:
				definition_names.add(field_name)
		field_names = definition_names
		object_names = set()
		results = set(field_names)
		for field_name in field_names:
			definition_name = field_name
			if definition_name in self.model_validator.definition_names:
				definition_name = self.model_validator.definition_names[field_name]
			field = DefinitionApi.get(definition_name)
			if field.data_type == DataType.Object:
				results.update(field.validator.list_definition_names())
				object_names.add(field_name)
			elif field.data_type == DataType.Array:
				pass
			else:
				pass
		for name in object_names:
			results.remove(name)
		return results


class ModelValidator:
	def __init__(self, name, allow_unknown_fields):
		self.name = name
		self.allow_unknown_fields = allow_unknown_fields
		self.required = set()
		self.optional = set()
		self.ignored = set()
		self.unvalidated = set()
		self.definition_names = {}
		self.output_names = {}
		self.dependencies = {}
		self.dependency_order = None

	def get_definition_name(self, field_name):
		if field_name in self.definition_names:
			return self.definition_names[field_name]
		return field_name

	def get_dependency_order(self):
		self._update_dependency_order()
		return self.dependency_order

	def _list_input_entries(self, vector):
		if isinstance(vector, dict):
			return [k for k in vector]
		result = []
		for attribute_name in dir(vector):
			try:
				if attribute_name.startswith('_'):
					continue
				if not hasattr(vector, attribute_name): # possible dangling attr name if someone smashed the vector
					continue
				if callable(getattr(vector, attribute_name)):
					continue
				result.append(attribute_name)
			except:
				pass
		return result

	def _get_input_entry(self, field_name, source):
		if isinstance(source, dict):
			return source[field_name]
		return getattr(source, field_name)

	def _set_input_entry(self, field_name, target, value):
		if isinstance(target, dict):
			target[field_name] = value
		else:
			old_val = getattr(target, field_name)
			if old_val != value: # avoid overwriting read-only values
				setattr(target, field_name, value)
		return value

	def _rename_output(self, src_field_name, target_field_name, target):
		if isinstance(target, dict):
			tmp = target[src_field_name]
			del target[src_field_name]
			target[target_field_name] = tmp
		else:
			tmp = getattr(target, src_field_name)
			delattr(target, src_field_name)
			setattr(target, target_field_name, tmp)

	def _validate(self, validated, fqn, field_name, values, callback):
		result = Parameters.Index.ensure(validated)
		if isinstance(values, dict):
			normalized = Parameters.Index(values)
		else:
			normalized = values
		field_names = self._list_input_entries(values)
		kw = Parameters.Index()
		missing = set(self.required)

		self._update_dependency_order()

		# Build kw
		##########
		for field_name in field_names:
			if field_name in missing:
				missing.remove(field_name)
			elif field_name not in self.optional:
				if not self.allow_unknown_fields:
					raise ExceptionApi.create_input_error(NameApi.get_fqn(fqn, field_name), 'Unknown field.')
				else:
					continue
			if field_name not in self.ignored:
				kw[field_name] = self._get_input_entry(field_name, normalized)

		# Validate
		##########
		if len(missing) > 0:
			raise ExceptionApi.create_input_error(self.name, 'Missing required values: {0}'.format(', '.join(missing)))
		for entry in self.dependency_order:
			if entry in kw:
				if entry in self.unvalidated:
					result[entry] = self._get_input_entry(entry, normalized)
				else:
					definition_name = self.get_definition_name(entry)
					dependencies = DefinitionApi.get(definition_name).dependencies
					dependent_values = {k:kw[k] for k in kw if k in dependencies}
					child_fqn = NameApi.get_fqn(fqn, entry)
					definition_result = callback(
							validated=None,
							field_fqn=child_fqn,
							field_name=entry,
							definition_name=definition_name,
							value=kw[entry],
							dependent_values=dependent_values)
					for definition_result_entry in definition_result:
						self._set_input_entry(
								definition_result_entry,
								result,
								self._get_input_entry(
										definition_result_entry,
										definition_result
									)
							)

		# Output Names
		##############
		result_keys = self._list_input_entries(result)
		for entry in result_keys:
			if entry in self.output_names:
				output_name = self.output_names[entry]
				self._rename_output(entry, output_name, result)
		
		return result

	def _update_dependency_order(self):
		'''
		Depth-first topo sort
		'''
		# Initialize
		############
		if self.dependency_order is not None:
			return
		dependencies_idx = {}
		for k in self.required:
			if k in self.unvalidated:
				continue
			definition_name = self.get_definition_name(k)
			dependencies_idx[k] = DefinitionApi.get(definition_name).dependencies
		for k in self.optional:
			if k in self.unvalidated:
				continue
			definition_name = self.get_definition_name(k)
			dependencies_idx[k] = DefinitionApi.get(definition_name).dependencies
		remaining = set([k for k in dependencies_idx.keys()])
		result = []
		# Visit
		#######
		def visit(k, branch):
			if k not in remaining:
				return
			if k in branch:
				raise ExceptionApi.create_internal_error(self.name, 'Dependency circular reference.')
			branch.add(k)
			for edge in dependencies_idx[k]:
				visit(edge, branch)
			branch.remove(k)
			remaining.remove(k)
			result.append(k)
		# Iterate
		#########
		while len(remaining) > 0:
			branch = set()
			for k in remaining:
				selected = k
				break
			visit(selected, branch)
		self.dependency_order = result

	def add_required(self, names):
		for name in names:
			if name not in self.dependencies:
				self.dependencies[name] = set()
		self.required.update(names)

	def add_optional(self, names):
		for name in names:
			if name not in self.dependencies:
				self.dependencies[name] = set()
		self.optional.update(names)

	def add_ignored(self, names):
		self.ignored.update(names)

	def add_unvalidated(self, names):
		self.unvalidated.update(names)

	def add_definition_names(self, definition_names):
		self.definition_names.update(definition_names)

	def add_output_names(self, output_names):
		self.output_names.update(output_names)

	def add_dependencies(self, new_dependencies):
		for name in new_dependencies:
			if name not in self.dependencies:
				raise ExceptionApi.create_internal_error(str(add_dependencies) + '.' + str(name), 'Unknown field')
			self.dependencies[name].update(new_dependencies[name])
		self.dependency_order = None

	def add_spec(self, required, optional, ignored, unvalidated, definition_names={}, output_names={}, dependencies={}):
		self.add_required(required)
		self.add_optional(optional)
		self.add_ignored(ignored)
		self.add_unvalidated(unvalidated)
		self.add_definition_names(definition_names)
		self.add_output_names(output_names)
		self.add_dependencies(dependencies)

	def validate_values(self, validated, fqn, field_name, definition, values):
		return self._validate(
				validated,
				fqn,
				field_name,
				values,
				DefinitionApi.validate_input,
			)

	def __call__(self, validated, fqn, field_name, definition, values):
		return self.validate_values(
				validated,
				fqn,
				field_name,
				definition,
				values
			)