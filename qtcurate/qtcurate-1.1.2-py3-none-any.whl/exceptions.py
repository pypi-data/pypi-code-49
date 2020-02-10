class QtConnectionError(Exception):
    pass


class QtRestApiError(Exception):
    """ Problem with authentification"""
    pass


class QtFileTypeError(Exception):
    """Invalid type of file"""
    pass


class QtDictIdError(Exception):
    """ Invalid resource"""
    pass


class QtArgumentError(Exception):
    pass


class QtDictError(Exception):
    pass

class QtDataProcessError(Exception):
    pass