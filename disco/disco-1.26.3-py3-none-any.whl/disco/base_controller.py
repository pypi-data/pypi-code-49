"""
Base functionality for SDK and CLI
"""
from .gql import Authentication


class BaseController(Authentication):
    """Base controller that provides authenticated methods of calling `rest` ,
    `gql` and `stream` functions
    """

    def __init__(self):
        pass
