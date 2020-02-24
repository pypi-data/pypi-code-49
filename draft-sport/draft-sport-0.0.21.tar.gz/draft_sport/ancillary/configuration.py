"""
Draft Sport
Configuration Module
author: hugh@blinkybeach.com
"""


class Configuration:
    """
    Abstract protocol defining an interfaces for classes that may
    serve as a configuration store for Draft Sport Python.
    """

    api_endpoint: str = NotImplemented
