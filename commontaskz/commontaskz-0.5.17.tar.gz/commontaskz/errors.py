# This error occurs when the data returned by a query is empty or None
bad_response = "Could Not Query"

def query_failed(url):
    """
    This error occurs when a service is queried, ex. Datasys, Rankings, Zirra.dev and the quiery failed.
    Likely because the company id is not in the system. (Except in the case of Zirra.dev because that uses search
    instead of id lookup)
    :param url:
    :return:
    """
    return "failed to query with url {}".format(url)

def response_code(code):
    """
    This error occurs when the data returned by querying a service returns some sort of response code other than 200.
    :param code:
    :return:
    """
    return "response code was {}".format(code)

# CA Specific Errors
def service_name_dne(service):
    """
    This error occurs when a service name is missing. Ex. There is no "datasys" entry in the list of biids in CA.
    :param service:
    :return:
    """
    return "CA entry does not include {} id".format(service)

def field_dne(field):
    """
    This occurs when the title of a field is missing. Example, there is no "biids" at all.
    :param field:
    :return:
    """
    return "no {} field".format(field)

