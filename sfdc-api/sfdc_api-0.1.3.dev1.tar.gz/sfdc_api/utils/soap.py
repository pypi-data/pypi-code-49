from .constants import SOAP_BODY_TEMPLATE


def soap_body_builder(session_id, body):
    body_str = SOAP_BODY_TEMPLATE
    return body_str.format(session_id, body)
