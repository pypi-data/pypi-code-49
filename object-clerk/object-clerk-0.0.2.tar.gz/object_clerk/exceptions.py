"""
Exceptions raised by the object clerk
"""


class ObjectClerkException(Exception):
    """
    Base Exception for the object clerk
    """


class ObjectNotFoundException(ObjectClerkException):
    """
    Exception when an object cannot be found either due to bucket or object key validity
    """


class ObjectVerificationException(ObjectClerkException):
    """
    Exception when checksums of source and destination data mismatch
    """


class ObjectSaveException(ObjectClerkException):
    """
    Exception when objects cannot be saved due to size or readability
    """
