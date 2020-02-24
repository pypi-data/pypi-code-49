from azureml.dataprep.native import StreamInfo


def get_stream_info_value(si):
    return {
        'streaminfo': {
            'handler': si.handler,
            'resourceidentifier': si.resource_identifier,
            'arguments': {k: _get_value(v) for k, v in si.arguments.items()}
        }
    }


def _get_value(value):
    if isinstance(value, StreamInfo):
        return get_stream_info_value(value)
    elif isinstance(value, str):
        return {'string': value}
    elif isinstance(value, bool):
        return {'boolean': value}
    elif isinstance(value, float):
        return {'double': value}
    elif isinstance(value, int):
        return {'long': value}
    elif isinstance(value, dict):
        return {'record': {k: _get_value(v) for k, v in value.items()}}
    elif isinstance(value, list):
        return {'list': [_get_value(v) for v in value]}
    elif value is None:
        return None
    else:
        raise TypeError('Unexpected type "{}"'.format(type(value)))
