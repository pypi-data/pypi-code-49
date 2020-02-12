import inspect

import crolib.input.classes.input_classes as Input
import crolib.input.validate_input as ValidateInput
import crolib.exception.classes.exception_classes as Exceptions

def bind(f, args, kw, ignore_unknown_inputs=False):

	if callable(f) and not inspect.isroutine(f):
		f = f.__call__ 
	sig = inspect.signature(f)
	normalized_kw = {}
	definition_names = {}
	i = 0
	for parameter_name in sig.parameters:
		parameter = sig.parameters[parameter_name]
		if parameter.annotation != inspect.Parameter.empty:
			if isinstance(parameter.annotation, str):
				definition_names[parameter_name] = parameter.annotation
		if i < len(args):
			normalized_kw[parameter_name] = args[i]
		i = i + 1
	normalized_kw.update(kw)
	bound_kw = Input.ParameterIndex()
	for field_name in normalized_kw:
		definition_name = field_name
		if field_name in definition_names:
			definition_name = definition_names[field_name]
		value = normalized_kw[field_name]
		bound_kw.update(ValidateInput.validate_input(None, field_name, definition_name, value, {}))
	nullables = {}
	unknowns = []
	for field_name in bound_kw:
		if field_name not in sig.parameters:
			if 'nullable_' + field_name in sig.parameters:
				nullables[field_name] = bound_kw[field_name]
			else:
				if ignore_unknown_inputs:
					unknowns.append(field_name)
				else:
					msg = "{0}() got an unexpected keyword argument {1}.".format(f.__name__, field_name)
					raise Exceptions.InputError(field_name, msg)
	for field_name in unknowns:
		del bound_kw[field_name]
	for field_name in nullables:
		value = bound_kw[field_name]
		del bound_kw[field_name]
		bound_kw['nullable_' + field_name] = value
	return bound_kw