"""
    Custom errors and error handling decorators.
"""

from __future__ import print_function, absolute_import, unicode_literals
import grpc
import wrapt

__all__ = [
    "handle_exceptions",
    "LegacyMessageError",
    "GrpcError",
    "TimeOutError",
    "NotFoundError",
]


# Exception decorator to catch common gRPC exceptions
@wrapt.decorator
def handle_exceptions(f, _, args, kwargs):
    """Custom decorator that re-raises exceptions in terms of dgpy custom exceptions."""
    try:
        return f(*args, **kwargs)
    except grpc.RpcError as e:
        # Many grpc errors (e.g. _Rendezvous error) are very verbose, reduce amount of information here:
        if e.code() == grpc.StatusCode.INTERNAL:
            # We use INTERNAL for backend-related errors, so strip code:
            raise GrpcError(e.details())
        elif e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
            raise TimeOutError(e.details())
        elif e.code() == grpc.StatusCode.NOT_FOUND:
            raise NotFoundError(e.details())
    raise GrpcError("{}: {}".format(e.code(), e.details()))


#------------------------------------------------------------------------------------------------------------
# Errors exported by this package
#------------------------------------------------------------------------------------------------------------
class LegacyMessageError(Exception):
    """LegacyMessageError is used to communicate the cause of a failed legacy C Syntropy call"""

class GrpcError(Exception):
    """GrpcError wraps common gRPC errors"""

class TimeOutError(Exception):
    """TimeOutError indicates that a command or action did not complete within the given timeout."""

class NotFoundError(GrpcError):
    """NotFoundError is a GrpcError whose status code indicates that a resource was NOT_FOUND."""
