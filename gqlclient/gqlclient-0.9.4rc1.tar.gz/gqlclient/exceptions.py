"""
Exceptions raised by the gql client
"""
from dataclasses import dataclass


__all__ = [
    "EncoderResponseException",
    "GQLClientException",
    "GraphQLException",
    "ModelException",
    "ServerConnectionException",
    "ServerResponseException",
]


class GQLClientException(Exception):
    """
    Base Exception for all exceptions raised by the gql client
    """


class ModelException(GQLClientException):
    """
    Exception raised when the input model (parameter or response)
    can't be used
    """


class ServerConnectionException(GQLClientException):
    """
    Exception raised when the graphql server can't be reached
    """


class ServerResponseException(GQLClientException):
    """
    Exception raised when the graphql server returns a HTTP status >= 500
    """


class EncoderResponseException(ServerResponseException):
    """
    Exception raised when the response encoder encounters a
    response it cannot encode
    """


@dataclass
class GraphQLException(GQLClientException):
    """
    Exception raised when there is are graphql error(s) returned by the server
    e.g. with a status code of 400 - 499
    """

    errors: list = None

    def __str__(self):
        return f"Errors were raised during graphql processing: details={self.errors}"
