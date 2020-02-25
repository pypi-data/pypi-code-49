import re


def to_underscore(name):
    """
    >>> to_underscore('ADC')
    'adc'
    >>> to_underscore('FizzBuzz')
    'fizz_buzz'
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def chevron_list_mark_last(data, last_key='last'):
    if data:
        data[-1][last_key] = True
    return data


def list_to_chevron_list(data, key_name, last_key=None):
    """Transform a list of key-value pairs to a list of dicts with given key and value names.

    This is useful for passing dictionaries to chevron.
    If the last_key is given, the last item has an extra element with the last_key as key and True as value.

    >>> list_to_chevron_list(['foo', 'bar'], 'key')
    [{'key': 'foo'}, {'key': 'bar'}]
    >>> list_to_chevron_list(['foo', 'bar'], 'key', 'last')
    [{'key': 'foo'}, {'key': 'bar', 'last': True}]
    """
    chevron_list = [{key_name: value} for value in data]
    if last_key:
        chevron_list_mark_last(chevron_list, last_key)
    return chevron_list


def dict_to_chevron_list(data, key_name, value_name, last_key=None):
    """Transform a list of key-value pairs to a list of dicts with given key and value names.

    This is useful for passing dictionaries to chevron.
    If the last_key is given, the last item has an extra element with the last_key as key and True as value.

    >>> dict_to_chevron_list({'foo': 'bar'}, 'key', 'value')
    [{'key': 'foo', 'value': 'bar'}]
    >>> dict_to_chevron_list({'foo': 'bar', 'bar': 'baz'}, 'key', 'value', 'last')
    [{'key': 'foo', 'value': 'bar'}, {'key': 'bar', 'value': 'baz', 'last': True}]
    """
    chevron_list = [{key_name: key, value_name: value} for key, value in data.items()]
    if last_key:
        chevron_list_mark_last(chevron_list, last_key)
    return chevron_list


def process_dict(src, required, optional):
    """This function makes sure src contains required and optional keys and nothing else"""

    required_keys = set(required)
    present_keys = set(src.keys())
    optional_keys = set(optional.keys())

    missing_required = required_keys - present_keys
    not_required = present_keys - required_keys
    unexpected_keys = not_required - optional_keys

    if unexpected_keys:
        raise Exception(f'Unexpected keys: {", ".join(unexpected_keys)}')

    if missing_required:
        raise Exception(f'Missing keys: {", ".join(missing_required)}')

    return {**optional, **src}
