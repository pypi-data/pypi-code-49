import cro_validate.classes.exception_classes as Exceptions
import cro_validate.classes.example_generator_classes as Examples
import cro_validate.classes.name_resolver_classes as NameResolvers
import cro_validate.classes.name_strategy_classes as NameStrategies


class _Config:
	exception_factory = Exceptions.DefaultExceptionFactory()
	example_generator_factory = Examples.DefaultGeneratorFactory()
	default_examples_provider = Examples.DefaultExamplesProvider()
	definition_name_resolver = NameResolvers.DefaultNameResolver()
	parameter_name_resolver = NameResolvers.DefaultNameResolver()
	definition_name_strategy = NameStrategies.DefaultDefinitionNameStrategy()


def get_exception_factory():
	return _Config.exception_factory


def set_exception_factory(f):
	_Config.exception_factory = f


def get_definition_name_resolver():
	return _Config.definition_name_resolver


def set_definition_name_resolver(r):
	_Config.definition_name_resolver = r


def get_parameter_name_resolver():
	return _Config.parameter_name_resolver


def set_parameter_name_resolver(r):
	_Config.parameter_name_resolver = r


def get_example_generator_factory():
	return _Config.example_generator_factory


def set_example_generator_factory(f):
	_Config.example_generator_factory = f


def get_default_examples_provider():
	return _Config.default_examples_provider


def set_default_examples_provider(p):
	_Config.default_examples_provider = p


def set_definition_name_strategy(s):
	_Config.definition_name_strategy = s


def get_definition_name_strategy():
	return _Config.definition_name_strategy