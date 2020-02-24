import enum


class AuthenticationMode(enum.IntEnum):
    unauthenticated = -1
    username_password_rest_flow = 0
    web_server_rest_flow = 1
    user_agent_rest_flow = 2
    username_password_soap_flow = 3


# Dictionary of default headers used in order to better streamline creation of new requests to the salesforce api
HEADERS = {
    "oauth_login_headers": {"Content-Type": "application/x-www-form-urlencoded"},
    "soap_login_headers": {"Content-Type": "text/xml", "SOAPAction": '""' },
    "rest_authorized_headers": {
        "Authorization": None,
        "Content-Type": "application/json",
        "charset": "UTF-8"
    },
    "soap_authorized_headers": {}  # TODO: get the generic structure for this
}

SFDC_XML_NAMESPACE = "{urn:partner.soap.sforce.com}"

SOAP_BODY_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>\
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\
     xmlns:xsd="http://www.w3.org/2001/XMLSchema"\
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\
     xmlns:met="http://soap.sforce.com/2006/04/metadata">\
     <soapenv:Header>\
     <met:CallOptions>\
     </met:CallOptions>\
     <met:SessionHeader>\
     <met:sessionId>\
     {}\
     </met:sessionId>\
     </met:SessionHeader>\
     </soapenv:Header>\
     <soapenv:Body>\
     {}\
     </soapenv:Body>\
     </soapenv:Envelope>\
    """