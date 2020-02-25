import uuid


def generate_guid():
    return str(uuid.uuid1())


def parse_headers(msg_header):
    """
    Converts headers to a dict
    :param msg_header: A message .headers() (confluent) or .headers (faust) instance
    :return: a decoded dict version of the headers
    """
    if msg_header:
        msg_header = dict(msg_header)
        return {key: value.decode() for key, value in msg_header.items()}
    return {}
