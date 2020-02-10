import six
import base64


def base64_encode_bytes(data, *args, **kwargs):
    return base64.b64encode(data, *args, **kwargs).decode("ascii")


def base64_encode(data, *args, **kwargs):
    if isinstance(data, bytes):
        return base64_encode_bytes(data, *args, **kwargs)

    if six.PY3:
        input_data = data.encode("utf-8")
    else:
        input_data = data

    output_data = base64.b64encode(input_data, *args, **kwargs)
    if six.PY3:
        return output_data.decode("ascii")
    else:
        return output_data


def base64_decode_to_bytes(data, *args, **kwargs):
    return base64.b64decode(data, *args, **kwargs)


def base64_decode(data, *args, **kwargs):
    output_data = base64_decode_to_bytes(data, *args, **kwargs)
    if six.PY3:
        return output_data.decode()
    else:
        return output_data


def to_unicode(ss, enc=None, errors=None):
    # Strings are already unicode inheritly in python3
    return ss
