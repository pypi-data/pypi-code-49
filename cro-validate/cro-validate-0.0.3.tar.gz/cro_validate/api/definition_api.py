import cro_validate.api.name_resolver_api as NameResolverApi
import cro_validate.classes.definition_classes as Definitions
import cro_validate.classes.parameter_classes as Parameters
from cro_validate.enum import DataType


class _Index:
	index = Definitions.DefinitionIndex()


def get(name):
	result = _Index.index.get(name)
	return result


def exists(name):
	result = _Index.index.exists(name)
	return result


def as_dict():
	result = _Index.index.as_dict()
	return result


def register_definition(
 			name=None,
			aliases=set(),
			description='',
			data_type=DataType.String,
			data_format=None,
			default_value=Definitions.DataDefinitionDefaultValue(),
			examples=None,
			nullable=False,
			is_internal=False,
			rules=[],
			transforms=[],
			meta=None,
			dependency_resolver=None
		):
	if meta is None:
		meta = Definitions.DefaultMeta()
	if dependency_resolver is None:
		dependency_resolver = Definitions.DefaultResolver()
	result = _Index.index.register_definition(
			definition_index=_Index.index,
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
	return result


def ensure_alias(name, alias):
	_Index.index.ensure_alias(name, alias)


def list_definitions():
	results = _Index.index.list_definitions()
	return results


def list_dependent_definitions(definition_name):
	results = _Index.index.list_dependent_definitions(definition_name)
	return results


def list_fields(name):
	definition = get(name)
	if definition.data_type == DataType.Object:
		return definition.validator.list_field_names()
	return [name]


def validate_inputs(validated, **kw):
	results = _Index.index.validate_inputs(validated, **kw)
	return results


def validate_input(definition_name, value, validated=None, field_fqn=None, field_name=None, dependent_values={}):
	if field_name is None:
		field_name = definition_name
	if field_fqn is None:
		field_fqn = field_name
	results = _Index.index.validate_input(validated, field_fqn, field_name, definition_name, value, dependent_values)
	return results