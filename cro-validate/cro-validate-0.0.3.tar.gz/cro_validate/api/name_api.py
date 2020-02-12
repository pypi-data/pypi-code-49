
def get_fqn(namespace, field_name):
	if namespace is not None and len(namespace) > 0:
		return namespace + '.' + field_name
	return field_name


def get_parent_fqn(fqn):
	index = fqn.rfind('.')
	if index < 0:
		return ''
	return fqn[:index]


def get_field_name_from_fqn(fqn):
	index = fqn.rfind('.')
	if index < 0:
		return ''
	return fqn[index+1:]