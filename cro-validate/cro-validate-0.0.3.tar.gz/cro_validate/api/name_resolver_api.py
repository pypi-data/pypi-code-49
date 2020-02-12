import cro_validate.api.configuration_api as ConfigApi


def resolve_definition_name(definitions, definition_name):
	return ConfigApi.get_definition_name_resolver().resolve(definitions, definition_name)


def is_definition_name_nullable(definitions, definition_name):
	return ConfigApi.get_definition_name_resolver().is_nullable(definitions, definition_name)


def get_definition_base_name(parameters, parameter_name):
	return ConfigApi.get_definition_name_resolver().get_base_name(parameters, parameter_name)


def get_definition_nullable_name(parameters, parameter_name):
	return ConfigApi.get_definition_name_resolver().get_nullable_name(parameters, parameter_name)	


def resolve_parameter(parameters, parameter_name):
	return ConfigApi.get_parameter_name_resolver().resolve(parameters, parameter_name)


def is_parameter_name_nullable(parameters, parameter_name):
	return ConfigApi.get_parameter_name_resolver().is_nullable(parameters, parameter_name)


def get_parameter_base_name(parameters, parameter_name):
	return ConfigApi.get_parameter_name_resolver().get_base_name(parameters, parameter_name)


def get_parameter_nullable_name(parameters, parameter_name):
	return ConfigApi.get_parameter_name_resolver().get_nullable_name(parameters, parameter_name)	

