from .router import Route


def __route_builder(endpoint, rule, view, *methods):
    # TODO: Make documentation
    return Route(endpoint, rule, view, *methods)


def route_get(endpoint, rule, view):
    """
    Generate route for GET method HTTP
    
    :param endpoint:
    :param rule:
    :param view:
    :return Route:
    """
    return __route_builder(endpoint, rule, view, 'GET')


def route_post(endpoint, rule, view):
    """
    Generate route for POST method HTTP
    
    :param endpoint:
    :param rule:
    :param view:
    :return Route:
    """
    return __route_builder(endpoint, rule, view, 'POST')


def route_delete(endpoint, rule, view):
    """
    Generate route for DELETE method HTTP
    
    :param endpoint:
    :param rule:
    :param view:
    :return Route:
    """
    return __route_builder(endpoint, rule, view, 'DELETE')


def route_put(endpoint, rule, view):
    """
    Generate route for PUT method HTTP
    
    :param endpoint:
    :param rule:
    :param view:
    :return Route:
    """
    return __route_builder(endpoint, rule, view, 'PUT')


def route_prefix(prefix, *routes):
    """
    Generate routes pack with prefix added
    
    :param prefix:
    :param *route:
    :return list:
    """
    if not prefix.startswith('/'):
        prefix = '/' + prefix

    for n in range(len(routes)):
        routes[n].rule = prefix + routes[n].rule
    return routes
